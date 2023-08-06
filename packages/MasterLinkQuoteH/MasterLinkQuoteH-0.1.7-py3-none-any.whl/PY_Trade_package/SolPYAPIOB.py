from collections import UserDict #line:3
import decimal #line:4
from enum import Enum #line:5
import math #line:6
from pydoc_data import topics #line:7
import queue #line:8
import threading #line:9
from threading import Lock #line:10
import time #line:11
from solace .messaging .messaging_service import MessagingService #line:13
from solace .messaging .receiver .message_receiver import MessageHandler ,InboundMessage #line:14
from solace .messaging .publisher .outbound_message import OutboundMessage #line:15
from solace .messaging .resources .topic import Topic #line:16
from solace .messaging .resources .topic_subscription import TopicSubscription #line:17
from solace .messaging .utils .converter import BytesToObject #line:18
from solace .messaging .receiver .direct_message_receiver import DirectMessageReceiver #line:19
from solace .messaging .publisher .request_reply_message_publisher import RequestReplyMessagePublisher #line:20
import json #line:22
import os #line:23
from os .path import dirname #line:24
from decimal import Decimal #line:25
from PY_Trade_package .MarketDataMart import MarketDataMart ,SystemEvent #line:26
from PY_Trade_package .Product import ProductSnapshot ,ProductTick_Fut ,ProductTick_Stk ,TMapPrdOvs ,TMapPrdSnapshot #line:27
from PY_Trade_package .SolPYAPI_Model import *#line:29
from PY_Trade_package .SolLog import *#line:31
import logging #line:32
from time import sleep #line:33
class TStkQuoteConnStu (Enum ):#line:36
    stuUnConn =0 #line:37
    """未連線"""#line:38
    stuConnIng =10 #line:39
    """連線中"""#line:40
    stuConnected =20 #line:41
    """初次連線成功"""#line:42
    stuReConnected =21 #line:43
    """再次連線成功"""#line:44
    stuDisConnIng =30 #line:45
    """準備斷線"""#line:46
class TStkProdKind (Enum ):#line:49
    pkNone =0 #line:50
    pkNormal =10 #line:51
    """一般證券"""#line:52
    pkIndex =20 #line:53
    """指數商品(EX:加權指數)"""#line:54
class STKxFUT (Enum ):#line:57
    STK =0 #line:58
    FUT =1 #line:59
    OPT =2 #line:60
    OVSFUT =3 #line:61
class TStkQtBase ():#line:65
    fHasBAS =False #line:66
    fBAS =[]#line:67
    StkNo :str #line:68
    """證券代碼"""#line:69
    StkName :str #line:70
    """證券中文"""#line:71
    RefPriceOrg :str #line:72
    """參考價"""#line:73
    LimitPrice_UpOrg :str #line:74
    """漲停價"""#line:75
    LimitPrice_DownOrg :str #line:76
    """跌停價"""#line:77
    IndustryCategory :str #line:78
    "產業別"#line:79
    StockCategory :str #line:80
    "證券別"#line:81
    StockAnomalyCode :str #line:82
    "股票異常代碼"#line:83
    BoardRemark :str #line:84
    "板別註記"#line:85
    ClassRemark :str #line:86
    "類股註記"#line:87
    NonTenFaceValueIndicator :str #line:88
    "非10元面額註記"#line:89
    AbnormalRecommendationIndicator :str #line:90
    "異常推介個股註記"#line:91
    AbnormalSecuritiesIndicator :str #line:92
    "特殊異常證券註記"#line:93
    DayTradingIndicator :str #line:94
    "可現股當沖註記"#line:95
    TradingUnit :str #line:96
    "交易單位"#line:97
    def Get_TradingUnit (O0OOO00O0OOOOO0O0 ):#line:98
        return O0OOO00O0OOOOO0O0 .TransToInt (O0OOO00O0OOOOO0O0 .fBAS [30 ])#line:99
    TickSizeInfo :str #line:100
    """跳動點資訊"""#line:101
    TotQtyPre :str #line:102
    """(前交易日)成交總量"""#line:103
    TotAmtPre :str #line:104
    """(前交易日)成交總額"""#line:105
    RefPPre :str #line:107
    "上一交易日參考價"#line:108
    CPPre :str #line:109
    "上一交易日收盤價"#line:110
    def __init__ (OO00000O00OO00OO0 ):#line:112
        pass #line:113
    def Get_RefPrice (O0O00O0OOO00OO00O )->decimal :#line:115
        return O0O00O0OOO00OO00O .TransToDecimal (O0O00O0OOO00OO00O .fBAS [4 ])#line:116
    def Get_LimitPrice_Up (OO000OOOO00O0OOO0 )->decimal :#line:118
        return OO000OOOO00O0OOO0 .TransToDecimal (OO000OOOO00O0OOO0 .fBAS [5 ])#line:119
    def Get_LimitPrice_Down (O00OOO0O00O0O0O00 )->decimal :#line:121
        return O00OOO0O00O0O0O00 .TransToDecimal (O00OOO0O00O0O0O00 .fBAS [6 ])#line:122
    def Get_TotQtyPre (O000OOO000OO0O0O0 )->decimal :#line:124
        return O000OOO000OO0O0O0 .TransToDecimal (O000OOO000OO0O0O0 .fBAS [34 ])#line:125
    def Get_TotAmtPre (O00OO0OOO00O0000O )->decimal :#line:127
        return O00OO0OOO00O0000O .TransToDecimal (O00OO0OOO00O0000O .fBAS [35 ])#line:128
    def Handle_BAS (O0OO000OOO0OOO0OO ,O0O0O0OO0OOOOO0O0 :str ):#line:130
        O0OO000OOO0OOO0OO .fBAS =O0O0O0OO0OOOOO0O0 .split ('|')#line:131
        O0OO000OOO0OOO0OO .fHasBAS =len (O0OO000OOO0OOO0OO .fBAS )>0 #line:132
        O0OO000OOO0OOO0OO .StkNo =O0OO000OOO0OOO0OO .fBAS [0 ]#line:133
        O0OO000OOO0OOO0OO .StkName =O0OO000OOO0OOO0OO .fBAS [1 ]#line:134
        O0OO000OOO0OOO0OO .RefPriceOrg =O0OO000OOO0OOO0OO .fBAS [4 ]#line:135
        O0OO000OOO0OOO0OO .LimitPrice_UpOrg =O0OO000OOO0OOO0OO .fBAS [5 ]#line:136
        O0OO000OOO0OOO0OO .LimitPrice_DownOrg =O0OO000OOO0OOO0OO .fBAS [6 ]#line:137
        O0OO000OOO0OOO0OO .IndustryCategory =O0OO000OOO0OOO0OO .fBAS [7 ]#line:138
        O0OO000OOO0OOO0OO .StockCategory =O0OO000OOO0OOO0OO .fBAS [8 ]#line:139
        O0OO000OOO0OOO0OO .StockAnomalyCode =O0OO000OOO0OOO0OO .fBAS [10 ]#line:140
        O0OO000OOO0OOO0OO .BoardRemark =O0OO000OOO0OOO0OO .fBAS [11 ]#line:141
        O0OO000OOO0OOO0OO .ClassRemark =O0OO000OOO0OOO0OO .fBAS [12 ]#line:142
        O0OO000OOO0OOO0OO .NonTenFaceValueIndicator =O0OO000OOO0OOO0OO .fBAS [13 ]#line:143
        O0OO000OOO0OOO0OO .AbnormalRecommendationIndicator =O0OO000OOO0OOO0OO .fBAS [14 ]#line:144
        O0OO000OOO0OOO0OO .AbnormalSecuritiesIndicator =O0OO000OOO0OOO0OO .fBAS [15 ]#line:145
        O0OO000OOO0OOO0OO .DayTradingIndicator =O0OO000OOO0OOO0OO .fBAS [16 ]#line:146
        O0OO000OOO0OOO0OO .TradingUnit =O0OO000OOO0OOO0OO .fBAS [30 ]#line:147
        O0OO000OOO0OOO0OO .TickSizeInfo =O0OO000OOO0OOO0OO .fBAS [33 ]#line:148
        O0OO000OOO0OOO0OO .TotQtyPre =O0OO000OOO0OOO0OO .fBAS [34 ]#line:149
        O0OO000OOO0OOO0OO .TotAmtPre =O0OO000OOO0OOO0OO .fBAS [35 ]#line:150
        O0OO000OOO0OOO0OO .RefPPre =O0OO000OOO0OOO0OO .fBAS [36 ]#line:151
        O0OO000OOO0OOO0OO .CPPre =O0OO000OOO0OOO0OO .fBAS [37 ]#line:152
    def TransToInt (O00000000O000OOOO ,O0O0000000O0OO0O0 :str )->int :#line:154
        try :#line:156
            return int (O0O0000000O0OO0O0 )#line:157
        except Exception as O0OO0O0O0O000OOO0 :#line:158
            pass #line:159
        return 0 #line:161
    def TransToDecimal (O000000OO00O000OO ,O0O0O0OO0OO0O00OO :str )->decimal :#line:163
        try :#line:164
            return Decimal (O0O0O0OO0OO0O00OO )#line:165
        except Exception as OO0O00O0O00OOO000 :#line:166
            print (f"Not a Decimal{OO0O00O0O00OOO000}")#line:167
        return 0 #line:168
class TStkQtHL ():#line:169
    HasHL =False #line:170
    fHL =[]#line:171
    TopicTX :str =""#line:172
    Topic5Q :str =""#line:173
    Market :str #line:175
    """市場別(TSE/OTC)"""#line:176
    StkKind :str #line:177
    """"證券別(S/W/Idx)"""#line:178
    Symbol :str #line:179
    """委託商品代碼(2330)"""#line:180
    DealTime :str #line:181
    """撮合時間(成交)(EX:173547.32700)"""#line:182
    DealSn :str #line:183
    """成交序號"""#line:184
    def Get_DealSn (OOO000OOOOO0OO00O )->int :#line:186
        return OOO000OOOOO0OO00O .TransToInt (OOO000OOOOO0OO00O .fHL [4 ])#line:187
    Sn_5Q :str #line:188
    """五檔序號(指數類=空字串)"""#line:189
    def Get_Sn_5Q (O00OO00O0O0O000O0 )->int :#line:191
        return O00OO00O0O0O000O0 .TransToInt (O00OO00O0O0O000O0 .fHL [5 ])#line:192
    DealPriceOrg :str #line:193
    """成交價"""#line:194
    def Get_DealPrice (O00OO00O000000OOO )->decimal :#line:196
        return O00OO00O000000OOO .TransToDecimal (O00OO00O000000OOO .fHL [6 ])#line:197
    DealPrice :decimal #line:200
    """成交價"""#line:201
    DealQty :str #line:202
    """成交單量(指數類=0)"""#line:203
    def Get_DealQty2Dec (O00O0O00O0O0O0O00 )->decimal :#line:205
        return O00O0O00O0O0O0O00 .TransToDecimal (O00O0O00O0O0O0O00 .fHL [7 ])#line:206
    def Get_DealQty2Int (O0O0O0OO00000O0O0 )->int :#line:208
        return O0O0O0OO00000O0O0 .TransToInt (O0O0O0OO00000O0O0 .fHL [7 ])#line:209
    HighPriceOrg :str #line:211
    """當日最高價"""#line:212
    def Get_HighPrice (OOOO00O0000OO0O00 )->decimal :#line:214
        return OOOO00O0000OO0O00 .TransToDecimal (OOOO00O0000OO0O00 .fHL [8 ])#line:215
    LowPriceOrg :str #line:217
    """當日最低價"""#line:218
    def Get_LowPrice (O00OO00OO0OOOOOO0 )->decimal :#line:220
        return O00OO00OO0OOOOOO0 .TransToDecimal (O00OO00OO0OOOOOO0 .fHL [9 ])#line:221
    TotAmt :str #line:223
    """成交總額(指數類=0)"""#line:224
    def Get_TotAmt2Dec (OO00O0OO0OOOO0O00 )->decimal :#line:226
        return OO00O0OO0OOOO0O00 .TransToDecimal (OO00O0OO0OOOO0O00 .fHL [10 ])#line:227
    def Get_TotAmt2Int (OO00OO000OOOO0O00 )->int :#line:229
        return OO00OO000OOOO0O00 .TransToInt (OO00OO000OOOO0O00 .fHL [10 ])#line:230
    TotQty :str #line:232
    """成交總量(指數類=0)"""#line:233
    def Get_TotQty2Dec (OOOO00O0O0OO0000O )->decimal :#line:235
        return OOOO00O0O0OO0000O .TransToDecimal (OOOO00O0O0OO0000O .fHL [11 ])#line:236
    def Get_TotQty2Int (O00O000O00O0OO0O0 )->int :#line:238
        return O00O000O00O0OO0O0 .TransToInt (O00O000O00O0OO0O0 .fHL [11 ])#line:239
    FirstDerivedBuyPrice :str #line:242
    "衍生委託單第一檔買進價格"#line:243
    FirstDerivedBuyQty :str #line:244
    "衍生委託單第一檔買進價格數量"#line:245
    FirstDerivedSellPrice :str #line:246
    "衍生委託單第一檔賣出價格數量"#line:247
    FirstDerivedSellQty :str #line:248
    "衍生委託單第一檔賣出價格數量"#line:249
    OpenPriceOrg :str #line:251
    """開盤價"""#line:252
    def Get_OpenPrice (O000OOOOOOO0OO0O0 )->decimal :#line:254
        return O000OOOOOOO0OO0O0 .TransToDecimal (O000OOOOOOO0OO0O0 .fHL [42 ])#line:255
    TryMark_Deal :str #line:257
    "成交試撮註記(試撮=1, 非試撮=0)"#line:258
    TryMark_5Q :str #line:259
    "五檔試撮註記(試撮=1, 非試撮=0)"#line:260
    fAryB5Q_P =[13 ,15 ,17 ,19 ,21 ]#line:263
    """買五檔價在字串中的位置"""#line:264
    fAryB5Q_Q =[14 ,16 ,18 ,20 ,22 ]#line:265
    """買五檔價在字串中的位置"""#line:266
    """買5檔的檔數"""#line:268
    B5QCountOrg :str #line:269
    """買5檔的檔數(指數類=0)"""#line:270
    B5QCount =0 #line:271
    """買5檔的檔數(指數類=0)"""#line:272
    def B5Q_POrg (OO0OO00O000OOO000 ,O00O00OO0O0OOOOOO :int )->str :#line:274
        ""#line:275
        if O00O00OO0O0OOOOOO >OO0OO00O000OOO000 .B5QCount :#line:276
            return ""#line:277
        else :#line:278
            return OO0OO00O000OOO000 .fHL [OO0OO00O000OOO000 .fAryB5Q_P [O00O00OO0O0OOOOOO -1 ]]#line:279
    def Get_B5Q_P (OOO0OO0O00O00OOO0 ,O00OOOOO0OOOO0OO0 :int )->decimal :#line:281
        ""#line:282
        if O00OOOOO0OOOO0OO0 >OOO0OO0O00O00OOO0 .B5QCount :#line:283
            return 0 #line:284
        else :#line:285
            return OOO0OO0O00O00OOO0 .TransToDecimal (OOO0OO0O00O00OOO0 .fHL [OOO0OO0O00O00OOO0 .fAryB5Q_P [O00OOOOO0OOOO0OO0 -1 ]])#line:286
    def B5Q_QOrg (O0O0000OO00OOOO00 ,O00O000OO0000O0O0 :int )->str :#line:288
        ""#line:289
        if (O00O000OO0000O0O0 >O0O0000OO00OOOO00 .B5QCount ):#line:290
            return ""#line:291
        else :#line:292
            return O0O0000OO00OOOO00 .fHL [O0O0000OO00OOOO00 .fAryB5Q_Q [O00O000OO0000O0O0 -1 ]]#line:293
    def Get_B5Q_Q (OOO00OOO0O0OOO000 ,O0OO0O00OOO0O0000 :int )->int :#line:295
        ""#line:296
        if (O0OO0O00OOO0O0000 >OOO00OOO0O0OOO000 .B5QCount ):#line:297
            return 0 #line:298
        else :#line:299
            return OOO00OOO0O0OOO000 .TransToInt (OOO00OOO0O0OOO000 .fHL [OOO00OOO0O0OOO000 .fAryB5Q_Q [O0OO0O00OOO0O0000 -1 ]])#line:300
    fAryS5Q_P =[24 ,26 ,28 ,30 ,32 ]#line:303
    """賣五檔價在字串中的位置"""#line:304
    fAryS5Q_Q =[25 ,27 ,29 ,31 ,33 ]#line:305
    """賣五檔價在字串中的位置"""#line:306
    S5QCountOrg :str #line:308
    """賣5檔的檔數(指數類=0)"""#line:309
    S5QCount :int #line:310
    def S5Q_POrg (O00OO00O00OO0O0O0 ,OOO00OO0OO0OO0O0O :int )->str :#line:312
        ""#line:313
        if OOO00OO0OO0OO0O0O >O00OO00O00OO0O0O0 .S5QCount :#line:314
            return ""#line:315
        else :#line:316
            return O00OO00O00OO0O0O0 .fHL [O00OO00O00OO0O0O0 .fAryS5Q_P [OOO00OO0OO0OO0O0O -1 ]]#line:317
    def Get_S5Q_P (OOO0OOO0O0OOO0OOO ,OO00OOO00OO00OOO0 :int )->decimal :#line:319
        ""#line:320
        if OO00OOO00OO00OOO0 >OOO0OOO0O0OOO0OOO .S5QCount :#line:321
            return 0 #line:322
        else :#line:323
            return OOO0OOO0O0OOO0OOO .TransToDecimal (OOO0OOO0O0OOO0OOO .fHL [OOO0OOO0O0OOO0OOO .fAryS5Q_P [OO00OOO00OO00OOO0 -1 ]])#line:324
    def S5Q_QOrg (OO0O0OOOO00O00OO0 ,OO00OOOO0OO00O000 :int )->str :#line:326
        ""#line:327
        if OO00OOOO0OO00O000 >OO0O0OOOO00O00OO0 .S5QCount :#line:328
            return ""#line:329
        else :#line:330
            return OO0O0OOOO00O00OO0 .fHL [OO0O0OOOO00O00OO0 .fAryS5Q_Q [OO00OOOO0OO00O000 -1 ]]#line:331
    def Get_S5Q_Q (OOOO0O0O0OOO0OO00 ,O0OOO00O00OO0OO0O :int )->int :#line:333
        ""#line:334
        if O0OOO00O00OO0OO0O >OOOO0O0O0OOO0OO00 .fS5QCount :#line:335
            return 0 #line:336
        else :#line:337
            return OOOO0O0O0OOO0OO00 .TransToInt (OOOO0O0O0OOO0OO00 .fHL [OOOO0O0O0OOO0OO00 .fAryS5Q_Q [O0OOO00O00OO0OO0O -1 ]])#line:338
    WholeTotAmt :str #line:342
    """整體市場成交總額"""#line:343
    def Get_WholeTotAmt (O00O0O0OOO00O0000 )->int :#line:345
        return O00O0O0OOO00O0000 .TransToInt (O00O0O0OOO00O0000 .fHL [34 ])#line:346
    WholeTotQty :str #line:348
    """整體市場成交數量"""#line:349
    def Get_WholeTotQty (O00OOOO00O000OOO0 )->int :#line:351
        return O00OOOO00O000OOO0 .TransToInt (O00OOOO00O000OOO0 .fHL [35 ])#line:352
    WholeDealCount :str #line:354
    """整體市場成交筆數"""#line:355
    def Get_WholeDealCount (O0O00OO0OOO0O0000 )->int :#line:357
        return O0O00OO0OOO0O0000 .TransToInt (O0O00OO0OOO0O0000 .fHL [36 ])#line:358
    SumBuyOrderCount :str #line:360
    """整體市場委託買進筆數"""#line:361
    def Get_SumBuyOrderCount (OOOO0OO000O0000OO )->int :#line:363
        return OOOO0OO000O0000OO .TransToInt (OOOO0OO000O0000OO .fHL [37 ])#line:364
    SumSellOrderCount :str #line:366
    """整體市場委託賣出筆數"""#line:367
    def Get_SumSellOrderCount (OO0OO00O00OO0O0OO )->int :#line:369
        return OO0OO00O00OO0O0OO .TransToInt (OO0OO00O00OO0O0OO .fHL [38 ])#line:370
    SumBuyOrderQty :str #line:372
    """整體市場委託買進數量"""#line:373
    def Get_SumBuyOrderQty (OO0O000O0OO0OO0O0 )->int :#line:375
        return OO0O000O0OO0OO0O0 .TransToInt (OO0O000O0OO0OO0O0 .fHL [39 ])#line:376
    SumSellOrderQty :str #line:378
    """整體市場委託賣出數量"""#line:379
    def Get_SumSellOrderQty (OO0OOO0OOOOO000OO )->int :#line:381
        return OO0OOO0OOOOO000OO .TransToInt (OO0OOO0OOOOO000OO .fHL [40 ])#line:382
    def Handle_HL (OOO0OOO00OOO0O000 ,OO000OOOOO0OO0000 :str ):#line:385
        OOO0OOO00OOO0O000 .fHL =OO000OOOOO0OO0000 .split ('|')#line:386
        OOO0OOO00OOO0O000 .HasHL =len (OOO0OOO00OOO0O000 .fHL )>0 #line:387
        OOO0OOO00OOO0O000 .Market =OOO0OOO00OOO0O000 .fHL [0 ]#line:389
        OOO0OOO00OOO0O000 .StkKind =OOO0OOO00OOO0O000 .fHL [1 ]#line:390
        OOO0OOO00OOO0O000 .Symbol =OOO0OOO00OOO0O000 .fHL [2 ]#line:391
        OOO0OOO00OOO0O000 .DealTime =OOO0OOO00OOO0O000 .fHL [3 ]#line:392
        OOO0OOO00OOO0O000 .DealSn =OOO0OOO00OOO0O000 .fHL [4 ]#line:393
        OOO0OOO00OOO0O000 .Sn_5Q =OOO0OOO00OOO0O000 .fHL [5 ]#line:394
        OOO0OOO00OOO0O000 .DealPriceOrg =OOO0OOO00OOO0O000 .fHL [6 ]#line:395
        OOO0OOO00OOO0O000 .DealPrice =OOO0OOO00OOO0O000 .TransToDecimal (OOO0OOO00OOO0O000 .DealPriceOrg )#line:396
        OOO0OOO00OOO0O000 .DealQty =OOO0OOO00OOO0O000 .fHL [7 ]#line:397
        OOO0OOO00OOO0O000 .HighPriceOrg =OOO0OOO00OOO0O000 .fHL [8 ]#line:398
        OOO0OOO00OOO0O000 .LowPriceOrg =OOO0OOO00OOO0O000 .fHL [9 ]#line:399
        OOO0OOO00OOO0O000 .TotAmt =OOO0OOO00OOO0O000 .fHL [10 ]#line:400
        OOO0OOO00OOO0O000 .TotQty =OOO0OOO00OOO0O000 .fHL [11 ]#line:401
        OOO0OOO00OOO0O000 .FirstDerivedBuyPrice =OOO0OOO00OOO0O000 .fHL [35 ]#line:402
        OOO0OOO00OOO0O000 .FirstDerivedBuyQty =OOO0OOO00OOO0O000 .fHL [36 ]#line:403
        OOO0OOO00OOO0O000 .FirstDerivedSellPrice =OOO0OOO00OOO0O000 .fHL [37 ]#line:404
        OOO0OOO00OOO0O000 .FirstDerivedSellQty =OOO0OOO00OOO0O000 .fHL [38 ]#line:405
        OOO0OOO00OOO0O000 .B5QCountOrg =OOO0OOO00OOO0O000 .fHL [12 ]#line:407
        OOO0OOO00OOO0O000 .B5QCount =OOO0OOO00OOO0O000 .TransToInt (OOO0OOO00OOO0O000 .B5QCountOrg )#line:408
        OOO0OOO00OOO0O000 .S5QCountOrg =OOO0OOO00OOO0O000 .fHL [23 ]#line:409
        OOO0OOO00OOO0O000 .S5QCount =OOO0OOO00OOO0O000 .TransToInt (OOO0OOO00OOO0O000 .S5QCountOrg )#line:410
        OOO0OOO00OOO0O000 .WholeTotAmt =OOO0OOO00OOO0O000 .fHL [34 ]#line:411
        OOO0OOO00OOO0O000 .WholeTotQty =OOO0OOO00OOO0O000 .fHL [35 ]#line:412
        OOO0OOO00OOO0O000 .WholeDealCount =OOO0OOO00OOO0O000 .fHL [36 ]#line:413
        OOO0OOO00OOO0O000 .SumBuyOrderCount =OOO0OOO00OOO0O000 .fHL [37 ]#line:414
        OOO0OOO00OOO0O000 .SumSellOrderCount =OOO0OOO00OOO0O000 .fHL [38 ]#line:415
        OOO0OOO00OOO0O000 .SumBuyOrderQty =OOO0OOO00OOO0O000 .fHL [39 ]#line:416
        OOO0OOO00OOO0O000 .SumSellOrderQty =OOO0OOO00OOO0O000 .fHL [40 ]#line:417
        OOO0OOO00OOO0O000 .OpenPriceOrg =OOO0OOO00OOO0O000 .fHL [42 ]#line:419
        OOO0OOO00OOO0O000 .TryMark_Deal =OOO0OOO00OOO0O000 .fHL [43 ]#line:420
        OOO0OOO00OOO0O000 .TryMark_5Q =OOO0OOO00OOO0O000 .fHL [44 ]#line:421
        if OOO0OOO00OOO0O000 .HasHL :#line:422
            OOO0OOO00OOO0O000 .TopicTX =f"Quote/TWS/{OOO0OOO00OOO0O000.StkKind}/{OOO0OOO00OOO0O000.Market}/{OOO0OOO00OOO0O000.Symbol}/TX"#line:423
            OOO0OOO00OOO0O000 .Topic5Q =f"Quote/TWS/{OOO0OOO00OOO0O000.StkKind}/{OOO0OOO00OOO0O000.Market}/{OOO0OOO00OOO0O000.Symbol}/5Q"#line:424
    def TransToInt (O00O0O00O00OOOOOO ,O0O0O000OO0000O00 :str )->int :#line:428
        try :#line:429
            return int (O0O0O000OO0000O00 )#line:430
        except Exception as OOO0O00O00OOO0O00 :#line:431
            return 0 #line:432
    def TransToDecimal (O000O0O000OO00O00 ,OO0O0O0OO000O00OO :str )->decimal :#line:434
        try :#line:435
            return Decimal (OO0O0O0OO000O00OO )#line:436
        except Exception as O0OO0OOO0OOO00O0O :#line:437
            return 0 #line:438
    def __init__ (O000000OO00OOO0O0 )->None :#line:441
        pass #line:442
    def __str__ (OO00O0OOO0000O00O )->str :#line:444
        return f"""Market:{OO00O0OOO0000O00O.Market} StkKind:{OO00O0OOO0000O00O.StkKind} Symbol:{OO00O0OOO0000O00O.Symbol} DealTime:{OO00O0OOO0000O00O.DealTime}"""+"""DealSn:{self.DealSn} Sn_5Q:{self.Sn_5Q} DealPriceOrg:{self.DealPriceOrg} DealQty:{self.DealQty}"""+"""HighPriceOrg:{self.HighPriceOrg} LowPriceOrg:{self.LowPriceOrg} TotAmt:{self.TotAmt} TotQty:{self.TotQty}"""+"""B5QCountOrg:{self.B5QCountOrg} S5QCount:{self.S5QCount} WholeTotAmt:{self.WholeTotAmt} WholeTotQty:{self.WholeTotQty}"""+"""WholeDealCount:{self.WholeDealCount} SumBuyOrderCount:{self.SumBuyOrderCount} SumSellOrderCount:{self.SumSellOrderCount}"""+"""SumBuyOrderQty:{self.SumBuyOrderQty} SumSellOrderQty:{self.SumSellOrderQty} OpenPriceOrg:{self.OpenPriceOrg}"""#line:450
class TStkQtTX :#line:451
    fTX =[]#line:452
    HL_Sn_5Q =0 #line:453
    """來自HL回補的5檔序號(當收到即時成交行情時,若帶五檔行情,需判斷是否比HL紀錄的還大, 若比較小, 表示很久沒有成交行情, 但五檔一直在變動, 則不可使用成交行情裡的五檔資料)"""#line:454
    HL_TotAmt :decimal =0 #line:455
    """來自HL的成交總額，用於累加收到成交行情時的成交價*成交單量*交易單位"""#line:456
    BAS_TradingUnit =1 #line:457
    """來自BAS的交易單位用，用於累加收到成交行情時的成交價*成交單量*交易單位"""#line:458
    def Handle_TXRcv (OO0O00O0000O000OO ,O0000O0O00000O0OO :str ):#line:460
        ""#line:461
        try :#line:462
            O0OO0OOOOOO0OO000 :int =0 #line:463
            OOOOOOO0OOO00O0O0 :int =0 #line:464
            OOO00OO0OOOO0OOO0 =O0000O0O00000O0OO .split ('|')#line:465
            if OOO00OO0OOOO0OOO0 [4 ]==TSolQuoteStkSet .TryMark_No :#line:467
                OO0O00O0000O000OO .fPROC_HandleData =OO0O00O0000O000OO .HandleData #line:468
                if OO0O00O0000O000OO .fTX ==None :#line:470
                    OO0O00O0000O000OO .fTX =OOO00OO0OOOO0OOO0 #line:471
                    OO0O00O0000O000OO .SetData ()#line:472
                else :#line:473
                    OOOOOOO0OOO00O0O0 =OO0O00O0000O000OO .TransToInt (OOO00OO0OOOO0OOO0 [3 ])#line:474
                    O0OO0OOOOOO0OO000 =OO0O00O0000O000OO .Get_DealSn ()#line:475
                    if OOOOOOO0OOO00O0O0 >O0OO0OOOOOO0OO000 :#line:476
                        OO0O00O0000O000OO .fTX =OOO00OO0OOOO0OOO0 #line:477
                        OO0O00O0000O000OO .SetData ()#line:478
                OO0O00O0000O000OO .fPROC_CalcHightLowPrice ()#line:480
                OO0O00O0000O000OO .CalTotalTradingAmount ()#line:481
                O0OO0OOOOOO0OO000 =OO0O00O0000O000OO .Get_DealSn ()#line:484
                if O0OO0OOOOOO0OO000 >=OO0O00O0000O000OO .HL_Sn_5Q :#line:485
                    OO0O00O0000O000OO .fB5QCount =OO0O00O0000O000OO .TransToInt (OO0O00O0000O000OO .B5QCountOrg )#line:487
                    OO0O00O0000O000OO .fS5QCount =OO0O00O0000O000OO .TransToInt (OO0O00O0000O000OO .S5QCountOrg )#line:489
                else :#line:490
                    OO0O00O0000O000OO .fB5QCount =0 #line:491
                    OO0O00O0000O000OO .fS5QCount =0 #line:492
            else :#line:493
                OO0O00O0000O000OO .fPROC_HandleData =OO0O00O0000O000OO .HandleData_TryMarket #line:494
                OO0O00O0000O000OO .fPROC_HandleData (O0000O0O00000O0OO )#line:495
        except Exception as O00OO000OO0O0O0OO :#line:496
            pass #line:497
    def Handle_TX (O00O0O0000O000OOO ,O0OOO000O00OO0O0O :str ):#line:499
        ""#line:500
        O00O0O0000O000OOO .fPROC_HandleData (O0OOO000O00OO0O0O )#line:501
    def HandleData_TryMarket (O00OOOOO0000O0O0O ,OOO00OOOOO000O0OO :str ):#line:505
        ""#line:506
        if OOO00OOOOO000O0OO .split ('|')[4 ]==TSolQuoteStkSet .TryMark_No :#line:507
            OO0OO00OOOOOO0O00 =O00OOOOO0000O0O0O .HandleData #line:508
            OO0OO00OOOOOO0O00 (OOO00OOOOO000O0OO )#line:509
        else :#line:510
            O00OOOOO0000O0O0O .fTX =OOO00OOOOO000O0OO .split ('|')#line:511
            O00OOOOO0000O0O0O .SetData ()#line:512
            O00OOOOO0000O0O0O .B5QCount =O00OOOOO0000O0O0O .TransToInt (O00OOOOO0000O0O0O .B5QCountOrg )#line:513
            O00OOOOO0000O0O0O .S5QCount =O00OOOOO0000O0O0O .TransToInt (O00OOOOO0000O0O0O .S5QCountOrg )#line:514
    def HandleData (O0OOOO0O00000O0OO ,O0000O0OO0000O000 :str ):#line:516
        ""#line:517
        O0OOOO0O00000O0OO .fTX =O0000O0OO0000O000 .split ('|')#line:518
        O0OOOO0O00000O0OO .SetData ()#line:519
        O0OOOO0O00000O0OO .fPROC_CalcHightLowPrice ()#line:520
        O0OOOO0O00000O0OO .CalTotalTradingAmount ()#line:521
        O0OOOO0O00000O0OO .B5QCount =O0OOOO0O00000O0OO .TransToInt (O0OOOO0O00000O0OO .B5QCountOrg )#line:522
        O0OOOO0O00000O0OO .S5QCount =O0OOOO0O00000O0OO .TransToInt (O0OOOO0O00000O0OO .S5QCountOrg )#line:523
    def SetData (OOO0O0000O00OO00O ):#line:525
        OOO0O0000O00OO00O .SysTime =OOO0O0000O00OO00O .fTX [1 ]#line:526
        OOO0O0000O00OO00O .DealTime =OOO0O0000O00OO00O .fTX [2 ]#line:527
        OOO0O0000O00OO00O .DealSn =OOO0O0000O00OO00O .fTX [3 ]#line:528
        OOO0O0000O00OO00O .TryMark =OOO0O0000O00OO00O .fTX [4 ]#line:529
        OOO0O0000O00OO00O .Has5Q =OOO0O0000O00OO00O .fTX [5 ]#line:530
        OOO0O0000O00OO00O .TotQty =OOO0O0000O00OO00O .fTX [9 ]#line:531
        OOO0O0000O00OO00O .DealPriceOrg =OOO0O0000O00OO00O .fTX [10 ]#line:532
        OOO0O0000O00OO00O .DealQty =OOO0O0000O00OO00O .fTX [11 ]#line:533
        OOO0O0000O00OO00O .B5QCountOrg =OOO0O0000O00OO00O .fTX [12 ]#line:534
        OOO0O0000O00OO00O .S5QCountOrg =OOO0O0000O00OO00O .fTX [23 ]#line:535
        OOO0O0000O00OO00O .WholeTotAmt =OOO0O0000O00OO00O .fTX [34 ]#line:537
        OOO0O0000O00OO00O .WholeTotQty =OOO0O0000O00OO00O .fTX [35 ]#line:538
        OOO0O0000O00OO00O .WholeDealCount =OOO0O0000O00OO00O .fTX [36 ]#line:539
        OOO0O0000O00OO00O .SumBuyOrderCount =OOO0O0000O00OO00O .fTX [37 ]#line:540
        OOO0O0000O00OO00O .SumSellOrderCount =OOO0O0000O00OO00O .fTX [38 ]#line:541
        OOO0O0000O00OO00O .SumBuyOrderQty =OOO0O0000O00OO00O .fTX [39 ]#line:542
        OOO0O0000O00OO00O .SumSellOrderQty =OOO0O0000O00OO00O .fTX [40 ]#line:543
        OOO0O0000O00OO00O .IsFixedPriceTransaction =OOO0O0000O00OO00O .fTX [41 ]#line:544
    fPROC_HandleData :callable =None #line:547
    """PROC_HandleData"""#line:548
    SysTime :str #line:552
    """系統時間Unix Timestamp(us)(EX:1642553376085607)"""#line:553
    DealTime :str #line:554
    """撮合時間(成交)(EX:085229.843665)"""#line:555
    DealSn :str #line:556
    """序號(成交序號、5檔序號)"""#line:557
    def Get_DealSn (OO0OOO0000O0O0OOO )->int :#line:559
        return OO0OOO0000O0O0OOO .TransToInt (OO0OOO0000O0O0OOO .fTX [3 ])#line:560
    TryMark ="1"#line:561
    """試撮註記(試撮=1, 非試撮=0)"""#line:562
    Has5Q :str #line:563
    """五檔揭示註記(揭示=1, 不揭示=0)"""#line:564
    TotQty :str #line:565
    """成交總量"""#line:566
    def Get_TotQty2Dec (OO00O00000OOOOOOO )->decimal :#line:568
        return OO00O00000OOOOOOO .TransToDecimal (OO00O00000OOOOOOO .fTX [9 ])#line:569
    def Get_TotQty2Int (O0OO0OOO0O0000OO0 )->int :#line:571
        return O0OO0OOO0O0000OO0 .TransToInt (O0OO0OOO0O0000OO0 .fTX [9 ])#line:572
    DealPriceOrg :str #line:574
    """成交價"""#line:575
    def Get_DealPrice (OO0OOO0O0O00OO000 )->decimal :#line:577
        return OO0OOO0O0O00OO000 .TransToDecimal (OO0OOO0O0O00OO000 .fTX [10 ])#line:578
    DealQty :str #line:580
    """成交單量"""#line:581
    def Get_DealQty2Dec (O00OOOO0000OOOOO0 )->decimal :#line:583
        return O00OOOO0000OOOOO0 .TransToDecimal (O00OOOO0000OOOOO0 .fTX [11 ])#line:584
    def Get_DealQty2Int (O000OOO0000OO000O )->int :#line:586
        return O000OOO0000OO000O .TransToInt (O000OOO0000OO000O .fTX [11 ])#line:587
    fAryB5Q_P =[13 ,15 ,17 ,19 ,21 ]#line:591
    """買五檔價在字串中的位置"""#line:592
    fAryB5Q_Q =[14 ,16 ,18 ,20 ,22 ]#line:593
    """買五檔價在字串中的位置"""#line:594
    B5QCountOrg :str #line:597
    """買5檔的檔數"""#line:598
    B5QCount :int #line:599
    """買5檔的檔數"""#line:600
    def B5Q_POrg (O000OO0O00O0O000O ,OO000OO00O00O0OO0 :int )->str :#line:602
        ""#line:603
        if (OO000OO00O00O0OO0 >O000OO0O00O0O000O .B5QCount ):#line:604
            return ""#line:605
        else :#line:606
            return O000OO0O00O0O000O .fTX [O000OO0O00O0O000O .fAryB5Q_P [OO000OO00O00O0OO0 -1 ]]#line:607
    def Get_B5Q_P (OOOO0OOOO0O00OOO0 ,O000000OOO0OOO0O0 :int )->decimal :#line:609
        ""#line:610
        if (O000000OOO0OOO0O0 >OOOO0OOOO0O00OOO0 .B5QCount ):#line:611
            return 0 #line:612
        else :#line:613
            return OOOO0OOOO0O00OOO0 .TransToDecimal (OOOO0OOOO0O00OOO0 .fTX [OOOO0OOOO0O00OOO0 .fAryB5Q_P [O000000OOO0OOO0O0 -1 ]])#line:614
    def B5Q_QOrg (OOO0O00OOO0OOOOO0 ,OO00O0O000O000OOO :int )->str :#line:616
        ""#line:617
        if (OO00O0O000O000OOO >OOO0O00OOO0OOOOO0 .B5QCount ):#line:618
            return ""#line:619
        else :#line:620
            return OOO0O00OOO0OOOOO0 .fTX [OOO0O00OOO0OOOOO0 .fAryB5Q_Q [OO00O0O000O000OOO -1 ]]#line:621
    def Get_B5Q_Q (OO0OO0OOOO000O00O ,O0OOOOOO00OOO0OO0 :int )->int :#line:623
        ""#line:624
        if (O0OOOOOO00OOO0OO0 >OO0OO0OOOO000O00O .B5QCount ):#line:625
            return 0 #line:626
        else :#line:627
            return OO0OO0OOOO000O00O .TransToInt (OO0OO0OOOO000O00O .fTX [OO0OO0OOOO000O00O .fAryB5Q_Q [O0OOOOOO00OOO0OO0 -1 ]])#line:628
    fAryS5Q_P =[24 ,26 ,28 ,30 ,32 ]#line:632
    """賣五檔價在字串中的位置"""#line:633
    fAryS5Q_Q =[25 ,27 ,29 ,31 ,33 ]#line:634
    """賣五檔價在字串中的位置"""#line:635
    S5QCountOrg :str #line:638
    """賣5檔的檔數"""#line:639
    S5QCount :int #line:640
    """賣5檔的檔數"""#line:641
    def S5Q_POrg (OOOO0OO0OO00O0O00 ,OOOO0O0O00000OO00 :int )->str :#line:643
        ""#line:644
        if (OOOO0O0O00000OO00 >OOOO0OO0OO00O0O00 .S5QCount ):#line:645
            return ""#line:646
        else :#line:647
            return OOOO0OO0OO00O0O00 .fTX [OOOO0OO0OO00O0O00 .fAryS5Q_P [OOOO0O0O00000OO00 -1 ]]#line:648
    def Get_S5Q_P (O000OOO00OO0000OO ,OO00O0O0O00OOOOOO :int )->decimal :#line:650
        ""#line:651
        if (OO00O0O0O00OOOOOO >O000OOO00OO0000OO .S5QCount ):#line:652
            return 0 #line:653
        else :#line:654
            return O000OOO00OO0000OO .TransToDecimal (O000OOO00OO0000OO .fTX [O000OOO00OO0000OO .fAryS5Q_P [OO00O0O0O00OOOOOO -1 ]])#line:655
    def S5Q_QOrg (OO0OOOOO0000OOO00 ,OOOO00OOOO0OO0000 :int )->str :#line:657
        ""#line:658
        if (OOOO00OOOO0OO0000 >OO0OOOOO0000OOO00 .S5QCount ):#line:659
            return ""#line:660
        else :#line:661
            return OO0OOOOO0000OOO00 .fTX [OO0OOOOO0000OOO00 .fAryS5Q_Q [OOOO00OOOO0OO0000 -1 ]]#line:662
    def Get_S5Q_Q (OOO0O0OO0OO000O00 ,O0O00OO0000O0OO0O :int )->int :#line:664
        ""#line:665
        if (O0O00OO0000O0OO0O >OOO0O0OO0OO000O00 .S5QCount ):#line:666
            return 0 #line:667
        else :#line:668
            return OOO0O0OO0OO000O00 .TransToInt (OOO0O0OO0OO000O00 .fTX [OOO0O0OO0OO000O00 .fAryS5Q_Q [O0O00OO0000O0OO0O -1 ]])#line:669
    fDealPrice =0 #line:673
    """成交價"""#line:674
    HighPrice =0 #line:675
    """當日最高價"""#line:676
    LowPrice =0 #line:677
    """當日最低價"""#line:678
    def CalcHightLowPrice (OO0O00O000O0O0000 ):#line:680
        ""#line:681
        try :#line:682
            OO00O0OO0OOO00O00 =OO0O00O000O0O0000 .Get_DealPrice ()#line:683
            OO0O00O000O0O0000 .HighPrice =math .Max (OO00O0OO0OOO00O00 ,OO0O00O000O0O0000 .HighPrice )#line:684
            if OO0O00O000O0O0000 .LowPrice ==0 :#line:685
                OO0O00O000O0O0000 .LowPrice =OO00O0OO0OOO00O00 #line:686
            else :#line:687
                OO0O00O000O0O0000 .LowPrice =math .Min (OO00O0OO0OOO00O00 ,OO0O00O000O0O0000 .LowPrice )#line:688
        except :#line:690
            pass #line:691
    def CalcHightLowPrice_None (O0OO000OO00OO0O0O ):#line:693
        pass #line:694
    fPROC_CalcHightLowPrice :callable =None #line:697
    """PROC_CalcHightLowPrice """#line:698
    fDealQty :int =0 #line:703
    def CalTotalTradingAmount (O00000O0000OOO0O0 ):#line:706
        ""#line:707
        try :#line:709
            O00000O0000OOO0O0 .fDealQty =O00000O0000OOO0O0 .Get_DealQty2Int ()#line:710
            O00000O0000OOO0O0 .HL_TotAmt +=O00000O0000OOO0O0 .fDealPrice *O00000O0000OOO0O0 .fDealQty *O00000O0000OOO0O0 .BAS_TradingUnit #line:713
        except Exception as O000O0O000O0O0OO0 :#line:714
            pass #line:715
    WholeTotAmt :str #line:720
    "整體市場成交總額"#line:721
    def Get_WholeTotAmt (OOOO0000OO0OO000O )->int :#line:722
        return OOOO0000OO0OO000O .TransToInt (OOOO0000OO0OO000O .fTX [34 ])#line:723
    WholeTotQty :str #line:724
    "整體市場成交數量"#line:725
    def Get_WholeTotQty (OO00O0O00O0O0000O )->int :#line:726
        return OO00O0O00O0O0000O .TransToInt (OO00O0O00O0O0000O .fTX [35 ])#line:727
    WholeDealCount :str #line:728
    "整體市場成交筆數"#line:729
    def Get_WholeDealCount (OOO000O0O0O0OO000 )->int :#line:730
        return OOO000O0O0O0OO000 .TransToInt (OOO000O0O0O0OO000 .fTX [36 ])#line:731
    SumBuyOrderCount :str #line:732
    "整體市場委託買進筆數"#line:733
    def Get_SumBuyOrderCount (O0O0O0O0OOO00O000 )->int :#line:734
        return O0O0O0O0OOO00O000 .TransToInt (O0O0O0O0OOO00O000 .fTX [37 ])#line:735
    SumSellOrderCount :str #line:736
    "整體市場委託賣出筆數"#line:737
    def Get_SumSellOrderCount (O00000OOO00O00O00 )->int :#line:738
        return O00000OOO00O00O00 .TransToInt (O00000OOO00O00O00 .fTX [38 ])#line:739
    SumBuyOrderQty :str #line:740
    "整體市場委託買進數量"#line:741
    def Get_SumBuyOrderQty (O0OO00000OO00OOO0 ):#line:742
        return O0OO00000OO00OOO0 .TransToInt (O0OO00000OO00OOO0 .fTX [39 ])#line:743
    SumSellOrderQty :str #line:744
    "整體市場委託賣出數量"#line:745
    def Get_SumSellOrderQty (OOO000O00000O0OO0 ):#line:746
        return OOO000O00000O0OO0 .TransToInt (OOO000O00000O0OO0 .fTX [40 ])#line:747
    IsFixedPriceTransaction :str #line:748
    "是否為定盤交易"#line:749
    def TransToInt (O00OO0OOO000OOO0O ,O0OO0OOO0O0OOO0O0 :str )->int :#line:754
        try :#line:755
            return int (O0OO0OOO0O0OOO0O0 )#line:756
        except Exception as OOOOO000OOO00000O :#line:757
            return 0 #line:758
    def TransToDecimal (OO00000O00000OO0O ,OOO00O0OOO0OO00O0 :str )->decimal :#line:760
        try :#line:761
            return Decimal (OOO00O0OOO0OO00O0 )#line:762
        except Exception as O0OOOO0OO00000O00 :#line:763
            return 0 #line:764
    def __init__ (O0O000O0OOOOOOOO0 ,OOOO0OOOO00OO0O0O :bool )->None :#line:767
        O0O000O0OOOOOOOO0 .fPROC_CalcHightLowPrice =O0O000O0OOOOOOOO0 .CalcHightLowPrice_None #line:768
        if OOOO0OOOO00OO0O0O :#line:769
            O0O000O0OOOOOOOO0 .fPROC_CalcHightLowPrice =O0O000O0OOOOOOOO0 .CalcHightLowPrice #line:770
        O0O000O0OOOOOOOO0 .fPROC_HandleData =O0O000O0OOOOOOOO0 .HandleData_TryMarket #line:772
    def __str__ (OO0O0O0O0000000O0 )->str :#line:774
        return f"""SysTime:{OO0O0O0O0000000O0.SysTime} DealTime:{OO0O0O0O0000000O0.DealTime} DealSn:{OO0O0O0O0000000O0.DealSn} TryMark:{OO0O0O0O0000000O0.TryMark}"""+"""Has5Q:{self.Has5Q} TotQty:{self.TotQty} DealPriceOrg:{self.DealPriceOrg} DealQty:{self.DealQty}"""+"""B5QCountOrg:{self.B5QCountOrg} S5QCountOrg:{self.S5QCountOrg} fTX:{self.fTX}"""#line:777
class TStkQt5Q ():#line:778
    f5Q =[]#line:779
    def Handle_5Q (O0O00O00O00000OOO ,OOOO00OO00OO0O000 :str ):#line:781
        O0O00O00O00000OOO .fPROC_HandleData (OOOO00OO00OO0O000 )#line:782
    def HandleData_TryMarket (O0OOOO000OOOOO0O0 ,OOOOO0O00000O00OO :str ):#line:785
        ""#line:786
        if OOOOO0O00000O00OO .split ('|')[4 ]==TSolQuoteStkSet .TryMark_No :#line:787
            O0OOOO000OOOOO0O0 .fPROC_HandleData =O0OOOO000OOOOO0O0 .HandleData #line:788
            O0OOOO000OOOOO0O0 .fPROC_HandleData (OOOOO0O00000O00OO )#line:789
        else :#line:790
            O0OOOO000OOOOO0O0 .f5Q =OOOOO0O00000O00OO .split ('|')#line:791
            O0OOOO000OOOOO0O0 .SetData ()#line:792
            O0OOOO000OOOOO0O0 .B5QCount =O0OOOO000OOOOO0O0 .TransToInt (O0OOOO000OOOOO0O0 .B5QCountOrg )#line:793
            O0OOOO000OOOOO0O0 .S5QCount =O0OOOO000OOOOO0O0 .TransToInt (O0OOOO000OOOOO0O0 .S5QCountOrg )#line:794
    def HandleData (O00O0OO0000O000O0 ,OO00O0000OO0OO000 :str ):#line:796
        O00O0OO0000O000O0 .f5Q =OO00O0000OO0OO000 .split ('|')#line:797
        O00O0OO0000O000O0 .SetData ()#line:798
        O00O0OO0000O000O0 .B5QCount =O00O0OO0000O000O0 .TransToInt (O00O0OO0000O000O0 .B5QCountOrg )#line:799
        O00O0OO0000O000O0 .S5QCount =O00O0OO0000O000O0 .TransToInt (O00O0OO0000O000O0 .S5QCountOrg )#line:800
    def SetData (O000O0O0OOO00000O ):#line:802
        O000O0O0OOO00000O .SysTime =O000O0O0OOO00000O .f5Q [1 ]#line:803
        O000O0O0OOO00000O .DataTime =O000O0O0OOO00000O .f5Q [2 ]#line:804
        O000O0O0OOO00000O .DealSn =O000O0O0OOO00000O .f5Q [3 ]#line:805
        O000O0O0OOO00000O .TryMark =O000O0O0OOO00000O .f5Q [4 ]#line:806
        O000O0O0OOO00000O .TotQty =O000O0O0OOO00000O .f5Q [9 ]#line:807
        O000O0O0OOO00000O .B5QCountOrg =O000O0O0OOO00000O .f5Q [12 ]#line:808
        O000O0O0OOO00000O .S5QCountOrg =O000O0O0OOO00000O .f5Q [23 ]#line:809
    fPROC_HandleData =None #line:812
    """PROC_HandleData"""#line:813
    SysTime :str #line:816
    """系統時間Unix Timestamp(us)(EX:1642553376085607)"""#line:817
    DataTime :str #line:818
    """資料時間(交易所)(EX:173547.32700)"""#line:819
    DealSn :str #line:820
    """序號(5檔序號)"""#line:821
    def Get_DealSn (O0O0O0O0OOO0O0O0O )->int :#line:823
        return O0O0O0O0OOO0O0O0O .TransToInt (O0O0O0O0OOO0O0O0O .f5Q [3 ])#line:824
    TryMark ="1"#line:825
    """試撮註記(試撮=1, 非試撮=0)"""#line:826
    TotQty :str #line:827
    """成交總量"""#line:828
    def Get_TotQty2Dec (OO0OOOOO0OO0OOO0O )->decimal :#line:830
        return OO0OOOOO0OO0OOO0O .TransToDecimal (OO0OOOOO0OO0OOO0O .f5Q [9 ])#line:831
    def Get_TotQty2Int (OOO0OOO0OOOO0O0O0 )->int :#line:833
        return OOO0OOO0OOOO0O0O0 .TransToInt (OOO0OOO0OOOO0O0O0 .f5Q [9 ])#line:834
    fAryB5Q_P =[13 ,15 ,17 ,19 ,21 ]#line:837
    """買五檔價在字串中的位置"""#line:838
    fAryB5Q_Q =[14 ,16 ,18 ,20 ,22 ]#line:839
    """買五檔價在字串中的位置"""#line:840
    B5QCountOrg :str #line:842
    """買5檔的檔數"""#line:843
    B5QCount :int #line:844
    """買5檔的檔數"""#line:845
    def B5Q_POrg (OOO0000OOO0OOOO0O ,OO00OOOOO0O0O00OO :int )->str :#line:847
        ""#line:848
        if (OO00OOOOO0O0O00OO >OOO0000OOO0OOOO0O .B5QCount ):#line:849
            return ""#line:850
        else :#line:851
            return OOO0000OOO0OOOO0O .f5Q [OOO0000OOO0OOOO0O .fAryB5Q_P [OO00OOOOO0O0O00OO -1 ]]#line:852
    def Get_B5Q_P (O0OOO0O0O00OO0OO0 ,OO000O00OO0OO00OO :int )->decimal :#line:854
        ""#line:855
        if (OO000O00OO0OO00OO >O0OOO0O0O00OO0OO0 .B5QCount ):#line:856
            return 0 #line:857
        else :#line:858
            return O0OOO0O0O00OO0OO0 .TransToDecimal (O0OOO0O0O00OO0OO0 .f5Q [O0OOO0O0O00OO0OO0 .fAryB5Q_P [OO000O00OO0OO00OO -1 ]])#line:859
    def B5Q_QOrg (O0O0OOO0O0OO00O0O ,OO00000OOO00OOOO0 :int )->str :#line:861
        ""#line:862
        if (OO00000OOO00OOOO0 >O0O0OOO0O0OO00O0O .B5QCount ):#line:863
            return ""#line:864
        else :#line:865
            return O0O0OOO0O0OO00O0O .f5Q [O0O0OOO0O0OO00O0O .fAryB5Q_Q [OO00000OOO00OOOO0 -1 ]]#line:866
    def Get_B5Q_Q (OO00000O00000O0OO ,O00O0O00O000OO000 :int )->int :#line:868
        ""#line:869
        if (O00O0O00O000OO000 >OO00000O00000O0OO .B5QCount ):#line:870
            return 0 #line:871
        else :#line:872
            return OO00000O00000O0OO .TransToInt (OO00000O00000O0OO .f5Q [OO00000O00000O0OO .fAryB5Q_Q [O00O0O00O000OO000 -1 ]])#line:873
    fAryS5Q_P =[24 ,26 ,28 ,30 ,32 ]#line:877
    """賣五檔價在字串中的位置"""#line:878
    fAryS5Q_Q =[25 ,27 ,29 ,31 ,33 ]#line:879
    """賣五檔價在字串中的位置"""#line:880
    S5QCountOrg :str #line:882
    """賣5檔的檔數"""#line:883
    S5QCount :int #line:884
    """賣5檔的檔數"""#line:885
    def S5Q_POrg (OO00O000000O00OOO ,O0OOO0OOOOOOO0O00 :int )->str :#line:887
        ""#line:888
        if (O0OOO0OOOOOOO0O00 >OO00O000000O00OOO .S5QCount ):#line:889
            return ""#line:890
        else :#line:891
            return OO00O000000O00OOO .f5Q [OO00O000000O00OOO .fAryS5Q_P [O0OOO0OOOOOOO0O00 -1 ]]#line:892
    def Get_S5Q_P (O00O0OO0OOO0O0O0O ,OOO0OO0O0O0OOOO00 :int )->decimal :#line:894
        ""#line:895
        if (OOO0OO0O0O0OOOO00 >O00O0OO0OOO0O0O0O .S5QCount ):#line:896
            return 0 #line:897
        else :#line:898
            return O00O0OO0OOO0O0O0O .TransToDecimal (O00O0OO0OOO0O0O0O .f5Q [O00O0OO0OOO0O0O0O .fAryS5Q_P [OOO0OO0O0O0OOOO00 -1 ]])#line:899
    def S5Q_QOrg (O0OOO00O00OOOOOO0 ,O0OOO0OOOO000000O :int )->str :#line:901
        ""#line:902
        if (O0OOO0OOOO000000O >O0OOO00O00OOOOOO0 .S5QCount ):#line:903
            return ""#line:904
        else :#line:905
            return O0OOO00O00OOOOOO0 .f5Q [O0OOO00O00OOOOOO0 .fAryS5Q_Q [O0OOO0OOOO000000O -1 ]]#line:906
    def Get_S5Q_Q (OO0O0O0O00OO0O000 ,OO00O00OOO0OO0OO0 :int )->int :#line:908
        ""#line:909
        if (OO00O00OOO0OO0OO0 >OO0O0O0O00OO0O000 .S5QCount ):#line:910
            return 0 #line:911
        else :#line:912
            return OO0O0O0O00OO0O000 .TransToInt (OO0O0O0O00OO0O000 .f5Q [OO0O0O0O00OO0O000 .fAryS5Q_Q [OO00O00OOO0OO0OO0 -1 ]])#line:913
    def TransToInt (OO0000O0OO00OO0OO ,O0OOOOO0OOO0O0000 :str )->int :#line:917
        try :#line:918
            return int (O0OOOOO0OOO0O0000 )#line:919
        except Exception as O0O00O00OO0OOOO0O :#line:920
            return 0 #line:921
    def TransToDecimal (O00OO000O0O00O0OO ,OO0000OO00OOO0000 :str )->decimal :#line:923
        try :#line:924
            return Decimal (OO0000OO00OOO0000 )#line:925
        except Exception as O000O00OO0OO000O0 :#line:926
            return 0 #line:927
    def __init__ (OO0O0OOOO0O0O0000 )->None :#line:930
        OO0O0OOOO0O0O0000 .fPROC_HandleData =OO0O0OOOO0O0O0000 .HandleData_TryMarket #line:932
    def __str__ (OO0O0O0O0000O00O0 )->str :#line:934
        return f"""SysTime:{OO0O0O0O0000O00O0.SysTime} DataTime:{OO0O0O0O0000O00O0.DataTime} DealSn:{OO0O0O0O0000O00O0.DealSn} TryMark:{OO0O0O0O0000O00O0.TryMark}"""+"""TotQty:{self.TotQty} B5QCountOrg:{self.B5QCountOrg} S5QCountOrg:{self.S5QCountOrg} f5Q:{self.f5Q}"""#line:936
class TStkQtIDX ():#line:937
    fIDX =[]#line:938
    def Handle_IDXRcv (OO00OO00OOOO00000 ,OOOOO0O0O000OO0OO :str ):#line:940
        ""#line:941
        try :#line:942
            OOOO00OO0OOO0O000 :int =0 #line:943
            O0OOO00O0O0O000OO :int =0 #line:944
            O0OOOOOOOOOOO0OO0 =OOOOO0O0O000OO0OO .split ('|')#line:945
            if OO00OO00OOOO00000 .fIDX ==None :#line:946
                OO00OO00OOOO00000 .fIDX =O0OOOOOOOOOOO0OO0 #line:947
            else :#line:948
                O0OOO00O0O0O000OO =OO00OO00OOOO00000 .TransToInt (O0OOOOOOOOOOO0OO0 [3 ])#line:949
                OOOO00OO0OOO0O000 =OO00OO00OOOO00000 .Get_DealSn ()#line:950
                if O0OOO00O0O0O000OO >OOOO00OO0OOO0O000 :#line:951
                    OO00OO00OOOO00000 .fIDX =O0OOOOOOOOOOO0OO0 #line:952
                    OO00OO00OOOO00000 .SetData ()#line:953
                OO00OO00OOOO00000 .fPROC_CalcHightLowPrice ()#line:955
        except Exception as OOOOOO00O0O00O0O0 :#line:957
            pass #line:958
    def Handle_IDX (OOO00O0O000000O0O ,O0OOOO00O000O0000 :str ):#line:960
        ""#line:961
        OOO00O0O000000O0O .fIDX =O0OOOO00O000O0000 .split ('|')#line:962
        OOO00O0O000000O0O .SetData ()#line:963
        OOO00O0O000000O0O .fPROC_CalcHightLowPrice ()#line:964
    def SetData (OOO0O0OO0OO00OOO0 ):#line:966
        OOO0O0OO0OO00OOO0 .SysTime =OOO0O0OO0OO00OOO0 .fIDX [1 ]#line:967
        OOO0O0OO0OO00OOO0 .DealTime =OOO0O0OO0OO00OOO0 .fIDX [2 ]#line:968
        OOO0O0OO0OO00OOO0 .DealSn =OOO0O0OO0OO00OOO0 .fIDX [3 ]#line:969
        OOO0O0OO0OO00OOO0 .DealPriceOrg =OOO0O0OO0OO00OOO0 .fIDX [10 ]#line:971
        OOO0O0OO0OO00OOO0 .WholeTotAmt =OOO0O0OO0OO00OOO0 .fIDX [34 ]#line:972
        OOO0O0OO0OO00OOO0 .TotQty =OOO0O0OO0OO00OOO0 .fIDX [35 ]#line:974
        OOO0O0OO0OO00OOO0 .WholeTotQty =OOO0O0OO0OO00OOO0 .fIDX [35 ]#line:975
        OOO0O0OO0OO00OOO0 .WholeDealCount =OOO0O0OO0OO00OOO0 .fIDX [36 ]#line:976
        OOO0O0OO0OO00OOO0 .SumBuyOrderCount =OOO0O0OO0OO00OOO0 .fIDX [37 ]#line:977
        OOO0O0OO0OO00OOO0 .SumSellOrderCount =OOO0O0OO0OO00OOO0 .fIDX [38 ]#line:978
        OOO0O0OO0OO00OOO0 .SumBuyOrderQty =OOO0O0OO0OO00OOO0 .fIDX [39 ]#line:979
        OOO0O0OO0OO00OOO0 .SumSellOrderQty =OOO0O0OO0OO00OOO0 .fIDX [40 ]#line:980
    SysTime :str #line:983
    """系統時間Unix Timestamp(us)(EX:1642553376085607)"""#line:984
    DealTime :str #line:985
    """撮合時間(成交)(EX:085229.843665)"""#line:986
    DealSn :str #line:987
    """序號"""#line:988
    def Get_DealSn (O00000O0OOO0OOO00 )->int :#line:990
        return O00000O0OOO0OOO00 .TransToInt (O00000O0OOO0OOO00 .fIDX [3 ])#line:991
    TotQty :str #line:992
    """成交總量"""#line:993
    def Get_TotQty2Dec (OO0OO000O0O0OO0O0 )->decimal :#line:995
        return OO0OO000O0O0OO0O0 .TransToDecimal (OO0OO000O0O0OO0O0 .fIDX [35 ])#line:996
    def Get_TotQty2Int (OO0OOOOOOOO0O0O0O )->int :#line:998
        return OO0OOOOOOOO0O0O0O .TransToInt (OO0OOOOOOOO0O0O0O .fIDX [35 ])#line:999
    DealPriceOrg :str #line:1000
    """成交價"""#line:1001
    def Get_DealPrice (O00OOOO0OOO0OO0OO )->decimal :#line:1003
        return O00OOOO0OOO0OO0OO .TransToDecimal (O00OOOO0OOO0OO0OO .fIDX [10 ])#line:1004
    fDealPrice =0 #line:1007
    """成交價"""#line:1008
    HighPrice =0 #line:1009
    """當日最高價"""#line:1010
    LowPrice =0 #line:1011
    """當日最低價"""#line:1012
    def CalcHightLowPrice (O00OOO0OO00O0O0OO ):#line:1014
        ""#line:1015
        try :#line:1016
            O00OOO0OO00O0O0OO .fDealPrice =O00OOO0OO00O0O0OO .Get_DealPrice ()#line:1017
            O00OOO0OO00O0O0OO .HighPrice =math .Max (O00OOO0OO00O0O0OO .fDealPrice ,O00OOO0OO00O0O0OO .HighPrice )#line:1019
            if O00OOO0OO00O0O0OO .LowPrice ==0 :#line:1020
                O00OOO0OO00O0O0OO .LowPrice =O00OOO0OO00O0O0OO .fDealPrice #line:1021
            else :#line:1022
                O00OOO0OO00O0O0OO .LowPrice =math .Min (O00OOO0OO00O0O0OO .fDealPrice ,O00OOO0OO00O0O0OO .LowPrice )#line:1023
        except Exception as O00O0O0O0OOOOOOOO :#line:1024
            pass #line:1025
    def CalcHightLowPrice_None (O0OOO000000000O00 ):#line:1027
        pass #line:1028
    fPROC_CalcHightLowPrice =None #line:1031
    """PROC_CalcHightLowPrice"""#line:1032
    HasWholeMarketData :bool #line:1037
    WholeTotAmt :str #line:1039
    """整體市場成交總額"""#line:1040
    def Get_WholeTotAmt (OOO0OO0OO00000O0O )->int :#line:1042
        if (OOO0OO0OO00000O0O .HasWholeMarketData ):#line:1043
            return OOO0OO0OO00000O0O .TransToInt (OOO0OO0OO00000O0O .fIDX [34 ])#line:1044
    def Get_WholeTotAmt (OO0O00O000OOO00OO )->decimal :#line:1046
        if (OO0O00O000OOO00OO .HasWholeMarketData ):#line:1047
            return OO0O00O000OOO00OO .TransToDecimal (OO0O00O000OOO00OO .fIDX [34 ])#line:1048
        else :#line:1049
            return 0 #line:1050
    WholeTotQty :str #line:1052
    """整體市場成交數量"""#line:1053
    def Get_WholeTotQty (O0OO0OO0OOOOOO00O )->int :#line:1055
        if (O0OO0OO0OOOOOO00O .HasWholeMarketData ):#line:1056
            return O0OO0OO0OOOOOO00O .TransToInt (O0OO0OO0OOOOOO00O .fIDX [35 ])#line:1057
        else :#line:1058
            return 0 #line:1059
    WholeDealCount :str #line:1060
    """整體市場成交筆數"""#line:1061
    def Get_WholeDealCount (O0OO00000O00O0O0O )->int :#line:1063
        if O0OO00000O00O0O0O .HasWholeMarketData :#line:1064
            return O0OO00000O00O0O0O .TransToInt (O0OO00000O00O0O0O .fIDX [36 ])#line:1065
        else :#line:1066
            return 0 #line:1067
    SumBuyOrderCount :str #line:1069
    """整體市場委託買進筆數"""#line:1070
    def Get_SumBuyOrderCount (OOO0O0O000OOOOOO0 )->int :#line:1072
        if OOO0O0O000OOOOOO0 .HasWholeMarketData :#line:1073
            return OOO0O0O000OOOOOO0 .TransToInt (OOO0O0O000OOOOOO0 .fIDX [37 ])#line:1074
        else :#line:1075
            return 0 #line:1076
    SumSellOrderCount :str #line:1077
    """整體市場委託賣出筆數"""#line:1078
    def Get_SumSellOrderCount (O000O0O000000OO00 )->int :#line:1080
        if O000O0O000000OO00 .HasWholeMarketData :#line:1081
            return O000O0O000000OO00 .TransToInt (O000O0O000000OO00 .fIDX [38 ])#line:1082
        else :#line:1083
            return 0 #line:1084
    SumBuyOrderQty :str #line:1085
    """整體市場委託買進數量"""#line:1086
    def Get_SumBuyOrderQty (OO0000O0O0OOO0000 )->int :#line:1088
        if OO0000O0O0OOO0000 .HasWholeMarketData :#line:1089
            return OO0000O0O0OOO0000 .TransToInt (OO0000O0O0OOO0000 .fIDX [39 ])#line:1090
        else :#line:1091
            return 0 #line:1092
    SumSellOrderQty :str #line:1093
    """整體市場委託賣出數量"""#line:1094
    def Get_SumSellOrderQty (O0OO0O000O00OO00O )->int :#line:1096
        if O0OO0O000O00OO00O .HasWholeMarketData :#line:1097
            return O0OO0O000O00OO00O .TransToInt (O0OO0O000O00OO00O .fIDX [40 ])#line:1098
        else :#line:1099
            return 0 #line:1100
    def TransToInt (OOO0O00O0000OO0OO ,O00OO0O0000OO0OOO :str )->int :#line:1104
        try :#line:1105
            return int (O00OO0O0000OO0OOO )#line:1106
        except Exception as OOOOOO000000O00O0 :#line:1107
            return 0 #line:1108
    def TransToDecimal (O00O0000OOO00OO00 ,OOOOO0O00O0O0OO0O :str )->decimal :#line:1110
        try :#line:1111
            return Decimal (OOOOO0O00O0O0OO0O )#line:1112
        except Exception as O0OOO0OO0O00OOO00 :#line:1113
            return 0 #line:1114
    def __init__ (OO00000O00OOOO00O ,O0O0O0OO0OOOO0000 :bool )->None :#line:1117
        ""#line:1118
        OO00000O00OOOO00O .fPROC_CalcHightLowPrice =OO00000O00OOOO00O .CalcHightLowPrice_None #line:1120
        if (O0O0O0OO0OOOO0000 ):#line:1121
            OO00000O00OOOO00O .fPROC_CalcHightLowPrice =OO00000O00OOOO00O .CalcHightLowPrice #line:1122
class TStkQuoteData :#line:1123
    BAS :TStkQtBase =None #line:1125
    HL :TStkQtHL =None #line:1126
    QtTX :TStkQtTX =None #line:1127
    Qt5Q :TStkQt5Q =None #line:1128
    QtIDX :TStkQtIDX =None #line:1129
    def __init__ (O00OOO0OO000O0OO0 ,O000O0OOO0O0OO0O0 :TStkProdKind ,OOO0O00O0OO00O00O :str ,OOOO000000OOO0OO0 :bool )->None :#line:1131
        ""#line:1132
        O00OOO0OO000O0OO0 .SolIce =OOO0O00O0OO00O00O #line:1133
        O00OOO0OO000O0OO0 .ProdKind :TStkProdKind =O000O0OOO0O0OO0O0 #line:1134
        O00OOO0OO000O0OO0 ._lock =Lock ()#line:1135
        if O000O0OOO0O0OO0O0 ==TStkProdKind .pkNormal :#line:1136
            O00OOO0OO000O0OO0 .BAS =TStkQtBase ()#line:1137
            O00OOO0OO000O0OO0 .HL =TStkQtHL ()#line:1138
            O00OOO0OO000O0OO0 .QtTX =TStkQtTX (OOOO000000OOO0OO0 )#line:1139
            O00OOO0OO000O0OO0 .Qt5Q =TStkQt5Q ()#line:1140
        elif O000O0OOO0O0OO0O0 ==TStkProdKind .pkIndex :#line:1141
            O00OOO0OO000O0OO0 .BAS =TStkQtBase ()#line:1142
            O00OOO0OO000O0OO0 .HL =TStkQtHL ()#line:1143
            O00OOO0OO000O0OO0 .QtIDX =TStkQtIDX (OOOO000000OOO0OO0 )#line:1144
    def SetDataInit (O0O000O0OOO000O00 ):#line:1171
        ""#line:1172
        if O0O000O0OOO000O00 .ProdKind ==TStkProdKind .pkNormal :#line:1173
            O0O000O0OOO000O00 .QtTX .HighPrice =O0O000O0OOO000O00 .HL .Get_HighPrice ()#line:1175
            O0O000O0OOO000O00 .QtTX .LowPrice =O0O000O0OOO000O00 .HL .Get_LowPrice ()#line:1176
            O0O000O0OOO000O00 .QtTX .HL_Sn_5Q =O0O000O0OOO000O00 .HL .Get_Sn_5Q ()#line:1178
            O0O000O0OOO000O00 .QtTX .BAS_TradingUnit =O0O000O0OOO000O00 .BAS .Get_TradingUnit ()#line:1180
            O0O000O0OOO000O00 .QtTX .HL_TotAmt =O0O000O0OOO000O00 .HL .Get_TotAmt2Int ()#line:1182
        elif O0O000O0OOO000O00 .ProdKind ==TStkProdKind .pkIndex :#line:1183
            O0O000O0OOO000O00 .QtIDX .HighPrice =O0O000O0OOO000O00 .HL .Get_HighPrice ()#line:1185
            O0O000O0OOO000O00 .QtIDX .LowPrice =O0O000O0OOO000O00 .HL .Get_LowPrice ()#line:1186
class TObjStkQuoteMap (UserDict ):#line:1201
    ""#line:1203
    """各商品拆解行情proc(EX:2330的TX與5Q, 行情拆解,是不同Proc)
        Dictionary<string, PROC_Handle_StkRTQuote> MapQtProc = new Dictionary<string, PROC_Handle_StkRTQuote>();"""#line:1206
    DefProc_TX :callable =None #line:1211
    DefProc_5Q :callable =None #line:1212
    DefProc_Idx :callable =None #line:1213
    def __init__ (O0O00O0OOOOO0OOO0 ,mapping =None ,**OOOO0OOO00OO0O0OO ):#line:1214
        if mapping is not None :#line:1215
            mapping ={str (OOOOOO0O0OOOOOO0O ).upper ():O0O000O000000OO0O for OOOOOO0O0OOOOOO0O ,O0O000O000000OO0O in mapping .items ()}#line:1218
        else :#line:1219
            mapping ={}#line:1220
        if OOOO0OOO00OO0O0OO :#line:1221
            mapping .update ({str (OOOO0O00000OO00O0 ).upper ():OOO0OOO0O0O00OOOO for OOOO0O00000OO00O0 ,OOO0OOO0O0O00OOOO in OOOO0OOO00OO0O0OO .items ()})#line:1224
        O0O00O0OOOOO0OOO0 .MapQtProc ={}#line:1225
        super ().__init__ (mapping )#line:1226
    def __setitem__ (O0O000O0OOOO0000O ,OOO0OOOO0OOOOOO00 ,O0000O000OO00O000 ):#line:1228
        super ().__setitem__ (OOO0OOOO0OOOOOO00 ,O0000O000OO00O000 )#line:1229
    def AddRcvData (OOO00OO0OO0O00O00 ,OO00O0O0OOOO000OO :TStkProdKind ,OOO00O000O00OOO0O :str ,OOO0O0000OO0O000O :str ,O00000O0OO0OOOO0O :bool ):#line:1231
        ""#line:1236
        O0000OOO00OOOOOO0 =""#line:1237
        O00OO000O0O000000 :TStkQuoteData =None #line:1238
        try :#line:1239
            O00000O00OOOOOOO0 =json .loads (OOO0O0000OO0O000O )#line:1242
            if "status"in O00000O00OOOOOOO0 and len (O00000O00OOOOOOO0 ["status"])>0 :#line:1243
                if O00000O00OOOOOOO0 ["status"][0 ]=="error":#line:1244
                    O0000OOO00OOOOOO0 =f"[證][AddRcvData](aSolIce={OOO00O000O00OOO0O}, aData={OOO0O0000OO0O000O})行情回補資料有誤!"#line:1245
                    return False ,O00OO000O0O000000 ,O0000OOO00OOOOOO0 #line:1246
            if "BAS"in O00000O00OOOOOOO0 and len (O00000O00OOOOOOO0 ["BAS"])==0 :#line:1247
                O0000OOO00OOOOOO0 =f"[證][AddRcvData](aSolIce={OOO00O000O00OOO0O}, aData={OOO0O0000OO0O000O})沒有BAS資料!"#line:1248
                return False ,O00OO000O0O000000 ,O0000OOO00OOOOOO0 #line:1249
            if "HL"in O00000O00OOOOOOO0 and len (O00000O00OOOOOOO0 ["HL"])==0 :#line:1250
                O0000OOO00OOOOOO0 =f"[證][AddRcvData](aSolIce={OOO00O000O00OOO0O}, aData={OOO0O0000OO0O000O})沒有HL資料!"#line:1251
                return False ,O00OO000O0O000000 ,O0000OOO00OOOOOO0 #line:1252
            if OOO00OO0OO0O00O00 .data .get (OOO00O000O00OOO0O )is None :#line:1255
                O0O0O0OOOOO0O0O00 =TStkQuoteData (OO00O0O0OOOO000OO ,OOO00O000O00OOO0O ,O00000O0OO0OOOO0O )#line:1256
                O0O0O0OOOOO0O0O00 .BAS .Handle_BAS (O00000O00OOOOOOO0 ["BAS"][0 ])#line:1257
                O0O0O0OOOOO0O0O00 .HL .Handle_HL (O00000O00OOOOOOO0 ["HL"][0 ])#line:1258
                O0O0O0OOOOO0O0O00 .SetDataInit ()#line:1259
                O00OO000O0O000000 =O0O0O0OOOOO0O0O00 #line:1260
                OOO00OO0OO0O00O00 [OOO00O000O00OOO0O ]=O0O0O0OOOOO0O0O00 #line:1261
                return True ,O00OO000O0O000000 ,""#line:1262
            else :#line:1263
                O0O0O0OOOOO0O0O00 :TStkQuoteData =OOO00OO0OO0O00O00 [OOO00O000O00OOO0O ]#line:1264
                with O0O0O0OOOOO0O0O00 ._lock :#line:1265
                    O0O0O0OOOOO0O0O00 .BAS .Handle_BAS (O00000O00OOOOOOO0 ["BAS"][0 ])#line:1266
                    O0O0O0OOOOO0O0O00 .HL .Handle_HL (O00000O00OOOOOOO0 ["HL"][0 ])#line:1267
                    O0O0O0OOOOO0O0O00 .SetDataInit ()#line:1268
                    O00OO000O0O000000 =O0O0O0OOOOO0O0O00 #line:1269
                return True ,O00OO000O0O000000 ,""#line:1270
        except Exception as O0O0O0OO00000OO00 :#line:1271
            O0000OOO00OOOOOO0 =f"[證][AddRcvData](aSolIce={OOO00O000O00OOO0O}, aData={OOO0O0000OO0O000O}){O0O0O0OO00000OO00}"#line:1272
            return False ,O00OO000O0O000000 ,O0000OOO00OOOOOO0 #line:1273
    def AddDataBySolIce (O00O0O0O000O0O000 ,O000O0O0O0OO000OO :bool ,OOO000O0OOO0OO00O :str ,OOOO0OOOOO00OO000 ,O000O00000OO0O0O0 :bool ):#line:1275
        ""#line:1283
        try :#line:1284
            OO0O00OOO0000O0O0 :O000OO0OO0OO0OOO0 =""#line:1285
            O0O0OO00OOO0000OO :TObjStkQuoteMap =TObjStkQuoteMap ()#line:1286
            for O000OO0OO0OO0OOO0 in OOOO0OOOOO00OO000 ["BAS"]:#line:1288
                OOO0O00OO00O000OO :TStkQtBase =TStkQtBase ()#line:1289
                OOO0O00OO00O000OO .Handle_BAS (O000OO0OO0OO0OOO0 )#line:1290
                if O0O0OO00OOO0000OO .data .get (OOO0O00OO00O000OO .StkNo )is None :#line:1291
                    O000OOOO0000OO000 :TStkQuoteData =TStkQuoteData (TStkProdKind .pkNormal ,OOO0O00OO00O000OO .StkNo ,O000O00000OO0O0O0 );#line:1292
                    O000OOOO0000OO000 .BAS =OOO0O00OO00O000OO #line:1293
                    O0O0OO00OOO0000OO [OOO0O00OO00O000OO .StkNo ]=O000OOOO0000OO000 #line:1294
            for O000OO0OO0OO0OOO0 in OOOO0OOOOO00OO000 ["HL"]:#line:1297
                O0OO0OO0OO000OOO0 =TStkQtHL ()#line:1298
                O0OO0OO0OO000OOO0 .Handle_HL (O000OO0OO0OO0OOO0 )#line:1299
                if O0O0OO00OOO0000OO .data .get (O0OO0OO0OO000OOO0 .Symbol ):#line:1300
                    O000OOOO0000OO000 =O0O0OO00OOO0000OO [O0OO0OO0OO000OOO0 .Symbol ]#line:1301
                    O000OOOO0000OO000 .HL =O0OO0OO0OO000OOO0 #line:1302
                    O000OOOO0000OO000 .SetDataInit ()#line:1303
                    OOOO00OOO00O0000O :O000OO0OO0OO0OOO0 =O000OOOO0000OO000 .HL .TopicTX #line:1305
                    O0000OOOO00OO0O0O :O000OO0OO0OO0OOO0 =O000OOOO0000OO000 .HL .Topic5Q #line:1306
                    O00O0O0O000O0O000 [OOOO00OOO00O0000O ]=O000OOOO0000OO000 #line:1308
                    O00O0O0O000O0O000 [O0000OOOO00OO0O0O ]=O000OOOO0000OO000 #line:1309
                    if O00O0O0O000O0O000 .MapQtProc .get (OOOO00OOO00O0000O )is None :#line:1310
                        O00O0O0O000O0O000 .MapQtProc [OOOO00OOO00O0000O ]=O00O0O0O000O0O000 .DefProc_TX #line:1311
                    if O00O0O0O000O0O000 .MapQtProc .get (O0000OOOO00OO0O0O )is None :#line:1312
                        O00O0O0O000O0O000 .MapQtProc [O0000OOOO00OO0O0O ]=O00O0O0O000O0O000 .DefProc_5Q #line:1313
            return len (O0O0OO00OOO0000OO )>0 ,O0O0OO00OOO0000OO ,OO0O00OOO0000O0O0 #line:1315
        except Exception as O0O00OO0O00OO00O0 :#line:1316
            OO0O00OOO0000O0O0 =f"[證][AddDataBySolIce](aIsCat={O000O0O0O0OO000OO}, aSolIce={OOO000O0OOO0OO00O}){O0O00OO0O00OO00O0}"#line:1317
        return False ,O0O0OO00OOO0000OO ,OO0O00OOO0000O0O0 #line:1318
    def AddIdxDataBySolIce (OOO0000O0O0OO000O ,OO00OO0OO00OO0000 :bool ,OO00OO00000000OOO :str ,OO0O0O0O0OO0O0O00 ,OO00OOO0OOOOOOOO0 :bool ):#line:1320
        ""#line:1327
        try :#line:1328
            O0O0O00OO0OOOOO00 =""#line:1329
            OO0OO0O0O000OO000 :TObjStkQuoteMap =TObjStkQuoteMap ()#line:1330
            for O0000OO00OO0OOO0O in OO0O0O0O0OO0O0O00 ["BAS"]:#line:1332
                O00O0OO0OO00O0O00 :TStkQtBase =TStkQtBase ()#line:1333
                O00O0OO0OO00O0O00 .Handle_BAS (O0000OO00OO0OOO0O )#line:1334
                if OO0OO0O0O000OO000 .data .get (O00O0OO0OO00O0O00 .StkNo )is None :#line:1335
                    OOOO00O0OO00OO0OO :TStkQuoteData =TStkQuoteData (TStkProdKind .pkIndex ,O00O0OO0OO00O0O00 .StkNo ,OO00OOO0OOOOOOOO0 )#line:1336
                    OOOO00O0OO00OO0OO .BAS =O00O0OO0OO00O0O00 #line:1337
                    OO0OO0O0O000OO000 [O00O0OO0OO00O0O00 .StkNo ]=OOOO00O0OO00OO0OO #line:1338
            for O0000OO00OO0OOO0O in OO0O0O0O0OO0O0O00 ["HL"]:#line:1341
                OOO0O0OOOO0OO0OO0 =TStkQtHL ()#line:1342
                OOO0O0OOOO0OO0OO0 .Handle_HL (O0000OO00OO0OOO0O )#line:1343
                if OO0OO0O0O000OO000 .data .get (OOO0O0OOOO0OO0OO0 .Symbol ):#line:1344
                    OOOO00O0OO00OO0OO =OO0OO0O0O000OO000 [OOO0O0OOOO0OO0OO0 .Symbol ]#line:1345
                    OOOO00O0OO00OO0OO .HL =OOO0O0OOOO0OO0OO0 #line:1346
                    OOOO00O0OO00OO0OO .SetDataInit ()#line:1347
                    OOOOOOOO0OO0OO0O0 :O0000OO00OO0OOO0O =OOOO00O0OO00OO0OO .HL .TopicTX #line:1349
                    OOO0000O0O0OO000O [OOOOOOOO0OO0OO0O0 ]=OOOO00O0OO00OO0OO #line:1351
                    if OOO0000O0O0OO000O .MapQtProc .get (OOOOOOOO0OO0OO0O0 )is None :#line:1353
                        OOO0000O0O0OO000O .MapQtProc [OOOOOOOO0OO0OO0O0 ]=OOO0000O0O0OO000O .DefProc_Idx #line:1354
            return len (OO0OO0O0O000OO000 )>0 ,OO0OO0O0O000OO000 ,O0O0O00OO0OOOOO00 #line:1356
        except Exception as OO0OO0O0OOO0O00O0 :#line:1357
            O0O0O00OO0OOOOO00 =f"[證][AddIdxDataBySolIce](aIsCat={OO00OO0OO00OO0000}, aSolIce={OO00OO00000000OOO}){OO0OO0O0OOO0O00O0}"#line:1358
        return False ,OO0OO0O0O000OO000 ,O0O0O00OO0OOOOO00 #line:1359
    def GetItem_BySolIce (OO000000OOO00OOOO ,O00OO00OO0O000000 :str ):#line:1362
        ""#line:1367
        try :#line:1368
            OOO000OOO00OO0OO0 =[]#line:1369
            for OOO00O00O0O0000OO ,O00OO0OO00OO00O00 in OO000000OOO00OOOO .items ():#line:1370
                OOO0000O00O0OO0O0 :TStkQuoteData #line:1371
                OOO0000O00O0OO0O0 =O00OO0OO00OO00O00 #line:1372
                if OOO0000O00O0OO0O0 .SolIce ==O00OO00OO0O000000 :#line:1373
                    OOO000OOO00OO0OO0 .append (OOO00O00O0O0000OO )#line:1374
            if OOO000OOO00OO0OO0 is None or len (OOO000OOO00OO0OO0 )==0 :#line:1375
                return False ,[],f"[證][GetItem_BySolIce](aSolIce={O00OO00OO0O000000})商品已不存存!"#line:1376
            else :#line:1377
                return True ,OOO000OOO00OO0OO0 ,""#line:1378
        except Exception as O0O00000OO0000000 :#line:1379
            return False ,[],f"[證][GetItem_BySolIce](aSolIce={O00OO00OO0O000000}){O0O00000OO0000000}"#line:1380
    def GetItem_ByCategory (O0O00000OOOO0O0O0 ,O0O0O0OOOOO000O00 :str ):#line:1381
        ""#line:1384
        try :#line:1386
            OO00OO00OOO0O0O0O =[]#line:1387
            for O0O0OOO0OOO0O0O0O ,O00O0O00O00O0OOOO in O0O00000OOOO0O0O0 .items ():#line:1388
                O00OOO00OO0O0OO00 :TStkQuoteData =O00O0O00O00O0OOOO #line:1389
                if O00OOO00OO0O0OO00 .HL .StkKind ==O0O0O0OOOOO000O00 :#line:1391
                    OO00OO00OOO0O0O0O .append (O0O0OOO0OOO0O0O0O )#line:1392
            if OO00OO00OOO0O0O0O is None or len (OO00OO00OOO0O0O0O )==0 :#line:1393
                return False ,[],f"[證][GetItem_ByCategory](aCat={O0O0O0OOOOO000O00})商品已不存存!"#line:1394
            else :#line:1395
                return True ,OO00OO00OOO0O0O0O ,""#line:1396
        except Exception as O0O0O000O00000O0O :#line:1398
            return False ,[],f"[證][GetItem_ByCategory](aCat={O0O0O0OOOOO000O00}){O0O0O000O00000O0O}"#line:1399
class TQryStkProdMap (UserDict ):#line:1403
    def __init__ (O0O0O0O0O0O0OOOO0 ,mapping =None ,**OOOOO0O0OOOOOO0O0 ):#line:1404
        if mapping is not None :#line:1405
            mapping ={str (O00OO00000OOO0OOO ).upper ():O0OO00000000OO0OO for O00OO00000OOO0OOO ,O0OO00000000OO0OO in mapping .items ()}#line:1408
        else :#line:1409
            mapping ={}#line:1410
        if OOOOO0O0OOOOOO0O0 :#line:1411
            mapping .update ({str (O0O0O0OOOO0O0O00O ).upper ():OO0OO0OO0OOO0OO0O for O0O0O0OOOO0O0O00O ,OO0OO0OO0OOO0OO0O in OOOOO0O0OOOOOO0O0 .items ()})#line:1414
        super ().__init__ (mapping )#line:1415
    """Dictionary<string, TQryStkProdRec>"""#line:1416
    def __setitem__ (OOO000O0O0OOOO00O ,O000OOOOO0O000O0O ,O0000O0OOO000O0O0 ):#line:1418
        super ().__setitem__ (O000OOOOO0O000O0O ,O0000O0OOO000O0O0 )#line:1419
class TQryStkProdRec ():#line:1422
    tmpBase :TStkQtBase =None #line:1423
    tmpHL :TStkQtHL =None #line:1424
    def SetDataInit (OO0OOOO00OO0O0000 ):#line:1426
        pass #line:1427
class TFutQtBase :#line:1433
    fHasBAS :bool =False #line:1435
    fBAS =[]#line:1436
    DECIMAL_LOCATOR_Org :int =0 #line:1438
    """價格欄位小數位數"""#line:1439
    DECIMAL_LOCATOR_Dgt :decimal =1 #line:1440
    """價格欄位小數位數(若DECIMAL_LOCATOR_Org=2, 則此值為0.001)"""#line:1441
    OrdProdID :str #line:1442
    """商品委託代碼(EX:CDFC3)"""#line:1443
    RefPriceOrg :str #line:1444
    """參考價"""#line:1445
    def Get_RefPrice2Str (OO000O00OO00O0O0O )->str :#line:1447
        return OO000O00OO00O0O0O .TransPrice2Str (OO000O00OO00O0O0O .fBAS [4 ])#line:1448
    def Get_RefPrice2Dec (OOO0OOO00O00OOO0O )->decimal :#line:1450
        return OOO0OOO00O00OOO0O .TransPrice2Dec (OOO0OOO00O00OOO0O .fBAS [4 ])#line:1451
    LimitPrice_UpOrg :str #line:1453
    """漲停價"""#line:1454
    def Get_LimitPrice_Up2Str (O0OO0OO0OO0OO0OOO )->str :#line:1456
        return O0OO0OO0OO0OO0OOO .TransPrice2Str (O0OO0OO0OO0OO0OOO .fBAS [5 ])#line:1457
    def Get_LimitPrice_Up2Dec (O0O0O000OO0OOOO0O )->decimal :#line:1459
        return O0O0O000OO0OOOO0O .TransPrice2Dec (O0O0O000OO0OOOO0O .fBAS [5 ])#line:1460
    LimitPrice_DownOrg :str #line:1462
    """跌停價"""#line:1463
    ProdKind :str #line:1465
    """契約種類"""#line:1466
    def Get_LimitPrice_Down2Str (OOO0O0O00O0OOOO0O )->str :#line:1468
        return OOO0O0O00O0OOOO0O .TransPrice2Str (OOO0O0O00O0OOOO0O .fBAS [6 ])#line:1469
    def Get_LimitPrice_Down2Dec (O00000OOO00OOOOOO )->decimal :#line:1471
        return O00000OOO00OOOOOO .TransPrice2Dec (O00000OOO00OOOOOO .fBAS [6 ])#line:1472
    IdxDgtOrg :str #line:1474
    """指數小數位數"""#line:1475
    def Get_IdxDgtOrg (O0O000OO00OOOO0O0 )->int :#line:1477
        return O0O000OO00OOOO0O0 .TransToInt (O0O000OO00OOOO0O0 .fBAS [8 ])#line:1478
    StrikePriceDecimalLocator :str #line:1480
    "選擇權商品代號之履約價小數位數"#line:1481
    BeginDate :str #line:1483
    "上市日期"#line:1484
    EndDate :str #line:1485
    "下市日期"#line:1486
    FlowGroup :str #line:1487
    "流程群組"#line:1488
    DeliveryDate :str #line:1489
    "最後結算日"#line:1490
    DynamicBanding :str #line:1491
    "適用動態價格穩定"#line:1492
    ProdID :str #line:1494
    """契約代號 (EX:CDF)"""#line:1495
    FutName :str #line:1496
    """期貨契約中文(EX:小型環球晶)"""#line:1497
    StkNo :str #line:1498
    """現股代碼(EX:2330)"""#line:1499
    ValuePerUnitOrg :str #line:1500
    """契約乘數"""#line:1501
    def Get_ValuePerUnit (OO00OO0OO000O0O00 )->decimal :#line:1503
        return OO00OO0OO000O0O00 .TransToDecimal (OO00OO0OO000O0O00 .fBAS [18 ])#line:1504
    StatusCode :str #line:1506
    "狀態碼"#line:1507
    Currency :str #line:1508
    "幣別"#line:1509
    AcceptQuoteFlag :str #line:1510
    "是否可報價"#line:1511
    BlockTradeFlag :str #line:1512
    "是否可鉅額交易"#line:1513
    ExpiryType :str #line:1514
    "到期別"#line:1515
    UnderlyingType :str #line:1516
    "現貨類別"#line:1517
    MarketCloseGroup :str #line:1518
    "商品收盤時間群組"#line:1519
    EndSession :str #line:1520
    MktType :str #line:1522
    """早午盤識別(早盤:0, 午盤:1)"""#line:1523
    SettleMth :str #line:1524
    """交割月"""#line:1525
    CallPutType :str #line:1526
    """C/P"""#line:1527
    StrikeP :str #line:1528
    """履約價"""#line:1529
    PreTotalMatchQty :str #line:1531
    """昨日成交總量"""#line:1532
    PreOpenInterest :str #line:1533
    """昨日未平倉合約數"""#line:1534
    PreTodayRefPrice :str #line:1535
    """昨日參考價"""#line:1536
    def Get_PreTodayRefPrice2Str (O0OOO0O0OOOO000OO ):#line:1537
        return O0OOO0O0OOOO000OO .TransPrice2Dec (O0OOO0O0OOOO000OO .fBAS [31 ])#line:1538
    def Get_PreTodayRefPrice2Dec (O0O0O00OOO00O0OO0 ):#line:1539
        return O0O0O00OOO00O0OO0 .TransPrice2Dec (O0O0O00OOO00O0OO0 .fBAS [31 ])#line:1540
    PreClosePrice :str #line:1542
    """昨日收盤價"""#line:1543
    def Get_PreClosePrice2Str (O0O00O00OO0O0OO0O ):#line:1544
        return O0O00O00OO0O0OO0O .TransPrice2Str (O0O00O00OO0O0OO0O .fBAS [32 ])#line:1545
    def Get_PreClosePrice2Dec (OOO00OO00OO0O0OO0 ):#line:1546
        return OOO00OO00OO0O0OO0 .TransPrice2Dec (OOO00OO00OO0O0OO0 .fBAS [32 ])#line:1547
    PreSettlePrice :str #line:1549
    """昨日結算價"""#line:1550
    def Get_PreSettlePrice2Str (OO00OOO00OO00O0O0 ):#line:1551
        return OO00OOO00OO00O0O0 .TransPrice2Str (OO00OOO00OO00O0O0 .fBAS [33 ])#line:1552
    def Get_PreSettlePrice2Dec (O000O0O0OOOOOO0O0 ):#line:1553
        return O000O0O0OOOOOO0O0 .TransPrice2Dec (O000O0O0OOOOOO0O0 .fBAS [33 ])#line:1554
    TickSizeInfo :str #line:1556
    """跳動點資訊"""#line:1557
    def Handle_BAS (O00000000O0OO00O0 ,OOO0OO00O0OO000OO :str ):#line:1560
        O00000000O0OO00O0 .fBAS =OOO0OO00O0OO000OO .split ("|")#line:1561
        O00000000O0OO00O0 .fHasBAS =len (O00000000O0OO00O0 .fBAS )>0 #line:1562
        O00000000O0OO00O0 .OrdProdID =O00000000O0OO00O0 .fBAS [0 ]#line:1563
        O00000000O0OO00O0 .RefPriceOrg =O00000000O0OO00O0 .fBAS [4 ]#line:1564
        O00000000O0OO00O0 .LimitPrice_UpOrg =O00000000O0OO00O0 .fBAS [5 ]#line:1565
        O00000000O0OO00O0 .LimitPrice_DownOrg =O00000000O0OO00O0 .fBAS [6 ]#line:1566
        O00000000O0OO00O0 .ProdKind =O00000000O0OO00O0 .fBAS [7 ]#line:1567
        O00000000O0OO00O0 .IdxDgtOrg =O00000000O0OO00O0 .fBAS [8 ]#line:1568
        O00000000O0OO00O0 .StrikePriceDecimalLocator =O00000000O0OO00O0 .fBAS [9 ]#line:1569
        O00000000O0OO00O0 .BeginDate =O00000000O0OO00O0 .fBAS [10 ]#line:1570
        O00000000O0OO00O0 .EndDate =O00000000O0OO00O0 .fBAS [11 ]#line:1571
        O00000000O0OO00O0 .FlowGroup =O00000000O0OO00O0 .fBAS [12 ]#line:1572
        O00000000O0OO00O0 .DeliveryDate =O00000000O0OO00O0 .fBAS [13 ]#line:1573
        O00000000O0OO00O0 .DynamicBanding =O00000000O0OO00O0 .fBAS [14 ]#line:1574
        O00000000O0OO00O0 .ProdID =O00000000O0OO00O0 .fBAS [15 ]#line:1575
        O00000000O0OO00O0 .FutName =O00000000O0OO00O0 .fBAS [16 ]#line:1576
        O00000000O0OO00O0 .StkNo =O00000000O0OO00O0 .fBAS [17 ]#line:1577
        O00000000O0OO00O0 .ValuePerUnitOrg =O00000000O0OO00O0 .fBAS [18 ]#line:1578
        O00000000O0OO00O0 .StatusCode =O00000000O0OO00O0 .fBAS [19 ]#line:1579
        O00000000O0OO00O0 .Currency =O00000000O0OO00O0 .fBAS [20 ]#line:1580
        O00000000O0OO00O0 .AcceptQuoteFlag =O00000000O0OO00O0 .fBAS [21 ]#line:1581
        O00000000O0OO00O0 .BlockTradeFlag =O00000000O0OO00O0 .fBAS [22 ]#line:1582
        O00000000O0OO00O0 .ExpiryType =O00000000O0OO00O0 .fBAS [23 ]#line:1583
        O00000000O0OO00O0 .UnderlyingType =O00000000O0OO00O0 .fBAS [24 ]#line:1584
        O00000000O0OO00O0 .MarketCloseGroup =O00000000O0OO00O0 .fBAS [25 ]#line:1585
        O00000000O0OO00O0 .EndSession =O00000000O0OO00O0 .fBAS [26 ]#line:1586
        O00000000O0OO00O0 .MktType =O00000000O0OO00O0 .fBAS [27 ]#line:1587
        if len (O00000000O0OO00O0 .fBAS [28 ])==0 or O00000000O0OO00O0 .fBAS [28 ]is None or O00000000O0OO00O0 .fBAS [28 ].isspace ():#line:1588
            O00000000O0OO00O0 .SettleMth =""#line:1589
        else :#line:1590
            O00000000O0OO00O0 .SettleMth =O00000000O0OO00O0 .fBAS [28 ].split (".")[1 ]#line:1591
        O00000000O0OO00O0 .CallPutType =""#line:1593
        if len (O00000000O0OO00O0 .fBAS [28 ])==0 or O00000000O0OO00O0 .fBAS [28 ]is None or O00000000O0OO00O0 .fBAS [28 ].isspace ():#line:1594
            O00000000O0OO00O0 .CallPutType =""#line:1595
        if "C"in O00000000O0OO00O0 .fBAS [28 ]:#line:1596
            O00000000O0OO00O0 .CallPutType ="C"#line:1597
        if "P"in O00000000O0OO00O0 .fBAS [28 ]:#line:1598
            O00000000O0OO00O0 .CallPutType ="P"#line:1599
        O00000000O0OO00O0 .StrikeP =""#line:1601
        if len (O00000000O0OO00O0 .fBAS [28 ])==0 or O00000000O0OO00O0 .fBAS [28 ]is None or O00000000O0OO00O0 .fBAS [28 ].isspace ():#line:1602
            O00000000O0OO00O0 .StrikeP =""#line:1603
        if "C"in O00000000O0OO00O0 .fBAS [28 ]:#line:1604
            O00000000O0OO00O0 .StrikeP =O00000000O0OO00O0 .fBAS [28 ].split (".")[1 ]#line:1605
        if "P"in O00000000O0OO00O0 .fBAS [28 ]:#line:1606
            O00000000O0OO00O0 .StrikeP =O00000000O0OO00O0 .fBAS [28 ].split (".")[1 ]#line:1607
        O00000000O0OO00O0 .PreTotalMatchQty =O00000000O0OO00O0 .fBAS [29 ]#line:1609
        O00000000O0OO00O0 .PreOpenInterest =O00000000O0OO00O0 .fBAS [30 ]#line:1610
        O00000000O0OO00O0 .PreTodayRefPrice =O00000000O0OO00O0 .fBAS [31 ]#line:1611
        O00000000O0OO00O0 .PreClosePrice =O00000000O0OO00O0 .fBAS [32 ]#line:1612
        O00000000O0OO00O0 .PreSettlePrice =O00000000O0OO00O0 .fBAS [33 ]#line:1613
        O00000000O0OO00O0 .TickSizeInfo =O00000000O0OO00O0 .fBAS [36 ]#line:1615
        if O00000000O0OO00O0 .fHasBAS :#line:1616
            O00000000O0OO00O0 .DECIMAL_LOCATOR_Org =O00000000O0OO00O0 .Get_IdxDgtOrg ()#line:1618
            if O00000000O0OO00O0 .DECIMAL_LOCATOR_Org ==0 :#line:1619
                O00000000O0OO00O0 .DECIMAL_LOCATOR_Dgt =1 #line:1620
            else :#line:1621
                O00000000O0OO00O0 .DECIMAL_LOCATOR_Dgt =1 /Decimal ("1".ljust (O00000000O0OO00O0 .DECIMAL_LOCATOR_Org +1 ,'0'))#line:1623
    def Handle_BAS_ChangeMktType (OOOOO0O0O0O0OOO00 ,OO0OOOOOO000O00O0 :str )->bool :#line:1625
        ""#line:1626
        try :#line:1627
            if OOOOO0O0O0O0OOO00 .fBAS is not None and len (OOOOO0O0O0O0OOO00 .fBAS )>28 :#line:1628
                O0OO0OO00OO000OOO =OO0OOOOOO000O00O0 .split ("|")#line:1629
                if len (O0OO0OO00OO000OOO )>28 :#line:1630
                    if O0OO0OO00OO000OOO [27 ]!=OOOOO0O0O0O0OOO00 .fBAS [27 ]:#line:1631
                        OOOOO0O0O0O0OOO00 .Handle_BAS (OO0OOOOOO000O00O0 )#line:1632
                        return True #line:1633
        except Exception as OOO00O0O0O000OOOO :#line:1634
            return False #line:1635
    def TransPrice2Dec (O0OOOOOOO00O0O000 ,OOO00O000O0O00O0O :str )->decimal :#line:1638
        try :#line:1639
            O0OOO0OO0O0O00OOO =Decimal (OOO00O000O0O00O0O )#line:1640
            O0OOO0OO0O0O00OOO =O0OOO0OO0O0O00OOO *O0OOOOOOO00O0O000 .DECIMAL_LOCATOR_Dgt #line:1641
            return O0OOO0OO0O0O00OOO #line:1642
        except Exception as OO0OO00OOOO00OOOO :#line:1643
            print (f"Not a Decimal{OO0OO00OOOO00OOOO}")#line:1644
            return 0 #line:1645
    def TransPrice2Str (OOOO0OOOOOOO0O000 ,OOOOO0O0O0O000O0O :str )->str :#line:1647
        if OOOO0OOOOOOO0O000 .DECIMAL_LOCATOR_Dgt ==1 :#line:1648
            return OOOOO0O0O0O000O0O #line:1649
        if OOOOO0O0O0O000O0O =="0":#line:1650
            return ""#line:1651
        if len (OOOOO0O0O0O000O0O )<OOOO0OOOOOOO0O000 .DECIMAL_LOCATOR_Org :#line:1652
            return OOOOO0O0O0O000O0O #line:1653
        if not OOOOO0O0O0O000O0O or OOOOO0O0O0O000O0O .isspace ():#line:1654
            return ""#line:1655
        try :#line:1656
            O000OO000O0O0OO0O =len (OOOOO0O0O0O000O0O )#line:1657
            return OOOOO0O0O0O000O0O [:O000OO000O0O0OO0O -OOOO0OOOOOOO0O000 .DECIMAL_LOCATOR_Org ]+'.'+OOOOO0O0O0O000O0O [O000OO000O0O0OO0O -OOOO0OOOOOOO0O000 .DECIMAL_LOCATOR_Org :]#line:1658
        except Exception as O0OO0O0OOO0OOOOOO :#line:1659
            return ""#line:1660
    def TransToInt (OOOO00O000OO0O0OO ,O000000000O0O0000 :str )->int :#line:1662
        try :#line:1663
            return int (O000000000O0O0000 )#line:1664
        except Exception as O00OO0O0O00OOOO00 :#line:1665
            pass #line:1667
        return 0 #line:1668
    def TransToDecimal (OO0O00OO00OOO00OO ,OOOOO0OOOOO0000OO :str )->decimal :#line:1670
        try :#line:1671
            return Decimal (OOOOO0OOOOO0000OO )#line:1672
        except Exception as OOO0000OOO0OO0O0O :#line:1673
            print (f"Not a Decimal{OOO0000OOO0OO0O0O}")#line:1674
        return 0 #line:1675
    def __init__ (O00O00OOO000OOOO0 )->None :#line:1678
        pass #line:1679
    def __str__ (O00OO0O0O00O00000 )->str :#line:1681
        return f"""OrdProdID:{O00OO0O0O00O00000.OrdProdID} RefPriceOrg:{O00OO0O0O00O00000.RefPriceOrg} LimitPrice_UpOrg:{O00OO0O0O00O00000.LimitPrice_UpOrg} LimitPrice_DownOrg:{O00OO0O0O00O00000.LimitPrice_DownOrg}"""+"""IdxDgtOrg:{self.IdxDgtOrg} ProdID:{self.ProdID} FutName:{self.FutName} StkNo:{self.StkNo} ValuePerUnitOrg:{self.ValuePerUnitOrg}"""+"""MktType:{self.MktType} SettleMth:{self.SettleMth} CallPutType:{self.CallPutType} StrikeP:{self.StrikeP} TickSizeInfo:{self.TickSizeInfo} """#line:1684
class TFutQtHL :#line:1685
    HasHL :bool =False #line:1687
    fHL =[]#line:1688
    TopicTX =""#line:1689
    Topic5Q =""#line:1690
    Topic5QTOT =""#line:1691
    TopicBas =""#line:1692
    DECIMAL_LOCATOR_Org :int =0 #line:1694
    """價格欄位小數位數"""#line:1695
    DECIMAL_LOCATOR_Dgt :decimal =1 #line:1696
    """價格欄位小數位數(若DECIMAL_LOCATOR_Org=2, 則此值為0.001)"""#line:1697
    Exchange :str #line:1698
    "市場別(TWS/TWF)"#line:1699
    Market :str #line:1700
    """商品別(FUT/OPT)"""#line:1701
    Symbol :str #line:1702
    """委託商品代碼(TXFA2)"""#line:1703
    TryMark_Deal :str #line:1704
    """成交試撮註記(試撮=1, 非試撮=0"""#line:1705
    TryMark :str #line:1706
    """試撮註記(試撮=1, 非試撮=0)"""#line:1707
    DealTime :str #line:1708
    """撮合時間(成交)(EX:173547.32700)"""#line:1709
    DealSn :str #line:1710
    """成交序號"""#line:1711
    def Get_DealSn (O0000O0OO0OO0OOOO )->int :#line:1713
        return O0000O0OO0OO0OOOO .TransToInt (O0000O0OO0OO0OOOO .fHL [7 ])#line:1714
    Sn_5Q :str #line:1715
    """五檔序號"""#line:1716
    def Get_Sn_5Q (O00OOO0OOOO000O00 )->int :#line:1718
        return O00OOO0OOOO000O00 .TransToInt (O00OOO0OOOO000O00 .fHL [8 ])#line:1719
    DealPriceOrg :str #line:1720
    """成交價"""#line:1721
    def Get_DealPrice2Str (OO0000000O0OOOO00 )->str :#line:1722
        return OO0000000O0OOOO00 .TransPrice2Str (OO0000000O0OOOO00 .fHL [9 ])#line:1723
    def Get_DealPrice2Dec (OO0O00O00O0O000OO )->decimal :#line:1724
        return OO0O00O00O0O000OO .TransPrice2Dec (OO0O00O00O0O000OO .fHL [9 ])#line:1725
    fDealPrice :decimal =0 #line:1727
    """成交價"""#line:1728
    def DealPrice (O0OOO00OO00OO0OOO )->decimal :#line:1730
        return O0OOO00OO00OO0OOO .fDealPrice #line:1731
    DealQty :str #line:1732
    """成交單量"""#line:1733
    def Get_DealQty2Dec (O0OO0OOOO00O0O00O )->decimal :#line:1735
        return O0OO0OOOO00O0O00O .TransToDecimal (O0OO0OOOO00O0O00O .fHL [10 ])#line:1736
    def Get_DealQty2Int (O000O0O0OOOOO0000 )->int :#line:1738
        return O000O0O0OOOOO0000 .TransToInt (O000O0O0OOOOO0000 .fHL [10 ])#line:1739
    HighPriceOrg :str #line:1740
    """當日最高價"""#line:1741
    def Get_HighPrice2Str (O000O000O00OOO000 )->str :#line:1743
        return O000O000O00OOO000 .TransPrice2Str (O000O000O00OOO000 .fHL [11 ])#line:1744
    def Get_HighPrice2Dec (OO0OO00O00OOOOO0O )->decimal :#line:1746
        return OO0OO00O00OOOOO0O .TransPrice2Dec (OO0OO00O00OOOOO0O .fHL [11 ])#line:1747
    LowPriceOrg :str #line:1748
    """當日最低價"""#line:1749
    def Get_LowPrice2Str (O0OOOOO00O000O0O0 )->str :#line:1751
        return O0OOOOO00O000O0O0 .TransPrice2Str (O0OOOOO00O000O0O0 .fHL [12 ])#line:1752
    def Get_LowPrice2Dec (O00O00O00OOO00OO0 )->decimal :#line:1754
        return O00O00O00OOO00OO0 .TransPrice2Dec (O00O00O00OOO00OO0 .fHL [12 ])#line:1755
    TotAmt :str #line:1756
    """成交總額"""#line:1757
    TotQty :str #line:1758
    """成交總量"""#line:1759
    def Get_TotQty2Dec (OO0000O0O00OO0OO0 )->decimal :#line:1761
        return OO0000O0O00OO0OO0 .TransToDecimal (OO0000O0O00OO0OO0 .fHL [14 ])#line:1762
    def Get_TotQty2Int (O0000O00O0O00OOO0 )->int :#line:1764
        return O0000O00O0O00OOO0 .TransToInt (O0000O00O0O00OOO0 .fHL [14 ])#line:1765
    FirstDerivedBuyPriceOrg :str #line:1767
    "衍生委託單第一檔買進價格"#line:1768
    def Get_FirstDerivedBuyPrice (OO0OO0OOOOO00O000 ):#line:1769
        return OO0OO0OOOOO00O000 .TransPrice2Str (OO0OO0OOOOO00O000 .fHL [35 ])#line:1770
    FirstDerivedBuyQty :str #line:1771
    "衍生委託單第一檔買進價格數量"#line:1772
    FirstDerivedSellPriceOrg :str #line:1773
    "衍生委託單第一檔賣出價格數量"#line:1774
    def Get_FirstDerivedSellPrice (OOO0OO000OOOO0OO0 ):#line:1775
        return OOO0OO000OOOO0OO0 .TransPrice2Str (OOO0OO000OOOO0OO0 .fHL [37 ])#line:1776
    FirstDerivedSellQty :str #line:1777
    "衍生委託單第一檔賣出價格數量"#line:1778
    OpenPriceOrg :str #line:1780
    """開盤價"""#line:1781
    def Get_OpenPrice2Str (OO00O0O0OO0OOOO0O ):#line:1782
        return OO00O0O0OO0OOOO0O .TransPrice2Str (OO00O0O0OO0OOOO0O .fHL [39 ])#line:1783
    def Get_OpenPrice2Dec (O000OOOO0O00OOOOO ):#line:1784
        return O000OOOO0O00OOOOO .TransPrice2Dec (O000OOOO0O00OOOOO .fHL [39 ])#line:1785
    def Get_OpenPrice2Str (OOO0O0O0OOOOO000O )->str :#line:1787
        return OOO0O0O0OOOOO000O .TransPrice2Str (OOO0O0O0OOOOO000O .fHL [39 ])#line:1788
    def Get_OpenPrice2Dec (O000O0OOOO0O00O00 )->decimal :#line:1790
        return O000O0OOOO0O00O00 .TransPrice2Dec (O000O0OOOO0O00O00 .fHL [39 ])#line:1791
    TryMark_5Q :str #line:1793
    "五檔試撮註記(試撮=1, 非試撮=0)"#line:1794
    ClosePrice :str #line:1795
    "收盤價"#line:1796
    def Get_ClosePrice (OO0O0OO0OO0OO00OO ):#line:1797
        return OO0O0OO0OO0OO00OO .TransPrice2Str (OO0O0OO0OO0OO00OO .fHL [41 ])#line:1798
    SettlePrice :str #line:1799
    "結算價<"#line:1800
    def Get_SettlePrice (OOOO00OOO0000OOOO ):#line:1801
        return OOOO00OOO0000OOOO .TransPrice2Str (OOOO00OOO0000OOOO .fHL [42 ])#line:1802
    OpenInterest :str #line:1803
    "未平倉合約數"#line:1804
    fAryB5Q_P =[15 ,17 ,19 ,21 ,23 ]#line:1808
    """買五檔價在字串中的位置"""#line:1809
    fAryB5Q_Q =[16 ,18 ,20 ,22 ,24 ]#line:1810
    """買五檔價在字串中的位置"""#line:1811
    fB5QCount :int =5 #line:1812
    """買5檔的檔數"""#line:1813
    def B5Q_POrg (OO0OOOO0OOOOOOOO0 ,O000000000O0OOO00 :int )->str :#line:1815
        ""#line:1816
        if O000000000O0OOO00 >OO0OOOO0OOOOOOOO0 .fB5QCount :#line:1817
            return ""#line:1818
        else :#line:1819
            return OO0OOOO0OOOOOOOO0 .fHL [OO0OOOO0OOOOOOOO0 .fAryB5Q_P [O000000000O0OOO00 -1 ]]#line:1820
    def Get_B5Q_P2Dec (O000O0OOO00O0OOO0 ,O00OO00O0000O0O0O :int )->decimal :#line:1822
        ""#line:1823
        if O00OO00O0000O0O0O >O000O0OOO00O0OOO0 .fB5QCount :#line:1824
            return 0 #line:1825
        else :#line:1826
            return O000O0OOO00O0OOO0 .TransPrice2Dec (O000O0OOO00O0OOO0 .fHL [O000O0OOO00O0OOO0 .fAryB5Q_P [O00OO00O0000O0O0O -1 ]])#line:1827
    def Get_B5Q_P2Str (OOOO0O00OOOO00O0O ,OO0O0OO000OOO0OOO :int )->str :#line:1829
        ""#line:1830
        if OO0O0OO000OOO0OOO >OOOO0O00OOOO00O0O .fB5QCount :#line:1831
            return ""#line:1832
        else :#line:1833
            return OOOO0O00OOOO00O0O .TransPrice2Str (OOOO0O00OOOO00O0O .fHL [OOOO0O00OOOO00O0O .fAryB5Q_P [OO0O0OO000OOO0OOO -1 ]])#line:1834
    def B5Q_QOrg (O000OOOOO00OO0OO0 ,OOOOOO0OO0O000O0O :int )->str :#line:1836
        ""#line:1837
        if OOOOOO0OO0O000O0O >O000OOOOO00OO0OO0 .fB5QCount :#line:1838
            return ""#line:1839
        else :#line:1840
            return O000OOOOO00OO0OO0 .fHL [O000OOOOO00OO0OO0 .fAryB5Q_Q [OOOOOO0OO0O000O0O -1 ]]#line:1841
    def Get_B5Q_Q (OO0OO00O0000OO000 ,OOOO0OO000O00O00O :int )->int :#line:1843
        ""#line:1844
        if OOOO0OO000O00O00O >OO0OO00O0000OO000 .fB5QCount :#line:1845
            return 0 #line:1846
        else :#line:1847
            return OO0OO00O0000OO000 .TransToInt (OO0OO00O0000OO000 .fHL [OO0OO00O0000OO000 .fAryB5Q_Q [OOOO0OO000O00O00O -1 ]])#line:1848
    fAryS5Q_P =[25 ,27 ,29 ,31 ,33 ]#line:1852
    """買五檔價在字串中的位置"""#line:1853
    fAryS5Q_Q =[26 ,28 ,30 ,32 ,34 ]#line:1854
    """買五檔價在字串中的位置"""#line:1855
    fS5QCount :int =5 #line:1856
    """賣5檔的檔數"""#line:1857
    def S5Q_POrg (OO0OO0O000OOOO0O0 ,OOOOOOO0O000OOO00 :int )->str :#line:1859
        ""#line:1860
        if OOOOOOO0O000OOO00 >OO0OO0O000OOOO0O0 .fS5QCount :#line:1861
            return ""#line:1862
        else :#line:1863
            return OO0OO0O000OOOO0O0 .fHL [OO0OO0O000OOOO0O0 .fAryS5Q_P [OOOOOOO0O000OOO00 -1 ]]#line:1864
    def Get_S5Q_P2Dec (OOOO0O0OOOOO00OOO ,O0OOOO0O00O0OO00O :int )->decimal :#line:1866
        ""#line:1867
        if O0OOOO0O00O0OO00O >OOOO0O0OOOOO00OOO .fS5QCount :#line:1868
            return 0 #line:1869
        else :#line:1870
            return OOOO0O0OOOOO00OOO .TransPrice2Dec (OOOO0O0OOOOO00OOO .fHL [OOOO0O0OOOOO00OOO .fAryS5Q_P [O0OOOO0O00O0OO00O -1 ]])#line:1871
    def Get_S5Q_P2Str (O000O0OO0000OO0OO ,OO00OO00000OO0O00 :int )->str :#line:1873
        ""#line:1874
        if OO00OO00000OO0O00 >O000O0OO0000OO0OO .fS5QCount :#line:1875
            return ""#line:1876
        else :#line:1877
            return O000O0OO0000OO0OO .TransPrice2Str (O000O0OO0000OO0OO .fHL [O000O0OO0000OO0OO .fAryS5Q_P [OO00OO00000OO0O00 -1 ]])#line:1878
    def S5Q_QOrg (O0OO0OO0O0OO0OO00 ,OOO0O00OO0O000O0O :int )->str :#line:1880
        ""#line:1881
        if OOO0O00OO0O000O0O >O0OO0OO0O0OO0OO00 .fS5QCount :#line:1882
            return ""#line:1883
        else :#line:1884
            return O0OO0OO0O0OO0OO00 .fHL [O0OO0OO0O0OO0OO00 .fAryS5Q_Q [OOO0O00OO0O000O0O -1 ]]#line:1885
    def Get_S5Q_Q (OOO0O00O0OOOOO000 ,O0OOO0O0O00O000O0 :int )->int :#line:1887
        ""#line:1888
        if O0OOO0O0O00O000O0 >OOO0O00O0OOOOO000 .fS5QCount :#line:1889
            return 0 #line:1890
        else :#line:1891
            return OOO0O00O0OOOOO000 .TransToInt (OOO0O00O0OOOOO000 .fHL [OOO0O00O0OOOOO000 .fAryS5Q_Q [O0OOO0O0O00O000O0 -1 ]])#line:1892
    def Handle_HL (O00OOOO00OOO0O000 ,OO00O0000O00O00O0 :str ):#line:1895
        O00OOOO00OOO0O000 .fHL =OO00O0000O00O00O0 .split ('|')#line:1896
        O00OOOO00OOO0O000 .HasHL =len (O00OOOO00OOO0O000 .fHL )>0 #line:1897
        O00OOOO00OOO0O000 .Exchange =O00OOOO00OOO0O000 .fHL [0 ]#line:1898
        O00OOOO00OOO0O000 .Market =O00OOOO00OOO0O000 .fHL [1 ]#line:1899
        O00OOOO00OOO0O000 .Symbol =O00OOOO00OOO0O000 .fHL [3 ]#line:1900
        O00OOOO00OOO0O000 .TryMark_Deal =O00OOOO00OOO0O000 .fHL [4 ]#line:1901
        O00OOOO00OOO0O000 .TryMark =O00OOOO00OOO0O000 .fHL [5 ]#line:1902
        O00OOOO00OOO0O000 .DealTime =O00OOOO00OOO0O000 .fHL [6 ]#line:1903
        O00OOOO00OOO0O000 .DealSn =O00OOOO00OOO0O000 .fHL [7 ]#line:1904
        O00OOOO00OOO0O000 .Sn_5Q =O00OOOO00OOO0O000 .fHL [8 ]#line:1905
        O00OOOO00OOO0O000 .DealPriceOrg =O00OOOO00OOO0O000 .fHL [9 ]#line:1906
        O00OOOO00OOO0O000 .DealQty =O00OOOO00OOO0O000 .fHL [10 ]#line:1907
        O00OOOO00OOO0O000 .HighPriceOrg =O00OOOO00OOO0O000 .fHL [11 ]#line:1908
        O00OOOO00OOO0O000 .LowPriceOrg =O00OOOO00OOO0O000 .fHL [12 ]#line:1909
        O00OOOO00OOO0O000 .TotAmt =O00OOOO00OOO0O000 .fHL [13 ]#line:1910
        O00OOOO00OOO0O000 .TotQty =O00OOOO00OOO0O000 .fHL [14 ]#line:1911
        O00OOOO00OOO0O000 .FirstDerivedBuyPriceOrg =O00OOOO00OOO0O000 .fHL [35 ]#line:1912
        O00OOOO00OOO0O000 .FirstDerivedBuyQty =O00OOOO00OOO0O000 .fHL [36 ]#line:1913
        O00OOOO00OOO0O000 .FirstDerivedSellPriceOrg =O00OOOO00OOO0O000 .fHL [37 ]#line:1914
        O00OOOO00OOO0O000 .FirstDerivedSellQty =O00OOOO00OOO0O000 .fHL [38 ]#line:1915
        O00OOOO00OOO0O000 .OpenPriceOrg =O00OOOO00OOO0O000 .fHL [39 ]#line:1916
        O00OOOO00OOO0O000 .TryMark_5Q =O00OOOO00OOO0O000 .fHL [40 ]#line:1917
        O00OOOO00OOO0O000 .ClosePrice =O00OOOO00OOO0O000 .fHL [41 ]#line:1918
        O00OOOO00OOO0O000 .SettlePrice =O00OOOO00OOO0O000 .fHL [42 ]#line:1919
        O00OOOO00OOO0O000 .OpenInterest =O00OOOO00OOO0O000 .fHL [43 ]#line:1920
        if O00OOOO00OOO0O000 .HasHL :#line:1921
            O00OOOO00OOO0O000 .TopicTX =f"Quote/TWF/{O00OOOO00OOO0O000.Market}/{O00OOOO00OOO0O000.Symbol}/TX"#line:1922
            O00OOOO00OOO0O000 .Topic5Q =f"Quote/TWF/{O00OOOO00OOO0O000.Market}/{O00OOOO00OOO0O000.Symbol}/5Q"#line:1923
            O00OOOO00OOO0O000 .Topic5QTOT =f"Quote/TWF/{O00OOOO00OOO0O000.Market}/{O00OOOO00OOO0O000.Symbol}/5QTOT"#line:1924
            O00OOOO00OOO0O000 .TopicBas =f"Quote/TWF/{O00OOOO00OOO0O000.Market}/{O00OOOO00OOO0O000.Symbol}/BAS"#line:1925
        O00OOOO00OOO0O000 .fDealPrice =O00OOOO00OOO0O000 .TransPrice2Dec (O00OOOO00OOO0O000 .DealPriceOrg )#line:1927
    def TransPrice2Dec (O0O00OOOOOO000000 ,O00O000OOOO0OO0O0 :str )->decimal :#line:1930
        try :#line:1931
            O0OOOOO0O000OOO00 =Decimal (O00O000OOOO0OO0O0 )#line:1932
            O0OOOOO0O000OOO00 =O0OOOOO0O000OOO00 *O0O00OOOOOO000000 .DECIMAL_LOCATOR_Dgt #line:1933
            return O0OOOOO0O000OOO00 #line:1934
        except Exception as OO0000OOOOO0OOOO0 :#line:1935
            return 0 #line:1936
    def TransPrice2Str (O00000O00OO00O0OO ,OO00OO00OO0O00OO0 :str )->str :#line:1938
        if O00000O00OO00O0OO .DECIMAL_LOCATOR_Dgt ==1 :#line:1939
            return OO00OO00OO0O00OO0 #line:1940
        if OO00OO00OO0O00OO0 =="0":#line:1941
            return ""#line:1942
        if len (OO00OO00OO0O00OO0 )<O00000O00OO00O0OO .DECIMAL_LOCATOR_Org :#line:1943
            return OO00OO00OO0O00OO0 #line:1944
        if not OO00OO00OO0O00OO0 or OO00OO00OO0O00OO0 .isspace ():#line:1945
            return ""#line:1946
        try :#line:1947
            OO0OOOO0OO00O00O0 =len (OO00OO00OO0O00OO0 )#line:1948
            return OO00OO00OO0O00OO0 [:OO0OOOO0OO00O00O0 -O00000O00OO00O0OO .DECIMAL_LOCATOR_Org ]+'.'+OO00OO00OO0O00OO0 [OO0OOOO0OO00O00O0 -O00000O00OO00O0OO .DECIMAL_LOCATOR_Org :]#line:1949
        except Exception as OOOO00OOOOOOOO000 :#line:1950
            return ""#line:1951
    def TransToInt (O0OOO000OO00O0OOO ,O00O00O0OOOOOOO00 :str )->int :#line:1953
        try :#line:1954
            return int (O00O00O0OOOOOOO00 )#line:1955
        except Exception as O0OOO0OO0OOOO0O0O :#line:1956
            pass #line:1958
        return 0 #line:1959
    def TransToDecimal (O0O000O0O000O0O00 ,O00OO00O00O0O0OO0 :str )->decimal :#line:1961
        try :#line:1962
            return Decimal (O00OO00O00O0O0OO0 )#line:1963
        except Exception as O0000OO0O00000O0O :#line:1964
            print (f"Not a Decimal{O0000OO0O00000O0O}")#line:1965
        return 0 #line:1966
    def __init__ (O0000O000OO0O0O00 )->None :#line:1969
        pass #line:1970
    def __str__ (OOOO00O0OO0O00O0O )->str :#line:1972
        return f"""Market:{OOOO00O0OO0O00O0O.Market} Symbol:{OOOO00O0OO0O00O0O.Symbol} TryMark:{OOOO00O0OO0O00O0O.TryMark} DealTime:{OOOO00O0OO0O00O0O.DealTime} DealSn:{OOOO00O0OO0O00O0O.DealSn}"""+"""Sn_5Q:{self.Sn_5Q} DealPriceOrg:{self.DealPriceOrg} DealQty:{self.DealQty} HighPriceOrg:{self.HighPriceOrg} LowPriceOrg:{self.LowPriceOrg}"""+"""TotQty:{self.TotQty} OpenPriceOrg:{self.OpenPriceOrg}"""#line:1975
class TFutQtTX :#line:1976
    DECIMAL_LOCATOR_Org :int =0 #line:1978
    """價格欄位小數位數"""#line:1979
    DECIMAL_LOCATOR_Dgt :decimal =1 #line:1980
    """價格欄位小數位數(若DECIMAL_LOCATOR_Org=2, 則此值為0.001)"""#line:1981
    fTX =[]#line:1982
    DataTime :str #line:1984
    """資料時間(交易所給的)(EX:173547.32700)"""#line:1985
    TryMark :str #line:1986
    """試撮註記(試撮=1, 非試撮=0)"""#line:1987
    DealTime :str #line:1988
    """撮合時間(成交)(EX:173547.32700)"""#line:1989
    DealSn :str #line:1990
    """成交序號"""#line:1991
    def Get_DealSn (O00O00OO0O000O0OO )->int :#line:1993
        return O00O00OO0O000O0OO .TransToInt (O00O00OO0O000O0OO .fTX [3 ])#line:1994
    TotQty :str #line:1995
    """成交總量"""#line:1996
    def Get_TotQty2Dec (OOO0OO0OO0OO0O000 )->decimal :#line:1998
        return OOO0OO0OO0OO0O000 .TransToDecimal (OOO0OO0OO0OO0O000 .fTX [7 ])#line:1999
    def Get_TotQty2Int (OOOOOO0O00OO00O0O )->int :#line:2001
        return OOOOOO0O00OO00O0O .TransToInt (OOOOOO0O00OO00O0O .fTX [7 ])#line:2002
    SumBuyDealCount :str #line:2003
    """累計買進成交筆數"""#line:2004
    def Get_SumBuyDealCount (OO00O0OO0OOO0O00O )->int :#line:2006
        return OO00O0OO0OOO0O00O .TransToInt (OO00O0OO0OOO0O00O .fTX [8 ])#line:2007
    SumSellDealCount :str #line:2008
    """累計賣出成交筆數"""#line:2009
    def Get_SumSellDealCount (O00000OOO0OO00O0O )->int :#line:2011
        return O00000OOO0OO00O0O .TransToInt (O00000OOO0OO00O0O .fTX [9 ])#line:2012
    DealCount :str #line:2013
    """成交價量檔數"""#line:2014
    def Get_DealCount (O0O0O0O0OO0O000OO )->int :#line:2016
        return O0O0O0O0OO0O000OO .TransToInt (O0O0O0O0OO0O000OO .fTX [11 ])#line:2017
    DealPriceOrg :str #line:2018
    """成交價"""#line:2019
    def Get_DealPrice2Dec (O00O0O0O0O00O000O )->decimal :#line:2021
        return O00O0O0O0O00O000O .TransPrice2Dec (O00O0O0O0O00O000O .fTX [12 ])#line:2022
    def Get_DealPrice2Str (OO00O0OO0OO0O000O )->str :#line:2024
        return OO00O0OO0OO0O000O .TransPrice2Str (OO00O0OO0OO0O000O .fTX [12 ])#line:2025
    DealQty :str #line:2027
    """成交單量"""#line:2028
    def Get_DealQty2Dec (O0OO00OO000OOO000 )->decimal :#line:2030
        return O0OO00OO000OOO000 .TransToDecimal (O0OO00OO000OOO000 .fTX [13 ])#line:2031
    def Get_DealQty2Int (OOO0000O0O000OO00 )->int :#line:2033
        return OOO0000O0O000OO00 .TransToInt (OOO0000O0O000OO00 .fTX [13 ])#line:2034
    def Get_DealQty2IdxVal (O0OOOO0O0OOO00O0O ,OOOO0OOO00O0O0000 :int )->int :#line:2035
        return O0OOOO0O0OOO00O0O .TransToInt (O0OOOO0O0OOO00O0O .fTX [13 +(OOOO0OOO00O0O0000 *2 )])#line:2036
    fDealPrice :decimal =0 #line:2040
    "成交價"#line:2041
    HighPrice :decimal =0 #line:2042
    "當日最高價"#line:2043
    LowPrice :decimal =0 #line:2044
    "當日最低價"#line:2045
    def CalcHightLowPrice (OO00OO00OOO0000OO ):#line:2047
        ""#line:2048
        try :#line:2049
            OO00OO00OOO0000OO .fDealPrice =OO00OO00OOO0000OO .Get_DealPrice ()#line:2050
            OO00OO00OOO0000OO .HighPrice =math .Max (OO00OO00OOO0000OO .fDealPrice ,OO00OO00OOO0000OO .HighPrice )#line:2051
            OO00OO00OOO0000OO .LowPrice =OO00OO00OOO0000OO .fDealPrice if OO00OO00OOO0000OO .LowPrice ==0 else math .Min (OO00OO00OOO0000OO .fDealPrice ,OO00OO00OOO0000OO .LowPrice )#line:2053
        except Exception as O0000O0OOO0O0OOOO :#line:2054
            pass #line:2055
    def CalcHightLowPrice_None (OOOOOO000OOO00000 ):#line:2057
        pass #line:2058
    fPROC_CalcHightLowPrice :callable =None #line:2060
    "PROC_CalcHightLowPrice"#line:2061
    def SetData (OOOOO00OO00OO0O00 ):#line:2064
        OOOOO00OO00OO0O00 .DataTime =OOOOO00OO00OO0O00 .fTX [2 ]#line:2065
        OOOOO00OO00OO0O00 .DealSn =OOOOO00OO00OO0O00 .fTX [3 ]#line:2066
        OOOOO00OO00OO0O00 .TryMark ="1"if OOOOO00OO00OO0O00 .fTX [4 ]is None else OOOOO00OO00OO0O00 .fTX [4 ]#line:2067
        OOOOO00OO00OO0O00 .DealTime =OOOOO00OO00OO0O00 .fTX [5 ]#line:2068
        OOOOO00OO00OO0O00 .TotQty =OOOOO00OO00OO0O00 .fTX [7 ]#line:2069
        OOOOO00OO00OO0O00 .SumBuyDealCount =OOOOO00OO00OO0O00 .fTX [8 ]#line:2070
        OOOOO00OO00OO0O00 .SumSellDealCount =OOOOO00OO00OO0O00 .fTX [9 ]#line:2071
        OOOOO00OO00OO0O00 .DealCount =OOOOO00OO00OO0O00 .fTX [11 ]#line:2072
        OOOOO00OO00OO0O00 .DealPriceOrg =OOOOO00OO00OO0O00 .fTX [12 ]#line:2073
        OOOOO00OO00OO0O00 .DealQty =OOOOO00OO00OO0O00 .fTX [13 ]#line:2074
    def Handle_TXRcv (OO0OOOOO00000000O ,OOO0OOOOO0OO0OO00 :str ):#line:2076
        try :#line:2077
            O0OOOO000000OOOOO :int =0 #line:2078
            OOOO0000O0O0O00O0 :int =0 #line:2079
            O0OO0OO000OO000O0 =OOO0OOOOO0OO0OO00 .split ('|')#line:2080
            if O0OO0OO000OO000O0 [4 ]==TSolQuoteFutSet .TryMark_No :#line:2082
                OO0OOOOO00000000O .fPROC_HandleData =OO0OOOOO00000000O .HandleData #line:2083
                if OO0OOOOO00000000O .fTX ==None :#line:2085
                    OO0OOOOO00000000O .fTX =O0OO0OO000OO000O0 #line:2086
                    OO0OOOOO00000000O .SetData ()#line:2087
                else :#line:2088
                    OOOO0000O0O0O00O0 =OO0OOOOO00000000O .TransToInt (O0OO0OO000OO000O0 [3 ])#line:2089
                    O0OOOO000000OOOOO =OO0OOOOO00000000O .Get_DealSn ()#line:2090
                    if OOOO0000O0O0O00O0 >O0OOOO000000OOOOO :#line:2091
                        OO0OOOOO00000000O .fTX =O0OO0OO000OO000O0 #line:2092
                        OO0OOOOO00000000O .SetData ()#line:2093
                OO0OOOOO00000000O .fPROC_CalcHightLowPrice ()#line:2094
            else :#line:2095
                OO0OOOOO00000000O .fPROC_HandleData =OO0OOOOO00000000O .HandleData_TryMarket #line:2096
                OO0OOOOO00000000O .fPROC_HandleData (OOO0OOOOO0OO0OO00 )#line:2097
        except Exception as O0OOOO0OO0OO00OO0 :#line:2099
            pass #line:2100
    def Handle_TX (OO0O0O00O0000OO0O ,O0O0O000OO0O00OOO :str ):#line:2102
        OO0O0O00O0000OO0O .fPROC_HandleData (O0O0O000OO0O00OOO )#line:2103
    def HandleData_TryMarket (O0O000OO0OO0O00O0 ,O0OOOOOOOO0O000OO :str ):#line:2106
        ""#line:2107
        if O0OOOOOOOO0O000OO .split ('|')[4 ]==TSolQuoteFutSet .TryMark_No :#line:2108
            O0O000OO0OO0O00O0 .fPROC_HandleData =O0O000OO0OO0O00O0 .HandleData #line:2109
            O0O000OO0OO0O00O0 .fPROC_HandleData (O0OOOOOOOO0O000OO )#line:2110
        else :#line:2111
            O0O000OO0OO0O00O0 .fTX =O0OOOOOOOO0O000OO .split ('|')#line:2112
            O0O000OO0OO0O00O0 .SetData ()#line:2113
    def HandleData (O0O0O00O0OO0000OO ,O0O00O0O0O0OO0000 :str ):#line:2115
        ""#line:2116
        O0O0O00O0OO0000OO .fTX =O0O00O0O0O0OO0000 .split ('|')#line:2117
        O0O0O00O0OO0000OO .SetData ()#line:2118
        O0O0O00O0OO0000OO .fPROC_CalcHightLowPrice ()#line:2119
    fPROC_HandleData :callable =None #line:2121
    "PROC_HandleData"#line:2122
    def TransPrice2Dec (O00O0O0000O0O0O0O ,OOOO0OO00O00O0O00 :str )->decimal :#line:2126
        try :#line:2127
            OOOO000OO00OO0O00 =Decimal (OOOO0OO00O00O0O00 )#line:2128
            OOOO000OO00OO0O00 =OOOO000OO00OO0O00 *O00O0O0000O0O0O0O .DECIMAL_LOCATOR_Dgt #line:2129
            return OOOO000OO00OO0O00 #line:2130
        except Exception as OO00OO000O000O000 :#line:2131
            return 0 #line:2132
    def TransPrice2Str (OO0OO0OOOOOO00OO0 ,OOO0OO0O0O0O0O000 :str )->str :#line:2134
        if OO0OO0OOOOOO00OO0 .DECIMAL_LOCATOR_Dgt ==1 :#line:2135
            return OOO0OO0O0O0O0O000 #line:2136
        if OOO0OO0O0O0O0O000 =="0":#line:2137
            return ""#line:2138
        if len (OOO0OO0O0O0O0O000 )<OO0OO0OOOOOO00OO0 .DECIMAL_LOCATOR_Org :#line:2139
            return OOO0OO0O0O0O0O000 #line:2140
        if not OOO0OO0O0O0O0O000 or OOO0OO0O0O0O0O000 .isspace ():#line:2141
            return ""#line:2142
        try :#line:2143
            OO0O0000000OO000O =len (OOO0OO0O0O0O0O000 )#line:2144
            return OOO0OO0O0O0O0O000 [:OO0O0000000OO000O -OO0OO0OOOOOO00OO0 .DECIMAL_LOCATOR_Org ]+'.'+OOO0OO0O0O0O0O000 [OO0O0000000OO000O -OO0OO0OOOOOO00OO0 .DECIMAL_LOCATOR_Org :]#line:2145
        except Exception as OOOOO00O000OO0000 :#line:2146
            return ""#line:2147
    def TransToInt (O0O0OO0000OO0OO00 ,OOO0O000OO0O00OO0 :str )->int :#line:2149
        try :#line:2150
            return int (OOO0O000OO0O00OO0 )#line:2151
        except Exception as O0OO00O0O00O0OOO0 :#line:2152
            pass #line:2154
        return 0 #line:2155
    def TransToDecimal (OO00O00O00OO0OOOO ,O00OOO00O0000OOO0 :str )->decimal :#line:2157
        try :#line:2158
            return Decimal (O00OOO00O0000OOO0 )#line:2159
        except Exception as O000O0OOOOOO0O000 :#line:2160
            print (f"Not a Decimal{O000O0OOOOOO0O000}")#line:2161
        return 0 #line:2162
    def __init__ (OOOOO00O00OO00O0O ,O0O0OOOO00000O00O :bool )->None :#line:2165
        OOOOO00O00OO00O0O .fPROC_CalcHightLowPrice =OOOOO00O00OO00O0O .CalcHightLowPrice_None #line:2167
        if O0O0OOOO00000O00O :#line:2168
            OOOOO00O00OO00O0O .fPROC_CalcHightLowPrice =OOOOO00O00OO00O0O .CalcHightLowPrice #line:2169
        OOOOO00O00OO00O0O .fPROC_HandleData =OOOOO00O00OO00O0O .HandleData_TryMarket #line:2171
    def __str__ (O00000O0O0O0OOO00 ):#line:2173
        return f"""DataTime:{O00000O0O0O0OOO00.DataTime} TryMark:{O00000O0O0O0OOO00.TryMark} DealTime:{O00000O0O0O0OOO00.DealTime} DealSn:{O00000O0O0O0OOO00.DealSn}"""+"""TotQty:{self.TotQty} SumBuyDealCount:{self.SumBuyDealCount} SumSellDealCount:{self.SumSellDealCount}"""+"""DealCount:{self.DealCount} DealPriceOrg:{self.DealPriceOrg} DealQty:{self.DealQty} fDealPrice:{self.fDealPrice}"""+"""HighPrice:{self.HighPrice} LowPrice:{self.LowPrice} \n"""#line:2177
class TFutQt5Q :#line:2178
    DECIMAL_LOCATOR_Org :int =0 #line:2180
    "價格欄位小數位數"#line:2181
    DECIMAL_LOCATOR_Dgt :decimal =1 #line:2182
    "價格欄位小數位數(若DECIMAL_LOCATOR_Org=2, 則此值為0.001)"#line:2183
    f5Q =[]#line:2184
    DataTime :str #line:2186
    "資料時間(交易所給的)(EX:173547.32700)"#line:2187
    Sn :str #line:2188
    "序號"#line:2189
    def Get_Sn (O00OOOOOO000000OO )->int :#line:2191
        return O00OOOOOO000000OO .TransToInt (O00OOOOOO000000OO .f5Q [3 ])#line:2192
    TryMark :str #line:2193
    "試撮註記(試撮=1, 非試撮=0)"#line:2194
    FirstDerivedBuyPriceOrg :str #line:2196
    "衍生委託單第一檔買進價格"#line:2197
    def Get_FirstDerivedBuyPrice (O0000OO00O0OO0O00 ):#line:2198
        return O0000OO00O0OO0O00 .TransPrice2Dec (O0000OO00O0OO0O00 .f5Q [25 ])#line:2199
    FirstDerivedBuyQty :str #line:2200
    "衍生委託單第一檔買進價格數量"#line:2201
    FirstDerivedSellPriceOrg :str #line:2202
    "衍生委託單第一檔賣出價格數量"#line:2203
    def Get_FirstDerivedSellPrice (O0OO00000OO000000 ):#line:2204
        return O0OO00000OO000000 .TransPrice2Str (O0OO00000OO000000 .f5Q [27 ])#line:2205
    FirstDerivedSellQty :str #line:2206
    "衍生委託單第一檔賣出價格數量"#line:2207
    def Handle_5Q (OOO0OO0O0O0O000OO ,O0O0OOO0OOOO00000 :str ):#line:2208
        OOO0OO0O0O0O000OO .fPROC_HandleData (O0O0OOO0OOOO00000 )#line:2209
    def HandleData_TryMarket (O0O0O0O0O000O0OOO ,OOOO00OOO00000O00 :str ):#line:2212
        ""#line:2213
        if OOOO00OOO00000O00 .split ('|')[4 ]==TSolQuoteFutSet .TryMark_No :#line:2214
            O0O0O0O0O000O0OOO .fPROC_HandleData =O0O0O0O0O000O0OOO .HandleData #line:2215
            O0O0O0O0O000O0OOO .fPROC_HandleData (OOOO00OOO00000O00 )#line:2216
        else :#line:2217
            O0O0O0O0O000O0OOO .f5Q =OOOO00OOO00000O00 .split ('|')#line:2218
            O0O0O0O0O000O0OOO .SetData ()#line:2219
    def HandleData (O0OO00O0OOO0OOOOO ,OO0O0OO00O0OOO00O :str ):#line:2221
        ""#line:2222
        O0OO00O0OOO0OOOOO .f5Q =OO0O0OO00O0OOO00O .split ('|')#line:2223
        O0OO00O0OOO0OOOOO .SetData ()#line:2224
    def SetData (O0OO00O0O0OOOO000 ):#line:2226
        O0OO00O0O0OOOO000 .DataTime =O0OO00O0O0OOOO000 .f5Q [2 ]#line:2227
        O0OO00O0O0OOOO000 .Sn =O0OO00O0O0OOOO000 .f5Q [3 ]#line:2228
        O0OO00O0O0OOOO000 .TryMark ="1"if O0OO00O0O0OOOO000 .f5Q is None else O0OO00O0O0OOOO000 .f5Q [4 ]#line:2229
        O0OO00O0O0OOOO000 .FirstDerivedBuyPriceOrg =O0OO00O0O0OOOO000 .f5Q [25 ]#line:2230
        O0OO00O0O0OOOO000 .FirstDerivedBuyQty =O0OO00O0O0OOOO000 .f5Q [26 ]#line:2231
        O0OO00O0O0OOOO000 .FirstDerivedSellPriceOrg =O0OO00O0O0OOOO000 .f5Q [27 ]#line:2232
        O0OO00O0O0OOOO000 .FirstDerivedSellQty =O0OO00O0O0OOOO000 .f5Q [28 ]#line:2233
    fPROC_HandleData :callable =None #line:2235
    "PROC_HandleData"#line:2236
    fAryB5Q_P =[5 ,7 ,9 ,11 ,13 ]#line:2240
    "買五檔價在字串中的位置"#line:2241
    fAryB5Q_Q =[6 ,8 ,10 ,12 ,14 ]#line:2242
    "買五檔價在字串中的位置"#line:2243
    fB5QCount :int =5 #line:2244
    "買5檔的檔數"#line:2245
    def B5Q_POrg (OO00000OOOOOO0000 ,O0OOO00000O0000OO :int )->str :#line:2247
        ""#line:2248
        if O0OOO00000O0000OO >OO00000OOOOOO0000 .fB5QCount :#line:2249
            return ""#line:2250
        elif OO00000OOOOOO0000 .f5Q is None :#line:2251
            return ""#line:2252
        else :#line:2253
            return OO00000OOOOOO0000 .f5Q [OO00000OOOOOO0000 .fAryB5Q_P [O0OOO00000O0000OO -1 ]]#line:2254
    def Get_B5Q_P2Dec (OOO00000OO00O0O00 ,O0000OOOO00000000 :int )->decimal :#line:2256
        ""#line:2257
        if O0000OOOO00000000 >OOO00000OO00O0O00 .fB5QCount :#line:2258
            return 0 #line:2259
        elif OOO00000OO00O0O00 .f5Q is None :#line:2260
            return 0 #line:2261
        else :#line:2262
            return OOO00000OO00O0O00 .TransPrice2Dec (OOO00000OO00O0O00 .f5Q [OOO00000OO00O0O00 .fAryB5Q_P [O0000OOOO00000000 -1 ]])#line:2263
    def Get_B5Q_P2Str (O00O0OOO00O0OO0O0 ,OOOOO00O000O00O00 :int )->str :#line:2265
        ""#line:2266
        if OOOOO00O000O00O00 >O00O0OOO00O0OO0O0 .fB5QCount :#line:2267
            return ""#line:2268
        elif O00O0OOO00O0OO0O0 .f5Q is None :#line:2269
            return ""#line:2270
        else :#line:2271
            return O00O0OOO00O0OO0O0 .TransPrice2Str (O00O0OOO00O0OO0O0 .f5Q [O00O0OOO00O0OO0O0 .fAryB5Q_P [OOOOO00O000O00O00 -1 ]])#line:2272
    def B5Q_QOrg (O0O00OO000O0000OO ,O0O000O00OO0OO0OO :int )->str :#line:2274
        ""#line:2275
        if O0O000O00OO0OO0OO >O0O00OO000O0000OO .fB5QCount :#line:2277
            return ""#line:2278
        elif O0O00OO000O0000OO .f5Q is None :#line:2279
            return ""#line:2280
        else :#line:2281
            return O0O00OO000O0000OO .f5Q [O0O00OO000O0000OO .fAryB5Q_Q [O0O000O00OO0OO0OO -1 ]]#line:2282
    def Get_B5Q_Q (OO0OOO000O0O0OOO0 ,OO00OOOO0O0O000OO :int )->int :#line:2284
        ""#line:2285
        if OO00OOOO0O0O000OO >OO0OOO000O0O0OOO0 .fB5QCount :#line:2286
            return 0 #line:2287
        elif OO0OOO000O0O0OOO0 .f5Q is None :#line:2288
            return 0 #line:2289
        else :#line:2290
            return OO0OOO000O0O0OOO0 .TransToInt (OO0OOO000O0O0OOO0 .f5Q [OO0OOO000O0O0OOO0 .fAryB5Q_Q [OO00OOOO0O0O000OO -1 ]])#line:2291
    fAryS5Q_P =[15 ,17 ,19 ,21 ,23 ]#line:2296
    "買五檔價在字串中的位置"#line:2297
    fAryS5Q_Q =[16 ,18 ,20 ,22 ,24 ]#line:2298
    "買五檔價在字串中的位置"#line:2299
    fS5QCount :int =5 #line:2300
    "賣5檔的檔數"#line:2301
    def S5Q_POrg (OOO00000O00O0O0OO ,O000O00O0OO00000O :int )->str :#line:2303
        ""#line:2304
        if O000O00O0OO00000O >OOO00000O00O0O0OO .fS5QCount :#line:2305
            return ""#line:2306
        elif OOO00000O00O0O0OO .f5Q is None :#line:2307
            return ""#line:2308
        else :#line:2309
            return OOO00000O00O0O0OO .f5Q [OOO00000O00O0O0OO .fAryS5Q_P [O000O00O0OO00000O -1 ]]#line:2310
    def Get_S5Q_P2Dec (O000O0OO00000O000 ,OO0O0O000O0O00O0O :int )->decimal :#line:2312
        ""#line:2313
        if OO0O0O000O0O00O0O >O000O0OO00000O000 .fS5QCount :#line:2314
            return 0 #line:2315
        elif O000O0OO00000O000 .f5Q is None :#line:2316
            return 0 #line:2317
        else :#line:2318
            return O000O0OO00000O000 .TransPrice2Dec (O000O0OO00000O000 .f5Q [O000O0OO00000O000 .fAryS5Q_P [OO0O0O000O0O00O0O -1 ]])#line:2319
    def Get_S5Q_P2Str (OO000OOOO000OO000 ,OOOO0O0OOO0O00OO0 :int )->str :#line:2321
        ""#line:2322
        if OOOO0O0OOO0O00OO0 >OO000OOOO000OO000 .fS5QCount :#line:2323
            return ""#line:2324
        elif OO000OOOO000OO000 .f5Q is None :#line:2325
            return ""#line:2326
        else :#line:2327
            return OO000OOOO000OO000 .TransPrice2Str (OO000OOOO000OO000 .f5Q [OO000OOOO000OO000 .fAryS5Q_P [OOOO0O0OOO0O00OO0 -1 ]])#line:2328
    def S5Q_QOrg (O000OOOOO0O0OOOO0 ,O0O00OO0OOOOO0O0O :int )->str :#line:2330
        ""#line:2331
        if O0O00OO0OOOOO0O0O >O000OOOOO0O0OOOO0 .fS5QCount :#line:2332
            return ""#line:2333
        elif O000OOOOO0O0OOOO0 .f5Q is None :#line:2334
            return ""#line:2335
        else :#line:2336
            return O000OOOOO0O0OOOO0 .f5Q [O000OOOOO0O0OOOO0 .fAryS5Q_Q [O0O00OO0OOOOO0O0O -1 ]]#line:2337
    def Get_S5Q_Q (O00O0O0OOOO0OOOO0 ,OOO00OO00OOO00OOO :int )->int :#line:2339
        ""#line:2340
        if OOO00OO00OOO00OOO >O00O0O0OOOO0OOOO0 .fS5QCount :#line:2341
            return 0 #line:2342
        elif O00O0O0OOOO0OOOO0 .f5Q is None :#line:2343
            return 0 #line:2344
        else :#line:2345
            return O00O0O0OOOO0OOOO0 .TransToInt (O00O0O0OOOO0OOOO0 .f5Q [O00O0O0OOOO0OOOO0 .fAryS5Q_Q [OOO00OO00OOO00OOO -1 ]])#line:2346
    def TransPrice2Dec (O00OOOOO0O00000O0 ,OOOOOOO00000OOOOO :str )->decimal :#line:2351
        try :#line:2352
            O0OO00O0OOOO0O00O =Decimal (OOOOOOO00000OOOOO )#line:2353
            O0OO00O0OOOO0O00O =O0OO00O0OOOO0O00O *O00OOOOO0O00000O0 .DECIMAL_LOCATOR_Dgt #line:2354
            return O0OO00O0OOOO0O00O #line:2355
        except Exception as O00000O0000OOOOOO :#line:2356
            return 0 #line:2357
    def TransPrice2Str (O0O00O000O00OOOOO ,OOO00O0OO00OO000O :str )->str :#line:2359
        if O0O00O000O00OOOOO .DECIMAL_LOCATOR_Dgt ==1 :#line:2360
            return OOO00O0OO00OO000O #line:2361
        if OOO00O0OO00OO000O =="0":#line:2362
            return ""#line:2363
        if len (OOO00O0OO00OO000O )<O0O00O000O00OOOOO .DECIMAL_LOCATOR_Org :#line:2364
            return OOO00O0OO00OO000O #line:2365
        if not OOO00O0OO00OO000O or OOO00O0OO00OO000O .isspace ():#line:2366
            return ""#line:2367
        try :#line:2368
            OOOO0000O0O0OOOOO =len (OOO00O0OO00OO000O )#line:2369
            return OOO00O0OO00OO000O [:OOOO0000O0O0OOOOO -O0O00O000O00OOOOO .DECIMAL_LOCATOR_Org ]+'.'+OOO00O0OO00OO000O [OOOO0000O0O0OOOOO -O0O00O000O00OOOOO .DECIMAL_LOCATOR_Org :]#line:2370
        except Exception as OOO000OOOO000OO0O :#line:2371
            return ""#line:2372
    def TransToInt (O000OOO000O000000 ,O000O00OO0OO00O00 :str )->int :#line:2374
        try :#line:2375
            return int (O000O00OO0OO00O00 )#line:2376
        except Exception as O00000000OO00O000 :#line:2377
            pass #line:2379
        return 0 #line:2380
    def TransToDecimal (O0OO0OOOOO0000OOO ,OOO00OO0OOO0OO000 :str )->decimal :#line:2382
        try :#line:2383
            return Decimal (OOO00OO0OOO0OO000 )#line:2384
        except Exception as OOO000OO0O0OO00O0 :#line:2385
            print (f"Not a Decimal{OOO000OO0O0OO00O0}")#line:2386
        return 0 #line:2387
    def __init__ (O0O00000OO0O00000 )->None :#line:2390
        O0O00000OO0O00000 .fPROC_HandleData =O0O00000OO0O00000 .HandleData_TryMarket #line:2392
    def __str__ (OOOO0OOOO0OO00000 ):#line:2394
        return f"""DataTime:{OOOO0OOOO0OO00000.DataTime} Sn:{OOOO0OOOO0OO00000.Sn} TryMark:{OOOO0OOOO0OO00000.TryMark} f5Q:{OOOO0OOOO0OO00000.f5Q}"""#line:2395
class TFutQt5QTOT :#line:2396
    f5QTOT =[]#line:2397
    DataTime :str #line:2399
    "資料時間(交易所給的)(EX:173547.32700)"#line:2400
    Sn :str #line:2401
    "序號"#line:2402
    def Get_Sn (OOO00O0OO0O0O0OOO )->int :#line:2404
        return OOO00O0OO0O0O0OOO .TransToInt (OOO00O0OO0O0O0OOO .f5QTOT [3 ])#line:2405
    SumBuyOrderCount :str #line:2406
    "買進累計委託筆數"#line:2407
    def Get_SumBuyOrderCount (OOO0000O00O0OOO0O )->int :#line:2409
        return OOO0000O00O0OOO0O .TransToInt (OOO0000O00O0OOO0O .f5QTOT [4 ])#line:2410
    SumBuyOrderQty :str #line:2411
    "買進累計委託合約數"#line:2412
    def Get_SumBuyOrderQty (OOO0OOO0O000OO0OO )->int :#line:2414
        return OOO0OOO0O000OO0OO .TransToInt (OOO0OOO0O000OO0OO .f5QTOT [5 ])#line:2415
    SumSellOrderCount :str #line:2416
    "賣出累計委託筆數"#line:2417
    def Get_SumSellOrderCount (O0000O0O0O0O0O0OO )->int :#line:2419
        return O0000O0O0O0O0O0OO .TransToInt (O0000O0O0O0O0O0OO .f5QTOT [6 ])#line:2420
    SumSellOrderQty :str #line:2421
    "賣出累計委託合約數"#line:2422
    def Get_SumSellOrderQty (OO0O0O0000O00OO0O )->int :#line:2424
        return OO0O0O0000O00OO0O .TransToInt (OO0O0O0000O00OO0O .f5QTOT [7 ])#line:2425
    def Handle_5QTOT (OO0OOOOO0000OOOOO ,OOOO000O000O000O0 :str ):#line:2427
        OO0OOOOO0000OOOOO .f5QTOT =OOOO000O000O000O0 .split ('|')#line:2428
        OO0OOOOO0000OOOOO .DataTime =OO0OOOOO0000OOOOO .f5QTOT [2 ]#line:2430
        OO0OOOOO0000OOOOO .Sn =OO0OOOOO0000OOOOO .f5QTOT [3 ]#line:2431
        OO0OOOOO0000OOOOO .SumBuyOrderCount =OO0OOOOO0000OOOOO .f5QTOT [4 ]#line:2432
        OO0OOOOO0000OOOOO .SumBuyOrderQty =OO0OOOOO0000OOOOO .f5QTOT [5 ]#line:2433
        OO0OOOOO0000OOOOO .SumSellOrderCount =OO0OOOOO0000OOOOO .f5QTOT [6 ]#line:2434
        OO0OOOOO0000OOOOO .SumSellOrderQty =OO0OOOOO0000OOOOO .f5QTOT [7 ]#line:2435
    def TransToInt (OOO0OOOOO0OOOO0O0 ,OOO0OOO0O0OOO0OO0 :str )->int :#line:2438
        try :#line:2439
            return int (OOO0OOO0O0OOO0OO0 )#line:2440
        except Exception as OO0O00O000O0OOO00 :#line:2441
            return 0 #line:2442
    def TransToDecimal (OO000O00O0OOO000O ,O0000OOOOOO00O0O0 :str )->decimal :#line:2444
        try :#line:2445
            return Decimal (O0000OOOOOO00O0O0 )#line:2446
        except Exception as OO00OOO00O00O0O0O :#line:2447
            return 0 #line:2448
    def __init__ (O0O000000O0000OOO )->None :#line:2451
        pass #line:2452
    def __str__ (OOO00OOO00O0O0OOO )->str :#line:2454
        return f"""DataTime:{OOO00OOO00O0O0OOO.DataTime} Sn:{OOO00OOO00O0O0OOO.Sn} SumBuyOrderCount:{OOO00OOO00O0O0OOO.SumBuyOrderCount} SumBuyOrderQty:{OOO00OOO00O0O0OOO.SumBuyOrderQty}"""+"""SumSellOrderCount:{self.SumSellOrderCount} SumSellOrderQty:{self.SumSellOrderQty}"""#line:2456
class TFutQtIDX :#line:2457
    fIsGotDgtVal :bool =False #line:2458
    fDECIMAL_LOCATOR_Org :int =0 #line:2459
    "指數小數位數"#line:2460
    fDECIMAL_LOCATOR_Dgt :decimal =1 #line:2461
    "指數小數位數(若DECIMAL_LOCATOR_Org=2, 則此值為0.001)"#line:2462
    fIdx =[]#line:2463
    DataTime :str #line:2466
    "資料時間(交易所給的)(EX:173547.32700)"#line:2467
    Sn :str #line:2468
    "序號"#line:2469
    def Get_Sn (OO00O0O00000OO0O0 )->int :#line:2471
        return OO00O0O00000OO0O0 .TransToInt (OO00O0O00000OO0O0 .fIdx [3 ])#line:2472
    TryMark :str #line:2473
    "試撮註記(試撮=1, 非試撮=0)"#line:2474
    DealTime :str #line:2475
    "指數編篡時間(EX:173547.32700)"#line:2476
    IdxDgtOrg :str #line:2477
    "指數小數位數"#line:2478
    def Get_IdxDgtOrg (OO0O0OO00O00O00OO )->int :#line:2480
        return OO0O0OO00O00O00OO .TransToInt (OO0O0OO00O00O00OO .fIdx [7 ])#line:2481
    IdxValueOrg :str #line:2482
    "指數"#line:2483
    def Get_IdxValue2Dec (OOOOOO0OOOO00O00O )->decimal :#line:2485
        return OOOOOO0OOOO00O00O .TransPrice2Dec (OOOOOO0OOOO00O00O .fIdx [6 ])#line:2486
    def Get_IdxValue2Str (OOOO00O0O00OOOO0O )->str :#line:2488
        return OOOO00O0O00OOOO0O .TransPrice2Str (OOOO00O0O00OOOO0O .fIdx [6 ])#line:2489
    HighIdxValueOrg :str #line:2490
    "當日最高指數"#line:2491
    def Get_HighIdxValue2Dec (OOOOOO0O0OO0O0000 )->decimal :#line:2493
        return OOOOOO0O0OO0O0000 .TransPrice2Dec (OOOOOO0O0OO0O0000 .fIdx [8 ])#line:2494
    def Get_HighIdxValue2Str (O0O0O0OOOOOOO0000 )->str :#line:2496
        return O0O0O0OOOOOOO0000 .TransPrice2Str (O0O0O0OOOOOOO0000 .fIdx [8 ])#line:2497
    LowIdxValueOrg :str #line:2499
    "當日最低指數"#line:2500
    def Get_LowIdxValue2Dec (OOOO000O00OO0000O )->decimal :#line:2502
        return OOOO000O00OO0000O .TransPrice2Dec (OOOO000O00OO0000O .fIdx [9 ])#line:2503
    def Get_LowIdxValue2Str (OO0O0OOOO0OOO0O0O )->str :#line:2505
        return OO0O0OOOO0OOO0O0O .TransPrice2Str (OO0O0OOOO0OOO0O0O .fIdx [9 ])#line:2506
    OpenIdxValueOrg :str #line:2508
    "開盤指數"#line:2509
    def Get_OpenIdxValue2Dec (OOO0OO0OOO0O00OOO )->decimal :#line:2511
        return OOO0OO0OOO0O00OOO .TransPrice2Dec (OOO0OO0OOO0O00OOO .fIdx [10 ])#line:2512
    def Get_OpenIdxValue2Str (O0O0OO0OO000OO00O )->str :#line:2514
        return O0O0OO0OO000OO00O .TransPrice2Str (O0O0OO0OO000OO00O .fIdx [10 ])#line:2515
    def Handle_IDX (OO0O00OO0000O0O00 ,OO000000OO0O0000O :str ):#line:2518
        OO0O00OO0000O0O00 .fIdx =OO000000OO0O0000O .split ('|')#line:2519
        OO0O00OO0000O0O00 .DataTime =OO0O00OO0000O0O00 .fIdx [2 ]#line:2521
        OO0O00OO0000O0O00 .Sn =OO0O00OO0000O0O00 .fIdx [3 ]#line:2522
        OO0O00OO0000O0O00 .TryMark =OO0O00OO0000O0O00 .fIdx [4 ]#line:2523
        OO0O00OO0000O0O00 .DealTime =OO0O00OO0000O0O00 .fIdx [5 ]#line:2524
        OO0O00OO0000O0O00 .IdxValueOrg =OO0O00OO0000O0O00 .fIdx [6 ]#line:2525
        OO0O00OO0000O0O00 .IdxDgtOrg =OO0O00OO0000O0O00 .fIdx [7 ]#line:2526
        OO0O00OO0000O0O00 .HighIdxValueOrg =OO0O00OO0000O0O00 .fIdx [8 ]#line:2527
        OO0O00OO0000O0O00 .LowIdxValueOrg =OO0O00OO0000O0O00 .fIdx [9 ]#line:2528
        OO0O00OO0000O0O00 .OpenIdxValueOrg =OO0O00OO0000O0O00 .fIdx [10 ]#line:2529
        if OO0O00OO0000O0O00 .fIsGotDgtVal ==False :#line:2532
            OO0O00OO0000O0O00 .fDECIMAL_LOCATOR_Org =OO0O00OO0000O0O00 .Get_IdxDgtOrg ()#line:2534
            if OO0O00OO0000O0O00 .fDECIMAL_LOCATOR_Org ==0 :#line:2535
                OO0O00OO0000O0O00 .fDECIMAL_LOCATOR_Dgt =1 #line:2536
            else :#line:2537
                OO0O00OO0000O0O00 .fDECIMAL_LOCATOR_Dgt =1 /Decimal ("1".ljust (OO0O00OO0000O0O00 .fDECIMAL_LOCATOR_Dgt +1 ,'0'))#line:2539
            OO0O00OO0000O0O00 .fIsGotDgtVal =True #line:2541
    def TransPrice2Dec (OO000OO0OO0O0O0O0 ,OOOO0OOOOO00OO0OO :str )->decimal :#line:2544
        try :#line:2545
            O0O0OOOO000O0000O =Decimal (OOOO0OOOOO00OO0OO )#line:2546
            O0O0OOOO000O0000O =O0O0OOOO000O0000O *OO000OO0OO0O0O0O0 .DECIMAL_LOCATOR_Dgt #line:2547
            return O0O0OOOO000O0000O #line:2548
        except Exception as OO0OO0OOOO0OOO000 :#line:2549
            print (f"Not a Decimal{OO0OO0OOOO0OOO000}")#line:2550
            return 0 #line:2551
    def TransPrice2Str (O00OO0OOO0OOO00OO ,O000O0O0O0O000O0O :str )->str :#line:2553
        if O00OO0OOO0OOO00OO .DECIMAL_LOCATOR_Dgt ==1 :#line:2554
            return O000O0O0O0O000O0O #line:2555
        if O000O0O0O0O000O0O =="0":#line:2556
            return ""#line:2557
        if len (O000O0O0O0O000O0O )<O00OO0OOO0OOO00OO .DECIMAL_LOCATOR_Org :#line:2558
            return O000O0O0O0O000O0O #line:2559
        if not O000O0O0O0O000O0O or O000O0O0O0O000O0O .isspace ():#line:2560
            return ""#line:2561
        try :#line:2562
            OO000OOOOOOO000OO =len (O000O0O0O0O000O0O )#line:2563
            return O000O0O0O0O000O0O [:OO000OOOOOOO000OO -O00OO0OOO0OOO00OO .DECIMAL_LOCATOR_Org ]+'.'+O000O0O0O0O000O0O [OO000OOOOOOO000OO -O00OO0OOO0OOO00OO .DECIMAL_LOCATOR_Org :]#line:2564
        except Exception as OOO00O0OO0OO00OOO :#line:2565
            return ""#line:2566
    def TransToInt (O0O00O000000O0OOO ,OO0000000OO000O00 :str )->int :#line:2568
        try :#line:2569
            return int (OO0000000OO000O00 )#line:2570
        except Exception as O0O000O0O00O00OOO :#line:2571
            pass #line:2573
        return 0 #line:2574
    def TransToDecimal (O0O0O0OOO00O0O000 ,O0OOO000OO0OOO000 :str )->decimal :#line:2576
        try :#line:2577
            return Decimal (O0OOO000OO0OOO000 )#line:2578
        except Exception as O0O0O00O000OOOOOO :#line:2579
            print (f"Not a Decimal{O0O0O00O000OOOOOO}")#line:2580
        return 0 #line:2581
    def __init__ (O0OO0O0O00O00OO00 )->None :#line:2584
        pass #line:2585
    def __str__ (OO0OO00000O00OOOO )->str :#line:2587
        return f"""DataTime:{OO0OO00000O00OOOO.DataTime} Sn:{OO0OO00000O00OOOO.Sn} TryMark:{OO0OO00000O00OOOO.TryMark} DealTime:{OO0OO00000O00OOOO.DealTime} IdxValueOrg:{OO0OO00000O00OOOO.IdxValueOrg}"""+"""IdxDgtOrg:{self.IdxDgtOrg} HighIdxValueOrg:{self.HighIdxValueOrg} LowIdxValueOrg:{self.LowIdxValueOrg} OpenIdxValueOrg:{self.OpenIdxValueOrg}"""#line:2589
class TFutQuoteData :#line:2590
    SolIce =""#line:2591
    ProdKind :TFutProdKind =TFutProdKind .pkNone #line:2592
    BAS :TFutQtBase =None #line:2593
    HL :TFutQtHL =None #line:2594
    QtTX :TFutQtTX =None #line:2595
    Qt5Q :TFutQt5Q =None #line:2596
    Qt5QTOT :TFutQt5QTOT =None #line:2597
    QtIDX :TFutQtIDX =None #line:2598
    def __init__ (OOO00O0OOOOO0OO0O ,O0O0OOOOOOOO0O0O0 :TFutProdKind ,O00OO0OO000OOO0O0 :str ,OO00OO000O0O0OOOO :bool ):#line:2600
        ""#line:2601
        OOO00O0OOOOO0OO0O .SolIce =O00OO0OO000OOO0O0 #line:2603
        OOO00O0OOOOO0OO0O .ProdKind =O0O0OOOOOOOO0O0O0 #line:2604
        OOO00O0OOOOO0OO0O ._lock =Lock ()#line:2605
        if O0O0OOOOOOOO0O0O0 ==TFutProdKind .pkNormal :#line:2606
            OOO00O0OOOOO0OO0O .BAS =TFutQtBase ()#line:2607
            OOO00O0OOOOO0OO0O .HL =TFutQtHL ()#line:2608
            OOO00O0OOOOO0OO0O .QtTX =TFutQtTX (OO00OO000O0O0OOOO )#line:2609
            OOO00O0OOOOO0OO0O .Qt5Q =TFutQt5Q ()#line:2610
            OOO00O0OOOOO0OO0O .Qt5QTOT =TFutQt5QTOT ()#line:2611
        elif O0O0OOOOOOOO0O0O0 ==TFutProdKind .pkIndex :#line:2613
            OOO00O0OOOOO0OO0O .QtIDX =TFutQtIDX ()#line:2614
    def SetDataInit (OO0000O00OO00O0O0 ):#line:2616
        ""#line:2617
        if OO0000O00OO00O0O0 .ProdKind ==TFutProdKind .pkNormal :#line:2618
            OO0000O00OO00O0O0 .HL .DECIMAL_LOCATOR_Dgt =OO0000O00OO00O0O0 .BAS .DECIMAL_LOCATOR_Dgt #line:2619
            OO0000O00OO00O0O0 .QtTX .DECIMAL_LOCATOR_Dgt =OO0000O00OO00O0O0 .BAS .DECIMAL_LOCATOR_Dgt #line:2620
            OO0000O00OO00O0O0 .Qt5Q .DECIMAL_LOCATOR_Dgt =OO0000O00OO00O0O0 .BAS .DECIMAL_LOCATOR_Dgt #line:2621
            OO0000O00OO00O0O0 .HL .DECIMAL_LOCATOR_Org =OO0000O00OO00O0O0 .BAS .DECIMAL_LOCATOR_Org #line:2623
            OO0000O00OO00O0O0 .QtTX .DECIMAL_LOCATOR_Org =OO0000O00OO00O0O0 .BAS .DECIMAL_LOCATOR_Org #line:2624
            OO0000O00OO00O0O0 .Qt5Q .DECIMAL_LOCATOR_Org =OO0000O00OO00O0O0 .BAS .DECIMAL_LOCATOR_Org #line:2625
            OO0000O00OO00O0O0 .QtTX .HighPrice =OO0000O00OO00O0O0 .HL .Get_HighPrice2Dec ()#line:2627
            OO0000O00OO00O0O0 .QtTX .LowPrice =OO0000O00OO00O0O0 .HL .Get_LowPrice2Dec ()#line:2628
class TObjFutQuoteMap (UserDict ):#line:2630
    ""#line:2632
    DefProc_TX :callable =None #line:2636
    DefProc_5Q :callable =None #line:2637
    DefProc_Idx :callable =None #line:2638
    DefProc_5QTOT :callable =None #line:2639
    DefProc_BAS :callable =None #line:2640
    def __init__ (OOOO0OO0OO0OO000O ,mapping =None ,**O0OO0O0000O000OOO ):#line:2641
        if mapping is not None :#line:2642
            mapping ={str (O00OOOO00OO0OOOOO ).upper ():O0OOOOO0O0O0O0O00 for O00OOOO00OO0OOOOO ,O0OOOOO0O0O0O0O00 in mapping .items ()}#line:2645
        else :#line:2646
            mapping ={}#line:2647
        if O0OO0O0000O000OOO :#line:2648
            mapping .update ({str (OOOOOO0OO00O00OO0 ).upper ():O0OOOO000O0O0O00O for OOOOOO0OO00O00OO0 ,O0OOOO000O0O0O00O in O0OO0O0000O000OOO .items ()})#line:2651
        OOOO0OO0OO0OO000O .MapQtProc ={}#line:2653
        "各商品拆解行情proc(EX:TXF的TX與5Q, 行情拆解,是不同Proc)"#line:2654
        super ().__init__ (mapping )#line:2655
    def __setitem__ (O0O0OO0OOOO000OO0 ,O0000O00OO00000O0 ,O00O0O000O00OO000 ):#line:2657
        super ().__setitem__ (O0000O00OO00000O0 ,O00O0O000O00OO000 )#line:2658
    def AddRcvData (OOOO0O0OO0OO0000O ,OOOO0OOO00O0O0OO0 :str ,O00OO00O0OO0OO0OO :str ,O00O00O0000OOO0O0 :bool ):#line:2660
        ""#line:2664
        OO0000O0OO0OOOOO0 =""#line:2665
        O0000OO0OOOOO0000 :TFutQuoteData =None #line:2666
        try :#line:2667
            OO00O0O000OOO0OOO =json .loads (O00OO00O0OO0OO0OO )#line:2668
            if "status"in OO00O0O000OOO0OOO and len (OO00O0O000OOO0OOO ["status"])>0 :#line:2670
                if OO00O0O000OOO0OOO ["status"][0 ]=="error":#line:2671
                    OO0000O0OO0OOOOO0 =f"[期][AddRcvData](aSolIce={OOOO0OOO00O0O0OO0}, aData={O00OO00O0OO0OO0OO})行情回補資料有誤!"#line:2672
                    return False ,O0000OO0OOOOO0000 ,OO0000O0OO0OOOOO0 #line:2673
            if "BAS"in OO00O0O000OOO0OOO and len (OO00O0O000OOO0OOO ["BAS"])==0 :#line:2674
                OO0000O0OO0OOOOO0 =f"[期][AddRcvData](aSolIce={OOOO0OOO00O0O0OO0}, aData={O00OO00O0OO0OO0OO})沒有BAS資料!"#line:2675
                return False ,O0000OO0OOOOO0000 ,OO0000O0OO0OOOOO0 #line:2676
            if "HL"in OO00O0O000OOO0OOO and len (OO00O0O000OOO0OOO ["HL"])==0 :#line:2677
                OO0000O0OO0OOOOO0 =f"[期][AddRcvData](aSolIce={OOOO0OOO00O0O0OO0}, aData={O00OO00O0OO0OO0OO})沒有HL資料!"#line:2678
                return False ,O0000OO0OOOOO0000 ,OO0000O0OO0OOOOO0 #line:2679
            if OOOO0O0OO0OO0000O .data .get (OOOO0OOO00O0O0OO0 )is None :#line:2682
                O0OO00O0OOOOOOOOO =TFutQuoteData (TFutProdKind .pkNormal ,OOOO0OOO00O0O0OO0 ,O00O00O0000OOO0O0 )#line:2684
                O0OO00O0OOOOOOOOO .BAS .Handle_BAS (OO00O0O000OOO0OOO ["BAS"][0 ])#line:2685
                O0OO00O0OOOOOOOOO .HL .Handle_HL (OO00O0O000OOO0OOO ["HL"][0 ])#line:2686
                O0OO00O0OOOOOOOOO .SetDataInit ()#line:2687
                O0000OO0OOOOO0000 =O0OO00O0OOOOOOOOO #line:2688
                OOOO0O0OO0OO0000O [OOOO0OOO00O0O0OO0 ]=O0OO00O0OOOOOOOOO #line:2689
                return True ,O0000OO0OOOOO0000 ,""#line:2690
            else :#line:2691
                O0OO00O0OOOOOOOOO :TFutQuoteData =OOOO0O0OO0OO0000O [OOOO0OOO00O0O0OO0 ]#line:2692
                with O0OO00O0OOOOOOOOO ._lock :#line:2693
                    O0OO00O0OOOOOOOOO .BAS .Handle_BAS (OO00O0O000OOO0OOO ["BAS"][0 ])#line:2694
                    O0OO00O0OOOOOOOOO .HL .Handle_HL (OO00O0O000OOO0OOO ["HL"][0 ])#line:2695
                    O0OO00O0OOOOOOOOO .SetDataInit ()#line:2696
                    O0000OO0OOOOO0000 =O0OO00O0OOOOOOOOO #line:2697
                return True ,O0000OO0OOOOO0000 ,""#line:2698
        except Exception as OOOO0OOO0OOOO0OO0 :#line:2699
            OO0000O0OO0OOOOO0 =f"[期][AddRcvData](aSolIce={OOOO0OOO00O0O0OO0}, aData={O00OO00O0OO0OO0OO}){OOOO0OOO0OOOO0OO0}"#line:2700
        return False ,O0000OO0OOOOO0000 ,OO0000O0OO0OOOOO0 #line:2701
    def AddData (O00O00OO0O00OOO0O ,OOO00OOOO00OO0OO0 :TFutProdKind ,O0OO0O00O0O0O0OOO :str ,O0OOO0O0O00O0OO0O :bool ,O0OOO00O0OO0OO0O0 :str ,OO00O00O0OO000000 :callable ):#line:2703
        ""#line:2706
        try :#line:2707
            if O00O00OO0O00OOO0O .data .get (O0OO0O00O0O0O0OOO )is None :#line:2708
                OOO00OO00O0OOO0O0 =TFutQuoteData (OOO00OOOO00OO0OO0 ,O0OO0O00O0O0O0OOO ,O0OOO0O0O00O0OO0O )#line:2709
                O00O00OO0O00OOO0O [O0OOO00O0OO0OO0O0 ]=OOO00OO00O0OOO0O0 #line:2710
                if O00O00OO0O00OOO0O .MapQtProc .get (O0OOO00O0OO0OO0O0 )is None :#line:2712
                    O00O00OO0O00OOO0O .MapQtProc [O0OOO00O0OO0OO0O0 ]=OO00O00O0OO000000 #line:2713
                return True #line:2715
            else :#line:2716
                return True #line:2717
        except Exception as OOOOO00O00OO000O0 :#line:2718
            pass #line:2719
        return False #line:2720
    def AddDataBySolIce (OOO00OO00O00OO0O0 ,OO0000O000O0OOO0O :bool ,OOO0O000OO000O0OO :str ,OO0O0OOO0O0000000 ,O0O0OOOOO0OOOOO00 :bool ):#line:2722
        ""#line:2728
        OO000OO000O00O0O0 =""#line:2729
        OO000OO0O0O000OO0 :TObjFutQuoteMap =None #line:2730
        try :#line:2731
            OO000OO0O0O000OO0 =TObjFutQuoteMap ()#line:2733
            for O0OOOO00OO0O00O0O in OO0O0OOO0O0000000 ["BAS"]:#line:2734
                O0O000O00O000O0O0 =TFutQtBase ()#line:2735
                O0O000O00O000O0O0 .Handle_BAS (O0OOOO00OO0O00O0O )#line:2736
                if OO000OO0O0O000OO0 .data .get (O0O000O00O000O0O0 .OrdProdID )is None :#line:2738
                    OOOO0O0O0O00O0OO0 =TFutQuoteData (TFutProdKind .pkNormal ,O0O000O00O000O0O0 .OrdProdID ,O0O0OOOOO0OOOOO00 )#line:2739
                    OOOO0O0O0O00O0OO0 .BAS =O0O000O00O000O0O0 #line:2740
                    OO000OO0O0O000OO0 [O0O000O00O000O0O0 .OrdProdID ]=OOOO0O0O0O00O0OO0 #line:2741
            for O0OOOO00OO0O00O0O in OO0O0OOO0O0000000 ["HL"]:#line:2744
                O00O00O000O0O0O00 =TFutQtHL ()#line:2745
                O00O00O000O0O0O00 .Handle_HL (O0OOOO00OO0O00O0O )#line:2746
                if OO000OO0O0O000OO0 .data .get (O00O00O000O0O0O00 .Symbol ):#line:2747
                    OOOO0O0O0O00O0OO0 =OO000OO0O0O000OO0 [O00O00O000O0O0O00 .Symbol ]#line:2748
                    OOOO0O0O0O00O0OO0 .HL =O00O00O000O0O0O00 #line:2749
                    OOOO0O0O0O00O0OO0 .SetDataInit ()#line:2750
                    OOO0OOO0O0OOO00OO :O0OOOO00OO0O00O0O =OOOO0O0O0O00O0OO0 .HL .TopicTX #line:2752
                    O0OOOO000OOO000OO :O0OOOO00OO0O00O0O =OOOO0O0O0O00O0OO0 .HL .Topic5Q #line:2753
                    O0O0OO00O00O0OOOO :O0OOOO00OO0O00O0O =OOOO0O0O0O00O0OO0 .HL .Topic5QTOT #line:2754
                    OOOO0OO0OO00OOO00 :O0OOOO00OO0O00O0O =OOOO0O0O0O00O0OO0 .HL .TopicBas #line:2755
                    OOO00OO00O00OO0O0 [OOO0OOO0O0OOO00OO ]=OOOO0O0O0O00O0OO0 #line:2757
                    OOO00OO00O00OO0O0 [O0OOOO000OOO000OO ]=OOOO0O0O0O00O0OO0 #line:2758
                    OOO00OO00O00OO0O0 [O0O0OO00O00O0OOOO ]=OOOO0O0O0O00O0OO0 #line:2759
                    OOO00OO00O00OO0O0 [OOOO0OO0OO00OOO00 ]=OOOO0O0O0O00O0OO0 #line:2760
                    if OOO00OO00O00OO0O0 .MapQtProc .get (OOO0OOO0O0OOO00OO )is None :#line:2762
                        OOO00OO00O00OO0O0 .MapQtProc [OOO0OOO0O0OOO00OO ]=OOO00OO00O00OO0O0 .DefProc_TX #line:2763
                    if OOO00OO00O00OO0O0 .MapQtProc .get (O0OOOO000OOO000OO )is None :#line:2764
                        OOO00OO00O00OO0O0 .MapQtProc [O0OOOO000OOO000OO ]=OOO00OO00O00OO0O0 .DefProc_5Q #line:2765
                    if OOO00OO00O00OO0O0 .MapQtProc .get (O0O0OO00O00O0OOOO )is None :#line:2766
                        OOO00OO00O00OO0O0 .MapQtProc [O0O0OO00O00O0OOOO ]=OOO00OO00O00OO0O0 .DefProc_5QTOT #line:2767
                    if OOO00OO00O00OO0O0 .MapQtProc .get (OOOO0OO0OO00OOO00 )is None :#line:2768
                        OOO00OO00O00OO0O0 .MapQtProc [OOOO0OO0OO00OOO00 ]=OOO00OO00O00OO0O0 .DefProc_BAS #line:2769
            return len (OO000OO0O0O000OO0 )>0 ,OO000OO0O0O000OO0 ,OO000OO000O00O0O0 #line:2771
        except Exception as O000OOO0O0OOO00OO :#line:2772
            OO000OO000O00O0O0 =f"[期][AddDataBySolIce](aIsCat={OO0000O000O0OOO0O}, aSolIce={OOO0O000OO000O0OO}){O000OOO0O0OOO00OO}"#line:2773
        return False ,OO000OO0O0O000OO0 ,OO000OO000O00O0O0 #line:2774
    def GetItem_BySolIce (O00O0000O0O0O0OOO ,OO0OOOOO00O000O00 :str ):#line:2777
        ""#line:2780
        OOO0O000O0OOOO0OO =""#line:2781
        OO000O00O0O0OOOO0 =None #line:2782
        try :#line:2783
            OO0O00000O00OOO0O =[]#line:2784
            for O0OO0OOO0O0O000OO ,O00000OO0O0O00O00 in O00O0000O0O0O0OOO .items ():#line:2785
                O0OOOOOO0O00OO0O0 :TFutQuoteData #line:2786
                O0OOOOOO0O00OO0O0 =O00000OO0O0O00O00 #line:2787
                if (O0OOOOOO0O00OO0O0 .SolIce ==OO0OOOOO00O000O00 ):#line:2788
                    OO0O00000O00OOO0O .append (O0OO0OOO0O0O000OO )#line:2789
            OO000O00O0O0OOOO0 =OO0O00000O00OOO0O #line:2790
            if OO000O00O0O0OOOO0 is None or len (OO000O00O0O0OOOO0 )==0 :#line:2791
                OOO0O000O0OOOO0OO =f"[期][GetItem_BySolIce](aSolIce={OO0OOOOO00O000O00})商品已不存存!"#line:2792
                return False ,OO000O00O0O0OOOO0 ,OOO0O000O0OOOO0OO #line:2793
            else :#line:2794
                return True ,OO000O00O0O0OOOO0 ,""#line:2795
        except Exception as OO00OOOOOOOOOOO0O :#line:2796
            OOO0O000O0OOOO0OO =f"[期][GetItem_BySolIce](aSolIce={OO0OOOOO00O000O00}){OO00OOOOOOOOOOO0O}"#line:2797
        return False ,OO000O00O0O0OOOO0 ,OOO0O000O0OOOO0OO #line:2798
    def GetItem_ByCategory (OO0000OOO0OOOO00O ,OOO00O0O000OOO0OO :str ):#line:2800
        ""#line:2803
        OOO0OO0OO000OO0OO :str =""#line:2804
        OO000OO00O00O000O =None #line:2805
        try :#line:2806
            OO000O0OO000000OO =[]#line:2807
            for O0O0O0O000O00000O ,O00OO0OOO0O0OOO0O in OO0000OOO0OOOO00O .items ():#line:2808
                O00OOO0O0OOOOOO00 :TFutQuoteData #line:2809
                O00OOO0O0OOOOOO00 =O00OO0OOO0O0OOO0O #line:2810
                if (O00OOO0O0OOOOOO00 .HL .Market ==OOO00O0O000OOO0OO ):#line:2811
                    OO000O0OO000000OO .append (O0O0O0O000O00000O )#line:2812
            OO000OO00O00O000O =OO000O0OO000000OO #line:2813
            if OO000OO00O00O000O is None or len (OO000OO00O00O000O )==0 :#line:2814
                OOO0OO0OO000OO0OO =f"期][GetItem_ByCategory](aCat={OOO00O0O000OOO0OO})商品已不存存!"#line:2815
                return False ,OO000OO00O00O000O ,OOO0OO0OO000OO0OO #line:2816
            else :#line:2817
                return True ,OO000OO00O00O000O ,""#line:2818
        except Exception as OOO00000OOO0O0OO0 :#line:2819
            OOO0OO0OO000OO0OO =f"[期][GetItem_ByCategory](aCat={OOO00O0O000OOO0OO}){OOO00000OOO0O0OO0}"#line:2820
        return False ,OO000OO00O00O000O ,OOO0OO0OO000OO0OO #line:2821
class TObjBaseFutMap (UserDict ):#line:2824
    ""#line:2826
    def __init__ (OO00O0O0O0O00O00O ,mapping =None ,**OO0OO000O0OO0OO0O ):#line:2829
        if mapping is not None :#line:2830
            mapping ={str (OO00O00OO0O0OOO0O ).upper ():O0O0O0O0O000OOOO0 for OO00O00OO0O0OOO0O ,O0O0O0O0O000OOOO0 in mapping .items ()}#line:2833
        else :#line:2834
            mapping ={}#line:2835
        if OO0OO000O0OO0OO0O :#line:2836
            mapping .update ({str (O0O0OO000O0000O0O ).upper ():O000OOOOOOOO0O0O0 for O0O0OO000O0000O0O ,O000OOOOOOOO0O0O0 in OO0OO000O0OO0OO0O .items ()})#line:2839
        OO00O0O0O0O00O00O .fSortMap ={}#line:2841
        "<ProdID, <交割月, TFutQtBase>>"#line:2842
        super ().__init__ (mapping )#line:2843
    def __setitem__ (OO00O000O00OOOO0O ,OOOOO0OOO00OOO00O ,O00OOOOOO0O0O0OO0 ):#line:2845
        super ().__setitem__ (OOOOO0OOO00OOO00O ,O00OOOOOO0O0O0OO0 )#line:2846
    def AddItem_ByStkNo (OO0O0O0O0OO0O0O0O ,O0000OOOO00O0000O :TFutQtBase ):#line:2848
        try :#line:2849
            if OO0O0O0O0OO0O0O0O .fSortMap .get (O0000OOOO00O0000O .StkNo )is None :#line:2850
                O00OO0O00O000OOO0 ={O0000OOOO00O0000O .SettleMth :O0000OOOO00O0000O }#line:2851
                OO0O0O0O0OO0O0O0O .fSortMap [O0000OOOO00O0000O .StkNo ]=O00OO0O00O000OOO0 #line:2852
            else :#line:2853
                O00000O0OO00000OO =OO0O0O0O0OO0O0O0O .fSortMap [O0000OOOO00O0000O .StkNo ]#line:2854
                O00000O0OO00000OO [O0000OOOO00O0000O .SettleMth ]=O0000OOOO00O0000O #line:2855
                O00O000OO00OOO000 =sorted (O00000O0OO00000OO .items ())#line:2856
                OO000OO0O00OOOO00 =dict (O00O000OO00OOO000 )#line:2857
                OO0O0O0O0OO0O0O0O .fSortMap [O0000OOOO00O0000O .StkNo ]=OO000OO0O00OOOO00 #line:2858
        except Exception as O000OOOO0O0OOO0OO :#line:2859
            pass #line:2860
    def AddItem_ByProdID (OO0000OOO00000000 ,O000O0O0OOO00O0OO :TFutQtBase ):#line:2862
        try :#line:2863
            if OO0000OOO00000000 .fSortMap .get (O000O0O0OOO00O0OO .ProdID )is None :#line:2864
                O000OO000OOO0OO00 ={O000O0O0OOO00O0OO .SettleMth :O000O0O0OOO00O0OO }#line:2865
                OO0000OOO00000000 .fSortMap [O000O0O0OOO00O0OO .ProdID ]=O000OO000OOO0OO00 #line:2866
            else :#line:2867
                O000OOOO00OO0OOOO =OO0000OOO00000000 .fSortMap [O000O0O0OOO00O0OO .ProdID ]#line:2868
                O000OOOO00OO0OOOO [O000O0O0OOO00O0OO .SettleMth ]=O000O0O0OOO00O0OO #line:2869
                OO0O00000OOOO00O0 =sorted (O000OOOO00OO0OOOO .items ())#line:2870
                O00O00000O0O0000O =dict (OO0O00000OOOO00O0 )#line:2871
                OO0000OOO00000000 .fSortMap [O000O0O0OOO00O0OO .ProdID ]=O00O00000O0O0000O #line:2872
        except Exception as O0O0O00OOO0000OO0 :#line:2873
            pass #line:2874
    def ReAddAll (O00000O000O0O0000 ):#line:2876
        if O00000O000O0O0000 .fSortMap .keys ()is None :#line:2877
            return #line:2878
        for O0O0O0OOOO0OOOO00 in O00000O000O0O0000 .fSortMap .keys ():#line:2880
            OO0O000OOOOO0O00O =TObjBaseFutList ()#line:2881
            [OO0O000OOOOO0O00O .append (O00000O000O0O0000 .fSortMap [O0O0O0OOOO0OOOO00 ][O00000OOOO0O0O0O0 ])for O00000OOOO0O0O0O0 in O00000O000O0O0000 .fSortMap [O0O0O0OOOO0OOOO00 ]]#line:2882
            O00000O000O0O0000 [O0O0O0OOOO0OOOO00 ]=OO0O000OOOOO0O00O #line:2883
class TObjBaseFutList (list ):#line:2885
    ""#line:2886
    pass #line:2887
class TObjFutComList (UserDict ):#line:2888
    ""#line:2890
    def __init__ (OOOO0OO0OO00OO000 ,mapping =None ,**O00O00000O0O0OOOO ):#line:2892
        if mapping is not None :#line:2893
            mapping ={str (OOO00OOO00OO0OO00 ).upper ():OOO00O0OOO000O0OO for OOO00OOO00OO0OO00 ,OOO00O0OOO000O0OO in mapping .items ()}#line:2896
        else :#line:2897
            mapping ={}#line:2898
        if O00O00000O0O0OOOO :#line:2899
            mapping .update ({str (OOOO0OO0OO000O000 ).upper ():OOO0000OO00O00OO0 for OOOO0OO0OO000O000 ,OOO0000OO00O00OO0 in O00O00000O0O0OOOO .items ()})#line:2902
        super ().__init__ (mapping )#line:2903
    def __setitem__ (O00O0000O00O00O00 ,OOO00O0OO0OOOO000 ,OOO0OOO00OO0000O0 ):#line:2905
        super ().__setitem__ (OOO00O0OO0OOOO000 ,OOO0OOO00OO0000O0 )#line:2906
    def AddItem (O000O000000O0OOO0 ,OO00O0OOO0OOOOO00 :str ):#line:2908
        try :#line:2909
            O0OO000O0OO00OOO0 =TFutCom ()#line:2910
            O0OO000O0OO00OOO0 .SolIce =OO00O0OOO0OOOOO00 #line:2911
            O0OO000O0OO00OOO0 .Leg1_SolIce =OO00O0OOO0OOOOO00 .split ('^')[0 ]#line:2912
            O0OO000O0OO00OOO0 .Leg2_SolIce =O0OO000O0OO00OOO0 .Leg1_SolIce [:len (O0OO000O0OO00OOO0 .Leg1_SolIce )-2 ]+OO00O0OOO0OOOOO00 .split ('^')[1 ]#line:2914
            O000O000000O0OOO0 [OO00O0OOO0OOOOO00 ]=O0OO000O0OO00OOO0 #line:2915
            O000O000000O0OOO0 .data =dict (sorted (O000O000000O0OOO0 .data .items ()))#line:2916
        except Exception as O0O0000O0O00OO0O0 :#line:2917
            pass #line:2918
class TFutCom :#line:2920
    SolIce :str #line:2921
    "CDFL2^C3"#line:2922
    Leg1_SolIce :str #line:2923
    "CDFL2"#line:2924
    Leg2_SolIce :str #line:2925
    "CDFC3"#line:2926
class TObjBaseOptMap (UserDict ):#line:2931
    ""#line:2933
    def __init__ (O000OOO0OOOO000OO ,mapping =None ,**O0OOOOOOOO0O00OOO ):#line:2935
        if mapping is not None :#line:2936
            mapping ={str (O0OO000O00O0O0O0O ).upper ():OOOO0OO0OOO0OOOO0 for O0OO000O00O0O0O0O ,OOOO0OO0OOO0OOOO0 in mapping .items ()}#line:2939
        else :#line:2940
            mapping ={}#line:2941
        if O0OOOOOOOO0O00OOO :#line:2942
            mapping .update ({str (OOO00OO0OOOOOOOOO ).upper ():O0O00OOO00O000OO0 for OOO00OO0OOOOOOOOO ,O0O00OOO00O000OO0 in O0OOOOOOOO0O00OOO .items ()})#line:2945
        super ().__init__ (mapping )#line:2946
    def __setitem__ (OO000O0O0OOO0000O ,O0000O0O0OOOOO0O0 ,OOO0O0OOOOO0OOOO0 ):#line:2948
        super ().__setitem__ (O0000O0O0OOOOO0O0 ,OOO0O0OOOOO0OOOO0 )#line:2949
    def AddItem_ByProdID (OOO0OO00O00OO00O0 ,OOOOOO0OOO00O000O :TFutQtBase ):#line:2951
        try :#line:2952
            if OOO0OO00O00OO00O0 .data .get (OOOOOO0OOO00O000O .ProdID )is None :#line:2953
                O00OO000O0O0O000O =TObjBaseOptMthList ()#line:2954
                O00OO000O0O0O000O .NewItem (OOOOOO0OOO00O000O )#line:2955
                OOO0OO00O00OO00O0 [OOOOOO0OOO00O000O .ProdID ]=O00OO000O0O0O000O #line:2956
            else :#line:2957
                O00OO000O0O0O000O :TObjBaseOptMthList =OOO0OO00O00OO00O0 [OOOOOO0OOO00O000O .ProdID ]#line:2958
                O00OO000O0O0O000O .NewItem (OOOOOO0OOO00O000O )#line:2959
        except Exception as OO0O00OO0000OO0OO :#line:2960
            pass #line:2961
class TObjBaseOptMthList (UserDict ):#line:2962
    ""#line:2964
    ProdName :str =""#line:2965
    def __init__ (OOOO00O0000OO0O0O ,mapping =None ,**OO00OOOOOO0OO000O ):#line:2967
        if mapping is not None :#line:2968
            mapping ={str (OOOOOO0O00000000O ).upper ():O00OOOOO0OO00O0O0 for OOOOOO0O00000000O ,O00OOOOO0OO00O0O0 in mapping .items ()}#line:2971
        else :#line:2972
            mapping ={}#line:2973
        if OO00OOOOOO0OO000O :#line:2974
            mapping .update ({str (OO0OOO0OO0OOOOOOO ).upper ():O00OOOOOO000O0000 for OO0OOO0OO0OOOOOOO ,O00OOOOOO000O0000 in OO00OOOOOO0OO000O .items ()})#line:2977
        super ().__init__ (mapping )#line:2978
    def __setitem__ (O0OOOOOOO000OO00O ,O0OOO0OO000OOO0OO ,OOOOO0O0O0O0OO00O ):#line:2980
        super ().__setitem__ (O0OOO0OO000OOO0OO ,OOOOO0O0O0O0OO00O )#line:2981
    def NewItem (OOO0O0O0OOOOOOO0O ,O00OOO0O000OO0O00 :TFutQtBase ):#line:2983
        O0000O0O00O000O00 =O00OOO0O000OO0O00 .SettleMth #line:2984
        if OOO0O0O0OOOOOOO0O .data .get (O0000O0O00O000O00 )is None :#line:2986
            OO00OO00000OOOO00 =O00OOO0O000OO0O00 .FutName #line:2987
            OO0OO0OO00OO00OO0 =TObjBaseOptCallPutList ()#line:2988
            OO0OO0OO00OO00OO0 .NewItem (O00OOO0O000OO0O00 )#line:2989
            OOO0O0O0OOOOOOO0O [O0000O0O00O000O00 ]=OO0OO0OO00OO00OO0 #line:2990
        else :#line:2991
            OO0OO0OO00OO00OO0 :TObjBaseOptCallPutList =OOO0O0O0OOOOOOO0O [O0000O0O00O000O00 ]#line:2992
            OO0OO0OO00OO00OO0 .NewItem (O00OOO0O000OO0O00 )#line:2993
        O0O0O0O000000O0O0 =OOO0O0O0OOOOOOO0O .data #line:2995
        OOO0O00OOOO0O0000 =sorted (O0O0O0O000000O0O0 .items ())#line:2996
        OOOOO00000OOOO000 =dict (OOO0O00OOOO0O0000 )#line:2997
        OOO0O0O0OOOOOOO0O .data =OOOOO00000OOOO000 #line:2998
class TObjBaseOptCallPutList (UserDict ):#line:2999
    ""#line:3001
    def __init__ (O0OO0O0OO0O0O0O0O ,mapping =None ,**OOO0O00O0O00O0O0O ):#line:3003
        if mapping is not None :#line:3004
            mapping ={str (O00OOOOO0000OO0O0 ).upper ():O00O00OO0O000OOO0 for O00OOOOO0000OO0O0 ,O00O00OO0O000OOO0 in mapping .items ()}#line:3007
        else :#line:3008
            mapping ={}#line:3009
        if OOO0O00O0O00O0O0O :#line:3010
            mapping .update ({str (O0O000000OOOO0OOO ).upper ():O0O0O00OO0O000OO0 for O0O000000OOOO0OOO ,O0O0O00OO0O000OO0 in OOO0O00O0O00O0O0O .items ()})#line:3013
        super ().__init__ (mapping )#line:3014
    def __setitem__ (O000O00O0O0O00OOO ,O0OOO00O0O0OO000O ,OOOOO0000OOOO0O00 ):#line:3016
        super ().__setitem__ (O0OOO00O0O0OO000O ,OOOOO0000OOOO0O00 )#line:3017
    def NewItem (OOOOO00OO0OOO0O0O ,O000OO0000O0OOOOO :TFutQtBase ):#line:3019
        OO00OO00O00O00OOO =O000OO0000O0OOOOO .CallPutType #line:3020
        if OOOOO00OO0OOO0O0O .data .get (OO00OO00O00O00OOO )is None :#line:3022
            OO0OOO0OOOO00OO0O =TObjBaseOptList ()#line:3023
            OO0OOO0OOOO00OO0O .append (O000OO0000O0OOOOO )#line:3024
            OOOOO00OO0OOO0O0O [OO00OO00O00O00OOO ]=OO0OOO0OOOO00OO0O #line:3025
        else :#line:3026
            OO0OO000O00O0O0OO :TObjBaseOptList =OOOOO00OO0OOO0O0O [OO00OO00O00O00OOO ]#line:3027
            OO0OO000O00O0O0OO .append (O000OO0000O0OOOOO )#line:3028
        O0OOOO0OOO00O0000 =OOOOO00OO0OOO0O0O .data #line:3030
        OO0O0OO00OO0OO0OO =sorted (O0OOOO0OOO00O0000 .items ())#line:3031
        O00OO0OO0OO0OOOO0 =dict (OO0O0OO00OO0OO0OO )#line:3032
        OOOOO00OO0OOO0O0O .data =O00OO0OO0OO0OOOO0 #line:3033
class TObjBaseOptList (list ):#line:3034
    ""#line:3035
    pass #line:3036
class TQryFutProdMap (UserDict ):#line:3040
    ""#line:3042
    def __init__ (O00O0O0OO0000O00O ,mapping =None ,**O00O00O0OO00O0O00 ):#line:3044
        if mapping is not None :#line:3045
            mapping ={str (OOOO0O0OOO0OOOOO0 ).upper ():OO000O00O0O0OO0O0 for OOOO0O0OOO0OOOOO0 ,OO000O00O0O0OO0O0 in mapping .items ()}#line:3048
        else :#line:3049
            mapping ={}#line:3050
        if O00O00O0OO00O0O00 :#line:3051
            mapping .update ({str (O0OOOOOOOO00000O0 ).upper ():OO0O0O00OOOO000O0 for O0OOOOOOOO00000O0 ,OO0O0O00OOOO000O0 in O00O00O0OO00O0O00 .items ()})#line:3054
        super ().__init__ (mapping )#line:3055
    def __setitem__ (O0OO00OOO00000000 ,OOO000OOO0OO0O00O ,O0000OOOOO0OOO0OO ):#line:3057
        super ().__setitem__ (OOO000OOO0OO0O00O ,O0000OOOOO0OOO0OO )#line:3058
class TQryFutProdRec :#line:3060
    tmpBase :TFutQtBase =None #line:3062
    tmpHL :TFutQtHL =None #line:3063
    def SetDataInit (OOO0OOOOOOOO00000 ):#line:3065
        OOO0OOOOOOOO00000 .tmpHL .DECIMAL_LOCATOR_Dgt =OOO0OOOOOOOO00000 .tmpBase .DECIMAL_LOCATOR_Dgt #line:3066
        OOO0OOOOOOOO00000 .tmpHL .DECIMAL_LOCATOR_Org =OOO0OOOOOOOO00000 .tmpBase .DECIMAL_LOCATOR_Org #line:3067
class TOvsFutQtDef :#line:3072
    DecimalMultiply :decimal =1 #line:3073
    "DecimalMultiply(一個契約含多少Shares)"#line:3074
    Price_Denominator :decimal =1 #line:3075
    "分母價格(為1者, 不是分子分母報價方式)"#line:3076
    def TransPrice2Dec (OO0O00OOO00O00OOO ,O00O000O0000OO00O :str ):#line:3079
        try :#line:3080
            return Decimal (O00O000O0000OO00O )#line:3081
        except Exception as O000OOOOO00OO00O0 :#line:3082
            return 0 #line:3083
    def TransPrice2Str (O0O0O0O0O0000000O ,O0O0OO00O00OOOOOO :decimal ,aDg_tPrice :str =""):#line:3086
        if O0O0O0O0O0000000O .Price_Denominator ==1 :#line:3087
            if O0O0O0O0O0000000O .DecimalMultiply ==1 :#line:3088
                if aDg_tPrice is None or not aDg_tPrice or aDg_tPrice .isspace ():#line:3089
                    return str (O0O0OO00O00OOOOOO )#line:3090
                else :#line:3091
                    return aDg_tPrice .format (O0O0OO00O00OOOOOO )#line:3092
            if aDg_tPrice is None or not aDg_tPrice or aDg_tPrice .isspace ():#line:3093
                return "{:.8f}".format (O0O0OO00O00OOOOOO *O0O0O0O0O0000000O .DecimalMultiply )#line:3094
            else :#line:3095
                return aDg_tPrice .format (O0O0OO00O00OOOOOO *O0O0O0O0O0000000O .DecimalMultiply )#line:3096
        else :#line:3098
            OO00OOOO00000O00O :decimal =math .trunc (O0O0OO00O00OOOOOO )#line:3100
            O0O0000O0OOOO0OO0 :decimal =O0O0OO00O00OOOOOO -OO00OOOO00000O00O #line:3101
            if aDg_tPrice is None or not aDg_tPrice or aDg_tPrice .isspace ():#line:3102
                return "{0} {1:.8f}/{2}".format (OO00OOOO00000O00O ,(O0O0000O0OOOO0OO0 *O0O0O0O0O0000000O .Price_Denominator ),O0O0O0O0O0000000O .Price_Denominator )#line:3103
            else :#line:3104
                return "{0} {1:.8f}/{2}".format (OO00OOOO00000O00O ,aDg_tPrice .format (O0O0000O0OOOO0OO0 *O0O0O0O0O0000000O .Price_Denominator ),O0O0O0O0O0000000O .Price_Denominator )#line:3105
    def TransToInt (O00000O000O00O0O0 ,OOOOOOO000OOOOOO0 :str ):#line:3107
        try :#line:3108
            return int (OOOOOOO000OOOOOO0 )#line:3109
        except Exception as OOOOO00OOO0000OO0 :#line:3110
            return 0 #line:3111
    def TransToDecimal (O00000O00O0O0O0O0 ,O0OOO00OOO00000O0 :str ):#line:3113
        try :#line:3114
            return Decimal (O0OOO00OOO00000O0 )#line:3115
        except Exception as O00OO00OOOO0000O0 :#line:3116
            return 0 #line:3117
    def __init__ (OOOO0OOO000OO000O )->None :#line:3120
        pass #line:3121
class TOvsFutQtBase (TOvsFutQtDef ):#line:3123
    fHasBAS :bool =False #line:3124
    fBAS =[]#line:3125
    SolICE :str #line:3127
    "元富行情代碼(NQ.202212)"#line:3128
    SysTime :str #line:3129
    "系統時間"#line:3130
    RefPriceOrg :str #line:3131
    "參考價"#line:3132
    def Get_RefPrice (OO00OOO00O0OO0000 ):#line:3134
        return OO00OOO00O0OO0000 .TransPrice2Dec (OO00OOO00O0OO0000 .RefPriceOrg )#line:3135
    def GetDply_RefPrice (OO0000OO00OO00O00 ,aDg_tPrice :str =""):#line:3137
        if (OO0000OO00OO00O00 .fBAS ==None ):#line:3138
            return ""#line:3139
        OO0OO00O00OOO0OOO :decimal =0 #line:3140
        OO0OO00O00OOO0OOO =OO0000OO00OO00O00 .TransPrice2Dec (OO0000OO00OO00O00 .RefPriceOrg )#line:3141
        return OO0000OO00OO00O00 .TransPrice2Str (OO0OO00O00OOO0OOO ,aDg_tPrice )#line:3142
    ProdID :str #line:3143
    "元富商品代碼 (EX:NQ)"#line:3144
    FutName :str #line:3145
    "商品中文名稱(EX:小型環球晶)"#line:3146
    OrdProdId :str #line:3147
    "元富商品委託代碼(EX:NQ)"#line:3148
    ICEProdId :str #line:3149
    "元富行情代碼(EX:NQ, 艾揚的為ICE開頭)"#line:3150
    MktStr :str #line:3151
    "元富市場別(FUT/OPT)"#line:3152
    Market :str #line:3153
    "元富市場別(4=FUT/5=OPT)"#line:3154
    BaseUnit :str #line:3155
    "基本跳動點(選擇權商品為TickSizeList, 如:0=0.05;5=0.25)"#line:3156
    def Get_BaseUnit (O000O00OOOOOO000O ):#line:3158
        OOO0OO0OO0O0OO0OO :decimal =1 #line:3159
        OOO0OO0OO0O0OO0OO =O000O00OOOOOO000O .TransToDecimal (O000O00OOOOOO000O .BaseUnit )#line:3160
        if OOO0OO0OO0O0OO0OO ==0 :#line:3161
            OOO0OO0OO0O0OO0OO =1 #line:3162
        return OOO0OO0OO0O0OO0OO #line:3163
    ValuePerUnitOrg :str #line:3165
    "每點價值"#line:3166
    def Get_ValuePerUnit (OOOOOOO0OOOO0O0O0 ):#line:3168
        return OOOOOOO0OOOO0O0O0 .TransToDecimal (OOOOOOO0OOOO0O0O0 .ValuePerUnitOrg )#line:3169
    DecimalMultiplyOrg :str #line:3170
    "DecimalMultiply(一個契約含多少Shares)"#line:3171
    def Get_DecimalMultiply (O0000O0O0O00OO000 ):#line:3173
        return O0000O0O0O00OO000 .TransToDecimal (O0000O0O0O00OO000 .DecimalMultiplyOrg )#line:3174
    Exchange :str #line:3175
    "元富交易所代碼"#line:3176
    ExchangeName :str #line:3177
    "元富商品代碼 (EX:NQ)"#line:3178
    Price_DenominatorOrg :str #line:3179
    "分母價格(為1者, 不是分子分母報價方式)"#line:3180
    def Get_Price_Denominator (OOO0O0OO00O00O0O0 ):#line:3182
        return OOO0O0OO00O00O0O0 .TransToDecimal (OOO0O0OO00O00O0O0 .Price_DenominatorOrg )#line:3183
    Display :str #line:3184
    "是否可交易(Y/N)"#line:3185
    SettleMth :str #line:3186
    "交割月"#line:3187
    CP :str #line:3188
    "C/P(非選擇權者為空字串)"#line:3189
    StrikeP :str #line:3190
    "履約價(非選擇權者為空字串)"#line:3191
    PreSettlePriceOrg :str #line:3192
    "昨日結算價"#line:3193
    def Get_PreSettlePrice (O000000O000OOOO00 ):#line:3195
        if O000000O000OOOO00 .fBAS is None :#line:3196
            return 0 #line:3197
        OOO0OO0OO0O0O0OOO :decimal =0 #line:3198
        OOO0OO0OO0O0O0OOO =O000000O000OOOO00 .TransPrice2Dec (O000000O000OOOO00 .PreSettlePriceOrg )#line:3199
        return OOO0OO0OO0O0O0OOO #line:3200
    def GetDply_PreSettlePrice (O00O0O00O0OOOOO00 ,aDg_tPrice :str =""):#line:3202
        if O00O0O00O0OOOOO00 .fBAS ==None :#line:3203
            return ""#line:3204
        OO0OO00OOOO00000O :decimal =0 #line:3205
        OO0OO00OOOO00000O =O00O0O00O0OOOOO00 .TransPrice2Dec (O00O0O00O0OOOOO00 .PreSettlePriceOrg )#line:3206
        return O00O0O00O0OOOOO00 .TransPrice2Str (OO0OO00OOOO00000O ,aDg_tPrice )#line:3207
    PreClosePriceOrg :str #line:3208
    def Get_PreClosePrice (OO0O0O000O0O0O00O ):#line:3210
        if OO0O0O000O0O0O00O .fBAS ==None :#line:3211
            return 0 #line:3212
        O0O0O0OOOOOOOO00O :decimal =0 #line:3213
        O0O0O0OOOOOOOO00O =OO0O0O000O0O0O00O .TransPrice2Dec (OO0O0O000O0O0O00O .PreClosePriceOrg )#line:3214
        return O0O0O0OOOOOOOO00O #line:3215
    def GetDply_PreClosePrice (O00O000O0OO00OOO0 ,aDg_tPrice :str =""):#line:3217
        if O00O000O0OO00OOO0 .fBAS ==None :#line:3218
            return ""#line:3219
        O0OOO00000O00O000 :decimal =0 #line:3220
        O0OOO00000O00O000 =O00O000O0OO00OOO0 .TransPrice2Str (O00O000O0OO00OOO0 .PreClosePriceOrg )#line:3221
        return O00O000O0OO00OOO0 .TransPrice2Str (O0OOO00000O00O000 ,aDg_tPrice )#line:3222
    LastTxDate :str #line:3224
    "最後交易日"#line:3225
    TickSizeList :str #line:3226
    "TickSizeList(僅選擇權有值, 如:0=0.05;5=0.25)"#line:3227
    def Get_OptTickSizeList (OOOOO0OO0O0O00OO0 ):#line:3229
        ""#line:3231
        O0O0000OO0OO0O000 ={}#line:3233
        try :#line:3234
            if OOOOO0OO0O0O00OO0 .MktStr =="FUT":#line:3235
                return O0O0000OO0OO0O000 #line:3236
            if OOOOO0OO0O0O00OO0 .TickSizeList is None or not OOOOO0OO0O0O00OO0 .TickSizeList or OOOOO0OO0O0O00OO0 .TickSizeList .isspace :#line:3237
                return O0O0000OO0OO0O000 #line:3238
            O000O0OO000O0O000 =OOOOO0OO0O0O00OO0 .TickSizeList .split (';')#line:3241
            for OOOOO00OO0OOOO00O in O000O0OO000O0O000 :#line:3242
                O0O0000OO0OO0O000 [Decimal (OOOOO00OO0OOOO00O .split ('=')[0 ])]=Decimal (OOOOO00OO0OOOO00O .split ('=')[1 ])#line:3244
            O0O0000OO0OO0O000 =dict (sorted (O0O0000OO0OO0O000 .items ()))#line:3245
        except Exception as O0O0OO0O0OOO0O0O0 :#line:3246
            pass #line:3247
        return O0O0000OO0OO0O000 #line:3248
    def WholeName (OOO000O000000OOOO )->str :#line:3250
        ""#line:3251
        return f"{OOO000O000000OOOO.FutName}.{OOO000O000000OOOO.SettleMth}{OOO000O000000OOOO.CP}{OOO000O000000OOOO.StrikeP}"#line:3252
    def GetFavorStr (OO000000OOOOO000O )->str :#line:3254
        ""#line:3255
        return "|{0}|{1}|{2}|{3}|".format (OO000000OOOOO000O .Exchange ,OO000000OOOOO000O .ProdID ,OO000000OOOOO000O .SettleMth ,OO000000OOOOO000O .SolICE )#line:3256
    def Handle_BAS (O0OOO0OO00OOO0OOO ,O00O0000OO0OO0OO0 :str ):#line:3258
        O0OOO0OO00OOO0OOO .fBAS =O00O0000OO0OO0OO0 .split ('|')#line:3259
        O0OOO0OO00OOO0OOO .fHasBAS =len (O0OOO0OO00OOO0OOO .fBAS )>0 #line:3260
        O0OOO0OO00OOO0OOO .Set_Data ()#line:3261
        if O0OOO0OO00OOO0OOO .fHasBAS :#line:3262
            O0OOO0OO00OOO0OOO .DecimalMultiply =O0OOO0OO00OOO0OOO .Get_DecimalMultiply ()#line:3263
            O0OOO0OO00OOO0OOO .Price_Denominator =O0OOO0OO00OOO0OOO .Get_Price_Denominator ()#line:3264
    def Set_Data (O0OO0OO0O0OO0OO0O ):#line:3266
        O0OO0OO0O0OO0OO0O .SolICE =O0OO0OO0O0OO0OO0O .fBAS [0 ]#line:3267
        O0OO0OO0O0OO0OO0O .SysTime =O0OO0OO0O0OO0OO0O .fBAS [1 ]#line:3268
        O0OO0OO0O0OO0OO0O .RefPriceOrg =O0OO0OO0O0OO0OO0O .fBAS [2 ]#line:3269
        O0OO0OO0O0OO0OO0O .ProdID =O0OO0OO0O0OO0OO0O .fBAS [3 ]#line:3270
        O0OO0OO0O0OO0OO0O .FutName =O0OO0OO0O0OO0OO0O .fBAS [4 ]#line:3271
        O0OO0OO0O0OO0OO0O .OrdProdId =O0OO0OO0O0OO0OO0O .fBAS [5 ]#line:3272
        O0OO0OO0O0OO0OO0O .ICEProdId =O0OO0OO0O0OO0OO0O .fBAS [6 ]#line:3273
        O0OO0OO0O0OO0OO0O .MktStr =O0OO0OO0O0OO0OO0O .fBAS [7 ]#line:3274
        O0OO0OO0O0OO0OO0O .Market ="4"if O0OO0OO0O0OO0OO0O .fBAS [7 ]=="FUT"else "5"#line:3275
        O0OO0OO0O0OO0OO0O .BaseUnit =O0OO0OO0O0OO0OO0O .fBAS [8 ]#line:3276
        O0OO0OO0O0OO0OO0O .ValuePerUnitOrg =O0OO0OO0O0OO0OO0O .fBAS [9 ]#line:3277
        O0OO0OO0O0OO0OO0O .DecimalMultiplyOrg =O0OO0OO0O0OO0OO0O .fBAS [10 ]#line:3278
        O0OO0OO0O0OO0OO0O .Exchange =O0OO0OO0O0OO0OO0O .fBAS [11 ]#line:3279
        O0OO0OO0O0OO0OO0O .ExchangeName =O0OO0OO0O0OO0OO0O .fBAS [12 ]#line:3280
        O0OO0OO0O0OO0OO0O .Price_DenominatorOrg =O0OO0OO0O0OO0OO0O .fBAS [13 ]#line:3281
        O0OO0OO0O0OO0OO0O .Display =O0OO0OO0O0OO0OO0O .fBAS [14 ]#line:3282
        O0OO0OO0O0OO0OO0O .SettleMth =O0OO0OO0O0OO0OO0O .fBAS [15 ]#line:3283
        O0OO0OO0O0OO0OO0O .CP =O0OO0OO0O0OO0OO0O .fBAS [16 ]#line:3284
        O0OO0OO0O0OO0OO0O .StrikeP =O0OO0OO0O0OO0OO0O .fBAS [17 ]#line:3285
        O0OO0OO0O0OO0OO0O .PreSettlePriceOrg =O0OO0OO0O0OO0OO0O .fBAS [18 ]#line:3286
        O0OO0OO0O0OO0OO0O .PreClosePriceOrg =O0OO0OO0O0OO0OO0O .fBAS [19 ]#line:3287
        O0OO0OO0O0OO0OO0O .LastTxDate =O0OO0OO0O0OO0OO0O .fBAS [20 ]#line:3288
        O0OO0OO0O0OO0OO0O .TickSizeList =O0OO0OO0O0OO0OO0O .fBAS [21 ]#line:3289
    def IsSameBAS (OO0OOO0OO0OO000OO ,OO00O00OOO00OO0OO :str ,OOO0OOOOO0O0OO0OO :str ):#line:3291
        return OO00O00OOO00OO0OO ==OO0OOO0OO0OO000OO .ProdID and OO0OOO0OO0OO000OO .SettleMth ==OOO0OOOOO0O0OO0OO #line:3292
class TOvsFutQtTX (TOvsFutQtDef ):#line:3293
    fTX =[]#line:3294
    SolICE :str #line:3297
    "元富行情代碼(NQ.202212)"#line:3298
    SysTime :str #line:3299
    "系統時間(EX:143211.693)"#line:3300
    DataTime :str #line:3301
    "資料時間(交易所給的)(EX:14:32:11.752025)"#line:3302
    QtSrc :str #line:3303
    "行情來源(EX:PATS.NQ/CQG.NQ)"#line:3304
    DealTime :str #line:3305
    "成交時間(EX:14:32:11.752025)"#line:3306
    DealShowMark :str #line:3307
    "成交資料揭示項目註記(0:請略過,1:成交行情,空字串:收盤/結算)"#line:3308
    TotQty :str #line:3309
    "成交總量"#line:3310
    def Get_TotQty2Dec (OO000OO00O0000O0O ):#line:3312
        return OO000OO00O0000O0O .TransToDecimal (OO000OO00O0000O0O .TotQty )#line:3313
    def Get_TotQty2Int (OOO00OO0O0000O00O ):#line:3315
        return OOO00OO0O0000O00O .TransToInt (OOO00OO0O0000O00O .TotQty )#line:3316
    SumBuyDealCount :str #line:3317
    "累計買進成交筆數"#line:3318
    def Get_SumBuyDealCount (O0OOOOOO00OO00OOO ):#line:3320
        return O0OOOOOO00OO00OOO .TransToInt (O0OOOOOO00OO00OOO .SumBuyDealCount )#line:3321
    SumSellDealCount :str #line:3322
    "累計賣出成交筆數"#line:3323
    def Get_SumSellDealCount (O0000000O0OOOOO00 ):#line:3325
        return O0000000O0OOOOO00 .TransToInt (O0000000O0OOOOO00 .SumSellDealCount )#line:3326
    DealCount :str #line:3327
    "成交價量檔數(目前海期都給1)"#line:3328
    def Get_DealCount (O0O0O00000OOO0O00 ):#line:3330
        return O0O0O00000OOO0O00 .TransToInt (O0O0O00000OOO0O00 .DealCount )#line:3331
    DealPriceOrg :str #line:3332
    "成交價"#line:3333
    def Get_DealPrice (O00OO000OOOOOO0OO ):#line:3335
        if O00OO000OOOOOO0OO .fTX is None :#line:3336
            return 0 #line:3337
        OOOOOO00000OOOOO0 :decimal =0 #line:3338
        OOOOOO00000OOOOO0 =O00OO000OOOOOO0OO .TransPrice2Dec (O00OO000OOOOOO0OO .DealPriceOrg )#line:3339
        return OOOOOO00000OOOOO0 #line:3340
    def GetDply_DealPrice (O0O00OOOO00OO0O00 ,aDg_tPrice :str =""):#line:3342
        if O0O00OOOO00OO0O00 .fTX ==None :#line:3343
            return ""#line:3344
        OOO00O0000O00O00O :decimal =0 #line:3345
        OOO00O0000O00O00O =O0O00OOOO00OO0O00 .TransPrice2Dec (O0O00OOOO00OO0O00 .DealPriceOrg )#line:3346
        return O0O00OOOO00OO0O00 .TransPrice2Str (OOO00O0000O00O00O ,aDg_tPrice )#line:3347
    DealQty :str #line:3348
    "成交單量"#line:3349
    def Get_DealQty2Dec (O0OO0O0O0OO0O0OOO ):#line:3351
        return O0OO0O0O0OO0O0OOO .TransPrice2Dec (O0OO0O0O0OO0O0OOO .DealQty )#line:3352
    def GetDealQty2Int (O0O0O0OO00O0O0O0O ):#line:3354
        return O0O0O0OO00O0O0O0O .TransToInt (O0O0O0OO00O0O0O0O .DealQty )#line:3355
    DayHighOrg :str #line:3356
    "最高價"#line:3357
    def Get_DayHigh (OOOO00OOOO00O00O0 ):#line:3359
        if OOOO00OOOO00O00O0 .fTX is None :#line:3360
            return 0 #line:3361
        O0O0OO0O0OOOO0O0O :decimal =0 #line:3362
        O0O0OO0O0OOOO0O0O =OOOO00OOOO00O00O0 .TransPrice2Dec (OOOO00OOOO00O00O0 .DayHighOrg )#line:3363
        return O0O0OO0O0OOOO0O0O #line:3364
    def GetDply_DayHigh (OOOOOOO0000000O0O ,aDg_tPrice :str =""):#line:3366
        if OOOOOOO0000000O0O .fTX ==None :#line:3367
            return ""#line:3368
        O00O000OOOO0OO00O :decimal =0 #line:3369
        O00O000OOOO0OO00O =OOOOOOO0000000O0O .TransPrice2Dec (OOOOOOO0000000O0O .DayHighOrg )#line:3370
        return OOOOOOO0000000O0O .TransPrice2Str (O00O000OOOO0OO00O ,aDg_tPrice )#line:3371
    DayLowOrg :str #line:3372
    "最低價"#line:3373
    def Get_DayLow (OOO00O00O00O00OO0 ):#line:3375
        if OOO00O00O00O00OO0 .fTX ==None :#line:3376
            return 0 #line:3377
        O0O0O00OO00O0O0O0 :decimal =0 #line:3378
        O0O0O00OO00O0O0O0 =OOO00O00O00O00OO0 .TransPrice2Dec (OOO00O00O00O00OO0 .DayLowOrg )#line:3379
        return O0O0O00OO00O0O0O0 #line:3380
    def GetDply_DayLow (O0OO00OOO0000OO0O ,aDg_tPrice :str =""):#line:3382
        if O0OO00OOO0000OO0O .fTX ==None :#line:3383
            return ""#line:3384
        O0O0000O0O0O000O0 :decimal =0 #line:3385
        O0O0000O0O0O000O0 =O0OO00OOO0000OO0O .TransPrice2Dec (O0OO00OOO0000OO0O .DayLowOrg )#line:3386
        return O0OO00OOO0000OO0O .TransPrice2Str (O0O0000O0O0O000O0 ,aDg_tPrice )#line:3387
    OpenPriceOrg :str #line:3388
    "開盤價"#line:3389
    def Get_OpenPrice (OOOOO000OOO00O000 ):#line:3391
        if OOOOO000OOO00O000 .fTX ==None :#line:3392
            return 0 #line:3393
        OO00OOOO000O00O0O :decimal =0 #line:3394
        OO00OOOO000O00O0O =OOOOO000OOO00O000 .TransPrice2Dec (OOOOO000OOO00O000 .OpenPriceOrg )#line:3395
        return OO00OOOO000O00O0O #line:3396
    def GetDply_OpenPrice (OO0OOOO0OOOO00O00 ,aDg_tPrice :str =""):#line:3398
        if OO0OOOO0OOOO00O00 .fTX ==None :#line:3399
            return ""#line:3400
        O0O00O00O0OOO000O :decimal =0 #line:3401
        O0O00O00O0OOO000O =OO0OOOO0OOOO00O00 .TransPrice2Dec (OO0OOOO0OOOO00O00 .OpenPriceOrg )#line:3402
        return OO0OOOO0OOOO00O00 .TransPrice2Dec (O0O00O00O0OOO000O ,aDg_tPrice )#line:3403
    ClosePriceOrg :str #line:3404
    "收盤價"#line:3405
    def Get_ClosePrice (OO00O000O0O00OOOO ):#line:3407
        if OO00O000O0O00OOOO .fTX ==None :#line:3408
            return 0 #line:3409
        OOOOO0O0O0000OOOO :decimal =0 #line:3410
        OOOOO0O0O0000OOOO =OO00O000O0O00OOOO .TransPrice2Dec (OO00O000O0O00OOOO .ClosePriceOrg )#line:3411
        return OOOOO0O0O0000OOOO #line:3412
    def GetDply_ClosePrice (OOO0OOO000OO00O00 ,aDg_tPrice :str =""):#line:3414
        if OOO0OOO000OO00O00 .fTX ==None :#line:3416
            return ""#line:3417
        O000OO00OOO00OO0O :decimal =0 #line:3418
        O000OO00OOO00OO0O =OOO0OOO000OO00O00 .TransPrice2Dec (OOO0OOO000OO00O00 .ClosePriceOrg )#line:3419
        return OOO0OOO000OO00O00 .TransPrice2Str (O000OO00OOO00OO0O ,aDg_tPrice )#line:3420
    SettlePriceOrg :str #line:3422
    "結算價"#line:3423
    def Get_SettlePrice (OOO0OO0O000OO0OO0 ):#line:3425
        if OOO0OO0O000OO0OO0 .fTX ==None :#line:3426
            return 0 #line:3427
        O00000OO00OOOOO0O :decimal =0 #line:3428
        O00000OO00OOOOO0O =OOO0OO0O000OO0OO0 .TransPrice2Dec (OOO0OO0O000OO0OO0 .SettlePriceOrg )#line:3429
        return O00000OO00OOOOO0O #line:3430
    def GetDply_SettlePrice (O00O0000000000O0O ,aDg_tPrice :str =""):#line:3432
        if O00O0000000000O0O .fTX ==None :#line:3433
            return ""#line:3434
        OOO0OOO000O00OOOO :decimal =0 #line:3435
        OOO0OOO000O00OOOO =O00O0000000000O0O .TransPrice2Dec (O00O0000000000O0O .SettlePriceOrg )#line:3436
        return O00O0000000000O0O .TransPrice2Str (OOO0OOO000O00OOOO ,aDg_tPrice )#line:3437
    fDealPrice :decimal =0 #line:3440
    "成交價"#line:3441
    HighPrice :decimal =0 #line:3442
    "當日最高價"#line:3443
    LowPrice :decimal =0 #line:3444
    "當日最低價"#line:3445
    def CalcHightLowPrice (O00O0O0OO00O0OO0O ):#line:3447
        ""#line:3448
        try :#line:3449
            O00O0O0OO00O0OO0O .fDealPrice =O00O0O0OO00O0OO0O .Get_DealPrice ()#line:3450
            O00O0O0OO00O0OO0O .HighPrice =math .Max (O00O0O0OO00O0OO0O .fDealPrice ,O00O0O0OO00O0OO0O .HighPrice )#line:3452
            if O00O0O0OO00O0OO0O .LowPrice ==0 :#line:3453
                O00O0O0OO00O0OO0O .LowPrice =O00O0O0OO00O0OO0O .fDealPrice #line:3454
            else :#line:3455
                O00O0O0OO00O0OO0O .LowPrice =min (O00O0O0OO00O0OO0O .fDealPrice ,O00O0O0OO00O0OO0O .LowPrice )#line:3456
        except Exception as OOOO00O0OOO00O0OO :#line:3457
            pass #line:3458
    def CalcHightLowPrice_None (O00O000O0O0O0OO00 ):#line:3460
        pass #line:3461
    fPROC_CalcHightLowPrice :callable =None #line:3462
    "PROC_CalcHightLowPrice"#line:3463
    def Set_Data (O0OOOOO000000O0O0 ):#line:3466
        O0OOOOO000000O0O0 .SolICE =O0OOOOO000000O0O0 .fTX [0 ]#line:3467
        O0OOOOO000000O0O0 .SysTime =O0OOOOO000000O0O0 .fTX [1 ]#line:3468
        O0OOOOO000000O0O0 .DataTime =O0OOOOO000000O0O0 .fTX [2 ]#line:3469
        O0OOOOO000000O0O0 .QtSrc =O0OOOOO000000O0O0 .fTX [3 ]#line:3470
        O0OOOOO000000O0O0 .DealTime =O0OOOOO000000O0O0 .fTX [4 ]#line:3471
        O0OOOOO000000O0O0 .DealShowMark =O0OOOOO000000O0O0 .fTX [5 ]#line:3472
        O0OOOOO000000O0O0 .TotQty =O0OOOOO000000O0O0 .fTX [6 ]#line:3473
        O0OOOOO000000O0O0 .SumBuyDealCount =O0OOOOO000000O0O0 .fTX [7 ]#line:3474
        O0OOOOO000000O0O0 .SumSellDealCount =O0OOOOO000000O0O0 .fTX [8 ]#line:3475
        O0OOOOO000000O0O0 .DealCount =O0OOOOO000000O0O0 .fTX [9 ]#line:3476
        O0OOOOO000000O0O0 .DealPriceOrg =O0OOOOO000000O0O0 .fTX [10 ]#line:3477
        O0OOOOO000000O0O0 .DealQty =O0OOOOO000000O0O0 .fTX [11 ]#line:3478
        O0OOOOO000000O0O0 .DayHighOrg =O0OOOOO000000O0O0 .fTX [12 ]#line:3479
        O0OOOOO000000O0O0 .DayLowOrg =O0OOOOO000000O0O0 .fTX [13 ]#line:3480
        O0OOOOO000000O0O0 .OpenPriceOrg =O0OOOOO000000O0O0 .fTX [14 ]#line:3481
        O0OOOOO000000O0O0 .ClosePriceOrg =O0OOOOO000000O0O0 .fTX [15 ]#line:3482
        O0OOOOO000000O0O0 .SettlePriceOrg =O0OOOOO000000O0O0 .fTX [16 ]#line:3483
    def Handle_TX (OOO0O0OOO0000000O ,O0OOO00OOO000000O :str ):#line:3485
        ""#line:3486
        OOO0O0OOO0000000O .fTX =O0OOO00OOO000000O .split ('|')#line:3487
        OOO0O0OOO0000000O .Set_Data ()#line:3488
        OOO0O0OOO0000000O .fPROC_CalcHightLowPrice ()#line:3490
    def __init__ (OOO00OO00O0O0O00O ,O00O000O000O0O000 :bool )->None :#line:3492
        OOO00OO00O0O0O00O .fPROC_CalcHightLowPrice =OOO00OO00O0O0O00O .CalcHightLowPrice_None #line:3494
        if O00O000O000O0O000 :#line:3495
            OOO00OO00O0O0O00O .fPROC_CalcHightLowPrice =OOO00OO00O0O0O00O .CalcHightLowPrice #line:3496
        super ().__init__ ()#line:3497
    def __str__ (OO00OO00O0O00OOO0 )->str :#line:3499
        return f"""SolICE:{OO00OO00O0O00OOO0.SolICE} SysTime:{OO00OO00O0O00OOO0.SysTime} DataTime:{OO00OO00O0O00OOO0.DataTime} QtSrc:{OO00OO00O0O00OOO0.QtSrc} DealTime:{OO00OO00O0O00OOO0.DealTime}"""+"""DealShowMark:{self.DealShowMark} TotQty:{self.TotQty} SumBuyDealCount:{self.SumBuyDealCount} SumSellDealCount:{self.SumSellDealCount}"""+"""DealCount:{self.DealCount} DealPriceOrg:{self.DealPriceOrg} DealQty:{self.DealQty} DayHighOrg:{self.DayHighOrg}"""+"""DayLowOrg:{self.DayLowOrg} OpenPriceOrg:{self.OpenPriceOrg} ClosePriceOrg:{self.ClosePriceOrg} SettlePriceOrg:{self.SettlePriceOrg}"""+"""fDealPrice:{self.fDealPrice} HighPrice:{self.HighPrice} LowPrice:{self.LowPrice}"""#line:3504
class TOvsFutQt5Q (TOvsFutQtDef ):#line:3505
    f5Q =[]#line:3506
    SolICE :str #line:3508
    "元富行情代碼(NQ.202212)"#line:3509
    DataTime :str #line:3510
    "資料時間(交易所給的)(EX:14:32:19.676684)"#line:3511
    QtSrc :str #line:3512
    "行情來源(EX:PATS.NQ/CQG.NQ)"#line:3513
    fAryB5Q_P =[4 ,6 ,8 ,10 ,12 ,24 ,26 ,28 ,30 ,32 ]#line:3515
    "買五檔價在字串中的位置"#line:3516
    fAryB5Q_Q =[5 ,7 ,9 ,11 ,13 ,25 ,27 ,29 ,31 ,33 ]#line:3517
    "買五檔價在字串中的位置"#line:3518
    fB5QCount :int =10 #line:3519
    "買5檔的檔數"#line:3520
    def B5Q_POrg (O0OO0OOO00OO0000O ,OO00000OOO0OO000O :int ):#line:3522
        ""#line:3523
        if OO00000OOO0OO000O >O0OO0OOO00OO0000O .fB5QCount :#line:3524
            return ""#line:3525
        elif O0OO0OOO00OO0000O .f5Q ==None :#line:3526
            return ""#line:3527
        else :#line:3528
            return O0OO0OOO00OO0000O .f5Q [O0OO0OOO00OO0000O .fAryB5Q_P [OO00000OOO0OO000O -1 ]]#line:3529
    def Set_B5Q_P (O0O0O00000O00OO0O ,O0OO00OO0O0OOO0O0 :int ):#line:3531
        ""#line:3532
        if O0OO00OO0O0OOO0O0 >O0O0O00000O00OO0O .fB5QCount :#line:3533
            return 0 #line:3534
        elif O0O0O00000O00OO0O .f5Q ==None :#line:3535
            return 0 #line:3536
        else :#line:3537
            return O0O0O00000O00OO0O .TransPrice2Dec (O0O0O00000O00OO0O .f5Q [O0O0O00000O00OO0O .fAryB5Q_P [O0OO00OO0O0OOO0O0 -1 ]])#line:3538
    def Get_B5Q_P (O00OO00OO00O00O00 ,O0OO000OO000O000O :int ):#line:3540
        if O00OO00OO00O00O00 .f5Q ==None :#line:3541
            return 0 #line:3542
        O00OO00OO0O00OO00 :decimal =0 #line:3543
        O00OO00OO0O00OO00 =O00OO00OO00O00O00 .TransPrice2Dec (O00OO00OO00O00O00 .f5Q [O00OO00OO00O00O00 .fAryB5Q_P [O0OO000OO000O000O -1 ]])#line:3544
        return O00OO00OO0O00OO00 #line:3545
    def GetDply_B5Q_P (O000OOO000OO00OO0 ,OOO00OOOOOOO00OO0 :int ,aDg_tPrice :str =""):#line:3547
        if OOO00OOOOOOO00OO0 >O000OOO000OO00OO0 .fB5QCount :#line:3548
            return ""#line:3549
        elif O000OOO000OO00OO0 .f5Q ==None :#line:3550
            return ""#line:3551
        else :#line:3552
            OO00OOOO0O00OO0O0 :decimal =0 #line:3553
            OO00OOOO0O00OO0O0 =O000OOO000OO00OO0 .TransPrice2Dec (O000OOO000OO00OO0 .f5Q [O000OOO000OO00OO0 .fAryB5Q_P [OOO00OOOOOOO00OO0 -1 ]])#line:3554
            return O000OOO000OO00OO0 .TransPrice2Str (OO00OOOO0O00OO0O0 ,aDg_tPrice )#line:3555
    def B5Q_QOrg (OO00O000000OOOOOO ,OOOOO00O0O0OOOOO0 :int ):#line:3557
        ""#line:3558
        if OOOOO00O0O0OOOOO0 >OO00O000000OOOOOO .fB5QCount :#line:3559
            return ""#line:3560
        elif OO00O000000OOOOOO .f5Q ==None :#line:3561
            return ""#line:3562
        else :#line:3563
            return OO00O000000OOOOOO .f5Q [OO00O000000OOOOOO .fAryB5Q_Q [OOOOO00O0O0OOOOO0 -1 ]]#line:3564
    def Set_B5Q_Q (OO0O00O00O0O0O0OO ,OOO0O0OO0O000O0OO :int ):#line:3566
        ""#line:3567
        if OOO0O0OO0O000O0OO >OO0O00O00O0O0O0OO .fB5QCount :#line:3569
            return 0 #line:3570
        elif OO0O00O00O0O0O0OO .f5Q ==None :#line:3571
            return 0 #line:3572
        else :#line:3573
            return OO0O00O00O0O0O0OO .TransToInt (OO0O00O00O0O0O0OO .f5Q [OO0O00O00O0O0O0OO .fAryB5Q_Q [OOO0O0OO0O000O0OO -1 ]])#line:3574
    def Get_B5Q_Q (O0O00O0000OOOOOOO ,OOO00O0OO0O0000OO :int ):#line:3576
        O00000OOOO0OOO0OO :int =0 #line:3578
        O00000OOOO0OOO0OO =O0O00O0000OOOOOOO .Set_B5Q_Q (OOO00O0OO0O0000OO )#line:3579
        return str (O00000OOOO0OOO0OO )#line:3580
    fAryS5Q_P =[14 ,16 ,18 ,20 ,22 ,34 ,36 ,38 ,40 ,42 ]#line:3583
    "買五檔價在字串中的位置"#line:3584
    fAryS5Q_Q =[15 ,17 ,19 ,21 ,23 ,35 ,37 ,39 ,41 ,43 ]#line:3585
    "買五檔價在字串中的位置"#line:3586
    fS5QCount :int =10 #line:3587
    "賣5檔的檔數"#line:3588
    def S5Q_POrg (O0OO00000OO00O00O ,O0OOO00OO00O00O00 :int ):#line:3590
        ""#line:3591
        if O0OOO00OO00O00O00 >O0OO00000OO00O00O .fS5QCount :#line:3592
            return ""#line:3593
        elif O0OO00000OO00O00O .f5Q ==None :#line:3594
            return ""#line:3595
        else :#line:3596
            return O0OO00000OO00O00O .f5Q [O0OO00000OO00O00O .fAryS5Q_P [O0OOO00OO00O00O00 -1 ]]#line:3597
    def Set_S5Q_P (O0O000OOOO00O0OOO ,OO0OOOO000O00OO0O :int ):#line:3599
        ""#line:3600
        if OO0OOOO000O00OO0O >O0O000OOOO00O0OOO .fS5QCount :#line:3601
            return 0 #line:3602
        elif O0O000OOOO00O0OOO .f5Q ==None :#line:3603
            return 0 #line:3604
        else :#line:3605
            return O0O000OOOO00O0OOO .TransPrice2Dec (O0O000OOOO00O0OOO .f5Q [O0O000OOOO00O0OOO .fAryS5Q_P [OO0OOOO000O00OO0O -1 ]])#line:3606
    def Get_S5Q_P (OO00000O000OOO00O ,O0O00O0000O0OO000 :int ):#line:3608
        if OO00000O000OOO00O .f5Q ==None :#line:3609
            return 0 #line:3610
        O0O0OOO0OOOOO0O00 :decimal =0 #line:3611
        O0O0OOO0OOOOO0O00 =OO00000O000OOO00O .TransPrice2Dec (OO00000O000OOO00O .f5Q [OO00000O000OOO00O .fAryS5Q_P [O0O00O0000O0OO000 -1 ]])#line:3612
        return O0O0OOO0OOOOO0O00 #line:3613
    def GetDply_S5Q_P (OOO0O0O00OOOOOO00 ,O000O00O0OOOOOOO0 :int ,aDg_tPrice :str =""):#line:3615
        if O000O00O0OOOOOOO0 >OOO0O0O00OOOOOO00 .fS5QCount :#line:3616
            return ""#line:3617
        elif OOO0O0O00OOOOOO00 .f5Q ==None :#line:3618
            return ""#line:3619
        else :#line:3620
            O0O00O00000O00000 :decimal =0 #line:3621
            O0O00O00000O00000 =OOO0O0O00OOOOOO00 .TransPrice2Dec (OOO0O0O00OOOOOO00 .f5Q [OOO0O0O00OOOOOO00 .fAryS5Q_P [O000O00O0OOOOOOO0 -1 ]])#line:3622
            return OOO0O0O00OOOOOO00 .TransPrice2Str (O0O00O00000O00000 ,aDg_tPrice )#line:3623
    def S5Q_QOrg (O00OOOO0O00000000 ,OO00O0OOOO0OOO0O0 :int ):#line:3625
        ""#line:3626
        if OO00O0OOOO0OOO0O0 >O00OOOO0O00000000 .fS5QCount :#line:3627
            return ""#line:3628
        elif O00OOOO0O00000000 .f5Q ==None :#line:3629
            return ""#line:3630
        else :#line:3631
            return O00OOOO0O00000000 .f5Q [O00OOOO0O00000000 .fAryS5Q_Q [OO00O0OOOO0OOO0O0 -1 ]]#line:3632
    def Set_S5Q_Q (OO0O0O0O0O00O00O0 ,O00O00OO0000OO00O :int ):#line:3634
        ""#line:3635
        if O00O00OO0000OO00O >OO0O0O0O0O00O00O0 .fS5QCount :#line:3636
            return 0 #line:3637
        elif OO0O0O0O0O00O00O0 .f5Q ==None :#line:3638
            return 0 #line:3639
        else :#line:3640
            return OO0O0O0O0O00O00O0 .TransToInt (OO0O0O0O0O00O00O0 .f5Q [OO0O0O0O0O00O00O0 .fAryS5Q_Q [O00O00OO0000OO00O -1 ]])#line:3641
    def Get_S5Q_Q (O0OOO0000000000O0 ,OOO0O0OO0OOO0OOOO :int ):#line:3643
        OOO000O0OOO0000O0 :int =0 #line:3644
        OOO000O0OOO0000O0 =O0OOO0000000000O0 .Set_S5Q_Q (OOO0O0OO0OOO0OOOO )#line:3645
        return str (OOO000O0OOO0000O0 )#line:3646
    def Handle_5Q (O0OOO0OO00O0000O0 ,OOO00O0OOO0OO0O00 :str ):#line:3649
        O0OOO0OO00O0000O0 .f5Q =OOO00O0OOO0OO0O00 .split ('|')#line:3650
        O0OOO0OO00O0000O0 .SetData ()#line:3651
    def SetData (OO000OOOO0O00000O ):#line:3653
        OO000OOOO0O00000O .SolICE =OO000OOOO0O00000O .f5Q [0 ]#line:3654
        OO000OOOO0O00000O .DataTime =OO000OOOO0O00000O .f5Q [2 ]#line:3655
        OO000OOOO0O00000O .QtSrc =OO000OOOO0O00000O .f5Q [3 ]#line:3656
    def __init__ (O0O0O00000OO000OO )->None :#line:3658
        pass #line:3659
    def __str__ (OOOOOO0O0OO000OO0 )->str :#line:3661
        return f"SolICE:{OOOOOO0O0OO000OO0.SolICE} DataTime:{OOOOOO0O0OO000OO0.DataTime} QtSrc:{OOOOOO0O0OO000OO0.QtSrc} f5Q:{OOOOOO0O0OO000OO0.f5Q}"#line:3662
class TOvsFutQuoteData :#line:3663
    SolIce :str =""#line:3664
    ProdKind :TOvsFutProdKind =TOvsFutProdKind .pkNone #line:3666
    BAS :TOvsFutQtBase =None #line:3668
    QtTX :TOvsFutQtTX =None #line:3669
    Qt5Q :TOvsFutQt5Q =None #line:3670
    def __init__ (OO0000OO00O0OO000 ,O0O0O0O00000000O0 :TOvsFutProdKind ,OOO00OO0OOOO0OO00 :str ,OOO0OOO0OO0O0OO00 :bool ):#line:3672
        ""#line:3673
        OO0000OO00O0OO000 .SolIce =OOO00OO0OOOO0OO00 #line:3674
        OO0000OO00O0OO000 .ProdKind =O0O0O0O00000000O0 #line:3675
        OO0000OO00O0OO000 ._lock =Lock ()#line:3676
        if O0O0O0O00000000O0 ==TOvsFutProdKind .pkNormal :#line:3677
            OO0000OO00O0OO000 .BAS =TOvsFutQtBase ()#line:3678
            OO0000OO00O0OO000 .QtTX =TOvsFutQtTX (OOO0OOO0OO0O0OO00 )#line:3679
            OO0000OO00O0OO000 .Qt5Q =TOvsFutQt5Q ()#line:3680
        elif O0O0O0O00000000O0 ==TOvsFutProdKind .pkIndex :#line:3681
            pass #line:3682
    def SetDataInit (OO0OO0O00O00OO000 ):#line:3684
        ""#line:3685
        if OO0OO0O00O00OO000 .ProdKind ==TOvsFutProdKind .pkNormal :#line:3686
            OO0OO0O00O00OO000 .QtTX .DecimalMultiply =OO0OO0O00O00OO000 .BAS .DecimalMultiply #line:3687
            OO0OO0O00O00OO000 .Qt5Q .DecimalMultiply =OO0OO0O00O00OO000 .BAS .DecimalMultiply #line:3688
            OO0OO0O00O00OO000 .QtTX .Price_Denominator =OO0OO0O00O00OO000 .BAS .Price_Denominator #line:3689
            OO0OO0O00O00OO000 .Qt5Q .Price_Denominator =OO0OO0O00O00OO000 .BAS .Price_Denominator #line:3690
class TMapOvsFutQuoteData (UserDict ):#line:3692
    ""#line:3693
    def __init__ (OO0OOO0OOO00OO0OO ,mapping =None ,**O0OOO0O00OO0O0O0O ):#line:3694
        if mapping is not None :#line:3695
            mapping ={str (OOO0O00O0OOOOO00O ).upper ():OOO0O000OOOOO000O for OOO0O00O0OOOOO00O ,OOO0O000OOOOO000O in mapping .items ()}#line:3698
        else :#line:3699
            mapping ={}#line:3700
        if O0OOO0O00OO0O0O0O :#line:3701
            mapping .update ({str (O00000OO0000O0OO0 ).upper ():O0O0O0OOOOO0000O0 for O00000OO0000O0OO0 ,O0O0O0OOOOO0000O0 in O0OOO0O00OO0O0O0O .items ()})#line:3704
        OO0OOO0OOO00OO0OO .MapQtProc ={}#line:3705
        super ().__init__ (mapping )#line:3706
    def __setitem__ (OO000O00OO000000O ,OOO0OOOOOO00OOO0O ,O0O0O0OOOO00O0OOO ):#line:3708
        super ().__setitem__ (OOO0OOOOOO00OOO0O ,O0O0O0OOOO00O0OOO )#line:3709
class TObjOvsFutQuoteMap (UserDict ):#line:3711
    DefProc_TX :callable =None #line:3713
    "成交行情解析proc"#line:3714
    DefProc_5Q :callable =None #line:3715
    "五檔行情解析proc"#line:3716
    def __init__ (OO0OOOOOO0O000OO0 ,mapping =None ,**O000000OO000000OO ):#line:3718
        if mapping is not None :#line:3719
            mapping ={str (OO00O0000OO000O00 ).upper ():O00O00OO0O0OOO000 for OO00O0000OO000O00 ,O00O00OO0O0OOO000 in mapping .items ()}#line:3722
        else :#line:3723
            mapping ={}#line:3724
        if O000000OO000000OO :#line:3725
            mapping .update ({str (O0OO000O000O00OO0 ).upper ():OOOO0O0OOOO00OOOO for O0OO000O000O00OO0 ,OOOO0O0OOOO00OOOO in O000000OO000000OO .items ()})#line:3728
        OO0OOOOOO0O000OO0 .MapQtProc ={}#line:3731
        "各商品拆解行情proc(EX:NQ的TX與5Q, 行情拆解,是不同Proc)"#line:3732
        super ().__init__ (mapping )#line:3733
    def __setitem__ (OO00OO00OOOOO000O ,O0OOO0O00OO0OO0OO ,OOO0O0O00O0O0OO00 ):#line:3735
        super ().__setitem__ (O0OOO0O00OO0OO0OO ,OOO0O0O00O0O0OO00 )#line:3736
    def AddRcvData (O0O0O000O0O0O0OO0 ,O000O0O00000OOO0O :str ,OOO0O00O0O0000OO0 :str ,OO0000OO000O0OO00 :bool ):#line:3738
        ""#line:3742
        O0OOO000OOOOO0O0O =""#line:3744
        OOO0O0O0OO0000O0O :TOvsFutQuoteData =None #line:3745
        try :#line:3746
            OO00OOOOO0OOO00OO =json .loads (OOO0O00O0O0000OO0 )#line:3747
            if "status"in OO00OOOOO0OOO00OO and len (OO00OOOOO0OOO00OO ["status"])>0 :#line:3749
                if OO00OOOOO0OOO00OO ["status"][0 ]=="error":#line:3750
                    O0OOO000OOOOO0O0O =f"[海期][AddRcvData](aSolIce={O000O0O00000OOO0O}, aData={OOO0O00O0O0000OO0})行情回補資料有誤!"#line:3751
                    return False ,OOO0O0O0OO0000O0O ,O0OOO000OOOOO0O0O #line:3752
            if "BAS"in OO00OOOOO0OOO00OO and len (OO00OOOOO0OOO00OO ["BAS"])==0 :#line:3753
                O0OOO000OOOOO0O0O =f"[海期][AddRcvData](aSolIce={O000O0O00000OOO0O}, aData={OOO0O00O0O0000OO0})沒有BAS資料!"#line:3754
                return False ,OOO0O0O0OO0000O0O ,O0OOO000OOOOO0O0O #line:3755
            if O0O0O000O0O0O0OO0 .data .get (O000O0O00000OOO0O )is None :#line:3758
                O000OO00OO0000O00 =TOvsFutQuoteData (TOvsFutProdKind .pkNormal ,O000O0O00000OOO0O ,OO0000OO000O0OO00 )#line:3760
                O000OO00OO0000O00 .BAS .Handle_BAS (OO00OOOOO0OOO00OO ["BAS"][0 ])#line:3761
                O000OO00OO0000O00 .SetDataInit ()#line:3763
                OOO0O0O0OO0000O0O =O000OO00OO0000O00 #line:3764
                O0O0O000O0O0O0OO0 [O000O0O00000OOO0O ]=O000OO00OO0000O00 #line:3765
                return True ,OOO0O0O0OO0000O0O ,""#line:3766
            else :#line:3767
                O000OO00OO0000O00 :TOvsFutQuoteData =O0O0O000O0O0O0OO0 [O000O0O00000OOO0O ]#line:3768
                with O000OO00OO0000O00 ._lock :#line:3769
                    O000OO00OO0000O00 .BAS .Handle_BAS (OO00OOOOO0OOO00OO ["BAS"][0 ])#line:3770
                    O000OO00OO0000O00 .SetDataInit ()#line:3772
                    OOO0O0O0OO0000O0O =O000OO00OO0000O00 #line:3773
                return True ,OOO0O0O0OO0000O0O ,""#line:3774
        except Exception as OO0OO00000O0OO0O0 :#line:3775
            O0OOO000OOOOO0O0O =f"[海期][AddRcvData](aSolIce={O000O0O00000OOO0O}, aData={OOO0O00O0O0000OO0}){OO0OO00000O0OO0O0}"#line:3776
        return False ,OOO0O0O0OO0000O0O ,O0OOO000OOOOO0O0O #line:3777
    def AddData (O0OOOO0OOOO0OO000 ,OOO0O0OO00OO0000O :TOvsFutProdKind ,OOO0OO0OOOOOO0OO0 :str ,O0O00OO0O0OO0O0O0 :bool ,O0O00000OOO0OO0OO :str ,OO000OOOO00O0O0O0 :callable ):#line:3779
        ""#line:3783
        try :#line:3784
            if O0OOOO0OOOO0OO000 .data .get (OOO0OO0OOOOOO0OO0 )is None :#line:3785
                O000O00O0O00O0O0O =TOvsFutQuoteData (OOO0O0OO00OO0000O ,OOO0OO0OOOOOO0OO0 ,O0O00OO0O0OO0O0O0 )#line:3786
                O0OOOO0OOOO0OO000 [O0O00000OOO0OO0OO ]=O000O00O0O00O0O0O #line:3787
                if O0OOOO0OOOO0OO000 .MapQtProc .get (O0O00000OOO0OO0OO )is None :#line:3789
                    O0OOOO0OOOO0OO000 .MapQtProc [O0O00000OOO0OO0OO ]=OO000OOOO00O0O0O0 #line:3790
                return True #line:3792
            else :#line:3793
                return True #line:3794
        except Exception as O00OO000OOO0O0000 :#line:3795
            pass #line:3796
        return False #line:3797
    def AddDataBySolIce (OOOO0OO0O0000O0OO ,O0O0OO00O0OOO0O0O :bool ,O0OOO0OO000O0OO00 :str ,OOO0O00OO0O00OOOO ,OO0OO000O0O0OO0OO :bool ):#line:3799
        ""#line:3807
        O0O00OO000OO00000 =""#line:3808
        OOOO00000O0OO0OOO :TOvsFutQuoteData =None #line:3809
        try :#line:3810
            OOOO00000O0OO0OOO =TMapOvsFutQuoteData ()#line:3812
            for OO0O00OO0O0O0000O in OOO0O00OO0O00OOOO ["BAS"]:#line:3813
                O0000O000OO00O0OO =TOvsFutQtBase ()#line:3814
                O0000O000OO00O0OO .Handle_BAS (OO0O00OO0O0O0000O )#line:3815
                if OOOO00000O0OO0OOO .data .get (O0000O000OO00O0OO .Symbol ):#line:3817
                    O000000OOO00O0000 =TOvsFutQuoteData (TOvsFutProdKind .pkNormal ,O0000O000OO00O0OO .Symbol ,OO0OO000O0O0OO0OO )#line:3818
                    O000000OOO00O0000 .BAS =O0000O000OO00O0OO #line:3819
                    O000000OOO00O0000 .SetDataInit ()#line:3820
                    O000000O000OO0O00 :OO0O00OO0O0O0000O =O000000OOO00O0000 .BAS .TopicTX #line:3822
                    OOO0O00O0O0000000 :OO0O00OO0O0O0000O =O000000OOO00O0000 .BAS .Topic5Q #line:3823
                    OOOO0OO0O0000O0OO [O000000O000OO0O00 ]=O000000OOO00O0000 #line:3825
                    OOOO0OO0O0000O0OO [OOO0O00O0O0000000 ]=O000000OOO00O0000 #line:3826
                    if OOOO0OO0O0000O0OO .MapQtProc .get (O000000O000OO0O00 )is None :#line:3828
                        OOOO0OO0O0000O0OO .MapQtProc [O000000O000OO0O00 ]=OOOO0OO0O0000O0OO .DefProc_TX #line:3829
                    if OOOO0OO0O0000O0OO .MapQtProc .get (OOO0O00O0O0000000 )is None :#line:3830
                        OOOO0OO0O0000O0OO .MapQtProc [OOO0O00O0O0000000 ]=OOOO0OO0O0000O0OO .DefProc_5Q #line:3831
                    OOOO00000O0OO0OOO .Add (O0000O000OO00O0OO .Symbol ,O000000OOO00O0000 )#line:3833
            return len (OOOO00000O0OO0OOO )>0 ,OOOO00000O0OO0OOO ,O0O00OO000OO00000 #line:3834
        except Exception as OO000OO0O000000OO :#line:3836
            O0O00OO000OO00000 =f"[海期][AddDataBySolIce](aIsCat={O0O0OO00O0OOO0O0O}, aSolIce={O0OOO0OO000O0OO00}){OO000OO0O000000OO}"#line:3837
        return False ,OOOO00000O0OO0OOO ,O0O00OO000OO00000 #line:3838
    def GetItem_BySolIce (OO0000OO00OOOOOO0 ,OO000OO00OOOOOOO0 :str ):#line:3840
        ""#line:3843
        OO00000OOO0O00OOO :str =""#line:3845
        O000O000O0O0000OO =None #line:3846
        try :#line:3847
            OO0O0O0OOOOOO0OOO =[]#line:3848
            for OOO0OOO000OO0OOO0 ,O00OO0OO0O0OO00O0 in OO0000OO00OOOOOO0 .items ():#line:3849
                OO0O00O0OO00OO0OO :TOvsFutQuoteData =O00OO0OO0O0OO00O0 #line:3850
                if OO0O00O0OO00OO0OO .SolIce ==OO000OO00OOOOOOO0 :#line:3851
                    OO0O0O0OOOOOO0OOO .append (OOO0OOO000OO0OOO0 )#line:3852
            O000O000O0O0000OO =OO0O0O0OOOOOO0OOO #line:3854
            if O000O000O0O0000OO is None or len (O000O000O0O0000OO )==0 :#line:3855
                OO00000OOO0O00OOO =f"[海期][GetItem_BySolIce](aSolIce={OO000OO00OOOOOOO0})商品已不存存!"#line:3856
                return False ,O000O000O0O0000OO ,OO00000OOO0O00OOO #line:3857
            return True ,O000O000O0O0000OO ,OO00000OOO0O00OOO #line:3858
        except Exception as OOOOO000O00OO0OO0 :#line:3859
            OO00000OOO0O00OOO =f"[海期][GetItem_BySolIce](aSolIce={OO000OO00OOOOOOO0}){OOOOO000O00OO0OO0}"#line:3860
        return False ,O000O000O0O0000OO ,OO00000OOO0O00OOO #line:3861
    def GetItem_ByExchange (O000O00O00OOOO000 ,OO0000OOO0O000OOO :str ):#line:3862
        ""#line:3863
        OOO00O000O0OO0OO0 =""#line:3864
        O00OO00OOO00O0OOO =None #line:3865
        try :#line:3866
            OO0000OO0OO00O0OO =[]#line:3867
            for O000000OO0O000O00 ,OO0O00O0OO00OO0O0 in O000O00O00OOOO000 .items ():#line:3868
                OOOO000O0OOOO0O00 :TOvsFutQuoteData =OO0O00O0OO00OO0O0 #line:3869
                if OOOO000O0OOOO0O00 .BAS .Exchange ==OO0000OOO0O000OOO :#line:3870
                    OO0000OO0OO00O0OO .append (O000000OO0O000O00 )#line:3871
                O00OO00OOO00O0OOO =OO0000OO0OO00O0OO #line:3872
            if O00OO00OOO00O0OOO is None or len (O00OO00OOO00O0OOO )==0 :#line:3873
                OOO00O000O0OO0OO0 =f"[海期][GetItem_ByExchange](aExchange={OO0000OOO0O000OOO})商品已不存存!"#line:3874
                return False ,O00OO00OOO00O0OOO ,OOO00O000O0OO0OO0 #line:3875
            return True ,O00OO00OOO00O0OOO ,OOO00O000O0OO0OO0 #line:3877
        except Exception as OO0OOO00OO0000O00 :#line:3879
            OOO00O000O0OO0OO0 =f"[海期][GetItem_ByExchange](aExchange={OO0000OOO0O000OOO}){OO0OOO00OO0000O00}"#line:3880
        return False ,O00OO00OOO00O0OOO ,OOO00O000O0OO0OO0 #line:3881
class TObjOvsFutProdMthMap (UserDict ):#line:3886
    ""#line:3888
    def __init__ (O0000OO0O0O00O0OO ,O00O0OO0000000O0O :str ,OOO0OOO0OO000OOOO :str ):#line:3890
        O0000OO0O0O00O0OO .Exchange =O00O0OO0000000O0O #line:3891
        O0000OO0O0O00O0OO .ExchangeName =OOO0OOO0OO000OOOO #line:3892
        O00OO0OOOOOO0OO00 ={}#line:3893
        super ().__init__ (O00OO0OOOOOO0OO00 )#line:3894
    def __setitem__ (OOOO000O0O0O0O000 ,O0O000OO0OOOOO00O ,O0O0OO00OOOO0OOO0 ):#line:3896
        super ().__setitem__ (O0O000OO0OOOOO00O ,O0O0OO00OOOO0OOO0 )#line:3897
    def AddItem (OOO00OOOO0000O000 ,OOO0O00O0OOOO000O :TOvsFutQtBase ):#line:3899
        if OOO00OOOO0000O000 .data .get (OOO0O00O0OOOO000O .ProdID )is None :#line:3900
            OO00O0O0OO0O0O000 =TObjOvsFutMthList (OOO0O00O0OOOO000O .ProdID ,OOO0O00O0OOOO000O .FutName )#line:3901
            OO00O0O0OO0O0O000 .AddItem (OOO0O00O0OOOO000O )#line:3902
            OOO00OOOO0000O000 [OOO0O00O0OOOO000O .ProdID ]=OO00O0O0OO0O0O000 #line:3903
        else :#line:3904
            OO00O0O0OO0O0O000 :TObjOvsFutMthList =OOO00OOOO0000O000 [OOO0O00O0OOOO000O .ProdID ]#line:3905
            OO00O0O0OO0O0O000 .AddItem (OOO0O00O0OOOO000O )#line:3906
class TObjOvsFutMthList (UserDict ):#line:3908
    ""#line:3910
    def __init__ (O0O0OO0O0OO0O00OO ,OO00OO0OO00O0OOO0 :str ,O0O0O0OOOO00OO00O :str ):#line:3912
        O0O0OO0O0OO0O00OO .ProdID =OO00OO0OO00O0OOO0 #line:3913
        O0O0OO0O0OO0O00OO .ProdName =O0O0O0OOOO00OO00O #line:3914
        O0O0O0O00O0O0OO0O ={}#line:3915
        super ().__init__ (O0O0O0O00O0O0OO0O )#line:3916
    def __setitem__ (O0OO0OOO0O0000O0O ,OO0OO0O0000O0OO0O ,O0OOOOOO0O00OOO0O ):#line:3918
        super ().__setitem__ (OO0OO0O0000O0OO0O ,O0OOOOOO0O00OOO0O )#line:3919
    def AddItem (OO0OO0O0O0OOO000O ,OOOO00O00OO00O0OO :TOvsFutQtBase ):#line:3921
        if OO0OO0O0O0OOO000O .data .get (OOOO00O00OO00O0OO .SettleMth )is None :#line:3922
            OOOO00OOOO0O0O000 :TObjOvsFutBasMap =TObjOvsFutBasMap (OOOO00O00OO00O0OO .SettleMth )#line:3923
            OOOO00OOOO0O0O000 .AddItem (OOOO00O00OO00O0OO )#line:3924
            OO0OO0O0O0OOO000O [OOOO00O00OO00O0OO .SettleMth ]=OOOO00OOOO0O0O000 #line:3925
        else :#line:3926
            OOOO00OOOO0O0O000 :TObjOvsFutBasMap =OO0OO0O0O0OOO000O [OOOO00O00OO00O0OO .SettleMth ]#line:3927
            OOOO00OOOO0O0O000 .AddItem (OOOO00O00OO00O0OO )#line:3928
        OO0OO0O0O0OOO000O .data =dict (sorted (OO0OO0O0O0OOO000O .data .items ()))#line:3929
class TObjOvsFutBasMap (UserDict ):#line:3931
    ""#line:3932
    def __init__ (O0O00O00O0OO0O00O ,O0O00OOO0OO0OOO00 :str ):#line:3934
        O0O00O00O0OO0O00O .SettleMth =O0O00OOO0OO0OOO00 #line:3935
        O0O0000OO000OO00O ={}#line:3936
        super ().__init__ (O0O0000OO000OO00O )#line:3937
    def __setitem__ (OO00O00OOOO0OOOO0 ,O0OO00OOO0OOO00OO ,O0000OO0O00O00000 ):#line:3939
        super ().__setitem__ (O0OO00OOO0OOO00OO ,O0000OO0O00O00000 )#line:3940
    def AddItem (O000O0O00OO0OOOOO ,OOO0OOOO000O00OO0 :TOvsFutQtBase ):#line:3942
        if O000O0O00OO0OOOOO .data .get (OOO0OOOO000O00OO0 .SolICE )is None :#line:3943
            O000O0O00OO0OOOOO [OOO0OOOO000O00OO0 .SolICE ]=OOO0OOOO000O00OO0 #line:3944
class TObjBaseOvsFutExchageTree (UserDict ):#line:3946
    ""#line:3948
    fProdMthList :TObjOvsFutProdMthMap =TObjOvsFutProdMthMap ("","")#line:3949
    "Key=ProdID, Values=可交易月份們"#line:3950
    fMapSolICE ={}#line:3952
    "Key=SolICE Dictionary<string, TOvsFutQtBase>()"#line:3953
    def __init__ (OO0000OOO000O000O ):#line:3955
        O00OOO0OO0OO00O0O ={}#line:3956
        super ().__init__ (O00OOO0OO0OO00O0O )#line:3957
    def __setitem__ (OOOO0O0O00OOOO0O0 ,O0O00O0OO00O0OO0O ,O0000O0O00OOOO000 ):#line:3959
        super ().__setitem__ (O0O00O0OO00O0OO0O ,O0000O0O00OOOO000 )#line:3960
    def AddItem (O0O00OOOO0O00O000 ,OOO0OOO000O0OOO00 :TOvsFutQtBase ):#line:3962
        if O0O00OOOO0O00O000 .data .get (OOO0OOO000O0OOO00 .Exchange )is None :#line:3963
            OO000OOO0O0O00O00 =TObjOvsFutProdMthMap (OOO0OOO000O0OOO00 .Exchange ,OOO0OOO000O0OOO00 .ExchangeName )#line:3965
            O0O00OOOO0O00O000 [OOO0OOO000O0OOO00 .Exchange ]=OO000OOO0O0O00O00 #line:3966
        else :#line:3967
            OO000OOO0O0O00O00 :TObjOvsFutMthList =O0O00OOOO0O00O000 [OOO0OOO000O0OOO00 .Exchange ]#line:3968
            OO000OOO0O0O00O00 .AddItem (OOO0OOO000O0OOO00 )#line:3969
    def SetInit (OO00000000OOO0OO0 ):#line:3971
        try :#line:3972
            for OO0O0O0O0O0OO000O in OO00000000OOO0OO0 .values ():#line:3974
                OO0O00OO0O00OOO0O :TObjOvsFutProdMthMap #line:3975
                OO0O00OO0O00OOO0O =OO0O0O0O0O0OO000O #line:3976
                O00OOOOOOO000OO00 :TObjOvsFutMthList =next (iter (OO0O00OO0O00OOO0O .values ()),None )#line:3979
                if O00OOOOOOO000OO00 .ProdID in OO00000000OOO0OO0 .fProdMthList :#line:3981
                    continue #line:3982
                OO00000000OOO0OO0 .fProdMthList [O00OOOOOOO000OO00 .ProdID ]=O00OOOOOOO000OO00 #line:3985
                for OOO0OOO00O0OO0O00 in O00OOOOOOO000OO00 .values ():#line:3987
                    for OO0O0O0O0OOOO0000 in OOO0OOO00O0OO0O00 .values ():#line:3988
                        OO00000000OOO0OO0 .fMapSolICE [OO0O0O0O0OOOO0000 .SolICE ]=OO0O0O0O0OOOO0000 #line:3989
        except Exception as OO000OOOO00O0OOOO :#line:3990
            pass #line:3991
    def GetItem_BySolICE (OOO0OOOOOO0000000 ,OO00O0O000O0OOOO0 :str ):#line:3993
        ""#line:3995
        OO0O000OOOO00OO0O =None #line:3996
        try :#line:3997
            if OOO0OOOOOO0000000 .fMapSolICE .get (OO00O0O000O0OOOO0 )is not None :#line:3998
                OO0O000OOOO00OO0O =OOO0OOOOOO0000000 .fMapSolICE [OO00O0O000O0OOOO0 ]#line:3999
                return True ,OO0O000OOOO00OO0O #line:4000
        except Exception as O00OO0OOO0OOO0OOO :#line:4001
            pass #line:4002
        return False ,OO0O000OOOO00OO0O #line:4003
    def IsExists (OOO00O0O00O00000O ,O00O0O000000O0O00 :str ,OOOO0OO00OOO0O00O :str ):#line:4005
        try :#line:4006
            if OOO00O0O00O00000O .fProdMthList .get (O00O0O000000O0O00 )is not None :#line:4007
                if OOOO0OO00OOO0O00O in OOO00O0O00O00000O .fProdMthList [O00O0O000000O0O00 ]:#line:4008
                    return True #line:4009
        except Exception as OO0OO00OOO00OO0OO :#line:4010
            pass #line:4011
        return False #line:4012
    def GetExchangeAndProdList (OOOO0O00O00O00OOO ):#line:4014
        ""#line:4017
        O0O00O0OOO0O00O00 ={}#line:4018
        O000O0O0O0000OOO0 ={}#line:4019
        try :#line:4020
            for OOO0OO0O0O0OOO0OO in OOOO0O00O00O00OOO .values ():#line:4022
                O0O00O0OOO0O00O00 [OOO0OO0O0O0OOO0OO .Exchange ]=OOO0OO0O0O0OOO0OO .ExchangeName #line:4023
                for OOO000O00O0OOO0OO in OOO0OO0O0O0OOO0OO .Values :#line:4024
                    O000O0O0O0000OOO0 [OOO000O00O0OOO0OO .ProdName ]=OOO000O00O0OOO0OO #line:4025
            return True ,O0O00O0OOO0O00O00 ,O000O0O0O0000OOO0 #line:4026
        except Exception as OOO0O0O0OO0OOO0OO :#line:4028
            pass #line:4029
        return False ,O0O00O0OOO0O00O00 ,O000O0O0O0000OOO0 #line:4030
class ITQtRcvEventData :#line:4033
    SolIce :str #line:4034
    IsOK :bool #line:4035
    tmpRcvKind :TOvsFutQtRcvKind #line:4036
    tmpQt :TOvsFutQuoteData #line:4037
class TQtRcvEventData (ITQtRcvEventData ):#line:4039
    def __init__ (O0OO0OO000OO0OOOO )->None :#line:4040
        O0OO0OO000OO0OOOO .SolIce =""#line:4041
        O0OO0OO000OO0OOOO .IsOK =False #line:4042
        O0OO0OO000OO0OOOO .tmpQt =None #line:4043
        super ().__init__ ()#line:4044
    def SetRcvBAS_Succ (OO00OOOOOO0O00O00 ,OOO0OO0000OOOOOOO :str ,OO00OOO0OOO000000 :TOvsFutQuoteData ):#line:4046
        OO00OOOOOO0O00O00 .IsOK =True #line:4047
        OO00OOOOOO0O00O00 .SolIce =OOO0OO0000OOOOOOO #line:4048
        OO00OOOOOO0O00O00 .tmpRcvKind =TOvsFutQtRcvKind .pkQtRcv_BAS #line:4049
        OO00OOOOOO0O00O00 .tmpQt =OO00OOO0OOO000000 #line:4050
    def SetRcvBAS_Fail (O0000OOOO00O000O0 ,OOO00O00OOOOO0OO0 :str ):#line:4052
        O0000OOOO00O000O0 .IsOK =False #line:4053
        O0000OOOO00O000O0 .SolIce =OOO00O00OOOOO0OO0 #line:4054
        O0000OOOO00O000O0 .tmpRcvKind =TOvsFutQtRcvKind .pkQtRcv_BAS #line:4055
class SolAPI :#line:4060
    ver ="v20230328_r"#line:4062
    __OOOO0OO00O0OOO0OO ='solacelink.json'#line:4063
    __O00OO0O000O0OO000 ='solaceProperties'#line:4065
    __OO0O000OO00OOO00O =os .path .join (dirname (__file__ ),__OOOO0OO00O0OOO0OO )#line:4067
    _fPrdSnapshotMap :TMapPrdSnapshot =TMapPrdSnapshot ()#line:4071
    _fPrdOvsMap :TMapPrdOvs =TMapPrdOvs ()#line:4072
    _fMapQuoteSTK :TObjStkQuoteMap =TObjStkQuoteMap ()#line:4074
    _fMapQuoteFUT :TObjFutQuoteMap =TObjFutQuoteMap ()#line:4075
    _fMapQuoteOvsFUT :TObjOvsFutQuoteMap =TObjOvsFutQuoteMap ()#line:4076
    def __init__ (O00O000OOO0O0O000 ,__OO0000OO0O0O000OO :MarketDataMart ,O00O0OOOO000OOO0O :str ,aRcvUseList :bool =False ,loglv =logging .INFO ,conlv =logging .INFO ):#line:4078
        ""#line:4079
        O00O000OOO0O0O000 .__O0O0O0O0OOO00OO0O =aRcvUseList #line:4082
        O00O000OOO0O0O000 .__OO0000OO0O0O000OO :MarketDataMart =__OO0000OO0O0O000OO #line:4083
        O00O000OOO0O0O000 ._pypath =O00O0OOOO000OOO0O #line:4084
        O00O000OOO0O0O000 ._is_connected =False #line:4085
        O00O000OOO0O0O000 ._lock =Lock ()#line:4086
        O00O000OOO0O0O000 ._lockQtTX_Stk =Lock ()#line:4087
        O00O000OOO0O0O000 ._lockQtTX_Fut =Lock ()#line:4088
        O00O000OOO0O0O000 ._lockQtIDX_Stk =Lock ()#line:4089
        O00O000OOO0O0O000 ._lockQtIDX_Fut =Lock ()#line:4090
        O00O000OOO0O0O000 ._fMapQuoteSTK .DefProc_TX =O00O000OOO0O0O000 .__OOOO0O0OO0O0OOO0O #line:4093
        O00O000OOO0O0O000 ._fMapQuoteSTK .DefProc_5Q =O00O000OOO0O0O000 .__O000O0000O0000000 #line:4094
        O00O000OOO0O0O000 ._fMapQuoteSTK .DefProc_Idx =O00O000OOO0O0O000 .__OOO000O00O0O00O0O #line:4095
        O00O000OOO0O0O000 .__O0OO000OO000OO000 =O00O000OOO0O0O000 .__OO00OOOO00O00O00O #line:4096
        O00O000OOO0O0O000 .__O000O00000O00OO0O =O00O000OOO0O0O000 .__OOO0OO000O0OO0OO0 #line:4097
        O00O000OOO0O0O000 .__OO0OO0O00O0OOOO00 =O00O000OOO0O0O000 .__OO000OOOOO00O00OO #line:4098
        O00O000OOO0O0O000 .__OOO0O00OO0O0O00O0 =O00O000OOO0O0O000 .__O00O00OO0OO0OOO00 #line:4099
        O00O000OOO0O0O000 .__O0O0OO0000O00OO00 =O00O000OOO0O0O000 .__O0O00O00OO0OO00OO #line:4100
        O00O000OOO0O0O000 ._fMapQuoteFUT .DefProc_TX =O00O000OOO0O0O000 .__O000OOOO0000OO00O #line:4103
        O00O000OOO0O0O000 ._fMapQuoteFUT .DefProc_5Q =O00O000OOO0O0O000 .__OO0O000O00OOOO000 #line:4104
        O00O000OOO0O0O000 ._fMapQuoteFUT .DefProc_5QTOT =O00O000OOO0O0O000 .__O000O0O000OO00O0O #line:4105
        O00O000OOO0O0O000 ._fMapQuoteFUT .DefProc_BAS =O00O000OOO0O0O000 .__O00000OO0O000OOOO #line:4106
        O00O000OOO0O0O000 .__O00O00O00000OO000 =O00O000OOO0O0O000 .__OO0O0000O00OOOO00 #line:4107
        O00O000OOO0O0O000 .__O0OO0OO000O0O0O00 =O00O000OOO0O0O000 .__O0O000O0OO0OOO0OO #line:4108
        O00O000OOO0O0O000 .__OO0O0OO000OO000O0 =O00O000OOO0O0O000 .__OOO0O0O000OO000OO #line:4109
        O00O000OOO0O0O000 .__O00OO0OO0OOO0O0OO =O00O000OOO0O0O000 .__OOOO00O0O00O0O000 #line:4110
        O00O000OOO0O0O000 .__O00OO000O0000OOO0 =O00O000OOO0O0O000 .__O0000000000000O0O #line:4111
        O00O000OOO0O0O000 .__OO00OO00O00O0O0O0 =O00O000OOO0O0O000 .__O0OOO0O0OO0O0OOOO #line:4112
        O00O000OOO0O0O000 ._fMapQuoteOvsFUT .DefProc_TX =O00O000OOO0O0O000 .__O00000OOO0O0OO0O0 #line:4114
        O00O000OOO0O0O000 ._fMapQuoteOvsFUT .DefProc_5Q =O00O000OOO0O0O000 .__O000000O0O0O000O0 #line:4115
        O00O000OOO0O0O000 .__O00O00OOOO0O00OO0 =O00O000OOO0O0O000 .__O0O0O0O00O00OOOO0 #line:4116
        O00O000OOO0O0O000 .__OO0O00O000O00OOOO =O00O000OOO0O0O000 .__OOOOO0O0O00OOO000 #line:4117
        O00O000OOO0O0O000 .__OOOOOOOO000OOO000 =O00O000OOO0O0O000 .__O0O0OOO0OO0OO000O #line:4118
        O00O000OOO0O0O000 ._message_service :MessagingService #line:4120
        O00O000OOO0O0O000 ._message_receiver :DirectMessageReceiver #line:4121
        O00O000OOO0O0O000 ._message_requester :RequestReplyMessagePublisher #line:4122
        O00O000OOO0O0O000 ._loglv =loglv #line:4123
        O00O000OOO0O0O000 ._conlv =conlv #line:4124
        O00O000OOO0O0O000 ._log =SolaceLog (O00O000OOO0O0O000 ._pypath ,loglv ,conlv )#line:4125
        O00O000OOO0O0O000 ._log .Add (arg1 =SolLogType .Debug ,arg2 =f"pypath:{O00O0OOOO000OOO0O}, aRcvUseList:{aRcvUseList}, loglv:{loglv} conlv:{conlv}")#line:4126
        O00O000OOO0O0O000 ._reply_timeout =120000 #line:4132
        O00O000OOO0O0O000 ._vRcvTopic_Stk ="Quote_TWS_RECOVER"#line:4133
        "證券回補TOPIC"#line:4134
        O00O000OOO0O0O000 ._vRcvTopic_Stk_Req ="Quote_TWS_REQ"#line:4135
        "收到證券回補TOPIC"#line:4136
        O00O000OOO0O0O000 ._vRcvTopic_Fut ="Quote_TWF_RECOVER"#line:4137
        "期貨回補TOPIC"#line:4138
        O00O000OOO0O0O000 ._vRcvTopic_Fut_Req ="Quote_TWF_REQ"#line:4139
        "收到期貨回補TOPIC"#line:4140
        O00O000OOO0O0O000 ._vRcvTopic_OvsFut ="QuoteOvs_RECOVER"#line:4141
        "海期貨回補TOPIC"#line:4142
        O00O000OOO0O0O000 ._vRcvTopic_OvsFut_Req ="QuoteOvs_REQ"#line:4143
        "收到海期貨回補TOPIC"#line:4144
        O00O000OOO0O0O000 ._vExchange =""#line:4145
        O00O000OOO0O0O000 .__O0O0O000O0000O0O0 ="Idx"#line:4146
        O00O000OOO0O0O000 ._vQuote_FUT ="Quote/TWF/"#line:4147
        O00O000OOO0O0O000 ._vQuote_STK ="Quote/TWS/"#line:4148
        O00O000OOO0O0O000 ._vQuote_OvsFUT ="QuoteOvs/"#line:4149
    def __O0O000OOO000O0OOO ():#line:4151
        try :#line:4152
            with open (SolAPI .__OO0O000OO00OOO00O ,'r')as O0O0000OOOOO0O00O :#line:4153
                O0OO0000O0OOO00O0 =O0O0000OOOOO0O00O .read ()#line:4154
            return json .loads (O0OO0000O0OOO00O0 )#line:4156
        except Exception as OO0O000O0OO00O00O :#line:4157
            raise Exception (f"Unable to read JSON in file: {SolAPI.__external_file_full_path}. Exception: {OO0O000O0OO00O00O}")#line:4158
    def __O0000O0O0O000O0O0 (O0OOO0000OO00OO00 :dict ):#line:4160
        if SolAPI .__O00OO0O000O0OO000 not in O0OOO0000OO00OO00 :#line:4161
            print (f'Solbroker details in [{SolAPI.__properties_from_external_file_name}] is unavailable, unable to find KEY: [{SolAPI.__solbroker_properties_key}]. Refer README...')#line:4162
        O0OOO0OOO00OO000O =O0OOO0000OO00OO00 [SolAPI .__O00OO0O000O0OO000 ]#line:4164
        return O0OOO0OOO00OO000O #line:4166
    __O0OO000OO000OO000 :callable =None #line:4171
    __O00O00O00000OO000 :callable =None #line:4172
    __O00O00OOOO0O00OO0 :callable =None #line:4173
    def __OOOO00OOO000O000O (O00O00000O0OOO0O0 ,O0OOO00OO0O0OO0OO :STKxFUT ,O00OOOO00OOO0OO0O ):#line:4175
        ""#line:4177
        if O0OOO00OO0O0OO0OO ==STKxFUT .STK :#line:4178
            if O00O00000O0OOO0O0 .__O0OO000OO000OO000 ==None :#line:4179
                return #line:4180
            O0O0OO00OO0O00OOO :TObjStkQuoteMap =O00OOOO00OOO0OO0O #line:4181
            O00O00000O0OOO0O0 .__O0OO000OO000OO000 ("STK",True ,O0O0OO00OO0O00OOO )#line:4182
        elif O0OOO00OO0O0OO0OO ==STKxFUT .FUT :#line:4183
            if O00O00000O0OOO0O0 .__O00O00O00000OO000 ==None :#line:4184
                return #line:4185
            O0O0OO00OO0O00OOO :TObjFutQuoteMap =O00OOOO00OOO0OO0O #line:4186
            O00O00000O0OOO0O0 .__O00O00O00000OO000 ("FUT",True ,O0O0OO00OO0O00OOO )#line:4187
        elif O0OOO00OO0O0OO0OO ==STKxFUT .OVSFUT :#line:4188
            if O00O00000O0OOO0O0 .__O00O00OOOO0O00OO0 ==None :#line:4189
                return #line:4190
            O0O0OO00OO0O00OOO :TQtRcvEventData =O00OOOO00OOO0OO0O #line:4191
            if O0O0OO00OO0O00OOO .IsOK :#line:4192
                O00O00000O0OOO0O0 .__O00O00OOOO0O00OO0 (O00O00000O0OOO0O0 ,O0O0OO00OO0O00OOO .SolIce ,O0O0OO00OO0O00OOO .IsOK ,O0O0OO00OO0O00OOO .tmpRcvKind ,O0O0OO00OO0O00OOO .tmpQt )#line:4194
            else :#line:4195
                O00O00000O0OOO0O0 .__O00O00OOOO0O00OO0 (O00O00000O0OOO0O0 ,O0O0OO00OO0O00OOO .SolIce ,O0O0OO00OO0O00OOO .IsOK ,O0O0OO00OO0O00OOO .tmpRcvKind ,None )#line:4197
    def __O00O00O000O00O000 (OOO0OOOO0OOOOOOOO ,O0000OO0OOO00OO0O :STKxFUT ,OOOO000O0O0OO0OOO :str ):#line:4199
        if O0000OO0OOO00OO0O ==STKxFUT .STK :#line:4200
            if OOO0OOOO0OOOOOOOO .__O0OO000OO000OO000 ==None :#line:4201
                return #line:4202
            OOO0OOOO0OOOOOOOO .__O0OO000OO000OO000 (OOOO000O0O0OO0OOO ,False ,None )#line:4203
        elif O0000OO0OOO00OO0O ==STKxFUT .FUT :#line:4204
            if OOO0OOOO0OOOOOOOO .__O00O00O00000OO000 ==None :#line:4205
                return #line:4206
            OOO0OOOO0OOOOOOOO .__O00O00O00000OO000 (OOOO000O0O0OO0OOO ,False ,None )#line:4207
        elif O0000OO0OOO00OO0O ==STKxFUT .OVSFUT :#line:4208
            if OOO0OOOO0OOOOOOOO .__O00O00OOOO0O00OO0 ==None :#line:4209
                return #line:4210
            pass #line:4211
    __O000O00000O00OO0O :callable =None #line:4214
    def Set_OnQtIdxRcvEventSTK (OO0OOO0O00OO0O0OO ,OO0OO0OO0O0OO0OO0 :callable ):#line:4216
        OO0OOO0O00OO0O0OO .__O000O00000O00OO0O =OO0OO0OO0O0OO0OO0 #line:4217
    def __O0000OOO0OOOO0000 (O00OOOO0O000OOOO0 ,OOO0O0O00000OOOOO :TObjStkQuoteMap ):#line:4219
        if O00OOOO0O000OOOO0 .__O000O00000O00OO0O ==None :#line:4220
            return #line:4221
        O00OOOO0O000OOOO0 .__O000O00000O00OO0O ("STKIdx",True ,OOO0O0O00000OOOOO )#line:4222
    def __OO0OOOO00O00OOO0O (O00OOO0O0000000OO ,O0O00O00O0OOO0O0O :str ):#line:4224
        if O00OOO0O0000000OO .OnQtIdxRcvEvent ==None :#line:4225
            return #line:4226
        O00OOO0O0000000OO .OnQtIdxRcvEvent (O00OOO0O0000000OO ,O0O00O00O0OOO0O0O ,False ,None )#line:4227
    __OO0OO0O00O0OOOO00 :callable =None #line:4231
    """QtTXEventHandler"""#line:4232
    def Set_OnQtTXEventSTK (O00OO0O0O0OO0OO0O ,O000OOOO0OO00OO00 :callable ):#line:4234
        O00OO0O0O0OO0OO0O .__OO0OO0O00O0OOOO00 =O000OOOO0OO00OO00 #line:4235
    def __O0000OO0O00OO0O00 (O0OO0O0OO0O0OO000 ,O0O00OOOO00O00O0O :str ,OOOOO0OO0OOOO0000 :TStkQtTX ):#line:4237
        if O0OO0O0OO0O0OO000 .__OO0OO0O00O0OOOO00 ==None :#line:4238
            return #line:4239
        O0OO0O0OO0O0OO000 .__OO0OO0O00O0OOOO00 (O0O00OOOO00O00O0O ,OOOOO0OO0OOOO0000 )#line:4240
    def __OO0O0000O00OOOO00 (OO0OO0000O000OOO0 ,OO0OOOOOO000OOOOO :str ,O00000000O00OOOOO :bool ,O00O00O0OO0O0OO00 :TObjFutQuoteMap ):#line:4242
        ""#line:4243
        if O00000000O00OOOOO ==False :#line:4245
            OO0OO0000O000OOO0 ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[期貨行情回補]{OO0OOOOOO000OOOOO}回補失敗!")#line:4246
            return #line:4247
        try :#line:4248
            for OO000OO0O00OOOO0O ,O0O0OO00O0O00O00O in O00O00O0OO0O0OO00 .items ():#line:4249
                OOOO0O00O0O0O0OO0 :TFutQuoteData =O0O0OO00O0O00O00O #line:4250
                O0OOOO0OOO0OOO000 =OOOO0O00O0O0O0OO0 .BAS .OrdProdID #line:4251
                if OO0OO0000O000OOO0 ._fPrdSnapshotMap .NewItemFut (O0OOOO0OOO0OOO000 ,OOOO0O00O0O0O0OO0 ):#line:4252
                    if OO0OO0000O000OOO0 .__O0O0O0O0OOO00OO0O ==False :#line:4253
                        OO000O0O0O0OOO000 :ProductSnapshot =OO0OO0000O000OOO0 ._fPrdSnapshotMap [O0OOOO0OOO0OOO000 ]#line:4254
                        OO0OO0000O000OOO0 .__OO0000OO0O0O000OO .Fire_OnUpdateBasic (OO000O0O0O0OOO000 .BasicData )#line:4255
                        OO0OO0000O000OOO0 .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (OO0OO0000O000OOO0 ._fPrdSnapshotMap [O0OOOO0OOO0OOO000 ])#line:4256
            if OO0OO0000O000OOO0 .__O0O0O0O0OOO00OO0O :#line:4257
                if len (OO0OO0000O000OOO0 ._fPrdSnapshotMap )>0 :#line:4258
                    O0O0000O0O000000O =list (OO0OO0000O000OOO0 ._fPrdSnapshotMap .values ())#line:4259
                    OO0OO0000O000OOO0 .__OO0000OO0O0O000OO .Fire_OnUpdateProductBasicList (O0O0000O0O000000O )#line:4260
        except Exception as OO0O0O0OO0O0O0O0O :#line:4261
            OO0OO0000O000OOO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteFutApi_OnQtRcvEvent]aMsg={OO0OOOOOO000OOOOO}, aIsOK={O00000000O00OOOOO}, ex:{OO0O0O0OO0O0O0O0O}")#line:4262
    def __O0O000O0OO0OOO0OO (OOO0O0OO00OOO000O ,O0000O0OO00OO000O :str ,O0OO00OO0000OO00O :TFutQtTX ):#line:4264
        ""#line:4265
        try :#line:4266
            OOO00O0OOOO00OO0O :ProductSnapshot =None #line:4267
            O0O0OO00O0000OO0O ,OOO00O0OOOO00OO0O =OOO0O0OO00OOO000O ._fPrdSnapshotMap .GetItem (O0000O0OO00OO000O )#line:4269
            if O0O0OO00O0000OO0O :#line:4270
                O00O0O0O0O0OOOO00 :ProductTick_Fut =OOO00O0OOOO00OO0O .TickData #line:4272
                if O00O0O0O0O0OOOO00 .Upt_TX (O0OO00OO0000OO00O ):#line:4274
                    OOO0O0OO00OOO000O .__OO0000OO0O0O000OO .Fire_OnMatch (OOO0O0OO00OOO000O ._fPrdSnapshotMap [O0000O0OO00OO000O ].TickData )#line:4275
                    OOO0O0OO00OOO000O .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (OOO0O0OO00OOO000O ._fPrdSnapshotMap [O0000O0OO00OO000O ])#line:4276
        except Exception as OOO0OO0O00OOO0OO0 :#line:4277
            OOO0O0OO00OOO000O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteFutApi_OnQtTXEvent]ProdID={O0000O0OO00OO000O}, ex:{OOO0OO0O00OOO0OO0}")#line:4278
    def __OOO0O0O000OO000OO (OOOOO000000OOOO00 ,O0O0OO00000OO00OO :str ,O00OOOOOO00O00OOO :TFutQt5Q ):#line:4280
        ""#line:4281
        try :#line:4282
            OO0O0OO0O00000O00 :ProductSnapshot =None #line:4283
            OO00O0OOO0O00OO0O ,OO0O0OO0O00000O00 =OOOOO000000OOOO00 ._fPrdSnapshotMap .GetItem (O0O0OO00000OO00OO )#line:4285
            if OO00O0OOO0O00OO0O :#line:4286
                OOO00000O00OOOO0O :ProductTick_Fut =OO0O0OO0O00000O00 .TickData #line:4287
                if OOO00000O00OOOO0O .Upt_5Q (O00OOOOOO00O00OOO ):#line:4289
                    OOOOO000000OOOO00 .__OO0000OO0O0O000OO .Fire_OnOrderBook (OOOOO000000OOOO00 ._fPrdSnapshotMap [O0O0OO00000OO00OO ].TickData )#line:4290
                    OOOOO000000OOOO00 .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (OOOOO000000OOOO00 ._fPrdSnapshotMap [O0O0OO00000OO00OO ])#line:4291
        except Exception as OO0OO0O00OOOO0OOO :#line:4292
         OOOOO000000OOOO00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteFutApi_OnQt5QEvent]ProdID={O0O0OO00000OO00OO}, ex:{OO0OO0O00OOOO0OOO}")#line:4293
    def __OOOO00O0O00O0O000 (O00OO00OOOO00O000 ,O0000OOOOO0O0000O :str ,O00O00OOO000000O0 :TFutQt5QTOT ):#line:4295
        ""#line:4296
        try :#line:4297
            OO0O00OO000OOO0OO :ProductSnapshot =None #line:4298
            OOO00OO00O00O0O0O ,OO0O00OO000OOO0OO =O00OO00OOOO00O000 ._fPrdSnapshotMap .GetItem (O0000OOOOO0O0000O )#line:4300
            if OOO00OO00O00O0O0O :#line:4301
                O0OOO000O00OOOOO0 :ProductTick_Fut =OO0O00OO000OOO0OO .TickData #line:4302
                if O0OOO000O00OOOOO0 .Upt_5QTOT (O00O00OOO000000O0 ):#line:4304
                    O00OO00OOOO00O000 .__OO0000OO0O0O000OO .Fire_OnUpdateTotalOrderQty (O00OO00OOOO00O000 ._fPrdSnapshotMap [O0000OOOOO0O0000O ].TickData )#line:4305
                    O00OO00OOOO00O000 .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (O00OO00OOOO00O000 ._fPrdSnapshotMap [O0000OOOOO0O0000O ])#line:4306
        except Exception as O0O0OOO00OO0O00OO :#line:4307
            O00OO00OOOO00O000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteFutApi_OnQt5QTOTEvent]ProdID={O0000OOOOO0O0000O}, ex:{O0O0OOO00OO0O00OO}")#line:4308
    def __O0000000000000O0O (OOOO000OOO00OO0OO ,OOOOOO000O0O000OO :str ,OOO00000OO00O00O0 :TFutQtIDX ):#line:4309
        try :#line:4310
            pass #line:4311
        except Exception as OO0OO0O00OOO0O00O :#line:4317
            OOOO000OOO00OO0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteFutApi_OnQtIDXEvent]ProdID={OOOOOO000O0O000OO}, ex:{OO0OO0O00OOO0O00O}")#line:4318
    def __O0OOO0O0OO0O0OOOO (O0O000O000000O000 ,O0OO0O00OO00OOO0O :str ,OO00O0000OOO000O0 :TFutQtBase ):#line:4319
        ""#line:4320
        try :#line:4321
            pass #line:4322
        except Exception as OOOOOOOO00000O0OO :#line:4339
            pass #line:4340
    def __O0O0O0O00O00OOOO0 (OOO00OOOO0OO00000 ,O0OO000O0O0OO0O00 :ITQtRcvEventData ):#line:4342
        if O0OO000O0O0OO0O00 ==None :#line:4343
            OOO00OOOO0OO00000 ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[海期行情回補] 回補失敗!")#line:4344
            return #line:4345
        if O0OO000O0O0OO0O00 .IsOK ==False :#line:4346
            OOO00OOOO0OO00000 ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[海期行情回補]{O0OO000O0O0OO0O00.SolIce}回補失敗!")#line:4347
            return #line:4348
        try :#line:4349
            if OOO00OOOO0OO00000 ._fPrdOvsMap .NewItem (O0OO000O0O0OO0O00 .QtMap ):#line:4350
                OOO00OOOO0OO00000 .__OO0000OO0O0O000OO .Fire_OnUpdateOvsBasic (O0OO000O0O0OO0O00 .QtMap )#line:4351
        except Exception as O00000OOOOO0000O0 :#line:4353
            OOO00OOOO0OO00000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteOvsFutAPI_OnQtRcvEvent]aSolIce={O0OO000O0O0OO0O00.SolIce}, aIsOK={O0OO000O0O0OO0O00.IsOK}, ex:{O00000OOOOO0000O0}")#line:4354
    def __OOOOO0O0O00OOO000 (O000000OO0O0O0000 ,OO00000OOOOOOO0O0 :str ,O0OOO000O00000OO0 :TOvsFutQtTX ):#line:4355
        try :#line:4356
            OOOO0O00OOOOO00O0 :TOvsFutQuoteData =None #line:4357
            O00OOOO0OO0O0OOO0 ,OOOO0O00OOOOO00O0 =O000000OO0O0O0000 ._fPrdOvsMap .GetItem (OO00000OOOOOOO0O0 )#line:4359
            if O00OOOO0OO0O0OOO0 :#line:4360
                OOOO0O00OOOOO00O0 .QtTX =O0OOO000O00000OO0 #line:4361
                O000000OO0O0O0000 .__OO0000OO0O0O000OO .Fire_OnUpdateOvsMatch (OOOO0O00OOOOO00O0 )#line:4362
        except Exception as OO0OO0O0000O0000O :#line:4363
            O000000OO0O0O0000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteOvsFutAPI_OnQtTXEvent]ProdID={OO00000OOOOOOO0O0}, ex:{OO0OO0O0000O0000O}")#line:4364
    def __O0O0OOO0OO0OO000O (O0OO0OOOO0OO0O000 ,O0OO0000O0OO0O000 :str ,OO00OO0O00OO0O0OO :TOvsFutQt5Q ):#line:4365
        try :#line:4366
            OOOO00000OO00O00O :TOvsFutQuoteData =None #line:4367
            OO0000OOOO0OO0OO0 ,OOOO00000OO00O00O =O0OO0OOOO0OO0O000 ._fPrdOvsMap .GetItem (O0OO0000O0OO0O000 )#line:4369
            if OO0000OOOO0OO0OO0 :#line:4370
                OOOO00000OO00O00O .Qt5Q =OO00OO0O00OO0O0OO #line:4371
                O0OO0OOOO0OO0O000 .__OO0000OO0O0O000OO .Fire_OnUpdateOvsOrderBook (OOOO00000OO00O00O )#line:4372
        except Exception as O0O0000O00O00O00O :#line:4373
            O0OO0OOOO0OO0O000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteStkAPI_OnQt5QEvent]ProdID={O0OO0000O0OO0O000}, ex:{O0O0000O00O00O00O}")#line:4374
    __O0OO0OO000O0O0O00 :callable =None #line:4378
    def Set_OnQtTXEventFUT (O0000O00000OOO0O0 ,O0000OOOO0000O0O0 :callable ):#line:4380
        O0000O00000OOO0O0 .__O0OO0OO000O0O0O00 =O0000OOOO0000O0O0 #line:4381
    def __OOO000OO000O0OO00 (OOOOOO0O0OO0O0O00 ,OOOO0OOO000O00O0O :str ,OOOOO000OO000O00O :TFutQtTX ):#line:4383
        if OOOOOO0O0OO0O0O00 .__O0OO0OO000O0O0O00 ==None :#line:4384
            return #line:4385
        OOOOOO0O0OO0O0O00 .__O0OO0OO000O0O0O00 (OOOO0OOO000O00O0O ,OOOOO000OO000O00O )#line:4387
    __OO0O00O000O00OOOO :callable =None #line:4390
    def Set_OnQtTXEventOvsFUT (OO0O00000000O00O0 ,O00OOOO00OOO0OOOO :callable ):#line:4392
        OO0O00000000O00O0 .__OO0O00O000O00OOOO =O00OOOO00OOO0OOOO #line:4393
    def __O0OOO0O0O0O0OO0O0 (O00O0000OO00000O0 ,O0O0OOO00000O0OO0 :str ,O00OO0OO00OOOOOOO :TOvsFutQtTX ):#line:4395
        if O00O0000OO00000O0 .__OO0O00O000O00OOOO ==None :#line:4396
            return #line:4397
        O00O0000OO00000O0 .__OO0O00O000O00OOOO (O0O0OOO00000O0OO0 ,O00OO0OO00OOOOOOO )#line:4398
    __OOO0O00OO0O0O00O0 :callable =None #line:4402
    """Qt5QEventHandler"""#line:4403
    def Set_OnQt5QEventSTK (O000OOO000OO0O00O ,OOO000OOO000OOO00 :callable ):#line:4405
        O000OOO000OO0O00O .__OOO0O00OO0O0O00O0 =OOO000OOO000OOO00 #line:4406
    def __O0O0000OO0O000000 (O0OOO00O0OOO0O00O ,O00OO00OOO0O0O000 :str ,O0O0O0O000O0OO00O :TStkQt5Q ):#line:4408
        if O0OOO00O0OOO0O00O .__OOO0O00OO0O0O00O0 ==None :#line:4409
            return #line:4410
        O0OOO00O0OOO0O00O .__OOO0O00OO0O0O00O0 (O00OO00OOO0O0O000 ,O0O0O0O000O0OO00O )#line:4411
    __OO0O0OO000OO000O0 :callable =None #line:4414
    def Set_OnQt5QEventFUT (OOOO0OOO000O000O0 ,OOOOOO0O0OO00O0O0 :callable ):#line:4416
        OOOO0OOO000O000O0 .__OO0O0OO000OO000O0 =OOOOOO0O0OO00O0O0 #line:4417
    def __O0O0O00O00000OOO0 (O00O0OO0OOOO000OO ,OOOOO000OO0000000 :str ,O00000OOOOO0O0O00 :TFutQt5Q ):#line:4419
        if O00O0OO0OOOO000OO .__OO0O0OO000OO000O0 ==None :#line:4420
            return #line:4421
        O00O0OO0OOOO000OO .__OO0O0OO000OO000O0 (OOOOO000OO0000000 ,O00000OOOOO0O0O00 )#line:4423
    __OOOOOOOO000OOO000 :callable =None #line:4426
    def Set_OnQt5QEventOvsFUT (O00O0O00O0O0O0O0O ,OO0O0OO0OOO000OO0 :callable ):#line:4428
        O00O0O00O0O0O0O0O .__OOOOOOOO000OOO000 =OO0O0OO0OOO000OO0 #line:4429
    def __O00O000O00000000O (OO0OO0000O0OOOO0O ,O00OO0OO0000000OO :str ,O00OOOOO0O0O0000O :TOvsFutQt5Q ):#line:4431
        if OO0OO0000O0OOOO0O .__OOOOOOOO000OOO000 ==None :#line:4432
            return #line:4433
        OO0OO0000O0OOOO0O .__OOOOOOOO000OOO000 (OO0OO0000O0OOOO0O ,O00OO0OO0000000OO ,O00OOOOO0O0O0000O )#line:4434
    __O00OO0OO0OOO0O0OO :callable =None #line:4437
    def Set_OnQt5QTOTEventFUT (O00OO000O00OO00O0 ,O00O00OO00O0O0O0O :callable ):#line:4439
        O00OO000O00OO00O0 .__O00OO0OO0OOO0O0OO =O00O00OO00O0O0O0O #line:4440
    def __O0O0O00O0OOOO0O00 (O0O0O0O0OOO00000O ,OO0000O0OO0OO0O00 :str ,O00O0OO00OO0O00OO :TFutQt5QTOT ):#line:4442
        if O0O0O0O0OOO00000O .__O00OO0OO0OOO0O0OO ==None :#line:4443
            return #line:4444
        O0O0O0O0OOO00000O .__O00OO0OO0OOO0O0OO (OO0000O0OO0OO0O00 ,O00O0OO00OO0O00OO )#line:4445
    __OO00OO00O00O0O0O0 :callable =None #line:4448
    def Set_OnChangeMktStuEventFUT (O0OOO00OOOOO0O00O ,O00OO0000OO00OO0O :callable ):#line:4450
        O0OOO00OOOOO0O00O .__OO00OO00O00O0O0O0 =O00OO0000OO00OO0O #line:4451
    def __OOOO0O0OO0OOOO000 (OOO00O00000OOO0O0 ,OOO000O0000000OOO :str ,OO00OOO0OO0O000OO :TFutQtBase ):#line:4453
        if OOO00O00000OOO0O0 .__OO00OO00O00O0O0O0 ==None :#line:4454
            return #line:4455
        OOO00O00000OOO0O0 .__OO00OO00O00O0O0O0 (OOO000O0000000OOO ,OO00OOO0OO0O000OO )#line:4456
    __O0O0OO0000O00OO00 :callable =None #line:4459
    def Set_OnQtIDXEventSTK (OO00O0O0OOO0000OO ,OO000OOO0000O0O0O :callable ):#line:4461
        OO00O0O0OOO0000OO .__O0O0OO0000O00OO00 =OO000OOO0000O0O0O #line:4462
    def __O00O0OO00O00O0OO0 (OOO00O0O00OO000O0 ,OOO0O00O0000OO00O :str ,OOO0000OOO00O0O00 :TStkQtIDX ):#line:4464
        if OOO00O0O00OO000O0 .__O0O0OO0000O00OO00 ==None :#line:4465
            return #line:4466
        OOO00O0O00OO000O0 .__O0O0OO0000O00OO00 (OOO0O00O0000OO00O ,OOO0000OOO00O0O00 )#line:4467
    __O00OO000O0000OOO0 :callable =None #line:4468
    def Set_OnQtIDXEventFUT (O000OO0000000O00O ,OO000OOOOO0O0O0OO :callable ):#line:4470
        O000OO0000000O00O .__O00OO000O0000OOO0 =OO000OOOOO0O0O0OO #line:4471
    def __O000O000O00O000OO (OO0O00OOOOOOOO000 ,OOOO000OOOO0O00O0 :str ,O0O0000OOO00O000O :TFutQtIDX ):#line:4473
        if OO0O00OOOOOOOO000 .__O00OO000O0000OOO0 ==None :#line:4474
            return #line:4475
        OO0O00OOOOOOOO000 .__O00OO000O0000OOO0 (OOOO000OOOO0O00O0 ,O0O0000OOO00O000O )#line:4476
    __O000OOO000O00O00O :callable =None #line:4479
    """OtherMessageEventHandler"""#line:4480
    def Set_OnOtherMessageEvent (OO0OOO00OOOOOOOOO ,OOO000000O00O0O0O :callable ):#line:4482
        OO0OOO00OOOOOOOOO .__O000OOO000O00O00O =OOO000000O00O0O0O #line:4483
    def __OOOO0O000O0000O00 (O00OO0O00O0OOOO00 ,OOOOO0OO00O0OO00O :str ):#line:4485
        if O00OO0O00O0OOOO00 .__O000OOO000O00O00O ==None :#line:4486
            return #line:4487
        O00OO0O00O0OOOO00 .__O000OOO000O00O00O (OOOOO0OO00O0OO00O )#line:4488
    __OO0OOOOOO0O00O000 :callable =None #line:4491
    """LogEventHandler"""#line:4492
    def Set_OnLogEvent (O000OO0O000OO00O0 ,OO0OO0OO0OOO0O00O :callable ):#line:4494
        O000OO0O000OO00O0 .__OO0OOOOOO0O00O000 =OO0OO0OO0OOO0O00O #line:4495
    def __O0O000OO000000O0O (OOOO0OO00O0OOO0OO ,O0000OOOO000OO00O :str ):#line:4497
        if OOOO0OO00O0OOO0OO .__OO0OOOOOO0O00O000 ==None :#line:4498
            return #line:4499
        OOOO0OO00O0OOO0OO .__OO0OOOOOO0O00O000 (O0000OOOO000OO00O )#line:4500
    def __OO000O0O0O00OO0OO (OOOO00O00O0OO0O00 ,OO0O0OOO00O0O0O00 :TSolClientConnData )->RCode :#line:4504
        try :#line:4505
            if OOOO00O00O0OO0O00 ._is_connected :#line:4506
                return RCode .OK #line:4507
            if OOOO00O00O0OO0O00 ._log ._run ==False :#line:4508
                OOOO00O00O0OO0O00 ._log =SolaceLog (OOOO00O00O0OO0O00 ._pypath ,OOOO00O00O0OO0O00 ._loglv ,OOOO00O00O0OO0O00 ._conlve )#line:4509
            OOOO00O00O0OO0O00 ._log .Add (arg1 =SolLogType .Info ,arg2 ="DoSolaceConn")#line:4510
            OOOO00O00O0OO0O00 .__O0OO0O0O000000OO0 ()#line:4511
            OOOO00O00O0OO0O00 ._log .Add (arg1 =SolLogType .Debug ,arg2 =f"host:{OO0O0OOO00O0O0O00.Host} vpn:{OO0O0OOO00O0O0O00.MessageVPN} username:{OO0O0OOO00O0O0O00.Username} pwd:{OO0O0OOO00O0O0O00.Password} cmplv:{OO0O0OOO00O0O0O00.CompressLevel}")#line:4512
            O0O000OO00O0000O0 :dict ={}#line:4513
            O0O000OO00O0000O0 ["solace.messaging.transport.host"]=OO0O0OOO00O0O0O00 .Host #line:4514
            O0O000OO00O0000O0 ["solace.messaging.service.vpn-name"]=OO0O0OOO00O0O0O00 .MessageVPN #line:4515
            O0O000OO00O0000O0 ["solace.messaging.authentication.basic.username"]=OO0O0OOO00O0O0O00 .Username #line:4516
            O0O000OO00O0000O0 ["solace.messaging.authentication.basic.password"]=OO0O0OOO00O0O0O00 .Password #line:4517
            O0O000OO00O0000O0 ["solace.messaging.transport.compression-level"]=OO0O0OOO00O0O0O00 .CompressLevel #line:4518
            O0O000OO00O0000O0 ['solace.messaging.transport.connection-retries']=3 #line:4520
            O0O000OO00O0000O0 ['solace.messaging.transport.connection.retries-per-host']=4 #line:4521
            O0O000OO00O0000O0 ['solace.messaging.transport.connection-attempts-timeout']=30000 #line:4522
            O0O000OO00O0000O0 ['solace.messaging.transport.reconnection-attempts']=10 #line:4524
            O0O000OO00O0000O0 ['solace.messaging.transport.reconnection-attempts-wait-interval']=1000 #line:4525
            OOOO00O00O0OO0O00 ._message_service =MessagingService .builder ().from_properties (O0O000OO00O0000O0 ).build ()#line:4528
            OOOO00O00O0OO0O00 ._message_service .connect ()#line:4529
            OOOO00O00O0OO0O00 ._message_receiver =OOOO00O00O0OO0O00 ._message_service .create_direct_message_receiver_builder ().build ()#line:4531
            OOOO00O00O0OO0O00 ._message_receiver .start ()#line:4532
            OOOO00O00O0OO0O00 ._message_receiver .receive_async (OOOO00O00O0OO0O00 .__O0O000O0OO000OOO0 )#line:4535
            OOOO00O00O0OO0O00 ._direct_publish_service =OOOO00O00O0OO0O00 ._message_service .create_direct_message_publisher_builder ().build ()#line:4537
            OOOO00O00O0OO0O00 ._message_requester =OOOO00O00O0OO0O00 ._message_service .request_reply ().create_request_reply_message_publisher_builder ().build ().start ()#line:4539
            OOOO00O00O0OO0O00 ._is_connected =OOOO00O00O0OO0O00 ._message_service .is_connected #line:4540
            if OOOO00O00O0OO0O00 ._is_connected :#line:4542
                return RCode .OK #line:4543
            else :#line:4544
                return RCode .FAIL #line:4545
        except Exception as O0000O00OO0O0O0OO :#line:4546
            OOOO00O00O0OO0O00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSolaceConn error: {O0000O00OO0O0O0OO}")#line:4548
            return RCode .FAIL #line:4549
    def Connect (O0000OOOOO0O0O0O0 ,O0O0O000O000O0O00 :str ,O0O0000000OOOOO00 :str ,OOOOO00O0O0000000 :str ,OOOOO0O0000000O0O :str ,aCompressLevel :int =0 ):#line:4551
        OOOO00OOO00OOO000 :TSolClientConnData =TSolClientConnData ()#line:4552
        OOOO00OOO00OOO000 .Host =O0O0O000O000O0O00 #line:4553
        OOOO00OOO00OOO000 .MessageVPN =O0O0000000OOOOO00 #line:4554
        OOOO00OOO00OOO000 .Username =OOOOO00O0O0000000 #line:4555
        OOOO00OOO00OOO000 .Password =OOOOO0O0000000O0O #line:4556
        OOOO00OOO00OOO000 .CompressLevel =aCompressLevel #line:4557
        return O0000OOOOO0O0O0O0 .__OO000O0O0O00OO0OO (OOOO00OOO00OOO000 )#line:4559
    def DisConnect (O000000OOO0OO0O0O )->RCode :#line:4561
        if O000000OOO0OO0O0O ._is_connected :#line:4563
            O00OO00OO0O00O000 =time .time ()#line:4564
            while (True ):#line:4565
                if O000000OOO0OO0O0O .__OOO000OO00O00OOO0 ._queue .empty ()and O000000OOO0OO0O0O .__OO000O0OOOOO0OOO0 ._queue .empty ():#line:4566
                    sleep (2 )#line:4567
                    with O000000OOO0OO0O0O ._lock :#line:4568
                        if hasattr (O000000OOO0OO0O0O ,'_message_service')and O000000OOO0OO0O0O ._is_connected :#line:4569
                            O000000OOO0OO0O0O ._message_receiver .terminate ()#line:4570
                            O000000OOO0OO0O0O ._message_requester .terminate ()#line:4571
                            O000000OOO0OO0O0O ._message_service .disconnect ()#line:4572
                        O000000OOO0OO0O0O ._is_connected =False #line:4573
                    break #line:4574
                O0OO0OOOO0OOOOOOO =time .time ()#line:4575
                O000OO000OO00O00O =O0OO0OOOO0OOOOOOO -O00OO00OO0O00O000 #line:4576
                if O000OO000OO00O00O >20 :#line:4577
                    with O000000OOO0OO0O0O ._lock :#line:4578
                        if hasattr (O000000OOO0OO0O0O ,'_message_service')and O000000OOO0OO0O0O ._is_connected :#line:4579
                            O000000OOO0OO0O0O ._message_receiver .terminate ()#line:4580
                            O000000OOO0OO0O0O ._message_requester .terminate ()#line:4581
                            O000000OOO0OO0O0O ._message_service .disconnect ()#line:4582
                        O000000OOO0OO0O0O ._is_connected =False #line:4583
                    break #line:4584
            O000000OOO0OO0O0O .__O0O0OO0OOO00O0O0O ()#line:4586
        if O000000OOO0OO0O0O ._log ._run :#line:4587
            O000000OOO0OO0O0O ._log .Wrtie_log (SolLogType .Info ,"DisConnect")#line:4588
            O000000OOO0OO0O0O ._log ._run =False #line:4589
        return RCode .OK #line:4590
    _vRealTime =-1 #line:4594
    def __O0OO00OOOO000O0O0 (O0O00OOO0OOO0O0O0 ,OO0O000000OO00O00 :'InboundMessage'):#line:4596
        ""#line:4597
        OO0OOO0OOOO00000O :str =""#line:4598
        try :#line:4599
            OO0OOO0OOOO00000O =OO0O000000OO00O00 .get_payload_as_bytes ().decode ('utf-8')#line:4601
            if len (OO0OOO0OOOO00000O )==0 :#line:4602
                return #line:4603
            OO0OO0O000OOO0O0O =OO0O000000OO00O00 .get_destination_name ()#line:4604
            if OO0OO0O000OOO0O0O .startswith (O0O00OOO0OOO0O0O0 ._vQuote_STK ):#line:4606
                OO0OOOOOO00000OO0 =O0O00OOO0OOO0O0O0 ._fMapQuoteSTK .get (OO0OO0O000OOO0O0O )#line:4607
                O0O00OOO0OOO0O0O0 ._fMapQuoteSTK .MapQtProc [OO0OO0O000OOO0O0O ](OO0OOOOOO00000OO0 ,OO0OOO0OOOO00000O ,OO0O000000OO00O00 )#line:4608
            elif OO0OO0O000OOO0O0O .startswith (O0O00OOO0OOO0O0O0 ._vQuote_FUT ):#line:4609
                OO0OOOOOO00000OO0 =O0O00OOO0OOO0O0O0 ._fMapQuoteFUT .get (OO0OO0O000OOO0O0O )#line:4610
                O0O00OOO0OOO0O0O0 ._fMapQuoteFUT .MapQtProc [OO0OO0O000OOO0O0O ](OO0OOOOOO00000OO0 ,OO0OOO0OOOO00000O ,OO0O000000OO00O00 )#line:4611
            elif OO0OO0O000OOO0O0O .startswith (O0O00OOO0OOO0O0O0 ._vQuote_OvsFUT ):#line:4612
                OO0OOOOOO00000OO0 =O0O00OOO0OOO0O0O0 ._fMapQuoteOvsFUT .get (OO0OO0O000OOO0O0O )#line:4613
                O0O00OOO0OOO0O0O0 ._fMapQuoteOvsFUT .MapQtProc [OO0OO0O000OOO0O0O ](OO0OOOOOO00000OO0 ,OO0OOO0OOOO00000O ,OO0O000000OO00O00 )#line:4614
        except Exception as OO000OO000O0OO0OO :#line:4615
            O0O00OOO0OOO0O0O0 .__O0O000OO000000O0O (f"[證][Solace_ReceiveSolaceTopic]aTopic={OO0O000000OO00O00.get_destination_name()}, aData={OO0OOO0OOOO00000O}, except={OO000OO000O0OO0OO}")#line:4617
            O0O00OOO0OOO0O0O0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[證][Solace_ReceiveSolaceTopic]aTopic={OO0O000000OO00O00.get_destination_name()}, aData={OO0OOO0OOOO00000O}, except={OO000OO000O0OO0OO}")#line:4619
    def __OOOO0O0OO0O0OOO0O (O0OO0OO00O0OO000O ,O0O00OOOOOO000OO0 :TStkQuoteData ,O0O0OO0000000O0OO :str ,O0O0OOOO0O0O0OO00 :'InboundMessage'):#line:4628
        ""#line:4629
        try :#line:4631
            with O0O00OOOOOO000OO0 ._lock :#line:4632
                O0O00OOOOOO000OO0 .QtTX .Handle_TX (O0O0OO0000000O0OO )#line:4634
            O0OO0OO00O0OO000O .__O0000OO0O00OO0O00 (O0O00OOOOOO000OO0 .SolIce ,O0O00OOOOOO000OO0 .QtTX )#line:4637
        except Exception as O00O00OOO0O0OO0OO :#line:4638
            O0OO0OO00O0OO000O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_TXSTK:{O00O00OOO0O0OO0OO}")#line:4640
    def __O000OOOO0000OO00O (O000OOOO0OO000OOO ,O0O0000000O0OOOO0 :TFutQuoteData ,OO0O0OOO00O0OOO0O :str ,O0O0O00OOO00OOO0O :'InboundMessage'):#line:4642
        ""#line:4643
        try :#line:4644
            with O0O0000000O0OOOO0 ._lock :#line:4645
                O0O0000000O0OOOO0 .QtTX .Handle_TX (OO0O0OOO00O0OOO0O )#line:4647
            O000OOOO0OO000OOO .__OOO000OO000O0OO00 (O0O0000000O0OOOO0 .SolIce ,O0O0000000O0OOOO0 .QtTX )#line:4650
        except Exception as OOO00O0O0O0OOOO00 :#line:4651
            O000OOOO0OO000OOO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_TXFUT:{OOO00O0O0O0OOOO00}")#line:4653
    def __O00000OOO0O0OO0O0 (O00000O00OO0OO000 ,O0O0O0OOO000O000O :TOvsFutQuoteData ,O000OOO000OOOOO0O :str ,OOOOO00O0O0OO0000 :'InboundMessage'):#line:4655
        ""#line:4656
        try :#line:4657
            with O0O0O0OOO000O000O ._lock :#line:4658
                O0O0O0OOO000O000O .QtTX .Handle_TX (O000OOO000OOOOO0O )#line:4659
            O00000O00OO0OO000 .__O0OOO0O0O0O0OO0O0 (O0O0O0OOO000O000O .SolIce ,O0O0O0OOO000O000O .QtTX )#line:4661
        except Exception as O0OOOOO0000OOOOO0 :#line:4662
            O00000O00OO0OO000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_TXOvsFUT:{O0OOOOO0000OOOOO0}")#line:4664
    def __O000O0000O0000000 (OOOOOOOOOO0O0OO0O ,OO0O0OO0O000OOOOO :TStkQuoteData ,O00OO0OO0O00O000O :str ,OOOO00OOOO000O0O0 :'InboundMessage'):#line:4666
        ""#line:4667
        try :#line:4668
            with OO0O0OO0O000OOOOO ._lock :#line:4669
                OO0O0OO0O000OOOOO .Qt5Q .Handle_5Q (O00OO0OO0O00O000O )#line:4670
            OOOOOOOOOO0O0OO0O .__O0O0000OO0O000000 (OO0O0OO0O000OOOOO .SolIce ,OO0O0OO0O000OOOOO .Qt5Q )#line:4671
        except Exception as OOO00OOO0O0O00O00 :#line:4672
            OOOOOOOOOO0O0OO0O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_5QSTK:{OOO00OOO0O0O00O00}")#line:4674
    def __OO0O000O00OOOO000 (O00OOO000OOO0OOOO ,O0O000OOO0OO00OO0 :TFutQuoteData ,O0OO0000O000OO00O :str ,OO0OOOOOO0O0OO000 :'InboundMessage'):#line:4676
        ""#line:4677
        try :#line:4678
            with O0O000OOO0OO00OO0 ._lock :#line:4679
                O0O000OOO0OO00OO0 .Qt5Q .Handle_5Q (O0OO0000O000OO00O )#line:4680
            O00OOO000OOO0OOOO .__O0O0O00O00000OOO0 (O0O000OOO0OO00OO0 .SolIce ,O0O000OOO0OO00OO0 .Qt5Q )#line:4681
        except Exception as O00O000OO0O000O00 :#line:4682
            O00OOO000OOO0OOOO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_5QFUT:{O00O000OO0O000O00}")#line:4684
    def __O000000O0O0O000O0 (OO0OOO00O000OO0OO ,OOO0OO0O000000OO0 :TOvsFutQuoteData ,O00OOO0O0OOOO00O0 :str ,O0O0OO0O0000O00O0 :'InboundMessage'):#line:4686
        try :#line:4687
            with OOO0OO0O000000OO0 ._lock :#line:4688
                OOO0OO0O000000OO0 .Qt5Q .Handle_5Q (O00OOO0O0OOOO00O0 )#line:4689
            OO0OOO00O000OO0OO .__O00O000O00000000O (OOO0OO0O000000OO0 .SolIce ,OOO0OO0O000000OO0 .Qt5Q )#line:4690
        except Exception as O000OO00O0OO0OOO0 :#line:4691
            OO0OOO00O000OO0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_5QOvsFUT:{O000OO00O0OO0OOO0}")#line:4693
    def __OOO000O00O0O00O0O (O0OOOOO0OO0000OO0 ,OO0OO0OO0OOOOO0O0 :TStkQuoteData ,OO0OO000O0O0OOOOO :str ,O0O000O0O0O00OOOO :'InboundMessage'):#line:4695
        ""#line:4696
        try :#line:4697
            with OO0OO0OO0OOOOO0O0 ._lock :#line:4698
                OO0OO0OO0OOOOO0O0 .QtIDX .Handle_IDX (OO0OO000O0O0OOOOO )#line:4700
            O0OOOOO0OO0000OO0 .__O00O0OO00O00O0OO0 (OO0OO0OO0OOOOO0O0 .SolIce ,OO0OO0OO0OOOOO0O0 .QtIDX )#line:4703
        except Exception as O000O00O0O000OOO0 :#line:4704
            O0OOOOO0OO0000OO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_IDXSTK:{O000O00O0O000OOO0}")#line:4706
    def __OOOOOOOOOO0O000O0 (OO0OOO00OO0O00O0O ,OO0OO0OOOO0OOO0O0 :TFutQuoteData ,OOOO0O0O0O0OOOO0O :str ,O0O0OO00O000O000O :'InboundMessage'):#line:4708
        ""#line:4709
        try :#line:4710
            with OO0OO0OOOO0OOO0O0 ._lock :#line:4711
                OO0OO0OOOO0OOO0O0 .QtIDX .Handle_IDX (OOOO0O0O0O0OOOO0O )#line:4712
            OO0OOO00OO0O00O0O .__O000O000O00O000OO (OO0OO0OOOO0OOO0O0 .SolIce ,OO0OO0OOOO0OOO0O0 .QtIDX )#line:4713
        except Exception as O0000000O0O00OO00 :#line:4714
            OO0OOO00OO0O00O0O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_IDXFUT:{O0000000O0O00OO00}")#line:4716
    def __O000O0O000OO00O0O (OOO00OOO00O0O00OO ,O00OOOOOOO0O00O00 :TFutQuoteData ,O0O000OO000O0000O :str ,O0OO00OOOO00O0OO0 :'InboundMessage'):#line:4718
        ""#line:4719
        try :#line:4720
            with O00OOOOOOO0O00O00 ._lock :#line:4721
                O00OOOOOOO0O00O00 .Qt5QTOT .Handle_5QTOT (O0O000OO000O0000O )#line:4722
            OOO00OOO00O0O00OO .__O0O0O00O0OOOO0O00 (O00OOOOOOO0O00O00 .SolIce ,O00OOOOOOO0O00O00 .Qt5QTOT )#line:4723
        except Exception as OO000O000O0O0O0O0 :#line:4724
            OOO00OOO00O0O00OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_5QTOT:{OO000O000O0O0O0O0}")#line:4726
    def __O00000OO0O000OOOO (OO00OO0O0OO00OOO0 ,O000OO00OO00O00OO :TFutQuoteData ,OO0OOOOO000O0O0OO :str ,O00OOOO00O0OOO0OO :'InboundMessage'):#line:4728
        ""#line:4729
        try :#line:4730
            O0OOOOOO0OOOO00O0 :bool =False #line:4731
            with O000OO00OO00O00OO ._lock :#line:4732
                O0OOOOOO0OOOO00O0 =O000OO00OO00O00OO .BAS .Handle_BAS_ChangeMktType (OO0OOOOO000O0O0OO )#line:4733
            if O0OOOOOO0OOOO00O0 :#line:4734
                OO00OO0O0OO00OOO0 .__OOOO0O0OO0OOOO000 (O000OO00OO00O00OO .SolIce ,O000OO00OO00O00OO .BAS )#line:4735
        except Exception as OOOOOOO0OOOOOOOO0 :#line:4736
            OO00OO0O0OO00OOO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"Handle_RTQuote_BAS:{OOOOOOO0OOOOOOOO0}")#line:4738
    def __O0O0OO0OO000000OO (O000O0O0O0O000O00 ,O0O0O0O0OO00O0OOO :str ,O0000000O000000OO :bool ):#line:4742
        ""#line:4743
        try :#line:4744
            O00000000O0O00000 =f"Quote/TWS/*/*/{O0O0O0O0OO00O0OOO}/RECOVER"#line:4745
            O0OO000OOO00O000O ,O0OOO0O0OO000OO00 =O000O0O0O0O000O00 .__O00O0O0000000O00O (O000O0O0O0O000O00 ._vRcvTopic_Stk ,O00000000O0O00000 ,'utf-8',O000O0O0O0O000O00 ._vRcvTopic_Stk_Req )#line:4747
            if O0OO000OOO00O000O :#line:4749
                OOOO000OO00OOOOO0 =json .loads (O0OOO0O0OO000OO00 )#line:4750
                if "status"in OOOO000OO00OOOOO0 and len (OOOO000OO00OOOOO0 ["status"])>0 :#line:4751
                    if OOOO000OO00OOOOO0 ["status"][0 ]=="error":#line:4752
                        O000O0O0O0O000O00 .__O0O000OO000000O0O (f"[證][DoSubQuoteSTK取個一般上市上櫃股票商品檔](aData={O0OOO0O0OO000OO00})行情回補資料有誤!")#line:4754
                        return RCode .FAIL #line:4755
                if "BAS"in OOOO000OO00OOOOO0 and len (OOOO000OO00OOOOO0 ["BAS"])==0 :#line:4756
                    O000O0O0O0O000O00 .__O0O000OO000000O0O (f"[證][DoSubQuoteSTK取個一般上市上櫃股票商品檔](aData={O0OOO0O0OO000OO00})沒有BAS資料!")#line:4758
                    return RCode .FAIL #line:4759
                if "HL"in OOOO000OO00OOOOO0 and len (OOOO000OO00OOOOO0 ["HL"])==0 :#line:4760
                    O000O0O0O0O000O00 .__O0O000OO000000O0O (f"[證][DoSubQuoteSTK取個一般上市上櫃股票商品檔](aData={O0OOO0O0OO000OO00})沒有HL資料!")#line:4762
                    return RCode .FAIL #line:4763
            if O0OO000OOO00O000O and O0OOO0O0OO000OO00 !="":#line:4765
                O00000O000O0O0OO0 =OOOO000OO00OOOOO0 ["HL"][0 ].split ('|')[0 ]#line:4766
                if O00000O000O0O0OO0 ==O000O0O0O0O000O00 .__O0O0O000O0000O0O0 :#line:4767
                    OOO0O00OO00OOOOOO =O000O0O0O0O000O00 .__OO000OO0O0O0O00O0 (False ,O0O0O0O0OO00O0OOO ,O0000000O000000OO ,OOOO000OO00OOOOO0 )#line:4768
                else :#line:4769
                    OOO0O00OO00OOOOOO =O000O0O0O0O000O00 .__OOOOO0OOO00O0O00O (False ,O0O0O0O0OO00O0OOO ,O0000000O000000OO ,OOOO000OO00OOOOO0 )#line:4770
                return OOO0O00OO00OOOOOO #line:4771
            else :#line:4772
                return RCode .FAIL #line:4773
        except Exception as O000OO0OOO00OO0O0 :#line:4774
            O000O0O0O0O000O00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubQuoteSTK:{O000OO0OOO00OO0O0}")#line:4775
            O000O0O0O0O000O00 .__O0O000OO000000O0O (f"[證][DoSubQuoteSTK]{O0O0O0O0OO00O0OOO}新增紀錄失敗!({O000OO0OOO00OO0O0})")#line:4776
            OOOOOO0OOOOO0O0O0 =threading .Thread (target =O000O0O0O0O000O00 .__O00O00O000O00O000 ,args =(STKxFUT .STK ,O0O0O0O0OO00O0OOO ))#line:4778
            OOOOOO0OOOOO0O0O0 .start ()#line:4779
            return RCode .FAIL #line:4780
    def __O00OO0000O0OOO00O (O00O0O0O0OOO0OO00 ,OOO000O00O0O0O0O0 :str ,O000000OOOOOO000O :bool ):#line:4782
        try :#line:4784
            OO0O0O00O0O00OO0O =f"Quote/TWS/{OOO000O00O0O0O0O0}/*/*/RECOVER"#line:4785
            OO00O0O0O0OOOOO0O ,O0000O0O00O0OO00O =O00O0O0O0OOO0OO00 .__O00O0O0000000O00O (O00O0O0O0OOO0OO00 ._vRcvTopic_Stk ,OO0O0O00O0O00OO0O ,'utf-8',O00O0O0O0OOO0OO00 ._vRcvTopic_Stk_Req )#line:4786
            if OO00O0O0O0OOOOO0O and O0000O0O00O0OO00O !="":#line:4788
                O00O0OOOO0O00OO0O =json .loads (O0000O0O00O0OO00O )#line:4790
                if "status"in O00O0OOOO0O00OO0O and len (O00O0OOOO0O00OO0O ["status"])>0 :#line:4791
                    if O00O0OOOO0O00OO0O ["status"][0 ]=="error":#line:4792
                        O0OO00OOOO0OO0OO0 =f"[證][DoSubQuoteByCategory](aCat={OOO000O00O0O0O0O0}, sResData={O0000O0O00O0OO00O})行情回補資料有誤!"#line:4793
                        O00O0O0O0OOO0OO00 .__O0O000OO000000O0O (O0OO00OOOO0OO0OO0 )#line:4794
                        return False #line:4795
                if "BAS"in O00O0OOOO0O00OO0O and len (O00O0OOOO0O00OO0O ["BAS"])==0 :#line:4796
                    O0OO00OOOO0OO0OO0 =f"[證][DoSubQuoteByCategory](aCat={OOO000O00O0O0O0O0}, sResData={O0000O0O00O0OO00O})沒有BAS資料!"#line:4797
                    O00O0O0O0OOO0OO00 .__O0O000OO000000O0O (O0OO00OOOO0OO0OO0 )#line:4798
                    return False #line:4799
                if "HL"in O00O0OOOO0O00OO0O and len (O00O0OOOO0O00OO0O ["HL"])==0 :#line:4800
                    O0OO00OOOO0OO0OO0 =f"[證][DoSubQuoteByCategory](aCat={OOO000O00O0O0O0O0}, sResData={O0000O0O00O0OO00O})沒有HL資料!"#line:4801
                    O00O0O0O0OOO0OO00 .__O0O000OO000000O0O (O0OO00OOOO0OO0OO0 )#line:4802
                    return False #line:4803
                if OOO000O00O0O0O0O0 ==O00O0O0O0OOO0OO00 .__O0O0O000O0000O0O0 :#line:4805
                    O00O0O0O0OOO0OO00 .__OO000OO0O0O0O00O0 (True ,OOO000O00O0O0O0O0 ,O000000OOOOOO000O ,O00O0OOOO0O00OO0O )#line:4806
                else :#line:4807
                    O00O0O0O0OOO0OO00 .__OOOOO0OOO00O0O00O (True ,OOO000O00O0O0O0O0 ,O000000OOOOOO000O ,O00O0OOOO0O00OO0O )#line:4808
                return True #line:4809
        except Exception as OOO0000O0OOOOO0O0 :#line:4810
            O00O0O0O0OOO0OO00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubQuoteByCategorySTK:{OOO0000O0OOOOO0O0}")#line:4811
            O00O0O0O0OOO0OO00 .__O0O000OO000000O0O (f"[證][DoSubQuoteByCategorySTK]{OOO000O00O0O0O0O0}新增紀錄失敗!({OOO0000O0OOOOO0O0})")#line:4812
        OO00OO0OOOO0000OO =threading .Thread (target =O00O0O0O0OOO0OO00 .__O00O00O000O00O000 ,args =(STKxFUT .STK ,OOO000O00O0O0O0O0 ))#line:4815
        OO00OO0OOOO0000OO .start ()#line:4816
    def __O00O0O00O000O0O0O (O0OO00OOOO0OOO0O0 ,O0OO0OOO0OO0O00OO :str ,O0000OO0OOOOOOO0O :bool ):#line:4818
        ""#line:4821
        try :#line:4822
            OO000O000OO00O000 :str =f"Quote/TWF/*/{O0OO0OOO0OO0O00OO}/RECOVER"#line:4823
            O0O0OOOOO0OOOO0OO ,OO0O00OO0OO0O0O0O =O0OO00OOOO0OOO0O0 .__O00O0O0000000O00O (O0OO00OOOO0OOO0O0 ._vRcvTopic_Fut ,OO000O000OO00O000 ,'utf-8',O0OO00OOOO0OOO0O0 ._vRcvTopic_Fut_Req )#line:4825
            if O0O0OOOOO0OOOO0OO and OO0O00OO0OO0O0O0O !="":#line:4827
                O0OO00OOO0O0OO000 =json .loads (OO0O00OO0OO0O0O0O )#line:4828
                if "status"in O0OO00OOO0O0OO000 and len (O0OO00OOO0O0OO000 ["status"])>0 :#line:4829
                    if O0OO00OOO0O0OO000 ["status"][0 ]=="error":#line:4830
                        O0OO00OOOO0OOO0O0 .__O0O000OO000000O0O (f"[期][DoSubQuoteFUT](aSolIce={O0OO0OOO0OO0O00OO}, aData={OO0O00OO0OO0O0O0O})行情回補資料有誤!")#line:4831
                        return RCode .FAIL #line:4832
                if "BAS"in O0OO00OOO0O0OO000 and len (O0OO00OOO0O0OO000 ["BAS"])==0 :#line:4833
                    O0OO00OOOO0OOO0O0 .__O0O000OO000000O0O (f"[期][DoSubQuoteFUT](aSolIce={O0OO0OOO0OO0O00OO},aData={OO0O00OO0OO0O0O0O})沒有BAS資料!")#line:4834
                    return RCode .FAIL #line:4835
                if "HL"in O0OO00OOO0O0OO000 and len (O0OO00OOO0O0OO000 ["HL"])==0 :#line:4836
                    O0OO00OOOO0OOO0O0 .__O0O000OO000000O0O (f"[期][DoSubQuoteFUT](aSolIce={O0OO0OOO0OO0O00OO},aData={OO0O00OO0OO0O0O0O})沒有HL資料!")#line:4837
                    return RCode .FAIL #line:4838
                O00000O00O0O0000O =O0OO00OOOO0OOO0O0 .__OO000000O00O0OO0O (False ,O0OO0OOO0OO0O00OO ,O0000OO0OOOOOOO0O ,O0OO00OOO0O0OO000 )#line:4841
                return O00000O00O0O0000O #line:4842
            else :#line:4843
                return RCode .FAIL #line:4844
        except Exception as OOOOOO00000O0O0O0 :#line:4845
            O0OO00OOOO0OOO0O0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubQuoteFUT:{OOOOOO00000O0O0O0}")#line:4846
            O0OO00OOOO0OOO0O0 .__O0O000OO000000O0O (f"[證][DoSubQuoteFUT]{O0OO0OOO0OO0O00OO}新增紀錄失敗!({OOOOOO00000O0O0O0})")#line:4847
            OO00O0O00OO00000O =threading .Thread (target =O0OO00OOOO0OOO0O0 .__O00O00O000O00O000 ,args =(STKxFUT .FUT ,O0OO0OOO0OO0O00OO ))#line:4848
            OO00O0O00OO00000O .start ()#line:4849
            return RCode .FAIL #line:4850
    def __O00OOOOO000000OO0 (OOOOO0O00OOO0O000 ,OOO0O00OOO0000O0O :str ,OOO0O00OOO000O0O0 :bool ):#line:4851
        try :#line:4852
            O0OO00O00OOO0OOO0 :bool =False #line:4853
            OO0OOO000000000O0 :str =f"Quote/TWF/{OOO0O00OOO0000O0O}/*/RECOVER"#line:4854
            OOOOO0OO000O000O0 :str =""#line:4855
            O0OO00O00OOO0OOO0 ,OOOOO0OO000O000O0 =OOOOO0O00OOO0O000 .__O00O0O0000000O00O (OOOOO0O00OOO0O000 ._vRcvTopic_Fut ,OO0OOO000000000O0 ,'utf-8',OOOOO0O00OOO0O000 ._vRcvTopic_Fut_Req )#line:4857
            if O0OO00O00OOO0OOO0 :#line:4859
                O0OO000O000OO000O =json .loads (OOOOO0OO000O000O0 )#line:4860
                if "status"in O0OO000O000OO000O and len (O0OO000O000OO000O ["status"])>0 :#line:4863
                    if O0OO000O000OO000O ["status"][0 ]=="error":#line:4864
                        OOOOO0O00OOO0O000 .__O0O000OO000000O0O (f"[期][DoSubQuoteByCategory](aCat={OOO0O00OOO0000O0O}, aData={OOOOO0OO000O000O0})行情回補資料有誤!")#line:4865
                        return #line:4866
                if "BAS"in O0OO000O000OO000O and len (O0OO000O000OO000O ["BAS"])==0 :#line:4867
                    OOOOO0O00OOO0O000 .__O0O000OO000000O0O (f"[期][DoSubQuoteByCategory](aCat={OOO0O00OOO0000O0O}, aData={OOOOO0OO000O000O0})沒有BAS資料!")#line:4868
                    return #line:4869
                if "HL"in O0OO000O000OO000O and len (O0OO000O000OO000O ["HL"])==0 :#line:4870
                    OOOOO0O00OOO0O000 .__O0O000OO000000O0O (f"[期][DoSubQuoteByCategory](aCat={OOO0O00OOO0000O0O}, aData={OOOOO0OO000O000O0})沒有HL資料!")#line:4871
                    return #line:4872
                OOOOO0O00OOO0O000 .__OO000000O00O0OO0O (True ,OOO0O00OOO0000O0O ,OOO0O00OOO000O0O0 ,O0OO000O000OO000O )#line:4875
                return #line:4876
        except Exception as OOO0O0O0OO000OOOO :#line:4877
            pass #line:4878
        OO00OO00OO0OO0OOO =threading .Thread (target =OOOOO0O00OOO0O000 .__O00O00O000O00O000 ,args =(STKxFUT .FUT ,f"[期]新增分類紀錄失敗{OOO0O00OOO0000O0O}"))#line:4880
        OO00OO00OO0OO0OOO .start ()#line:4881
    def __OOO00O00OO00OO00O (O0OOOO00O0O0OOO0O ,OOOOOOO00OO000O00 :str ,O0OO000OOO00O0O00 :bool ):#line:4883
        try :#line:4884
            OO00O000OOO0OO00O :bool =False #line:4885
            O0O00OO0O00OO0O0O =f"QuoteOvs/*/*/{OOOOOOO00OO000O00}/RECOVER"#line:4887
            OO00O000OOO0OO00O ,OOOOO0000OOO0O0O0 =O0OOOO00O0O0OOO0O .__O00O0O0000000O00O (O0OOOO00O0O0OOO0O ._vRcvTopic_OvsFut ,O0O00OO0O00OO0O0O ,'big5',O0OOOO00O0O0OOO0O ._vRcvTopic_OvsFut_Req )#line:4888
            if OO00O000OOO0OO00O :#line:4890
                O0000OO0OOOOOO0O0 =json .loads (OOOOO0000OOO0O0O0 )#line:4891
                if "status"in O0000OO0OOOOOO0O0 and len (O0000OO0OOOOOO0O0 ["status"])>0 :#line:4892
                    if O0000OO0OOOOOO0O0 ["status"][0 ]=="error":#line:4893
                         O0OOOO00O0O0OOO0O .__O0O000OO000000O0O (f"[海期][DoSubQuoteOvsFUT](aSolIce={OOOOOOO00OO000O00}, aData={OOOOO0000OOO0O0O0})行情回補資料有誤!")#line:4894
                         return RCode .FAIL #line:4895
                    if "BAS"in O0000OO0OOOOOO0O0 and len (O0000OO0OOOOOO0O0 ["BAS"])==0 :#line:4896
                        O0OOOO00O0O0OOO0O .__O0O000OO000000O0O (f"[海期][DoSubQuoteOvsFUT](aSolIce={OOOOOOO00OO000O00}, aData={OOOOO0000OOO0O0O0})沒有BAS資料!")#line:4897
                        return RCode .FAIL #line:4898
                O0OOOO0OOO0O000O0 =O0OOOO00O0O0OOO0O .__OOOO000OOOO00OO0O (False ,OOOOOOO00OO000O00 ,O0OO000OOO00O0O00 ,O0000OO0OOOOOO0O0 )#line:4901
                return O0OOOO0OOO0O000O0 #line:4903
            else :#line:4904
                return RCode .FAIL #line:4905
        except Exception as OO000OO00OOOO00O0 :#line:4906
            O0OOOO00O0O0OOO0O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubQuoteOvsFUT: {OO000OO00OOOO00O0}")#line:4908
            OOO0000OO0OOO0OO0 =TQtRcvEventData ()#line:4910
            OOO0000OO0OOO0OO0 .SetRcvBAS_Fail (OOOOOOO00OO000O00 )#line:4911
            O0OOOO00O0O0OOO0O .__O0000OOO0OO0OOOO0 .Add (arg1 =STKxFUT .OVSFUT ,arg2 =OOO0000OO0OOO0OO0 )#line:4912
            return RCode .FAIL #line:4913
    def __O0O00OO0OO00O00O0 (OO000O000OOO0O000 ,O0OOOO00OOO0OO0OO :bool ,aExchange :str ="*"):#line:4915
        ""#line:4919
        try :#line:4920
            O000O00000OO0000O :bool =False #line:4921
            O00OO0O0O0O0000O0 :str =f"QuoteOvs/{aExchange}/FUT/*/RECOVER"#line:4922
            O00OOOOO000OO0000 :str =""#line:4923
            O000O00000OO0000O ,O00OOOOO000OO0000 =OO000O000OOO0O000 .__O00O0O0000000O00O (OO000O000OOO0O000 ._vRcvTopic_OvsFut ,O00OO0O0O0O0000O0 ,'big5',OO000O000OOO0O000 ._vRcvTopic_OvsFut_Req )#line:4924
            if O000O00000OO0000O :#line:4926
                O00OOOO00O000000O =json .loads (O00OOOOO000OO0000 )#line:4927
                if "status"in O00OOOO00O000000O and len (O00OOOO00O000000O ["status"])>0 :#line:4929
                    if O00OOOO00O000000O ["status"][0 ]=="error":#line:4930
                        OO000O000OOO0O000 .__O0O000OO000000O0O (f"[海期][DoSubQuoteByCategory](aSolIce={aExchange}, aData={O00OOOOO000OO0000})行情回補資料有誤!")#line:4931
                        return RCode .FAIL #line:4932
                    if "BAS"in O00OOOO00O000000O and len (O00OOOO00O000000O ["BAS"])==0 :#line:4933
                        OO000O000OOO0O000 .__O0O000OO000000O0O (f"[海期][DoSubQuoteByCategory](aSolIce={aExchange}, aData={O00OOOOO000OO0000})沒有BAS資料!")#line:4934
                        return RCode .FAIL #line:4935
                O00000O000O0O0OOO =OO000O000OOO0O000 .__OOOO000OOOO00OO0O (False ,aExchange ,O0OOOO00OOO0OO0OO ,O00OOOO00O000000O )#line:4939
                return O00000O000O0O0OOO #line:4940
            else :#line:4941
                return RCode .FAIL #line:4942
        except Exception as OOOOO00O0OO0OOO00 :#line:4943
            OO000O000OOO0O000 .__O0O000OO000000O0O (f"[海期][DoSubQuoteByCategoryOvsFUT] 新增分類紀錄失敗!")#line:4944
            return RCode .FAIL #line:4945
    def __O0OO000O0O00OO0O0 (OOO000O0OO0OO0O00 ,OOOO000O000O0O0OO :str ):#line:4947
        ""#line:4950
        O0000O0OO000OO0O0 :str =""#line:4952
        try :#line:4953
            O0OOOOOOOOOO000OO :list =[]#line:4954
            OOO00OO0O0O00OO00 ,O0OOOOOOOOOO000OO ,O0000O0OO000OO0O0 =OOO000O0OO0OO0O00 ._fMapQuoteOvsFUT .GetItem_ByExchange (OOOO000O000O0O0OO )#line:4955
            if OOO00OO0O0O00OO00 ==False :#line:4956
                return False ,O0000O0OO000OO0O0 #line:4957
            for O000O0OO0000O00OO in O0OOOOOOOOOO000OO :#line:4958
                OOO000O0OO0OO0O00 .__OO000O0OOOOO0OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =O000O0OO0000O00OO )#line:4959
            return True ,""#line:4960
        except Exception as O00O0O0O00OOO0O00 :#line:4962
            O0000O0OO000OO0O0 =f"[海期][DoUnSubQuoteByCategory](aExchange={OOOO000O000O0O0OO}){O00O0O0O00OOO0O00}"#line:4963
        return False ,O0000O0OO000OO0O0 #line:4964
    def __OOOOO0OOO00O0O00O (OOO00OO0O00O00OO0 ,O0O0OO0O0OOO000OO :bool ,OOOO00O00OO0OO000 :str ,OO0OO0000O0O000OO :bool ,O00OOOOOOO0O00OOO ):#line:4966
        ""#line:4967
        try :#line:4968
            OOO0O00O0O0OO00OO :TObjStkQuoteMap =None #line:4969
            O0OO0OOO000O0O0OO :str =""#line:4970
            O0O00O0OOO00O00O0 ,OOO0O00O0O0OO00OO ,O0OO0OOO000O0O0OO =OOO00OO0O00O00OO0 ._fMapQuoteSTK .AddDataBySolIce (O0O0OO0O0OOO000OO ,OOOO00O00OO0OO000 ,O00OOOOOOO0O00OOO ,OO0OO0000O0O000OO )#line:4971
            if O0O00O0OOO00O00O0 :#line:4972
                OOO00OO0O00O00OO0 .__O0000OOO0OO0OOOO0 .Add (arg1 =STKxFUT .STK ,arg2 =OOO0O00O0O0OO00OO )#line:4973
                for OOO0000OOOO00000O ,O00OOO0OO0OOO00OO in OOO0O00O0O0OO00OO .items ():#line:4976
                    OOOOO0OOO0O000OO0 :TStkQuoteData =O00OOO0OO0OOO00OO #line:4977
                    OOO00OO0O00O00OO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .STK ,arg2 =OOOOO0OOO0O000OO0 .HL .TopicTX )#line:4978
                    OOO00OO0O00O00OO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .STK ,arg2 =OOOOO0OOO0O000OO0 .HL .Topic5Q )#line:4979
                return RCode .OK #line:4980
            else :#line:4981
                OOO00OO0O00O00OO0 .__O0O000OO000000O0O (f"[證][DoSubQuote_RTonlySTK]({O0O0OO0O0OOO000OO},{OOOO00O00OO0OO000})回補失敗!({O0OO0OOO000O0O0OO})")#line:4982
                return RCode .FAIL #line:4983
        except Exception as OO00O0O0O0O0OO00O :#line:4985
            OOO00OO0O00O00OO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubQuote_RTonlySTK: {OO00O0O0O0O0OO00O}")#line:4987
            return RCode .FAIL #line:4988
    def __OO000000O00O0OO0O (OO0O0OOO00O00OOO0 ,OOOOOOOOO00OOO0O0 :bool ,OOOO0000O0OOO0OOO :str ,O0000000000OOOOOO :bool ,OO0OO000OOOOO00O0 ):#line:4990
        ""#line:4993
        try :#line:4994
            OOO00OO00OO0O0O00 :TObjFutQuoteMap =None #line:4995
            OO0OOOO00O000OOO0 :str =""#line:4996
            OO0O0OOOOOO0OOO0O ,OOO00OO00OO0O0O00 ,OO0OOOO00O000OOO0 =OO0O0OOO00O00OOO0 ._fMapQuoteFUT .AddDataBySolIce (OOOOOOOOO00OOO0O0 ,OOOO0000O0OOO0OOO ,OO0OO000OOOOO00O0 ,O0000000000OOOOOO )#line:4997
            if OO0O0OOOOOO0OOO0O :#line:4998
                OO0O0OOO00O00OOO0 .__O0000OOO0OO0OOOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =OOO00OO00OO0O0O00 )#line:4999
                for O000OOO0OO0OOO0OO ,O00O00000O0O0O00O in OOO00OO00OO0O0O00 .items ():#line:5002
                    O00OOO0000O00OO0O :TFutQuoteData =O00O00000O0O0O00O #line:5003
                    OO0O0OOO00O00OOO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =O00OOO0000O00OO0O .HL .TopicTX )#line:5004
                    OO0O0OOO00O00OOO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =O00OOO0000O00OO0O .HL .Topic5Q )#line:5005
                    OO0O0OOO00O00OOO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =O00OOO0000O00OO0O .HL .Topic5QTOT )#line:5006
                    OO0O0OOO00O00OOO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =O00OOO0000O00OO0O .HL .TopicBas )#line:5007
                return RCode .OK #line:5008
            else :#line:5009
                OO0O0OOO00O00OOO0 .__O0O000OO000000O0O (f"[期][DoSubQuote_RTonlyFUT]{OOOO0000O0OOO0OOO}新增紀錄失敗!({OO0OOOO00O000OOO0})")#line:5010
                return RCode .FAIL #line:5011
        except Exception as OO0O0OO00O000O0O0 :#line:5013
            OO0O0OOO00O00OOO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubQuote_RTonlyFUT: {OO0O0OO00O000O0O0}")#line:5015
            return RCode .FAIL #line:5016
    def __OOOO000OOOO00OO0O (OOO00OOO0O0O00OO0 ,OOOOOOOOOOOO0O0OO :bool ,O0O00O0O0O000OO00 :str ,O00O00OOOOO0OO000 :bool ,OO00O0OOO0OOOO0O0 ):#line:5018
        ""#line:5020
        try :#line:5021
            O0OO0OOO0O0OO0OOO :TMapOvsFutQuoteData =None #line:5022
            OOOOOO00000O000O0 :str =""#line:5023
            O0O00OO0OOO000OOO ,O0OO0OOO0O0OO0OOO ,OOOOOO00000O000O0 =OOO00OOO0O0O00OO0 ._fMapQuoteOvsFUT .AddDataBySolIce (OOOOOOOOOOOO0O0OO ,O0O00O0O0O000OO00 ,OO00O0OOO0OOOO0O0 ,O00O00OOOOO0OO000 )#line:5024
            if O0O00OO0OOO000OOO :#line:5025
                O0O0O000000000OO0 =TQtRcvEventData ()#line:5027
                O0O0O000000000OO0 .SetRcvBAS_Succ ("",O0OO0OOO0O0OO0OOO )#line:5028
                OOO00OOO0O0O00OO0 .__O0000OOO0OO0OOOO0 .Add (arg1 =STKxFUT .OVSFUT ,arg2 =O0O0O000000000OO0 )#line:5029
                for OOO0000OO0OOOOOOO ,O0O00O00OOOO00O0O in O0OO0OOO0O0OO0OOO .items ():#line:5032
                    O000OO0OOOOOO00O0 :TOvsFutQuoteData =O0O00O00OOOO00O0O #line:5033
                    OOO00OOO0O0O00OO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .OVSFUT ,arg2 =O000OO0OOOOOO00O0 .HL .TopicTX )#line:5034
                    OOO00OOO0O0O00OO0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .OVSFUT ,arg2 =O000OO0OOOOOO00O0 .HL .Topic5Q )#line:5035
                return RCode .OK #line:5036
            else :#line:5037
                OOO00OOO0O0O00OO0 .__O0O000OO000000O0O (f"[海期][DoSubQuote_RTonlyOvsFUT]{O0O00O0O0O000OO00}新增紀錄失敗!({OOOOOO00000O000O0})")#line:5038
                return RCode .FAIL #line:5039
        except Exception as OO0O0O0O0O0O0O00O :#line:5040
            OOO00OOO0O0O00OO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubQuote_RTonlyOvsFUT: {OO0O0O0O0O0O0O00O}")#line:5041
            return RCode .FAIL #line:5042
    def __OO0OOOO0000O000O0 (O0O0O00O00O0OO00O ,O00OO0O0OO0OOO000 :str ,O00000OO000O0O000 :bool ):#line:5046
        ""#line:5049
        try :#line:5050
            OO000O0OOOOO0OOO0 =False #line:5051
            O00OOOO0OO00OOOO0 =f"Quote/TWS/*/*/{O00OO0O0OO0OOO000}/RECOVER"#line:5052
            OO00OO0OOO0O00OOO =""#line:5053
            OO000O0OOOOO0OOO0 ,OO00OO0OOO0O00OOO =O0O0O00O00O0OO00O .__O00O0O0000000O00O (O0O0O00O00O0OO00O .vRcvTopic_Stk ,O00OOOO0OO00OOOO0 ,'utf-8',O0O0O00O00O0OO00O .vRcvTopic_Stk_Req )#line:5055
            if OO000O0OOOOO0OOO0 and OO00OO0OOO0O00OOO !="":#line:5056
                OOOOO00O0OO0OO0O0 :TStkQuoteData =None #line:5057
                O00O00O000OO000O0 :str #line:5058
                OOOOO000OO0OO00O0 ,OOOOO00O0OO0OO0O0 ,O00O00O000OO000O0 =O0O0O00O00O0OO00O ._fMapQuoteSTK .AddRcvData (TStkProdKind .pkIndex ,O00OO0O0OO0OOO000 ,OO00OO0OOO0O00OOO ,O00000OO000O0O000 )#line:5060
                if OOOOO000OO0OO00O0 :#line:5061
                    O0O0O00O00O0OO00O .__O0000OOO0OO0OOOO0 .Add (arg1 =STKxFUT .STK ,arg2 =OOOOO00O0OO0OO0O0 )#line:5063
                    O0O0O00O00O0OO00O .__OO000OO0O0O0O00O0 (OOOOO00O0OO0OO0O0 .HL .Market ,OOOOO00O0OO0OO0O0 .HL .StkKind ,O00OO0O0OO0OOO000 )#line:5065
                    return #line:5066
                else :#line:5067
                    O0O0O00O00O0OO00O .__O0O000OO000000O0O (f"[證][DoSubIdxQuoteSTK]{O00OO0O0OO0OOO000}新增紀錄失敗!")#line:5069
        except Exception as O00O00O0O00O00O0O :#line:5071
            O0O0O00O00O0OO00O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubIdxQuoteSTK:{O00O00O0O00O00O0O}")#line:5072
        OOO00000OO000OOO0 =threading .Thread (target =O0O0O00O00O0OO00O .__OO0OOOO00O00OOO0O ,args =O00OO0O0OO0OOO000 )#line:5074
        OOO00000OO000OOO0 .start ()#line:5075
    def __O00O0000O0000O0O0 (OOO0OOOOOOO0000O0 ,O00OOOO000OOO0O0O :str ,OOO0OO0O00OO00O00 :bool ):#line:5077
        ""#line:5080
        try :#line:5081
            OO00O0OO0O0O0OO0O :str =f"Quote/TWF/IDX/{O00OOOO000OOO0O0O}/MR"#line:5083
            if OOO0OOOOOOO0000O0 ._fMapQuoteFUT .AddData (TFutProdKind .pkIndex ,O00OOOO000OOO0O0O ,OOO0OO0O00OO00O00 ,OO00O0OO0O0O0OO0O ,OOO0OOOOOOO0000O0 .__OOOOOOOOOO0O000O0 ):#line:5084
                OOO0OOOOOOO0000O0 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =OO00O0OO0O0O0OO0O )#line:5085
            else :#line:5086
                OOO0OOOOOOO0000O0 .__O0O000OO000000O0O (f"[期][DoSubIdxQuote_RTonly]{O00OOOO000OOO0O0O}新增紀錄失敗!")#line:5088
        except Exception as OO0O0O00O00O0O0O0 :#line:5089
            OOO0OOOOOOO0000O0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubIdxQuoteFUT:{OO0O0O00O00O0O0O0}")#line:5090
    def __OO000OO0O0O0O00O0 (O0OO0OOO00OOOOO00 ,O000O00OO00OO0OOO :bool ,OOOO00O00OO0O0000 :str ,OO0OO00O00O000OO0 :bool ,OO0O0OO00O0OOOO00 ):#line:5092
        ""#line:5096
        try :#line:5097
            OO0O0O0000O000O0O :TObjStkQuoteMap =None #line:5098
            OO0OO0O0OOO0OO0O0 :str =""#line:5099
            O0O0O000O00OOO0OO ,OO0O0O0000O000O0O ,OO0OO0O0OOO0OO0O0 =O0OO0OOO00OOOOO00 ._fMapQuoteSTK .AddIdxDataBySolIce (O000O00OO00OO0OOO ,OOOO00O00OO0O0000 ,OO0O0OO00O0OOOO00 ,OO0OO00O00O000OO0 )#line:5100
            if O0O0O000O00OOO0OO :#line:5102
                O0OO0OOO00OOOOO00 .__O0000OOO0OOOO0000 (OO0O0O0000O000O0O )#line:5104
                for OO0OOOOOO0000OOOO ,O0O00OO00O0OOOO00 in OO0O0O0000O000O0O .items ():#line:5108
                    OOOO00OOO00OO0000 :TStkQuoteData =O0O00OO00O0OOOO00 #line:5109
                    O0OO0OOO00OOOOO00 .__OOO000OO00O00OOO0 .Add (arg1 =STKxFUT .STK ,arg2 =OOOO00OOO00OO0000 .HL .TopicTX )#line:5110
                return RCode .OK #line:5111
            else :#line:5112
                O0OO0OOO00OOOOO00 .__O0O000OO000000O0O (f"[證][HandleRecover_Idx]({O000O00OO00OO0OOO},{OOOO00O00OO0O0000})新增紀錄失敗!({OO0OO0O0OOO0OO0O0})")#line:5113
                return RCode .FAIL #line:5114
        except Exception as O0OO000OOOO00OO00 :#line:5115
            O0OO0OOO00OOOOO00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoSubIdxQuote_RTonlySTK:{O0OO000OOOO00OO00}")#line:5117
            return RCode .FAIL #line:5118
    def __OOOOOO00O0OO00000 (O000OO0OO000O000O ,OO000OO00OO0000OO :STKxFUT ,O00O0O00OO0O0OOO0 :str ):#line:5121
        try :#line:5122
            with O000OO0OO000O000O ._lock :#line:5123
                O000OO0OO000O000O ._message_receiver .add_subscription (TopicSubscription .of (O00O0O00OO0O0OOO0 ))#line:5125
        except Exception as O000O0O00O0O00000 :#line:5126
            O000OO0OO000O000O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"SolaceSubTopic:{O00O0O00OO0O0OOO0}, {O000O0O00O0O00000}")#line:5128
    def __O0O000OOO0O00O00O (O00OOO0O00000000O ,O0O00O0O00O0OOO00 :str ):#line:5130
        ""#line:5133
        O00OO00OO00000O0O :str =""#line:5134
        try :#line:5135
            O0OO0000OO00O0OOO =[]#line:5136
            OOOO0OO0000000OOO :bool #line:5137
            OOOO0OO0000000OOO ,O0OO0000OO00O0OOO ,O00OO00OO00000O0O =O00OOO0O00000000O ._fMapQuoteSTK .GetItem_BySolIce (O0O00O0O00O0OOO00 )#line:5139
            if OOOO0OO0000000OOO ==False :#line:5140
                return False ,O00OO00OO00000O0O #line:5141
            for OOO000OOO000O0OOO in O0OO0000OO00O0OOO :#line:5142
                O00OOO0O00000000O .__OO000O0OOOOO0OOO0 .Add (arg1 =STKxFUT .STK ,arg2 =OOO000OOO000O0OOO )#line:5143
            return True ,""#line:5144
        except Exception as O00OOO00000000O0O :#line:5145
            O00OOO0O00000000O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoUnSubTopicSTK:{O00OOO00000000O0O}")#line:5146
            return False ,f"[證][DoUnSubTopicSTK](aSolICE={O0O00O0O00O0OOO00}){O00OOO00000000O0O}"#line:5147
    def __O0O0000OOOO0OO00O (O000OO00OO00O0O00 ,O000OOOOOO00OO000 :str ):#line:5148
        ""#line:5150
        OOO00OO000O00O0O0 :str =""#line:5151
        try :#line:5152
            OOOO0O000OOO000OO =[]#line:5153
            O0OO0O0O00O0OO00O ,OOOO0O000OOO000OO ,OOO00OO000O00O0O0 =O000OO00OO00O0O00 ._fMapQuoteSTK .GetItem_ByCategory (O000OOOOOO00OO000 )#line:5154
            if O0OO0O0O00O0OO00O ==False :#line:5155
                return RCode .FAIL ,OOO00OO000O00O0O0 #line:5156
            for OOO000000OO0000O0 in OOOO0O000OOO000OO :#line:5158
                O000OO00OO00O0O00 .__OO000O0OOOOO0OOO0 .Add (arg1 =STKxFUT .STK ,arg2 =OOO000000OO0000O0 )#line:5159
            return RCode .OK ,""#line:5160
        except Exception as OOOO000000OO0O000 :#line:5161
            OOO00OO000O00O0O0 =f"[證][DoUnSubTopicByCategory](aCat={O000OOOOOO00OO000}){OOOO000000OO0O000}"#line:5162
        return RCode .FAIL ,OOO00OO000O00O0O0 #line:5163
    def __OO000OOO0OO000000 (O0O000O0O0OO00O0O ,OOO0O0OO0OOOO0OO0 :str ):#line:5165
        ""#line:5168
        OO00O00O0O0OOO000 :str =""#line:5169
        try :#line:5170
            OO000OO0OOOO00000 =[]#line:5171
            O00O0OO0OOOO0O000 :bool #line:5172
            O00O0OO0OOOO0O000 ,OO000OO0OOOO00000 ,OO00O00O0O0OOO000 =O0O000O0O0OO00O0O ._fMapQuoteFUT .GetItem_BySolIce (OOO0O0OO0OOOO0OO0 )#line:5174
            if O00O0OO0OOOO0O000 ==False :#line:5175
                return False ,OO00O00O0O0OOO000 #line:5176
            for OOOOO0OOO00OOOOO0 in OO000OO0OOOO00000 :#line:5177
                O0O000O0O0OO00O0O .__OO000O0OOOOO0OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =OOOOO0OOO00OOOOO0 )#line:5178
            return True ,""#line:5179
        except Exception as OO000000OO0OO0OO0 :#line:5180
            O0O000O0O0OO00O0O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoUnSubTopicFUT:{OO000000OO0OO0OO0}")#line:5181
            return False ,f"[期][DoUnSubTopicSTK](aSolICE={OOO0O0OO0OOOO0OO0}){OO000000OO0OO0OO0}"#line:5182
    def __O00OO0OO0000O0000 (O0OO0OO000OOO0OOO ,OOO00000OOO00O0OO :str ):#line:5185
        ""#line:5186
        OO0O0OO0OOO00O0OO :str =""#line:5187
        try :#line:5188
            OO0OOOO0OO0OO0O00 =[]#line:5189
            O0000O00O000OO0OO ,OO0OOOO0OO0OO0O00 ,OO0O0OO0OOO00O0OO =O0OO0OO000OOO0OOO ._fMapQuoteFUT .GetItem_ByCategory (OOO00000OOO00O0OO )#line:5190
            if O0000O00O000OO0OO ==False :#line:5191
                return RCode .FAIL ,OO0O0OO0OOO00O0OO #line:5192
            for OO0000O000OO00OO0 in OO0OOOO0OO0OO0O00 :#line:5193
                O0OO0OO000OOO0OOO .__OO000O0OOOOO0OOO0 .Add (arg1 =STKxFUT .FUT ,arg2 =OO0000O000OO00OO0 )#line:5194
            return RCode .OK ,""#line:5195
        except Exception as O000O000OOOO0OO0O :#line:5197
            OO0O0OO0OOO00O0OO =f"[期][DoUnSubTopicByCategoryFUT](aCat={OOO00000OOO00O0OO}){O000O000OOOO0OO0O}"#line:5198
        return RCode .FAIL ,OO0O0OO0OOO00O0OO #line:5199
    def __O0OOOO00O00OOOO0O (O0OO0O0000OO000OO ,O0000000O0OOO0OO0 :str ):#line:5202
        ""#line:5204
        OO00OOO0OOOOOOO00 =""#line:5205
        try :#line:5206
            OOO00000000OO0OOO =[]#line:5207
            O00OO0O0O0OOOO00O ,OOO00000000OO0OOO ,OO00O0OO0000O00OO =O0OO0O0000OO000OO ._fMapQuoteOvsFUT .GetItem_BySolIce (O0000000O0OOO0OO0 )#line:5209
            if O00OO0O0O0OOOO00O ==False :#line:5210
                return False ,OO00O0OO0000O00OO #line:5211
            for O00O0O0000O0O0O00 in OOO00000000OO0OOO :#line:5212
                O0OO0O0000OO000OO .__OO000O0OOOOO0OOO0 .Add (arg1 =STKxFUT .OVSFUT ,arg2 =O00O0O0000O0O0O00 )#line:5214
            return True ,""#line:5215
        except Exception as OO0OOOOOO0O0O00O0 :#line:5216
            O0OO0O0000OO000OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"DoUnSubTopicOvsFUT:{OO0OOOOOO0O0O00O0}")#line:5218
            OO00OOO0OOOOOOO00 =f"[證][DoUnSubTopic](aSolICE={O0000000O0OOO0OO0}){OO0OOOOOO0O0O00O0}"#line:5219
            return False ,OO00OOO0OOOOOOO00 #line:5220
    def __O0OO0OO0O00OO0OO0 (O0000OOO0OO0O0OO0 ,OOOOOO0OO000OOOOO :STKxFUT ,O0OOO0OO00000OO0O :str ):#line:5222
        try :#line:5223
            with O0000OOO0OO0O0OO0 ._lock :#line:5224
                O0000OOO0OO0O0OO0 ._message_receiver .remove_subscription (TopicSubscription .of (O0OOO0OO00000OO0O ))#line:5226
        except Exception as O000O0OO000OO00O0 :#line:5227
            O0000OOO0OO0O0OO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"SolaceUnSubTopic:{O0OOO0OO00000OO0O}, {O000O0OO000OO00O0}")#line:5229
    def __O0OO0O0O000000OO0 (OOO0OO0O0O0O0O0O0 ):#line:5231
        OOO0OO0O0O0O0O0O0 .__O0O000O0OO000OOO0 =TSolaceMessageThreadClass ("Trd_HandleQuote",OOO0OO0O0O0O0O0O0 ._log ,OOO0OO0O0O0O0O0O0 .__O0OO00OOOO000O0O0 )#line:5233
        OOO0OO0O0O0O0O0O0 .__O0000OOO0OO0OOOO0 =TMyWorkItemThreadClass ("Trd_HandleRcvQuote",OOO0OO0O0O0O0O0O0 ._log ,OOO0OO0O0O0O0O0O0 .__OOOO00OOO000O000O )#line:5235
        OOO0OO0O0O0O0O0O0 .__OOO000OO00O00OOO0 =TMyWorkItemThreadClass ("Trd_SolaceSubTopic",OOO0OO0O0O0O0O0O0 ._log ,OOO0OO0O0O0O0O0O0 .__OOOOOO00O0OO00000 )#line:5237
        OOO0OO0O0O0O0O0O0 .__OO000O0OOOOO0OOO0 =TMyWorkItemThreadClass ("Trd_SolaceUnSubTopic",OOO0OO0O0O0O0O0O0 ._log ,OOO0OO0O0O0O0O0O0 .__O0OO0OO0O00OO0OO0 )#line:5239
    def __O0O0OO0OOO00O0O0O (OO0O00O0OO0O0O0OO ):#line:5241
        with OO0O00O0OO0O0O0OO ._lock :#line:5242
                OO0O00O0OO0O0O0OO .__O0O000O0OO000OOO0 ._run =False #line:5244
                OO0O00O0OO0O0O0OO .__O0000OOO0OO0OOOO0 ._run =False #line:5246
                OO0O00O0OO0O0O0OO .__OOO000OO00O00OOO0 ._run =False #line:5248
                OO0O00O0OO0O0O0OO .__OO000O0OOOOO0OOO0 ._run =False #line:5250
    def QryProdID_NormalStock (OOOO0OOO000O0O0O0 ):#line:5253
        ""#line:5256
        OO0OO000OOO0O0OOO =None #line:5257
        try :#line:5258
            OO0O000OO0OO0OO00 =False #line:5259
            OOOO0OOO0O0OOO0O0 ="Quote/TWS/S/TSE/*/RECOVER"#line:5260
            OOO00O00OOOOO0000 =""#line:5261
            OO0O000OO0OO0OO00 ,OOO00O00OOOOO0000 =OOOO0OOO000O0O0O0 .__O00O0O0000000O00O (OOOO0OOO000O0O0O0 ._vRcvTopic_Stk ,OOOO0OOO0O0OOO0O0 ,'utf-8',OOOO0OOO000O0O0O0 ._vRcvTopic_Stk_Req )#line:5263
            if OO0O000OO0OO0OO00 :#line:5264
                OOOOOO0O0OOO0OOOO =json .loads (OOO00O00OOOOO0000 )#line:5265
                if "status"in OOOOOO0O0OOO0OOOO and len (OOOOOO0O0OOO0OOOO ["status"])>0 :#line:5268
                    if OOOOOO0O0OOO0OOOO ["status"][0 ]=="error":#line:5269
                        OOOO0OOO000O0O0O0 .__O0O000OO000000O0O (f"[證][取個一般上市上櫃股票商品檔](aData={OOO00O00OOOOO0000})行情回補資料有誤!")#line:5271
                        return RCode .FAIL ,OO0OO000OOO0O0OOO #line:5272
                if "BAS"in OOOOOO0O0OOO0OOOO and len (OOOOOO0O0OOO0OOOO ["BAS"])==0 :#line:5273
                    OOOO0OOO000O0O0O0 .__O0O000OO000000O0O (f"[證][取個一般上市上櫃股票商品檔](aData={OOO00O00OOOOO0000})沒有BAS資料!")#line:5275
                    return RCode .FAIL ,OO0OO000OOO0O0OOO #line:5276
                if "HL"in OOOOOO0O0OOO0OOOO and len (OOOOOO0O0OOO0OOOO ["HL"])==0 :#line:5277
                    OOOO0OOO000O0O0O0 .__O0O000OO000000O0O (f"[證][取個一般上市上櫃股票商品檔](aData={OOO00O00OOOOO0000})沒有HL資料!")#line:5279
                    return RCode .FAIL ,OO0OO000OOO0O0OOO #line:5280
                OO0OO000OOO0O0OOO =TQryStkProdMap ()#line:5283
                for O0OOOOO0O00OOOOOO in OOOOOO0O0OOO0OOOO ["BAS"]:#line:5284
                    try :#line:5285
                        OO0OOOO0O00OO0000 =TStkQtBase ()#line:5286
                        OO0OOOO0O00OO0000 .Handle_BAS (O0OOOOO0O00OOOOOO )#line:5287
                        if OO0OO000OOO0O0OOO .data .get (OO0OOOO0O00OO0000 .StkNo )is None :#line:5289
                            OO00O0O0OOOOOOOOO =TQryStkProdRec ()#line:5290
                            OO00O0O0OOOOOOOOO .tmpBase =OO0OOOO0O00OO0000 #line:5291
                            OO0OO000OOO0O0OOO [OO0OOOO0O00OO0000 .StkNo ]=OO00O0O0OOOOOOOOO #line:5292
                    except Exception as OOOO0000OOOO00000 :#line:5293
                        OOOO0OOO000O0O0O0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProdID_NormalStock(BAS):{OOOO0000OOOO00000}")#line:5295
                for O0OOOOO0O00OOOOOO in OOOOOO0O0OOO0OOOO ["HL"]:#line:5297
                    try :#line:5298
                        OO0OOOO0O00OO0000 =TStkQtHL ()#line:5299
                        OO0OOOO0O00OO0000 .Handle_HL (O0OOOOO0O00OOOOOO )#line:5300
                        O000OOO0000O000O0 :TQryStkProdRec =None #line:5302
                        O000OOO0000O000O0 =next ((OO0O00O0O00000O0O for OO0O00O0O00000O0O in OO0OO000OOO0O0OOO .values ()if OO0O00O0O00000O0O .tmpBase .StkNo ==OO0OOOO0O00OO0000 .Symbol ),None )#line:5304
                        if O000OOO0000O000O0 is not None :#line:5305
                            O000OOO0000O000O0 .tmpHL =OO0OOOO0O00OO0000 #line:5306
                            O000OOO0000O000O0 .SetDataInit ()#line:5307
                    except Exception as OOOO0000OOOO00000 :#line:5308
                        OOOO0OOO000O0O0O0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProdID_NormalStock(HL):{OOOO0000OOOO00000}")#line:5310
                return RCode .OK ,OO0OO000OOO0O0OOO #line:5312
        except Exception as OOOO0000OOOO00000 :#line:5313
            OOOO0OOO000O0O0O0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[證][QryProdID_NormalStock]取個一般上市上櫃股票商品檔失敗!({OOOO0000OOOO00000})")#line:5315
        return RCode .FAIL ,None #line:5317
    def QryProdID_FutStk_FirstMth (O000OOO0O000OO0OO ):#line:5319
        ""#line:5321
        OOOOOO0OO0OOO0OO0 :TQryFutProdMap =None #line:5322
        try :#line:5323
            O000OO0O0O0OOO0O0 :bool =False #line:5324
            O0OO0OOO000000O00 :OO0O00OO0O0OO0O0O ="Quote/TWF/FUT/*/RECOVER"#line:5325
            OOO0O0OO0O0OO00O0 :OO0O00OO0O0OO0O0O =""#line:5326
            O000OO0O0O0OOO0O0 ,OOO0O0OO0O0OO00O0 =O000OOO0O000OO0OO .__O00O0O0000000O00O (O000OOO0O000OO0OO ._vRcvTopic_Fut ,O0OO0OOO000000O00 ,'utf-8',O000OOO0O000OO0OO ._vRcvTopic_Fut_Req )#line:5329
            if O000OO0O0O0OOO0O0 and OOO0O0OO0O0OO00O0 !="":#line:5331
                O000O0OO0OO00OOOO =json .loads (OOO0O0OO0O0OO00O0 )#line:5332
                if "status"in O000O0OO0OO00OOOO and len (O000O0OO0OO00OOOO ["status"])>0 :#line:5334
                    if O000O0OO0OO00OOOO ["status"][0 ]=="error":#line:5335
                        O000OOO0O000OO0OO .__O0O000OO000000O0O (f"[期][QryProdID_FutStk_FirstMth](aData={OOO0O0OO0O0OO00O0})行情回補資料有誤!")#line:5337
                        return False ,OOOOOO0OO0OOO0OO0 #line:5338
                if "BAS"in O000O0OO0OO00OOOO and len (O000O0OO0OO00OOOO ["BAS"])==0 :#line:5339
                    O000OOO0O000OO0OO .__O0O000OO000000O0O (f"[期][QryProdID_FutStk_FirstMth](aData={OOO0O0OO0O0OO00O0})沒有BAS資料!")#line:5341
                    return False ,OOOOOO0OO0OOO0OO0 #line:5342
                if "HL"in O000O0OO0OO00OOOO and len (O000O0OO0OO00OOOO ["HL"])==0 :#line:5343
                    O000OOO0O000OO0OO .__O0O000OO000000O0O (f"[期][QryProdID_FutStk_FirstMth](aData={OOO0O0OO0O0OO00O0})沒有HL資料!")#line:5345
                    return False ,OOOOOO0OO0OOO0OO0 #line:5346
                OOOOOO0OO0OOO0OO0 =TQryFutProdMap ()#line:5350
                for OO0O00OO0O0OO0O0O in O000O0OO0OO00OOOO ["BAS"]:#line:5351
                    try :#line:5352
                        OO0O00O00OOOOOOO0 :TFutQtBase =TFutQtBase ()#line:5353
                        OO0O00O00OOOOOOO0 .Handle_BAS (OO0O00OO0O0OO0O0O )#line:5354
                        if OO0O00O00OOOOOOO0 .StkNo .isspace ()==False and len (OO0O00O00OOOOOOO0 .StkNo )>0 :#line:5355
                            if OOOOOO0OO0OOO0OO0 .data .get (OO0O00O00OOOOOOO0 .StkNo )is None :#line:5356
                                OOOOO0O0OOO000OO0 :TQryFutProdRec =TQryFutProdRec ()#line:5357
                                OOOOO0O0OOO000OO0 .tmpBase =OO0O00O00OOOOOOO0 #line:5358
                                OOOOOO0OO0OOO0OO0 [OO0O00O00OOOOOOO0 .ProdID ]=OOOOO0O0OOO000OO0 #line:5359
                            elif (int (OO0O00O00OOOOOOO0 .SettleMth )<int (OOOOOO0OO0OOO0OO0 [OO0O00O00OOOOOOO0 .ProdID ].tmpBase .SettleMth )):#line:5360
                                OOOOOO0OO0OOO0OO0 [OO0O00O00OOOOOOO0 .ProdID ].tmpBase =OO0O00O00OOOOOOO0 #line:5361
                    except Exception as OO0O0000O0OO00000 :#line:5362
                        O000OOO0O000OO0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProdID_FutStk_FirstMth(BAS):{OO0O0000O0OO00000}")#line:5364
                for OO0O00OO0O0OO0O0O in O000O0OO0OO00OOOO ["HL"]:#line:5367
                    try :#line:5368
                        OO0O00O00OOOOOOO0 :TFutQtHL =TFutQtHL ()#line:5369
                        OO0O00O00OOOOOOO0 .Handle_HL (OO0O00OO0O0OO0O0O )#line:5370
                        OOO000OOOOOO0O0O0 :TQryStkProdRec =None #line:5371
                        OOO000OOOOOO0O0O0 =next ((OOOOO000OO0OOO0OO for OOOOO000OO0OOO0OO in OOOOOO0OO0OOO0OO0 .values ()if OOOOO000OO0OOO0OO .tmpBase .OrdProdID ==OO0O00O00OOOOOOO0 .Symbol ),None )#line:5373
                        if OOO000OOOOOO0O0O0 is not None :#line:5374
                            OOO000OOOOOO0O0O0 .tmpHL =OO0O00O00OOOOOOO0 #line:5375
                            OOO000OOOOOO0O0O0 .SetDataInit ()#line:5376
                    except Exception as OO0O0000O0OO00000 :#line:5377
                        O000OOO0O000OO0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProdID_FutStk_FirstMth(HL):{OO0O0000O0OO00000}")#line:5379
                return True ,OOOOOO0OO0OOO0OO0 #line:5381
        except Exception as OO0O0000O0OO00000 :#line:5382
            O000OOO0O000OO0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProdID_FutStk_FirstMth:{OO0O0000O0OO00000}")#line:5384
            O000OOO0O000OO0OO .__O0O000OO000000O0O (f"[期][QryProdID_FutStk_FirstMth]取個期貨商品檔(近1月)失敗!({OO0O0000O0OO00000})")#line:5386
        return False ,None #line:5387
    def QryProd_Fut (O0000OOO0OOOOOOOO ,OO00O00OOO0000OOO :bool ,OO000O00O000O00O0 :bool ,O00O00O000OO0000O :bool ):#line:5389
        ""#line:5395
        OOO0OO00O0000O00O :TObjBaseFutMap =None #line:5396
        try :#line:5397
            O00OOO000O00O00O0 :O00OO000000000O0O ="Quote/TWF/FUT/*/RECOVER"#line:5398
            O00000OO0OO0OO000 :O00OO000000000O0O =""#line:5399
            OO0OO0OOOO0O0OOOO ,O00000OO0OO0OO000 =O0000OOO0OOOOOOOO .__O00O0O0000000O00O (O0000OOO0OOOOOOOO ._vRcvTopic_Fut ,O00OOO000O00O00O0 ,'utf-8',O0000OOO0OOOOOOOO ._vRcvTopic_Fut_Req )#line:5401
            if OO0OO0OOOO0O0OOOO and O00000OO0OO0OO000 !="":#line:5403
                O00OOOO0OOO00OOOO =json .loads (O00000OO0OO0OO000 )#line:5404
                if "status"in O00OOOO0OOO00OOOO and len (O00OOOO0OOO00OOOO ["status"])>0 :#line:5407
                    if O00OOOO0OOO00OOOO ["status"][0 ]=="error":#line:5408
                        O0000OOO0OOOOOOOO .__O0O000OO000000O0O (f"[期][QryProdID_Fut](aData={O00000OO0OO0OO000})行情回補資料有誤!")#line:5410
                        return RCode .FAIL ,OOO0OO00O0000O00O #line:5411
                if "BAS"in O00OOOO0OOO00OOOO and len (O00OOOO0OOO00OOOO ["BAS"])==0 :#line:5412
                    O0000OOO0OOOOOOOO .__O0O000OO000000O0O (f"[期][QryProdID_Fut](aData={O00000OO0OO0OO000})沒有BAS資料!")#line:5414
                    return RCode .FAIL ,OOO0OO00O0000O00O #line:5415
                if "HL"in O00OOOO0OOO00OOOO and len (O00OOOO0OOO00OOOO ["HL"])==0 :#line:5416
                    O0000OOO0OOOOOOOO .__O0O000OO000000O0O (f"[期][QryProdID_Fut](aData={O00000OO0OO0OO000})沒有HL資料!")#line:5418
                    return RCode .FAIL ,OOO0OO00O0000O00O #line:5419
                OOO0OO00O0000O00O :TObjBaseFutMap =TObjBaseFutMap ()#line:5423
                for O00OO000000000O0O in O00OOOO0OOO00OOOO ["BAS"]:#line:5424
                    try :#line:5425
                        OO0O000O000O00OOO :TFutQtBase =TFutQtBase ()#line:5426
                        OO0O000O000O00OOO .Handle_BAS (O00OO000000000O0O )#line:5427
                        if OO0O000O000O00OOO .StkNo .isspace ()==False and len (OO0O000O000O00OOO .StkNo )>0 :#line:5429
                            if OO000O00O000O00O0 :#line:5430
                                if O00O00O000OO0000O ==False and OO0O000O000O00OOO .FutName .startswith ("小型"):#line:5432
                                    pass #line:5433
                                else :#line:5434
                                    OOO0OO00O0000O00O .AddItem_ByProdID (OO0O000O000O00OOO )#line:5435
                        elif OO00O00OOO0000OOO :#line:5436
                            OOO0OO00O0000O00O .AddItem_ByProdID (OO0O000O000O00OOO )#line:5437
                    except Exception as OOOOOO00OOO00OOOO :#line:5438
                        O0000OOO0OOOOOOOO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_Fut(BAS):{OOOOOO00OOO00OOOO}")#line:5440
                OOO0OO00O0000O00O .ReAddAll ()#line:5442
                return RCode .OK ,OOO0OO00O0000O00O #line:5445
        except Exception as OOOOOO00OOO00OOOO :#line:5446
            O0000OOO0OOOOOOOO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_Fut:{OOOOOO00OOO00OOOO}")#line:5447
            O0000OOO0OOOOOOOO .__O0O000OO000000O0O (f"[期][QryProdID_Fut]取期貨商品檔(不含選擇權)失敗!({OOOOOO00OOO00OOOO})")#line:5448
        return RCode .FAIL ,OOO0OO00O0000O00O #line:5449
    def QryProd_FutCom (OO0OOOOO0OOO0OOO0 ):#line:5451
        ""#line:5452
        OOO00OO0O00OOOOOO :TObjFutComList =None #line:5453
        try :#line:5454
            O0OOO00OOO0O00OOO :str ="Quote/TWF/SPD/*/SYMBOL"#line:5455
            O000OO0O0OO0OOO00 :str =""#line:5456
            OOO00O0O0O0000OO0 ,O000OO0O0OO0OOO00 =OO0OOOOO0OOO0OOO0 .__O00O0O0000000O00O (OO0OOOOO0OOO0OOO0 ._vRcvTopic_Fut ,O0OOO00OOO0O00OOO ,'utf-8',OO0OOOOO0OOO0OOO0 ._vRcvTopic_Fut_Req )#line:5458
            if OOO00O0O0O0000OO0 :#line:5460
                OOOO0O000000O0000 =json .loads (O000OO0O0OO0OOO00 )#line:5461
                if "status"in OOOO0O000000O0000 and len (OOOO0O000000O0000 ["status"])>0 :#line:5463
                    if OOOO0O000000O0000 ["status"][0 ]=="error":#line:5464
                        OO0OOOOO0OOO0OOO0 .__O0O000OO000000O0O (f"[期][QryProd_FutCom](aData={O000OO0O0OO0OOO00})行情回補資料有誤!")#line:5466
                        return False ,OOO00OO0O00OOOOOO #line:5467
                if "SYMBOL"in OOOO0O000000O0000 and len (OOOO0O000000O0000 ["SYMBOL"])==0 :#line:5468
                    OO0OOOOO0OOO0OOO0 .__O0O000OO000000O0O (f"[期][QryProd_FutCom](aData={O000OO0O0OO0OOO00})沒有SYMBOL資料!")#line:5470
                    return False ,OOO00OO0O00OOOOOO #line:5471
                OOO00OO0O00OOOOOO :TObjFutComList =TObjFutComList ()#line:5474
                OOO0OOO0000OO000O =OOOO0O000000O0000 ["SYMBOL"][0 ].split ('|')#line:5475
                for O00O000OO00O0O00O in OOO0OOO0000OO000O :#line:5476
                    OOO00OO0O00OOOOOO .AddItem (O00O000OO00O0O00O )#line:5477
                return True ,OOO00OO0O00OOOOOO #line:5479
        except Exception as O00000O00OOO0O000 :#line:5480
            OO0OOOOO0OOO0OOO0 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_FutCom:{O00000O00OOO0O000}")#line:5481
            OO0OOOOO0OOO0OOO0 .__O0O000OO000000O0O (f"[期][QryProd_FutCom]取複式期貨商品檔失敗!({O00000O00OOO0O000})")#line:5482
        return False ,OOO00OO0O00OOOOOO #line:5483
    def QryProd_FutCom2 (O00OOO0OOO0O000OO ):#line:5485
        ""#line:5487
        O000O0OO0OOOOO00O :TObjFutComList =None #line:5488
        try :#line:5489
            O00OOOO0000OOO0OO :TObjBaseFutMap =None #line:5490
            OO0OO00O0O0OOOOOO ,O00OOOO0000OOO0OO =O00OOO0OOO0O000OO .QryProd_Fut (True ,True ,True )#line:5491
            if OO0OO00O0O0OOOOOO ==False :#line:5492
                O00OOO0OOO0O000OO .__O0O000OO000000O0O ("[QryProd_FutCom2]載入期貨單式商品失敗!")#line:5493
                return RCode .FAIL ,O000O0OO0OOOOO00O #line:5494
            O000O0OO0OOOOO00O :TObjFutComList =TObjFutComList ()#line:5495
            O0OOOO000OOO0O0O0 ,O00OOOOO0O0OOOO0O =0 ,0 #line:5497
            OO0O000000OOO00O0 =[O000OOO0OO0O00O0O for O000OOO0OO0O00O0O in O00OOOO0000OOO0OO .keys ()if not O000OOO0OO0O00O0O .startswith ("MX")or O000OOO0OO0O00O0O =="MXF"]#line:5499
            for O0O0OO0OO00OO0OOO in OO0O000000OOO00O0 :#line:5501
                O0000OOOO0O000000 =O00OOOO0000OOO0OO [O0O0OO0OO00OO0OOO ]#line:5502
                if len (O0000OOOO0O000000 )<=1 :#line:5503
                    continue #line:5504
                for O0OOOO000OOO0O0O0 in range (len (O0000OOOO0O000000 )):#line:5505
                    for O00OOOOO0O0OOOO0O in range (O0OOOO000OOO0O0O0 +1 ,len (O0000OOOO0O000000 )):#line:5506
                        OOOOOO0000OOOO000 =O0000OOOO0O000000 [O0OOOO000OOO0O0O0 ]#line:5507
                        OO00OOOO0O0OO0O00 =O0000OOOO0O000000 [O00OOOOO0O0OOOO0O ]#line:5508
                        O000O0OO0OOOOO00O .AddItem ("{}^{}".format (OOOOOO0000OOOO000 .OrdProdID ,OO00OOOO0O0OO0O00 .OrdProdID [3 :5 ]))#line:5510
            O0O0O000OO00O000O =O00OOOO0000OOO0OO ["MXF"]#line:5513
            O0OO00OO000OO0OOO =[O0000O0O000O00OOO for O0000O0O000O00OOO in O00OOOO0000OOO0OO .keys ()if O0000O0O000O00OOO .startswith ("MX")and O0000O0O000O00OOO !="MXF"]#line:5515
            for O0OOOO000OOO0O0O0 in range (len (O0OO00OO000OO0OOO )):#line:5516
                OO0O0O0000O000OOO =O00OOOO0000OOO0OO [O0OO00OO000OO0OOO [O0OOOO000OOO0O0O0 ]][0 ]#line:5517
                for O00OOOOO0O0OOOO0O in range (O0OOOO000OOO0O0O0 +1 ,len (O0OO00OO000OO0OOO )):#line:5519
                    O00000O00OOO0000O =O00OOOO0000OOO0OO [O0OO00OO000OO0OOO [O00OOOOO0O0OOOO0O ]][0 ]#line:5520
                    if OO0O0O0000O000OOO .SettleMth ==O00000O00OOO0000O .SettleMth :#line:5521
                        if ord (OO0O0O0000O000OOO .OrdProdID [2 ])<ord (O00000O00OOO0000O .OrdProdID [2 ]):#line:5523
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (OO0O0O0000O000OOO .OrdProdID ,O00000O00OOO0000O .OrdProdID ))#line:5525
                        else :#line:5526
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (O00000O00OOO0000O .OrdProdID ,OO0O0O0000O000OOO .OrdProdID ))#line:5529
                    else :#line:5530
                        if int (OO0O0O0000O000OOO .SettleMth )<int (O00000O00OOO0000O .SettleMth ):#line:5531
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (OO0O0O0000O000OOO .OrdProdID ,O00000O00OOO0000O .OrdProdID ))#line:5533
                        else :#line:5534
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (O00000O00OOO0000O .OrdProdID ,OO0O0O0000O000OOO .OrdProdID ))#line:5537
                if OO0O0O0000O000OOO .SettleMth ==O0O0O000OO00O000O [0 ].SettleMth :#line:5540
                    if OO0O0O0000O000OOO .ProdID =="MX1"or OO0O0O0000O000OOO .ProdID =="MX2":#line:5541
                        for O00O000000O0000OO in O0O0O000OO00O000O :#line:5542
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (OO0O0O0000O000OOO .OrdProdID ,O00O000000O0000OO .OrdProdID ))#line:5544
                    else :#line:5545
                        for O00O000000O0000OO in O0O0O000OO00O000O :#line:5546
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (O00O000000O0000OO .OrdProdID ,OO0O0O0000O000OOO .OrdProdID ))#line:5548
                else :#line:5549
                    if int (OO0O0O0000O000OOO .SettleMth )<int (O0O0O000OO00O000O [0 ].SettleMth ):#line:5550
                        for O00O000000O0000OO in O0O0O000OO00O000O :#line:5551
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (OO0O0O0000O000OOO .OrdProdID ,O00O000000O0000OO .OrdProdID ))#line:5553
                    else :#line:5554
                        for O00O000000O0000OO in O0O0O000OO00O000O :#line:5555
                            O000O0OO0OOOOO00O .AddItem ("{}^{}".format (O00O000000O0000OO .OrdProdID ,OO0O0O0000O000OOO .OrdProdID ))#line:5557
            return RCode .OK ,O000O0OO0OOOOO00O #line:5559
        except Exception as O00000OOOOO0O0O0O :#line:5560
            O00OOO0OOO0O000OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_FutCom2:{O00000OOOOO0O0O0O}")#line:5561
            O00OOO0OOO0O000OO .__O0O000OO000000O0O (f"[期][QryProd_FutCom2]取複式期貨商品檔失敗!({O00000OOOOO0O0O0O})")#line:5562
        return RCode .FAIL ,O000O0OO0OOOOO00O #line:5563
    def QryProd_Opt (O00O0O0OO0OO00000 ,O0OO00O00OOO00OOO :bool ,O0000OOO0O0O0OOO0 :bool ,OO0O000OO000OOO00 :bool ):#line:5565
        ""#line:5570
        O0OOO0O00O000OOO0 :TObjBaseOptMap =None #line:5571
        try :#line:5572
            OO00OO0O0O0000OO0 :O0OO0OO0O00O0O00O ="Quote/TWF/OPT/*/RECOVER"#line:5573
            OO00OO0O0O000O0O0 :O0OO0OO0O00O0O00O =""#line:5574
            O0000O0OO0OOOOOOO ,OO00OO0O0O000O0O0 =O00O0O0OO0OO00000 .__O00O0O0000000O00O (O00O0O0OO0OO00000 ._vRcvTopic_Fut ,OO00OO0O0O0000OO0 ,'utf-8',O00O0O0OO0OO00000 ._vRcvTopic_Fut_Req )#line:5576
            if O0000O0OO0OOOOOOO :#line:5578
                O000000O0OOO0O0OO =json .loads (OO00OO0O0O000O0O0 )#line:5579
                if "status"in O000000O0OOO0O0OO and len (O000000O0OOO0O0OO ["status"])>0 :#line:5581
                    if O000000O0OOO0O0OO ["status"][0 ]=="error":#line:5582
                        O00O0O0OO0OO00000 .__O0O000OO000000O0O (f"[期][QryProd_Opt](aData={OO00OO0O0O000O0O0})行情回補資料有誤!")#line:5584
                        return RCode .FAIL ,O0OOO0O00O000OOO0 #line:5585
                if "BAS"in O000000O0OOO0O0OO and len (O000000O0OOO0O0OO ["BAS"])==0 :#line:5586
                    O00O0O0OO0OO00000 .__O0O000OO000000O0O (f"[期][QryProd_Opt](aData={OO00OO0O0O000O0O0})沒有BAS資料!")#line:5588
                    return RCode .FAIL ,O0OOO0O00O000OOO0 #line:5589
                if "HL"in O000000O0OOO0O0OO and len (O000000O0OOO0O0OO ["HL"])==0 :#line:5590
                    O00O0O0OO0OO00000 .__O0O000OO000000O0O (f"[期][QryProd_Opt](aData={OO00OO0O0O000O0O0})沒有HL資料!")#line:5592
                    return RCode .FAIL ,O0OOO0O00O000OOO0 #line:5593
                O0OOO0O00O000OOO0 =TObjBaseOptMap ()#line:5596
                for O0OO0OO0O00O0O00O in O000000O0OOO0O0OO ["BAS"]:#line:5597
                    try :#line:5598
                        O0OO0OOOOOO00OO0O :TFutQtBase =TFutQtBase ()#line:5599
                        O0OO0OOOOOO00OO0O .Handle_BAS (O0OO0OO0O00O0O00O )#line:5600
                        if O0OO0OOOOOO00OO0O .StkNo .isspace ()==False and len (O0OO0OOOOOO00OO0O .StkNo )>0 :#line:5602
                            if O0000OOO0O0O0OOO0 :#line:5603
                                if OO0O000OO000OOO00 ==False and O0OO0OOOOOO00OO0O .FutName .startswith ("小型"):#line:5605
                                    pass #line:5606
                                else :#line:5607
                                    O0OOO0O00O000OOO0 .AddItem_ByProdID (O0OO0OOOOOO00OO0O )#line:5608
                        elif O0OO00O00OOO00OOO :#line:5609
                            O0OOO0O00O000OOO0 .AddItem_ByProdID (O0OO0OOOOOO00OO0O )#line:5610
                    except Exception as O0O0O0000O0O00000 :#line:5611
                        O00O0O0OO0OO00000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_Opt:{O0O0O0000O0O00000}")#line:5613
                return RCode .OK ,O0OOO0O00O000OOO0 #line:5616
        except Exception as O0O0O0000O0O00000 :#line:5617
            O00O0O0OO0OO00000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_Opt:{O0O0O0000O0O00000}")#line:5618
            O00O0O0OO0OO00000 .__O0O000OO000000O0O (f"[期][QryProd_Opt]取個選擇權商品檔失敗!({O0O0O0000O0O00000})")#line:5619
        return RCode .FAIL ,O0OOO0O00O000OOO0 #line:5620
    def QryProd_OvsFut (OO0OO0OO00O00000O ):#line:5622
        ""#line:5625
        O0O00OO00O000OOOO :TObjOvsFutProdMthMap =None #line:5626
        try :#line:5627
            O0OO00OO0OO0O0OOO =False #line:5628
            O0OOOO0O0O000OOO0 ="QuoteOvs/*/FUT/*/RECOVER"#line:5629
            OO000000OOOO0OOO0 =""#line:5630
            O0OO00OO0OO0O0OOO ,OO000000OOOO0OOO0 =OO0OO0OO00O00000O .__O00O0O0000000O00O (OO0OO0OO00O00000O ._vRcvTopic_OvsFut ,O0OOOO0O0O000OOO0 ,'big5',OO0OO0OO00O00000O ._vRcvTopic_OvsFut_Req )#line:5632
            if O0OO00OO0OO0O0OOO :#line:5633
                OOOO0OOOO000OOOOO =json .loads (OO000000OOOO0OOO0 )#line:5634
                if "status"in OOOO0OOOO000OOOOO and len (OOOO0OOOO000OOOOO ["status"])>0 :#line:5636
                    if OOOO0OOOO000OOOOO ["status"][0 ]=="error":#line:5637
                        OO0OO0OO00O00000O .__O0O000OO000000O0O (f"[海期][QryProd_OvsFut](aData={OO000000OOOO0OOO0})行情回補資料有誤!")#line:5639
                        return False ,O0O00OO00O000OOOO #line:5640
                if "BAS"in OOOO0OOOO000OOOOO and len (OOOO0OOOO000OOOOO ["BAS"])==0 :#line:5641
                    OO0OO0OO00O00000O .__O0O000OO000000O0O (f"[海期][QryProd_OvsFut](aData={OO000000OOOO0OOO0})沒有BAS資料!")#line:5643
                    return False ,O0O00OO00O000OOOO #line:5644
                O0O00OO00O000OOOO =TObjOvsFutProdMthMap ("","")#line:5647
                for O0OOO000O00O0O0OO in OOOO0OOOO000OOOOO ["BAS"]:#line:5648
                    try :#line:5649
                        OO0000OO0O000OOOO =TOvsFutQtBase ()#line:5650
                        OO0000OO0O000OOOO .Handle_BAS (O0OOO000O00O0O0OO )#line:5651
                        O0O00OO00O000OOOO .AddItem (OO0000OO0O000OOOO )#line:5653
                    except Exception as O00O000OO00O00OO0 :#line:5654
                        OO0OO0OO00O00000O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_OvsFut: {O00O000OO00O00OO0}")#line:5656
                return True ,O0O00OO00O000OOOO #line:5658
        except Exception as O00O000OO00O00OO0 :#line:5659
            OO0OO0OO00O00000O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_OvsFut:{O00O000OO00O00OO0}")#line:5660
            OO0OO0OO00O00000O .__O0O000OO000000O0O (f"[海期][QryProd_OvsFut]取期貨商品檔(不含選擇權)失敗!({O00O000OO00O00OO0})")#line:5661
        return False ,O0O00OO00O000OOOO #line:5662
    def QryProd_OvsOpt (O00OOO00O0OO0O0OO ):#line:5664
        ""#line:5666
        OO00O0O00O0O00O0O :None #line:5667
        try :#line:5668
            OO0OOOOOO0OOOO000 :bool =False #line:5669
            OO0OOOO0OOOO0O0OO ="QuoteOvs/*/OPT/*/RECOVER"#line:5670
            OO000000000O0OO00 =""#line:5671
            OO0OOOOOO0OOOO000 ,OO000000000O0OO00 =O00OOO00O0OO0O0OO .__O00O0O0000000O00O (O00OOO00O0OO0O0OO ._vRcvTopic_OvsFut ,OO0OOOO0OOOO0O0OO ,'big5',O00OOO00O0OO0O0OO ._vRcvTopic_OvsFut_Req )#line:5673
            if OO0OOOOOO0OOOO000 :#line:5674
                OO00OOO0O000OOOOO =json .loads (OO000000000O0OO00 )#line:5675
                if "status"in OO00OOO0O000OOOOO and len (OO00OOO0O000OOOOO ["status"])>0 :#line:5677
                    if OO00OOO0O000OOOOO ["status"][0 ]=="error":#line:5678
                        O00OOO00O0OO0O0OO .__O0O000OO000000O0O (f"[海期][QryProd_OvsOpt](aData={OO000000000O0OO00})行情回補資料有誤!")#line:5680
                        return False ,OO00O0O00O0O00O0O #line:5681
                if "BAS"in OO00OOO0O000OOOOO and len (OO00OOO0O000OOOOO ["BAS"])==0 :#line:5682
                    O00OOO00O0OO0O0OO .__O0O000OO000000O0O (f"[海期][QryProd_OvsOpt](aData={OO000000000O0OO00})沒有BAS資料!")#line:5684
                    return False ,OO00O0O00O0O00O0O #line:5685
                OO00O0O00O0O00O0O =TObjOvsFutProdMthMap ("","")#line:5688
                for OOO0OO0O00O0OOOOO in OO00OOO0O000OOOOO ["BAS"]:#line:5689
                    try :#line:5690
                        OOOO00000OO0O00OO =TOvsFutQtBase ()#line:5691
                        OOOO00000OO0O00OO .Handle_BAS (OOO0OO0O00O0OOOOO )#line:5692
                        OO00O0O00O0O00O0O .AddItem (OOOO00000OO0O00OO )#line:5693
                    except Exception as O000000OOO000O00O :#line:5694
                        O00OOO00O0OO0O0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_OvsOpt: {O000000OOO000O00O}")#line:5696
                return True ,OO00O0O00O0O00O0O #line:5698
        except Exception as O000000OOO000O00O :#line:5699
            O00OOO00O0OO0O0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_OvsOpt:{O000000OOO000O00O}")#line:5700
            O00OOO00O0OO0O0OO .__O0O000OO000000O0O (f"[海期][QryProd_OptOvs]取選擇權商品檔失敗!({O000000OOO000O00O})")#line:5701
        return False ,OO00O0O00O0O00O0O #line:5702
    def QryProd_Fut_ByExchangeTree (OO0OOOO00O0O0OO00 ,O0OOOOO0000OOO0O0 :bool ):#line:5704
        ""#line:5707
        OO0OOO0OO0000OOO0 :TObjBaseOvsFutExchageTree =None #line:5708
        try :#line:5709
            OOOOO0000OO000000 :bool =False #line:5710
            O00OOO0O0OOOO000O ="QuoteOvs/*/FUT/*/RECOVER"#line:5711
            O0OOOO000000O000O =""#line:5712
            OOOOO0000OO000000 ,O0OOOO000000O000O =OO0OOOO00O0O0OO00 .__O00O0O0000000O00O (OO0OOOO00O0O0OO00 ._vRcvTopic_OvsFut ,O00OOO0O0OOOO000O ,'big5',OO0OOOO00O0O0OO00 ._vRcvTopic_OvsFut_Req )#line:5714
            if OOOOO0000OO000000 :#line:5715
                O0O00OOOO00OO0000 =json .loads (O0OOOO000000O000O )#line:5716
                if "status"in O0O00OOOO00OO0000 and len (O0O00OOOO00OO0000 ["status"])>0 :#line:5718
                    if O0O00OOOO00OO0000 ["status"][0 ]=="error":#line:5719
                        OO0OOOO00O0O0OO00 .__O0O000OO000000O0O (f"[海期][QryProd_OvsFut](aData={O0OOOO000000O000O})行情回補資料有誤!")#line:5721
                        return False ,OO0OOO0OO0000OOO0 #line:5722
                if "BAS"in O0O00OOOO00OO0000 and len (O0O00OOOO00OO0000 ["BAS"])==0 :#line:5723
                    OO0OOOO00O0O0OO00 .__O0O000OO000000O0O (f"[海期][QryProd_OvsFut](aData={O0OOOO000000O000O})沒有BAS資料!")#line:5725
                    return False ,OO0OOO0OO0000OOO0 #line:5726
                OO0OOO0OO0000OOO0 =TObjBaseOvsFutExchageTree ()#line:5729
                for OO0OO0000OO0OO000 in O0O00OOOO00OO0000 ["BAS"]:#line:5730
                    try :#line:5731
                        O000OO0O00OO0O00O =TOvsFutQtBase ()#line:5732
                        O000OO0O00OO0O00O .Handle_BAS (OO0OO0000OO0OO000 )#line:5733
                        if O000OO0O00OO0O00O .Market =="4":#line:5734
                            if O0OOOOO0000OOO0O0 ==False or (O0OOOOO0000OOO0O0 and O000OO0O00OO0O00O .Display =="Y"):#line:5736
                                OO0OOO0OO0000OOO0 .AddItem (O000OO0O00OO0O00O )#line:5737
                    except Exception as OO000O000O000OOOO :#line:5738
                        OO0OOOO00O0O0OO00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_Fut_ByExchangeTree: {OO000O000O000OOOO}")#line:5740
                OO0OOO0OO0000OOO0 .SetInit ()#line:5741
                return True ,OO0OOO0OO0000OOO0 #line:5744
        except Exception as OO000O000O000OOOO :#line:5745
            OO0OOOO00O0O0OO00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"QryProd_Fut_ByExchangeTree:{OO000O000O000OOOO}")#line:5747
            OO0OOOO00O0O0OO00 .__O0O000OO000000O0O (f"[海期][QryProdID_Fut]取期貨商品檔(不含選擇權)失敗!({OO000O000O000OOOO})")#line:5748
        return False ,OO0OOO0OO0000OOO0 #line:5749
    def __O0OO0OOOOO0O0OOO0 (O00OOO0OOO00000OO ,O000000O0000OOOOO :str ,OO0OO0O00O000OOOO :str ):#line:5753
        try :#line:5754
            with O00OOO0OOO00000OO ._lock :#line:5755
                O000O00O00OO00O00 =O00OOO0OOO00000OO ._direct_publish_service .start_async ()#line:5756
                O000O00O00OO00O00 .result ()#line:5757
                OOOO00O0O0OOOOO00 ='utf-8'#line:5758
                O0OOOO0O00O0O0000 =bytearray (f'{OO0OO0O00O000OOOO}',OOOO00O0O0OOOOO00 )#line:5759
                OOO00OO0OO00OOO00 :OutboundMessage =O00OOO0OOO00000OO ._message_service .message_builder ().build (O0OOOO0O00O0O0000 )#line:5760
                O00OOO0OOO00000OO ._direct_publish_service .publish (O000000O0000OOOOO ,OOO00OO0OO00OOO00 )#line:5761
        except Exception as O000000O00O00O00O :#line:5763
            O00OOO0OOO00000OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"SendMessage:{O000000O00O00O00O}")#line:5764
    def __O00O0O0000000O00O (OO0O0O000000O0O00 ,O0O0OO00000000OO0 :str ,OO00OO0O0O0O00O0O :str ,O00O00O0O0O0OOOOO :str ,O0OO0OO0OOO0O0OO0 :str ):#line:5768
        ""#line:5771
        O00O0O00O000O0O00 =""#line:5772
        O0OO00OO0O0O0000O =bytearray (f'{OO00OO0O0O0O00O0O}',O00O00O0O0O0OOOOO )#line:5778
        OOO0O00O0OO0O00O0 :OutboundMessage =OO0O0O000000O0O00 ._message_service .message_builder ().build (payload =O0OO00OO0O0O0000O )#line:5779
        try :#line:5781
            with OO0O0O000000O0O00 ._lock :#line:5782
                OOOOO0O0000O000O0 =OO0O0O000000O0O00 ._message_requester .publish_await_response (request_message =OOO0O00O0OO0O00O0 ,request_destination =Topic .of (O0O0OO00000000OO0 ),reply_timeout =OO0O0O000000O0O00 ._reply_timeout )#line:5786
                OOOO0O0O0O0OO0O0O =OOOOO0O0000O000O0 .get_payload_as_bytes ().decode (O00O00O0O0O0OOOOO )#line:5787
                return True ,OOOO0O0O0O0OO0O0O #line:5788
        except Exception as OOO000OO0OO000OOO :#line:5789
            OO0O0O000000O0O00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"send_request exception! topic={O0O0OO00000000OO0}, msg={OO00OO0O0O0O00O0O}, exception={OOO000OO0OO000OOO}")#line:5791
            OOOO0O0O0O0OO0O0O =""#line:5792
        return False ,OOOO0O0O0O0OO0O0O #line:5794
    def Subscribe (OOO00O0O0OOO0O0O0 ,OO0O0O0OO000OO0O0 :str ,OOO0000O00OO0OOO0 :str )->RCode :#line:5798
        ""#line:5801
        OOO00O0O0OOO0O0O0 ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[Subscribe]exchange={OO0O0O0OO000OO0O0}, symbol={OOO0000O00OO0OOO0}")#line:5802
        if EXCHANGE .TWF ==OO0O0O0OO000OO0O0 :#line:5805
            O0O0O0OOO000O0OOO =OOO00O0O0OOO0O0O0 .__O00O0O00O000O0O0O (OOO0000O00OO0OOO0 ,True )#line:5806
        elif EXCHANGE .TWS ==OO0O0O0OO000OO0O0 :#line:5808
            O0O0O0OOO000O0OOO =OOO00O0O0OOO0O0O0 .__O0O0OO0OO000000OO (OOO0000O00OO0OOO0 ,True )#line:5809
        return O0O0O0OOO000O0OOO #line:5811
    def OvsSubscribe (O000OO0OOO00O0OO0 ,O000000OO0O0OOOOO :str ):#line:5812
        ""#line:5813
        return O000OO0OOO00O0OO0 .__OOO00O00OO00OO00O (O000000OO0O0OOOOO ,True )#line:5814
    def OvsSubscribeWithCategory (O0O00OOOO000OO0OO ,aMrt :str ="FUT",aExchange :str ="*"):#line:5816
        ""#line:5817
        if aMrt =="FUT":#line:5818
            return O0O00OOOO000OO0OO .__O0O00OO0OO00O00O0 (True ,aExchange )#line:5819
        else :#line:5820
            O0O00OOOO000OO0OO ._log .Add (arg1 =SolLogType .Error ,arg2 =f"OvsSubscribeWithCategory aMrt:{aMrt}")#line:5821
            return RCode .FAIL #line:5822
    def Unsubscribe (OOOOO0O00OOOOO00O ,OOOO0O0000OO00OOO :str ,O00OO0OO000OOO0OO :str )->RCode :#line:5824
        ""#line:5827
        OOOOO0O00OOOOO00O ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[Unsubscribe]exchange={OOOO0O0000OO00OOO}, symbol={O00OO0OO000OOO0OO}")#line:5828
        OOO0O0O0OOOOOO0O0 :str =""#line:5830
        if EXCHANGE .TWF ==OOOO0O0000OO00OOO :#line:5832
            O00O0OO0O00000O00 ,OOO0O0O0OOOOOO0O0 =OOOOO0O00OOOOO00O .__OO000OOO0OO000000 (O00OO0OO000OOO0OO )#line:5833
            if O00O0OO0O00000O00 ==False :#line:5834
                O0O0OO0O00000OOO0 =SystemEvent (RCode .SUBSCRIPTION_FAIL ,OOO0O0O0OOOOOO0O0 )#line:5835
                OOOOO0O00OOOOO00O .__OO0000OO0O0O000OO .Fire_OnSystemEvent (O0O0OO0O00000OOO0 )#line:5836
                return RCode .FAIL #line:5837
        elif EXCHANGE .TWS ==OOOO0O0000OO00OOO :#line:5839
            O00O0OO0O00000O00 ,OOO0O0O0OOOOOO0O0 =OOOOO0O00OOOOO00O .__O0O000OOO0O00O00O (O00OO0OO000OOO0OO )#line:5840
            if O00O0OO0O00000O00 ==False :#line:5841
                O0O0OO0O00000OOO0 =SystemEvent (RCode .SUBSCRIPTION_FAIL ,OOO0O0O0OOOOOO0O0 )#line:5842
                OOOOO0O00OOOOO00O .__OO0000OO0O0O000OO .Fire_OnSystemEvent (O0O0OO0O00000OOO0 )#line:5843
                return RCode .FAIL #line:5844
        return RCode .OK #line:5846
    def OvsUnSubscribe (OOOOO000000OOO00O ,O0O0OOOOO0O0O0O00 :str )->bool :#line:5847
        ""#line:5848
        O00OOOO00OO0O0OOO :str =""#line:5850
        OOO0OOOOOO0OO0O0O ,O00OOOO00OO0O0OOO =OOOOO000000OOO00O .__O0OOOO00O00OOOO0O (O0O0OOOOO0O0O0O00 )#line:5851
        if OOO0OOOOOO0OO0O0O :#line:5852
            OOOOO000000OOO00O ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[OvsUnSubscribe]aSymbol={O0O0OOOOO0O0O0O00}")#line:5853
            return RCode .OK #line:5854
        else :#line:5855
            OOOOO000000OOO00O ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[OvsUnSubscribe]aSymbol={O0O0OOOOO0O0O0O00}, sErrMsg={O00OOOO00OO0O0OOO}")#line:5856
            return RCode .FAIL #line:5857
    def SubscribeWithCategory (OO000O0OOO0OOOO00 ,OO0OO0OO0O000O00O :str ,O00OO0O0O0O00OOOO :str )->RCode :#line:5858
        OO000O0OOO0OOOO00 ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[SubscribeWithCategory]exchange={OO0OO0OO0O000O00O}, subscriptionCategory={O00OO0O0O0O00OOOO}")#line:5859
        if EXCHANGE .TWF ==OO0OO0OO0O000O00O :#line:5861
            O00OOOOO00OOOO0OO =threading .Thread (target =OO000O0OOO0OOOO00 .__O00OOOOO000000OO0 ,args =(O00OO0O0O0O00OOOO ,True ))#line:5863
            O00OOOOO00OOOO0OO .start ()#line:5864
        elif EXCHANGE .TWS ==OO0OO0OO0O000O00O :#line:5866
            O00OOOOO00OOOO0OO =threading .Thread (target =OO000O0OOO0OOOO00 .__O00OO0000O0OOO00O ,args =(O00OO0O0O0O00OOOO ,True ))#line:5868
            O00OOOOO00OOOO0OO .start ()#line:5869
        return RCode .OK #line:5870
    def UnsubscribeWithCategory (O0OOOO00OOO0000O0 ,OOOOO0O0OO00O0O00 :str ,OOOO0O00OO000O000 :str )->RCode :#line:5872
        ""#line:5874
        OOO0O000000OO0O00 :str =""#line:5875
        if EXCHANGE .TWF ==OOOOO0O0OO00O0O00 :#line:5877
            OO0O00OO00O0OOO00 ,OOO0O000000OO0O00 =O0OOOO00OOO0000O0 .__O00OO0OO0000O0000 (OOOO0O00OO000O000 )#line:5878
            if OO0O00OO00O0OOO00 ==RCode .FAIL :#line:5879
                return RCode .FAIL ,OOO0O000000OO0O00 #line:5880
        elif EXCHANGE .TWS ==OOOOO0O0OO00O0O00 :#line:5882
            OO0O00OO00O0OOO00 ,OOO0O000000OO0O00 =O0OOOO00OOO0000O0 .__O0O0000OOOO0OO00O (OOOO0O00OO000O000 )#line:5883
            if OO0O00OO00O0OOO00 ==RCode .FAIL :#line:5884
                return RCode .FAIL ,OOO0O000000OO0O00 #line:5885
        return RCode .OK ,OOO0O000000OO0O00 #line:5886
    def OvsUnSubscribeWithCategory (OO00OOO0OOO0000OO ,aMrt :str ="FUT",aExchange :str ="*"):#line:5887
        O000OO0O0OO0O000O :str =""#line:5888
        if aMrt =="FUT":#line:5889
            O0000OO0OOOO000O0 ,O000OO0O0OO0O000O =OO00OOO0OOO0000OO .__O0OO000O0O00OO0O0 (aExchange )#line:5890
            if O0000OO0OOOO000O0 :#line:5891
                return RCode .OK ,""#line:5892
            else :#line:5893
                return RCode .FAIL ,O000OO0O0OO0O000O #line:5894
        else :#line:5895
            return RCode .FAIL ,"Mart is not 'FUT'"#line:5896
    def __OO00OOOO00O00O00O (OO0O000OOO0O00O0O ,OO0O00000OOOO00OO :str ,OO0OO0OOOOOO00OOO :bool ,O0OOOOOOO0000O00O :TObjStkQuoteMap ):#line:5899
        ""#line:5900
        if OO0OO0OOOOOO00OOO ==False :#line:5901
            OO0O000OOO0O00O0O ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[證券行情回補]回補失敗!({OO0O00000OOOO00OO})")#line:5902
            return #line:5903
        try :#line:5905
            for OO0OOOO0OO000O000 ,O00OOOO00OO00OOOO in O0OOOOOOO0000O00O .items ():#line:5906
                O0O00OO0000O0O0OO :TStkQuoteData =O00OOOO00OO00OOOO #line:5907
                OO0OO0OO000000O0O =O0O00OO0000O0O0OO .BAS .StkNo #line:5908
                if OO0O000OOO0O00O0O ._fPrdSnapshotMap .NewItemStk (OO0OO0OO000000O0O ,O0O00OO0000O0O0OO ):#line:5909
                    if OO0O000OOO0O00O0O .__O0O0O0O0OOO00OO0O ==False :#line:5910
                        O0O0OO0000O00OO0O :ProductSnapshot =OO0O000OOO0O00O0O ._fPrdSnapshotMap [OO0OO0OO000000O0O ]#line:5911
                        OO0O000OOO0O00O0O .__OO0000OO0O0O000OO .Fire_OnUpdateBasic (O0O0OO0000O00OO0O .BasicData )#line:5912
                        OO0O000OOO0O00O0O .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (OO0O000OOO0O00O0O ._fPrdSnapshotMap [OO0OO0OO000000O0O ])#line:5913
            if OO0O000OOO0O00O0O .__O0O0O0O0OOO00OO0O :#line:5915
                if len (OO0O000OOO0O00O0O ._fPrdSnapshotMap )>0 :#line:5916
                    O00O0O000OOO00OOO =list (OO0O000OOO0O00O0O ._fPrdSnapshotMap .values ())#line:5917
                    OO0O000OOO0O00O0O .__OO0000OO0O0O000OO .Fire_OnUpdateProductBasicList (O00O0O000OOO00OOO )#line:5918
        except Exception as OO0O000O000O00000 :#line:5919
            OO0O000OOO0O00O0O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteStkAPI_OnQtRcvEvent]aMsg={OO0O00000OOOO00OO}, aIsOK={OO0OO0OOOOOO00OOO}, ex:{OO0O000O000O00000}")#line:5920
    def __OOO0OO000O0OO0OO0 (O0O0OOO00O0O0O00O ,O0OO0OO0000000OOO :str ,OOO0O00OO0O00000O :str ,OOO0O0O000O0O0OO0 :TObjStkQuoteMap ):#line:5922
        ""#line:5923
        if OOO0O00OO0O00000O ==False :#line:5924
            O0O0OOO00O0O0O00O ._log .Add (arg1 =SolLogType .Info ,arg2 =f"[證券行情回補(指數)]{O0OO0OO0000000OOO}回補失敗!")#line:5925
            return #line:5926
        try :#line:5927
            for O00O0O0000O0O0OOO ,OOO0OOO00000OOOO0 in OOO0O0O000O0O0OO0 .items ():#line:5928
                OOOOO00O000OOOO00 :TStkQuoteData =OOO0OOO00000OOOO0 #line:5929
                O0OOO0O0O0OOOOO00 =OOOOO00O000OOOO00 .BAS .StkNo #line:5930
                if O0O0OOO00O0O0O00O ._fPrdSnapshotMap .NewItemStk (O0OOO0O0O0OOOOO00 ,OOOOO00O000OOOO00 ):#line:5931
                    if O0O0OOO00O0O0O00O .__O0O0O0O0OOO00OO0O ==False :#line:5932
                        OO0OOOO0OO0O00O0O :ProductSnapshot =O0O0OOO00O0O0O00O ._fPrdSnapshotMap [O0OOO0O0O0OOOOO00 ]#line:5933
                        O0O0OOO00O0O0O00O .__OO0000OO0O0O000OO .Fire_OnUpdateBasic (OO0OOOO0OO0O00O0O .BasicData )#line:5934
                        O0O0OOO00O0O0O00O .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (O0O0OOO00O0O0O00O ._fPrdSnapshotMap [O0OOO0O0O0OOOOO00 ])#line:5935
            if O0O0OOO00O0O0O00O .__O0O0O0O0OOO00OO0O :#line:5936
                if len (O0O0OOO00O0O0O00O ._fPrdSnapshotMap )>0 :#line:5937
                    O00O0O0OOOO0OO0OO =list (O0O0OOO00O0O0O00O ._fPrdSnapshotMap .values ())#line:5938
                    O0O0OOO00O0O0O00O .__OO0000OO0O0O000OO .Fire_OnUpdateProductBasicList (O00O0O0OOOO0OO0OO )#line:5939
        except Exception as O00OO00OOO0OO0000 :#line:5940
            O0O0OOO00O0O0O00O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteStkAPI_OnQtIdxRcvEvent]aMsg={O0OO0OO0000000OOO}, aIsOK={OOO0O00OO0O00000O}, ex:{O00OO00OOO0OO0000}")#line:5941
    def __OO000OOOOO00O00OO (O0O0OO00O00OOOO00 ,OO00O00OO00O00OO0 :str ,OOO0OOOO00OOO00O0 :TStkQtTX ):#line:5943
        ""#line:5944
        try :#line:5945
            OOO0000OO0O00OOOO :ProductSnapshot =None #line:5946
            OOOO0000OOO0O0000 ,OOO0000OO0O00OOOO =O0O0OO00O00OOOO00 ._fPrdSnapshotMap .GetItem (OO00O00OO00O00OO0 )#line:5948
            if OOOO0000OOO0O0000 :#line:5950
                O00OOO000OO00OO00 :ProductTick_Stk =OOO0000OO0O00OOOO .TickData #line:5951
                OOOO0000OOO0O0000 ,OO0O0O0OO00OOO00O =O00OOO000OO00OO00 .Upt_TX (OOO0OOOO00OOO00O0 )#line:5952
                if OOOO0000OOO0O0000 :#line:5953
                    O0O0OO00O00OOOO00 .__OO0000OO0O0O000OO .Fire_OnMatch (O0O0OO00O00OOOO00 ._fPrdSnapshotMap [OO00O00OO00O00OO0 ].TickData )#line:5954
                    O0O0OO00O00OOOO00 .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (O0O0OO00O00OOOO00 ._fPrdSnapshotMap [OO00O00OO00O00OO0 ])#line:5955
                else :#line:5956
                    O0O0OO00O00OOOO00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"STK_TXEvent Error:{OO0O0O0OO00OOO00O} aSolIce:{OO00O00OO00O00OO0} tmpQtTx:{OOO0OOOO00OOO00O0}")#line:5957
        except Exception as OOO0O0OOO0OOOO00O :#line:5958
            O0O0OO00O00OOOO00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[STK_TXEvent]ProdID={OO00O00OO00O00OO0}, ex:{OOO0O0OOO0OOOO00O}")#line:5959
    def __O00O00OO0OO0OOO00 (O0O0O0OOO0O0O0O00 ,O0OOO0OO0O000O0O0 :str ,O0O000OOOO00O000O :TStkQt5Q ):#line:5960
        ""#line:5961
        try :#line:5962
            O00OOOOO000000000 :ProductSnapshot =None #line:5963
            OOOO0OOOO0OO0000O ,O00OOOOO000000000 =O0O0O0OOO0O0O0O00 ._fPrdSnapshotMap .GetItem (O0OOO0OO0O000O0O0 )#line:5964
            if OOOO0OOOO0OO0000O :#line:5965
                OO0O0O0O0OOOOO00O :ProductTick_Stk =O00OOOOO000000000 .TickData #line:5966
                OOOO0OOOO0OO0000O ,OO0OOO000OOO00O00 =OO0O0O0O0OOOOO00O .Upt_5Q (O0O000OOOO00O000O )#line:5968
                if OOOO0OOOO0OO0000O :#line:5969
                    O0O0O0OOO0O0O0O00 .__OO0000OO0O0O000OO .Fire_OnOrderBook (O0O0O0OOO0O0O0O00 ._fPrdSnapshotMap [O0OOO0OO0O000O0O0 ].TickData )#line:5970
                    O0O0O0OOO0O0O0O00 .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (O0O0O0OOO0O0O0O00 ._fPrdSnapshotMap [O0OOO0OO0O000O0O0 ])#line:5971
                else :#line:5972
                    O0O0O0OOO0O0O0O00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"STK_5QEvent Error:{OO0OOO000OOO00O00} aSolIce={O0OOO0OO0O000O0O0} tmpQt5Q:{O0O000OOOO00O000O}")#line:5973
        except Exception as O00O00OOO00OOOO0O :#line:5974
            O0O0O0OOO0O0O0O00 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[STK_5QEvent]ProdID={O0OOO0OO0O000O0O0}, ex:{O00O00OOO00OOOO0O}")#line:5975
    def __O0O00O00OO0OO00OO (O0OOOOO0O0OO0O000 ,OO00O0O0OO0O0O00O :str ,OOO00OOOO0OO00O00 :TStkQtIDX ):#line:5976
        ""#line:5977
        try :#line:5978
            OO00OO0000OOOOO0O :ProductSnapshot =None #line:5979
            O00000OO00OO00000 ,OO00OO0000OOOOO0O =O0OOOOO0O0OO0O000 ._fPrdSnapshotMap .GetItem (OO00O0O0OO0O0O00O )#line:5981
            if O00000OO00OO00000 :#line:5982
                O00000O00OO0OOO0O :ProductTick_Stk =OO00OO0000OOOOO0O .TickData #line:5983
                O00000OO00OO00000 ,OOOO0000OO0O0O000 =O00000O00OO0OOO0O .Upt_IDX (OOO00OOOO0OO00O00 )#line:5985
                if O00000OO00OO00000 :#line:5986
                    O0OOOOO0O0OO0O000 .__OO0000OO0O0O000OO .Fire_OnMatch (O0OOOOO0O0OO0O000 ._fPrdSnapshotMap [OO00O0O0OO0O0O00O ].TickData )#line:5987
                    O0OOOOO0O0OO0O000 .__OO0000OO0O0O000OO .Fire_OnUpdateLastSnapshot (O0OOOOO0O0OO0O000 ._fPrdSnapshotMap [OO00O0O0OO0O0O00O ])#line:5988
                else :#line:5989
                    O0OOOOO0O0OO0O000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"STK_IDXEvent Error:{OOOO0000OO0O0O000} aSolIce:{OO00O0O0OO0O0O00O} tmpQtIDX:{OOO00OOOO0OO00O00}")#line:5990
        except Exception as OO0O0000OOOOOO000 :#line:5991
            O0OOOOO0O0OO0O000 ._log .Add (arg1 =SolLogType .Error ,arg2 =f"[SolQuoteStkAPI_OnQtIDXEvent]ProdID={OO00O0O0OO0O0O00O}, ex:{OO0O0000OOOOOO000}")#line:5992
class SolAPIHH (SolAPI ):#line:5998
    def __init__ (O0O000000OOO0O00O ,__OOOOO0000O00O0OOO :MarketDataMart ,O000O0O0000000OO0 :str ,loglv =logging .INFO ,conlv =logging .INFO ):#line:5999
        super ().__init__ (__OOOOO0000O00O0OOO ,O000O0O0000000OO0 ,False ,loglv ,conlv )#line:6000
    def Logon (O000000O00OO0OO00 ,OOO0OO0O00OOOO000 :str ,OOO0O0O0000000O0O :str ,O0O0O0O00O00OO0O0 :str ,aCompressLevel :int =5 )->RCode :#line:6002
        ""#line:6008
        if aCompressLevel <1 :#line:6009
            return RCode .FAIL #line:6010
        return O000000O00OO0OO00 .Connect (OOO0OO0O00OOOO000 +":55003","api",OOO0O0O0000000O0O ,O0O0O0O00O00OO0O0 ,aCompressLevel )#line:6012
class TSolaceMessageThreadClass (MessageHandler ):#line:6018
    ""#line:6019
    def __init__ (OO0OOO0OOOO000000 ,OO000OOOOOOO00OOO :str ,O0OOOO0OO000000O0 :logging .Logger ,OO0OOOOO000O00O00 ):#line:6022
        OO0OOO0OOOO000000 ._name =OO000OOOOOOO00OOO #line:6023
        OO0OOO0OOOO000000 ._msgHandler =OO0OOOOO000O00O00 #line:6024
        OO0OOO0OOOO000000 ._lock =Lock ()#line:6025
        OO0OOO0OOOO000000 ._log =O0OOOO0OO000000O0 #line:6026
        OO0OOO0OOOO000000 ._list =[]#line:6027
        OO0OOO0OOOO000000 ._run =True #line:6028
        OO0OOO0OOOO000000 .thrd =threading .Thread (target =OO0OOO0OOOO000000 .OnThread ,name =OO0OOO0OOOO000000 ._name )#line:6029
        OO0OOO0OOOO000000 .thrd .start ()#line:6030
    def OnThread (O0OOO00000O0O0O0O ):#line:6032
        OOO000OOOO00OO0OO =[]#line:6033
        OO0O0O0O0O0O000O0 ,OOO0000OO000OO0OO ,O0O0OO0O0O0OOOOOO =0 ,0 ,0 #line:6034
        while O0OOO00000O0O0O0O ._run :#line:6035
            try :#line:6037
                with O0OOO00000O0O0O0O ._lock :#line:6038
                    OOO000OOOO00OO0OO =O0OOO00000O0O0O0O ._list .copy ()#line:6039
                    OO0O0O0O0O0O000O0 =len (OOO000OOOO00OO0OO )#line:6040
                    if (len (O0OOO00000O0O0O0O ._list )>1000 ):#line:6041
                        O0OOO00000O0O0O0O ._list =[]#line:6042
                for O0O0OO0O0O0OOOOOO in range (OOO0000OO000OO0OO ,OO0O0O0O0O0O000O0 ):#line:6044
                    O0OOO00000O0O0O0O ._msgHandler (OOO000OOOO00OO0OO [O0O0OO0O0O0OOOOOO ])#line:6045
                OOO0000OO000OO0OO =OO0O0O0O0O0O000O0 #line:6047
            except Exception as O00OOO0OO0OOOO0O0 :#line:6048
                O0OOO00000O0O0O0O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"TSolaceMessageThreadClass send_request exception! exception={O00OOO0OO0OOOO0O0}")#line:6050
            finally :#line:6051
                sleep (0.001 )#line:6052
    def Add (O0O0O0O00OOOO00OO ,OOOO000O0OOO00000 :'InboundMessage'):#line:6054
        with O0O0O0O00OOOO00OO ._lock :#line:6055
            O0O0O0O00OOOO00OO ._list .append (OOOO000O0OOO00000 )#line:6056
    def on_message (O0O0O0O000O000O0O ,O0O000O000OO00000 :'InboundMessage'):#line:6058
        ""#line:6059
        O0O0O0O000O000O0O .Add (O0O000O000OO00000 )#line:6060
class TMyWorkItemThreadClass :#line:6065
    def __init__ (OO0O0O0OO000OOO00 ,O00OO0OOO0000O0O0 :str ,OOO00O0OOO000OO00 :logging .Logger ,OOOOO0O00O0O000O0 ):#line:6066
        OO0O0O0OO000OOO00 ._name =O00OO0OOO0000O0O0 #line:6067
        OO0O0O0OO000OOO00 ._msgHandler =OOOOO0O00O0O000O0 #line:6068
        OO0O0O0OO000OOO00 ._lock =Lock ()#line:6069
        OO0O0O0OO000OOO00 ._log =OOO00O0OOO000OO00 #line:6070
        OO0O0O0OO000OOO00 ._run =True #line:6071
        OO0O0O0OO000OOO00 ._queue =queue .Queue ()#line:6072
        O00O0O0OOO0O000OO =threading .Thread (target =OO0O0O0OO000OOO00 .OnThread ,name =OO0O0O0OO000OOO00 ._name )#line:6073
        O00O0O0OOO0O000OO .start ()#line:6074
    def OnThread (OOOOO00O00O0OOO0O ):#line:6076
        while OOOOO00O00O0OOO0O ._run :#line:6077
            try :#line:6079
                with OOOOO00O00O0OOO0O ._lock :#line:6080
                    while not OOOOO00O00O0OOO0O ._queue .empty ():#line:6081
                        OOOO0O000O0OOO000 =OOOOO00O00O0OOO0O ._queue .get ()#line:6082
                        OOOOO00O00O0OOO0O ._msgHandler (OOOO0O000O0OOO000 ["arg1"],OOOO0O000O0OOO000 ["arg2"])#line:6084
            except Exception as OO0OO0000OO00OO0O :#line:6086
                OOOOO00O00O0OOO0O ._log .Add (arg1 =SolLogType .Error ,arg2 =f"TMyWorkItemThreadClass send_request exception! exception={OO0OO0000OO00OO0O}")#line:6087
            finally :#line:6088
                sleep (0.001 )#line:6089
    def Add (O00OO0O0OOOO00OO0 ,**OO00OO0O00O00OO0O ):#line:6091
        with O00OO0O0OOOO00OO0 ._lock :#line:6092
            O00OO0O0OOOO00OO0 ._queue .put (OO00OO0O00O00OO0O )#line:6093
