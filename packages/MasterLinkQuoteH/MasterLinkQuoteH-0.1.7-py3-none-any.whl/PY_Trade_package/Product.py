from collections import UserDict
import decimal
from datetime import datetime
from PY_Trade_package.SolPYAPI_Model import *

class ProductBasic:
    "國內商品基本資料"
    def __init__(self) -> None:                
    #region 一般
        self.__Exchange:str="" 
        "交易所代碼"
        self.__Symbol:str="" 
        "商品代碼"
        self.__Category:str="" 
        "商品分類"
        self.__TodayRefPrice:str="" 
        "參考價"
        self.__RiseStopPrice:str="" 
        "漲停價"
        self.__FallStopPrice:str="" 
        "跌停價"
        self.__ChineseName:str="" 
        "商品中文名稱"
        self.__PreTotalMatchQty:str="" 
        "上一交易日成交總量"
        self.__PreTodayRefPrice:str="" 
        "上一交易日參考價"
        self.__PreClosePrice:str="" 
        "上一交易日收盤價"
    #endregion 一般
    #region TWSE
        self.__IndustryCategory:str = ""
        "產業別"
        self.__StockCategory:str = ""
        "證券別"
        self.__BoardRemark:str = ""
        "板別註記"
        self.__ClassRemark:str = ""
        "類股註記"
        self.__StockAnomalyCode:str = ""
        "股票異常代碼"
        self.__NonTenParValueRemark:str = ""
        "非十元面額註記"
        self.__AbnormalRecommendationIndicator:str = ""
        "異常推介個股註記"
        self.__AbnormalSecuritiesIndicator:str = ""
        "異常推介個股註記"
        self.__DayTradingRemark:str = ""
        "可現股當沖註記"
        self.__TradingUnit:str = ""
        "交易單位"
        self.__TickSize:str = ""
        "最小跳動點"
        self.__PreTotalTradingAmount:str = ""
        "上一交易日成交總額"
    #endregion TWSE
    
    #region TAIFEX
        self.__ProdKind:str = "" 
        "契約種類"
        self.__DecimalLocator:str = "" 
        "價格小數位數"
        self.__StrikePrice:str = "" 
        "選擇權履約價 由GKS商品代碼拆解出"
        
        self.__StrikePriceDecimalLocator:str = "" 
        "選擇權商品代號之履約價小數位數"
        self.__BeginDate:str = "" 
        "上市日期"
        self.__EndDate:str = "" 
        "下市日期"
        self.__FlowGroup:str = "" 
        "流程群組"
        self.__DeliveryDate:str = "" 
        "最後結算日"
        self.__DynamicBanding:str = "" 
        "適用動態價格穩定"
        self.__ContractSymbol:str = "" 
        "契約代號"
        self.__ContractName:str = "" 
        "契約中文名稱"
        self.__StockID:str = "" 
        "現貨股票代碼"
        self.__ContractSize:str = "" 
        "契約乘數"
        self.__StatusCode:str = "" 
        "狀態碼"
        self.__Currency:str = "" 
        "幣別"
        self.__AcceptQuoteFlag:str = "" 
        "是否可報價"
        self.__BlockTradeFlag:str = "" 
        "是否可鉅額交易"
        self.__ExpiryType:str = "" 
        "到期別"
        self.__UnderlyingType:str = "" 
        "現貨類別"
        self.__MarketCloseGroup:str = "" 
        "商品收盤時間群組"
        self.__EndSession:str = "" 
        "交易時段"
        self.__IsAfterHours:str = "" 
        "早午盤識別"
        self.__PreOpenInterest:str = "" 
        "昨日未平倉合約數"
        self.__PreSettlePrice:str = "" 
        "昨日結算價"
    #endregion TAIFEX
    #region property
    @property
    def Exchange(self):
        return self.__Exchange

    @Exchange.setter
    def Exchange(self, value):
        self.__Exchange = value

    @property
    def Symbol(self):
        return self.__Symbol

    @Symbol.setter
    def Symbol(self, value):
        self.__Symbol = value

    @property
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        self.__Category = value

    @property
    def TodayRefPrice(self):
        return self.__TodayRefPrice

    @TodayRefPrice.setter
    def TodayRefPrice(self, value):
        self.__TodayRefPrice = value

    @property
    def RiseStopPrice(self):
        return self.__RiseStopPrice

    @RiseStopPrice.setter
    def RiseStopPrice(self, value):
        self.__RiseStopPrice = value

    @property
    def FallStopPrice(self):
        return self.__FallStopPrice

    @FallStopPrice.setter
    def FallStopPrice(self, value):
        self.__FallStopPrice = value

    @property
    def ChineseName(self):
        return self.__ChineseName

    @ChineseName.setter
    def ChineseName(self, value):
        self.__ChineseName = value

    @property
    def PreTotalMatchQty(self):
        return self.__PreTotalMatchQty

    @PreTotalMatchQty.setter
    def PreTotalMatchQty(self, value):
        self.__PreTotalMatchQty = value

    @property
    def PreTodayRefPrice(self):
        return self.__PreTodayRefPrice

    @PreTodayRefPrice.setter
    def PreTodayRefPrice(self, value):
        self.__PreTodayRefPrice = value

    @property
    def PreClosePrice(self):
        return self.__PreClosePrice

    @PreClosePrice.setter
    def PreClosePrice(self, value):
        self.__PreClosePrice = value

    @property
    def IndustryCategory(self) -> str:
        return self.__IndustryCategory

    @IndustryCategory.setter
    def IndustryCategory(self, value: str) -> None:
        self.__IndustryCategory = value

    @property
    def StockCategory(self) -> str:
        return self.__StockCategory

    @StockCategory.setter
    def StockCategory(self, value: str) -> None:
        self.__StockCategory = value

    @property
    def BoardRemark(self) -> str:
        return self.__BoardRemark

    @BoardRemark.setter
    def BoardRemark(self, value: str) -> None:
        self.__BoardRemark = value

    @property
    def ClassRemark(self) -> str:
        return self.__ClassRemark

    @ClassRemark.setter
    def ClassRemark(self, value: str) -> None:
        self.__ClassRemark = value

    @property
    def StockAnomalyCode(self) -> str:
        return self.__StockAnomalyCode

    @StockAnomalyCode.setter
    def StockAnomalyCode(self, value: str) -> None:
        self.__StockAnomalyCode = value

    @property
    def NonTenParValueRemark(self) -> str:
        return self.__NonTenParValueRemark

    @NonTenParValueRemark.setter
    def NonTenParValueRemark(self, value: str) -> None:
        self.__NonTenParValueRemark = value

    @property
    def AbnormalRecommendationIndicator(self) -> str:
        return self.__AbnormalRecommendationIndicator

    @AbnormalRecommendationIndicator.setter
    def AbnormalRecommendationIndicator(self, value: str) -> None:
        self.__AbnormalRecommendationIndicator = value

    @property
    def AbnormalSecuritiesIndicator(self) -> str:
        return self.__AbnormalSecuritiesIndicator

    @AbnormalSecuritiesIndicator.setter
    def AbnormalSecuritiesIndicator(self, value: str) -> None:
        self.__AbnormalSecuritiesIndicator = value

    @property
    def DayTradingRemark(self) -> str:
        return self.__DayTradingRemark

    @DayTradingRemark.setter
    def DayTradingRemark(self, value: str) -> None:
        self.__DayTradingRemark = value

    @property
    def TradingUnit(self) -> str:
        return self.__TradingUnit

    @TradingUnit.setter
    def TradingUnit(self, value: str) -> None:
        self.__TradingUnit = value

    @property
    def TickSize(self) -> str:
        return self.__TickSize

    @TickSize.setter
    def TickSize(self, value: str) -> None:
        self.__TickSize = value

    @property
    def PreTotalTradingAmount(self) -> str:
        return self.__PreTotalTradingAmount

    @PreTotalTradingAmount.setter
    def PreTotalTradingAmount(self, value: str) -> None:
        self.__PreTotalTradingAmount = value
    @property
    def ProdKind(self) -> str:
        return self.__ProdKind

    @ProdKind.setter
    def ProdKind(self, value: str):
        self.__ProdKind = value

    @property
    def DecimalLocator(self) -> str:
        return self.__DecimalLocator

    @DecimalLocator.setter
    def DecimalLocator(self, value: str):
        self.__DecimalLocator = value

    @property
    def StrikePrice(self) -> str:
        return self.__StrikePrice

    @StrikePrice.setter
    def StrikePrice(self, value: str):
        self.__StrikePrice = value

    @property
    def StrikePriceDecimalLocator(self) -> str:
        return self.__StrikePriceDecimalLocator

    @StrikePriceDecimalLocator.setter
    def StrikePriceDecimalLocator(self, value: str):
        self.__StrikePriceDecimalLocator = value

    @property
    def BeginDate(self) -> str:
        return self.__BeginDate

    @BeginDate.setter
    def BeginDate(self, value: str):
        self.__BeginDate = value

    @property
    def EndDate(self) -> str:
        return self.__EndDate

    @EndDate.setter
    def EndDate(self, value: str):
        self.__EndDate = value

    @property
    def FlowGroup(self) -> str:
        return self.__FlowGroup

    @FlowGroup.setter
    def FlowGroup(self, value: str):
        self.__FlowGroup = value

    @property
    def DeliveryDate(self) -> str:
        return self.__DeliveryDate

    @DeliveryDate.setter
    def DeliveryDate(self, value: str):
        self.__DeliveryDate = value

    @property
    def DynamicBanding(self) -> str:
        return self.__DynamicBanding

    @DynamicBanding.setter
    def DynamicBanding(self, value: str):
        self.__DynamicBanding = value

    @property
    def ContractSymbol(self) -> str:
        return self.__ContractSymbol

    @ContractSymbol.setter
    def ContractSymbol(self, value: str):
        self.__ContractSymbol = value

    @property
    def ContractName(self) -> str:
        return self.__ContractName

    @ContractName.setter
    def ContractName(self, value: str):
        self.__ContractName = value
    @property
    def StockID(self) -> str:
        return self.__StockID

    @StockID.setter
    def StockID(self, stock_id: str) -> None:
        self.__StockID = stock_id

    @property
    def ContractSize(self) -> str:
        return self.__ContractSize

    @ContractSize.setter
    def ContractSize(self, contract_size: str) -> None:
        self.__ContractSize = contract_size

    @property
    def StatusCode(self) -> str:
        return self.__StatusCode

    @StatusCode.setter
    def StatusCode(self, status_code: str) -> None:
        self.__StatusCode = status_code

    @property
    def Currency(self) -> str:
        return self.__Currency

    @Currency.setter
    def Currency(self, currency: str) -> None:
        self.__Currency = currency

    @property
    def AcceptQuoteFlag(self) -> str:
        return self.__AcceptQuoteFlag

    @AcceptQuoteFlag.setter
    def AcceptQuoteFlag(self, accept_quote_flag: str) -> None:
        self.__AcceptQuoteFlag = accept_quote_flag

    @property
    def BlockTradeFlag(self) -> str:
        return self.__BlockTradeFlag

    @BlockTradeFlag.setter
    def BlockTradeFlag(self, block_trade_flag: str) -> None:
        self.__BlockTradeFlag = block_trade_flag

    @property
    def ExpiryType(self) -> str:
        return self.__ExpiryType

    @ExpiryType.setter
    def ExpiryType(self, expiry_type: str) -> None:
        self.__ExpiryType = expiry_type

    @property
    def UnderlyingType(self) -> str:
        return self.__UnderlyingType

    @UnderlyingType.setter
    def UnderlyingType(self, underlying_type: str) -> None:
        self.__UnderlyingType = underlying_type

    @property
    def MarketCloseGroup(self) -> str:
        return self.__MarketCloseGroup

    @MarketCloseGroup.setter
    def MarketCloseGroup(self, market_close_group: str) -> None:
        self.__MarketCloseGroup = market_close_group

    @property
    def EndSession(self) -> str:
        return self.__EndSession

    @EndSession.setter
    def EndSession(self, end_session: str) -> None:
        self.__EndSession = end_session

    @property
    def IsAfterHours(self) -> str:
        return self.__IsAfterHours

    @IsAfterHours.setter
    def IsAfterHours(self, is_after_hours: str) -> None:
        self.__IsAfterHours = is_after_hours

    @property
    def PreOpenInterest(self) -> str:
        return self.__PreOpenInterest

    @PreOpenInterest.setter
    def PreOpenInterest(self, pre_open_interest: str) -> None:
        self.__PreOpenInterest = pre_open_interest

    @property
    def PreSettlePrice(self) -> str:
        return self.__PreSettlePrice

    @PreSettlePrice.setter
    def PreSettlePrice(self, pre_settle_price: str) -> None:
        self.__PreSettlePrice = pre_settle_price
    
    #endregion property
    def __str__(self):
        return f"""交易所代碼:{self.Exchange} 商品代碼:{self.Symbol} 商品分類:{self.Category} 參考價:{self.TodayRefPrice} 漲停價:{self.RiseStopPrice} 跌停價:{self.FallStopPrice} 商品中文名稱:{self.ChineseName}
上一交易日成交總量:{self.PreTotalMatchQty} 上一交易日參考價:{self.PreTodayRefPrice} 上一交易日收盤價:{self.PreClosePrice} 產業別:{self.IndustryCategory} 證券別:{self.StockCategory} 板別註記:{self.BoardRemark}
類股註記:{self.ClassRemark} 股票異常代碼:{self.StockAnomalyCode} 非十元面額註記:{self.NonTenParValueRemark} 異常推介個股註記:{self.AbnormalRecommendationIndicator} 異常推介個股註記:{self.AbnormalSecuritiesIndicator}
可現股當沖註記:{self.DayTradingRemark} 交易單位:{self.TradingUnit} 最小跳動點:{self.TickSize} 上一交易日成交總額:{self.PreTotalTradingAmount} 契約種類:{self.ProdKind} 價格小數位數:{self.DecimalLocator} 選擇權履約價:{self.StrikePrice}
選擇權商品代號小數位:{self.StrikePriceDecimalLocator} 上市日期:{self.BeginDate} 下市日期:{self.EndDate} 流程群組:{self.FlowGroup} 最後結算日:{self.DeliveryDate} 適用動態價格穩定:{self.DynamicBanding} 契約代號:{self.ContractSymbol}
契約中文名稱:{self.ContractName} 現貨股票代碼:{self.StockID} 契約乘數:{self.ContractSize} 狀態碼:{self.StatusCode} 幣別:{self.Currency} 是否可報價:{self.AcceptQuoteFlag} 是否可鉅額交易:{self.BlockTradeFlag} 到期別:{self.ExpiryType}
現貨類別:{self.UnderlyingType} 商品收盤時間群組:{self.MarketCloseGroup} 交易時段:{self.EndSession} 早午盤識別:{self.IsAfterHours} 昨日未平倉合約數:{self.PreOpenInterest} 昨日結算價:{self.PreSettlePrice}"""
class ProductTick:
    "國內商品Tick資料"
    #region Protected
    def __init__(self) -> None:        
        self.__CacheStatus:int = -1 #-1: init, 0:live, 1:cached
        self.__Exchange:str=""#交易所
        self.__Symbol:str=""#商品代號
        self.__MatchTime:str = ""#成交資料時間(交易所) 
        self.__OrderBookTime:str = ""#五檔資料時間(交易所)
        self.__TxSeq=0#交易所序號(成交資訊) 
        self.__ObSeq=0#交易所序號(五檔資訊)
        self.__IsTxTrial:bool=False#是否為成交試撮資料
        self.__Is5QTrial:bool=False#是否為五檔試撮資料
        self.__IsTrail:bool=False#是否為五檔試撮資料
        self.__DecimalLocator:str = ""#價格欄位小數位數
        self.__MatchPrice:str = ""#成交價
        self.__MatchQty:str = ""#商品成交量
        self.__MatchPriceList:list = [] #new List<string>();
        self.__MatchQtyList:list = []#new List<string>();
        self.__MatchBuyCount:str = ""#累計買進成交筆數
        self.__MatchSellCount:str = ""#累計賣出成交筆數
        self.__TotalMatchQty:str = ""#商品成交總量
        self.__TotalTradingAmount:str= ""#商品成交總額
        self.__TradingUnit:str = ""#交易單位
        self.__DayHigh:str = ""#當日最高價
        self.__DayLow:str = ""#當日最低價   
        self.__RefPrice:str = ""#參考價

        self.__BuyPrice:list = ['','','','','']#Enumerable.Repeat(string.Empty, 10).ToArray();
        self.__BuyQty:list = ['','','','','']#Enumerable.Repeat(string.Empty, 10).ToArray();
        self.__SellPrice:list = ['','','','','']#Enumerable.Repeat(string.Empty, 10).ToArray();
        self.__SellQty:list = ['','','','','']#Enumerable.Repeat(string.Empty, 10).ToArray();

        self.__AllMarketAmount:str = ""#整體市場成交總額
        self.__AllMarketVolume:str = ""#整體市場成交數量
        self.__AllMarketCnt:str = ""#整體市場成交筆數
        self.__AllMarketBuyCnt:str = ""#整體市場委託買進筆數
        self.__AllMarketSellCnt:str = ""#整體市場委託賣出筆數
        self.__AllMarketBuyQty:str = ""#整體市場委託買進數量
        self.__AllMarketSellQty:str = ""#整體市場委託賣出數量
        self.__IsFixedPriceTransaction:str = ""#是否為定盤交易
        self.__OpenPrice:str = ""#開盤價
        self.__Change:str = ""
        self.__ChangePercent:str = ""
        self.__FirstDerivedBuyPrice:str = ""#衍生委託單第一檔買進價格
        self.__FirstDerivedBuyQty:str = ""#衍生委託單第一檔買進價格數量
        self.__FirstDerivedSellPrice:str = ""#衍生委託單第一檔賣出價格數量
        self.__FirstDerivedSellQty:str = ""#衍生委託單第一檔賣出價格數量
        self.__TotalBuyOrder:str = ""#買進累計委託筆數
        self.__TotalBuyQty:str = ""#買進累計委託合約數
        self.__TotalSellOrder:str = ""#賣出累計委託筆數
        self.__TotalSellQty:str = ""#賣出累計委託合約數
        self.__Delta:str = ""
        self.__ClosePrice:str = ""#收盤價
        self.__SettlePrice:str = ""#結算價
        self.__OpenInterest:str = ""#未平倉合約數
    #endregion Protected
    def __str__(self):
        return f"""CacheStatus:{self.CacheStatus} Exchange:{self.Exchange} Symbol:{self.Symbol} MatchTime:{self.MatchTime} OrderBookTime:{self.OrderBookTime} TxSeq:{self.TxSeq} ObSeq:{self.ObSeq} IsTxTrial:{self.IsTxTrial} Is5QTrial:{self.Is5QTrial}
IsTrail:{self.IsTrail} DecimalLocator:{self.DecimalLocator} MatchPrice:{self.MatchPrice} MatchQty:{self.MatchQty} MatchPriceList:{self.MatchPriceList} MatchQtyList:{self.MatchQtyList} MatchBuyCount:{self.MatchBuyCount} MatchSellCount:{self.MatchSellCount}
TotalMatchQty:{self.TotalMatchQty} TotalTradingAmount:{self.TotalTradingAmount} TradingUnit:{self.TradingUnit} DayHigh:{self.DayHigh} DayLow:{self.DayLow} RefPrice:{self.RefPrice} BuyPrice:{self.BuyPrice} BuyQty:{self.BuyQty} SellPrice:{self.SellPrice} SellQty:{self.SellQty}
AllMarketAmount:{self.AllMarketAmount} AllMarketVolume:{self.AllMarketVolume} AllMarketCnt:{self.AllMarketCnt} AllMarketBuyCnt:{self.AllMarketBuyCnt} AllMarketSellCnt:{self.AllMarketSellCnt} AllMarketBuyQty:{self.AllMarketBuyQty} AllMarketSellQty:{self.AllMarketSellQty} IsFixedPriceTransaction:{self.IsFixedPriceTransaction}
OpenPrice:{self.OpenPrice} Change:{self.Change} ChangePercent:{self.ChangePercent} FirstDerivedBuyPrice:{self.FirstDerivedBuyPrice} FirstDerivedBuyQty:{self.FirstDerivedBuyQty} FirstDerivedSellPrice:{self.FirstDerivedSellPrice} FirstDerivedSellQty:{self.FirstDerivedSellQty} TotalBuyOrder:{self.TotalBuyOrder} TotalBuyQty:{self.TotalBuyQty}
TotalSellOrder:{self.TotalSellOrder} TotalSellQty:{self.TotalSellQty} Delta:{self.Delta} ClosePrice:{self.ClosePrice} SettlePrice:{self.SettlePrice} OpenInterest:{self.OpenInterest} """
    #region set property    
    @property
    def CacheStatus(self) -> int:
        return self.__CacheStatus

    @CacheStatus.setter
    def CacheStatus(self, value: int) -> None:
        self.__CacheStatus = value

    @property
    def Exchange(self) -> str:
        return self.__Exchange

    @Exchange.setter
    def Exchange(self, value: str) -> None:
        self.__Exchange = value
        
    @property
    def Symbol(self) -> str:
        return self.__Symbol

    @Symbol.setter
    def Symbol(self, value: str) -> None:
        self.__Symbol = value
        
    @property
    def MatchTime(self) -> str:
        return self.__MatchTime

    @MatchTime.setter
    def MatchTime(self, value: str) -> None:
        self.__MatchTime = value
        
    @property
    def OrderBookTime(self) -> str:
        return self.__OrderBookTime

    @OrderBookTime.setter
    def OrderBookTime(self, value: str) -> None:
        self.__OrderBookTime = value
        
    @property
    def TxSeq(self) -> int:
        return self.__TxSeq

    @TxSeq.setter
    def TxSeq(self, value: int) -> None:
        self.__TxSeq = value
        
    @property
    def ObSeq(self) -> int:
        return self.__ObSeq

    @ObSeq.setter
    def ObSeq(self, value: int) -> None:
        self.__ObSeq = value
        
    @property
    def IsTxTrial(self) -> bool:
        return self.__IsTxTrial

    @IsTxTrial.setter
    def IsTxTrial(self, value: bool) -> None:
        self.__IsTxTrial = value
        
    @property
    def Is5QTrial(self) -> bool:
        return self.__Is5QTrial

    @Is5QTrial.setter
    def Is5QTrial(self, value: bool) -> None:
        self.__Is5QTrial = value
        
    @property
    def IsTrail(self) -> bool:
        return self.__IsTrail

    @IsTrail.setter
    def IsTrail(self, value: bool) -> None:
        self.__IsTrail = value
    @property
    def DecimalLocator(self) -> str:
        return self.__DecimalLocator

    @DecimalLocator.setter
    def DecimalLocator(self, value: str) -> None:
        self.__DecimalLocator = value

    @property
    def MatchPrice(self) -> str:
        return self.__MatchPrice

    @MatchPrice.setter
    def MatchPrice(self, value: str) -> None:
        self.__MatchPrice = value

    @property
    def MatchQty(self) -> str:
        return self.__MatchQty

    @MatchQty.setter
    def MatchQty(self, value: str) -> None:
        self.__MatchQty = value

    @property
    def MatchPriceList(self) -> list:
        return self.__MatchPriceList

    @MatchPriceList.setter
    def MatchPriceList(self, value: list) -> None:
        self.__MatchPriceList = value

    @property
    def MatchQtyList(self) -> list:
        return self.__MatchQtyList

    @MatchQtyList.setter
    def MatchQtyList(self, value: list) -> None:
        self.__MatchQtyList = value

    @property
    def MatchBuyCount(self) -> str:
        return self.__MatchBuyCount

    @MatchBuyCount.setter
    def MatchBuyCount(self, value: str) -> None:
        self.__MatchBuyCount = value

    @property
    def MatchSellCount(self) -> str:
        return self.__MatchSellCount

    @MatchSellCount.setter
    def MatchSellCount(self, value: str) -> None:
        self.__MatchSellCount = value

    @property
    def TotalMatchQty(self) -> str:
        return self.__TotalMatchQty

    @TotalMatchQty.setter
    def TotalMatchQty(self, value: str) -> None:
        self.__TotalMatchQty = value

    @property
    def TotalTradingAmount(self) -> str:
        return self.__TotalTradingAmount

    @TotalTradingAmount.setter
    def TotalTradingAmount(self, value: str) -> None:
        self.__TotalTradingAmount = value

    @property
    def TradingUnit(self) -> str:
        return self.__TradingUnit

    @TradingUnit.setter
    def TradingUnit(self, value: str) -> None:
        self.__TradingUnit = value

    @property
    def DayHigh(self) -> str:
        return self.__DayHigh

    @DayHigh.setter
    def DayHigh(self, value: str) -> None:
        self.__DayHigh = value

    @property
    def DayLow(self) -> str:
        return self.__DayLow

    @DayLow.setter
    def DayLow(self, value: str) -> None:
        self.__DayLow = value
    @property
    def RefPrice(self) -> str:
        return self.__RefPrice

    @RefPrice.setter
    def RefPrice(self, value: str) -> None:
        self.__RefPrice = value

    @property
    def BuyPrice(self) -> list:
        return self.__BuyPrice

    @BuyPrice.setter
    def BuyPrice(self, value: list) -> None:
        self.__BuyPrice = value

    @property
    def BuyQty(self) -> list:
        return self.__BuyQty

    @BuyQty.setter
    def BuyQty(self, value: list) -> None:
        self.__BuyQty = value

    @property
    def SellPrice(self) -> list:
        return self.__SellPrice

    @SellPrice.setter
    def SellPrice(self, value: list) -> None:
        self.__SellPrice = value

    @property
    def SellQty(self) -> list:
        return self.__SellQty

    @SellQty.setter
    def SellQty(self, value: list) -> None:
        self.__SellQty = value

    @property
    def AllMarketAmount(self) -> str:
        return self.__AllMarketAmount

    @AllMarketAmount.setter
    def AllMarketAmount(self, value: str) -> None:
        self.__AllMarketAmount = value

    @property
    def AllMarketVolume(self) -> str:
        return self.__AllMarketVolume

    @AllMarketVolume.setter
    def AllMarketVolume(self, value: str) -> None:
        self.__AllMarketVolume = value

    @property
    def AllMarketCnt(self) -> str:
        return self.__AllMarketCnt

    @AllMarketCnt.setter
    def AllMarketCnt(self, value: str) -> None:
        self.__AllMarketCnt = value     
    @property
    def AllMarketBuyCnt(self) -> str:
        return self.__AllMarketBuyCnt

    @AllMarketBuyCnt.setter
    def AllMarketBuyCnt(self, value: str) -> None:
        self.__AllMarketBuyCnt = value

    @property
    def AllMarketSellCnt(self) -> str:
        return self.__AllMarketSellCnt

    @AllMarketSellCnt.setter
    def AllMarketSellCnt(self, value: str) -> None:
        self.__AllMarketSellCnt = value

    @property
    def AllMarketBuyQty(self) -> str:
        return self.__AllMarketBuyQty

    @AllMarketBuyQty.setter
    def AllMarketBuyQty(self, value: str) -> None:
        self.__AllMarketBuyQty = value

    @property
    def AllMarketSellQty(self) -> str:
        return self.__AllMarketSellQty

    @AllMarketSellQty.setter
    def AllMarketSellQty(self, value: str) -> None:
        self.__AllMarketSellQty = value

    @property
    def IsFixedPriceTransaction(self) -> str:
        return self.__IsFixedPriceTransaction

    @IsFixedPriceTransaction.setter
    def IsFixedPriceTransaction(self, value: str) -> None:
        self.__IsFixedPriceTransaction = value

    @property
    def OpenPrice(self) -> str:
        return self.__OpenPrice

    @OpenPrice.setter
    def OpenPrice(self, value: str) -> None:
        self.__OpenPrice = value

    @property
    def Change(self) -> str:
        try:
            if len(self.RefPrice) > 0 and len(self.MatchPrice) > 0 and self.RefPrice.isspace() == False and self.MatchPrice.isspace() == False:
                dRefPrice:float = float(self.RefPrice)
                dPrice:float = float(self.MatchPrice)
                return "{:.4f}".format(dPrice - dRefPrice)              
            else:
                return ""
        # return self.__Change
        except Exception as ex:
            return ""

    @Change.setter
    def Change(self, value: str) -> None:
        self.__Change = value

    @property
    def ChangePercent(self) -> str:
        try:
            if len(self.RefPrice)>0 and len(self.MatchPrice)>0 and self.RefPrice.isspace() == False and self.MatchPrice.isspace() == False:                
                dRefPrice:float = float(self.RefPrice)
                dPrice:float = float(self.MatchPrice)
                return "{:.4f}".format(( dPrice - dRefPrice ) / dRefPrice)
            else:
                return ""
        except Exception as ex:
            return ""
        # return self.__ChangePercent

    @ChangePercent.setter
    def ChangePercent(self, value: str) -> None:
        self.__ChangePercent = value

    @property
    def FirstDerivedBuyPrice(self) -> str:
        return self.__FirstDerivedBuyPrice

    @FirstDerivedBuyPrice.setter
    def FirstDerivedBuyPrice(self, value: str) -> None:
        self.__FirstDerivedBuyPrice = value

    @property
    def FirstDerivedBuyQty(self) -> str:
        return self.__FirstDerivedBuyQty

    @FirstDerivedBuyQty.setter
    def FirstDerivedBuyQty(self, value: str) -> None:
        self.__FirstDerivedBuyQty = value

    @property
    def FirstDerivedSellPrice(self) -> str:
        return self.__FirstDerivedSellPrice

    @FirstDerivedSellPrice.setter
    def FirstDerivedSellPrice(self, value: str) -> None:
        self.__FirstDerivedSellPrice = value

    @property
    def FirstDerivedSellQty(self) -> str:
        return self.__FirstDerivedSellQty
    
    @FirstDerivedSellQty.setter
    def FirstDerivedSellQty(self, value) -> str:
        self.__FirstDerivedSellQty = value

    @property
    def TotalBuyOrder(self):
        return self.__TotalBuyOrder

    @TotalBuyOrder.setter
    def TotalBuyOrder(self, value):
        self.__TotalBuyOrder = value
        
    @property
    def TotalBuyQty(self):
        return self.__TotalBuyQty

    @TotalBuyQty.setter
    def TotalBuyQty(self, value):
        self.__TotalBuyQty = value
    @property
    def TotalSellOrder(self) -> str:
        return self.__TotalSellOrder

    @TotalSellOrder.setter
    def TotalSellOrder(self, value: str):
        self.__TotalSellOrder = value

    @property
    def TotalSellQty(self) -> str:
        return self.__TotalSellQty

    @TotalSellQty.setter
    def TotalSellQty(self, value: str):
        self.__TotalSellQty = value

    @property
    def Delta(self) -> str:
        return self.__Delta

    @Delta.setter
    def Delta(self, value: str):
        self.__Delta = value

    @property
    def ClosePrice(self) -> str:
        return self.__ClosePrice

    @ClosePrice.setter
    def ClosePrice(self, value: str):
        self.__ClosePrice = value

    @property
    def SettlePrice(self) -> str:
        return self.__SettlePrice

    @SettlePrice.setter
    def SettlePrice(self, value: str):
        self.__SettlePrice = value

    @property
    def OpenInterest(self) -> str:
        return self.__OpenInterest

    @OpenInterest.setter
    def OpenInterest(self, value: str):
        self.__OpenInterest = value

#endregion property
    #region get buy sell
    def Buy1Price(self):
        return self.BuyPrice[0]
    def Buy2Price(self):
        return self.BuyPrice[1]
    def Buy2Price(self):
        return self.BuyPrice[2]
    def Buy3Price(self):
        return self.BuyPrice[3]
    def Buy4Price(self):
        return self.BuyPrice[4]

    def Buy1Qty(self):
        return self.BuyQty[0]
    def Buy2Qty(self):
        return self.BuyQty[1]
    def Buy3Qty(self):
        return self.BuyQty[2]
    def Buy4Qty(self):
        return self.BuyQty[3]
    def Buy5Qty(self):
        return self.BuyQty[4]        

    def Sell1Price(self):
         return self.SellPrice[0]
    def Sell2Price(self):
         return self.SellPrice[1]
    def Sell3Price(self):
         return self.SellPrice[2]
    def Sell4Price(self):
         return self.SellPrice[3]
    def Sell5Price(self):
         return self.SellPrice[4]        

    def Sell1Qty(self):
        return self.SellQty[0]
    def Sell2Qty(self):
        return self.SellQty[1]
    def Sell3Qty(self):
        return self.SellQty[2]
    def Sell4Qty(self):
        return self.SellQty[3]
    def Sell5Qty(self):
        return self.SellQty[4]
    #endregion get buy sell 
#==================================================
#國內商品商品快照
class ProductSnapshot:
    BasicData:ProductBasic = None
    "國內商品基本資料"
    TickData:ProductTick = None
    "國內商品Tick資料"
    def __init__(self) -> None:
        pass
# ==================================================
# 期貨
class ProductBasic_Fut(ProductBasic):
    # def __init__(self, aData:TFutQuoteData) -> None:
    def __init__(self, aData) -> None:

        super().__init__()

        #region BAS

        self.DecimalLocator = str(aData.BAS.DECIMAL_LOCATOR_Org)

        self.TodayRefPrice = aData.BAS.Get_RefPrice2Str()#參考價
        self.RiseStopPrice = aData.BAS.Get_LimitPrice_Up2Str()#漲停價
        self.FallStopPrice = aData.BAS.Get_LimitPrice_Down2Str()#跌停價 
        self.PreTodayRefPrice = aData.BAS.Get_PreTodayRefPrice2Str()#昨日參考價
        self.PreClosePrice = aData.BAS.Get_PreClosePrice2Str()#昨日收盤價
        self.PreSettlePrice = aData.BAS.Get_PreSettlePrice2Str()#昨日結算價
    

        self.ProdKind = aData.BAS.ProdKind
        self.StrikePriceDecimalLocator = aData.BAS.StrikePriceDecimalLocator
        self.BeginDate = aData.BAS.BeginDate
        self.EndDate = aData.BAS.EndDate
        self.FlowGroup = aData.BAS.FlowGroup
        self.DeliveryDate = aData.BAS.DeliveryDate
        self.DynamicBanding = aData.BAS.DynamicBanding
        self.Symbol = aData.BAS.OrdProdID
        self.ContractSymbol = aData.BAS.ProdID
        self.ContractName = aData.BAS.FutName
        self.StockID = aData.BAS.StkNo
        self.ContractSize = aData.BAS.ValuePerUnitOrg
        self.StatusCode = aData.BAS.StatusCode
        self.Currency = aData.BAS.Currency
        self.AcceptQuoteFlag = aData.BAS.AcceptQuoteFlag
        self.BlockTradeFlag = aData.BAS.BlockTradeFlag
        self.ExpiryType = aData.BAS.ExpiryType
        self.UnderlyingType = aData.BAS.UnderlyingType
        self.MarketCloseGroup = aData.BAS.MarketCloseGroup
        self.EndSession = aData.BAS.EndSession
        self.IsAfterHours = aData.BAS.MktType
        self.PreOpenInterest = aData.BAS.PreOpenInterest
        self.PreTotalMatchQty = aData.BAS.PreTotalMatchQty
        self.TickSize = aData.BAS.TickSizeInfo

        self.StrikePrice = aData.BAS.StrikeP

        if len(self.Symbol) >= 3:
            self.ChineseName = aData.BAS.FutName + self.Symbol[3:]
        else:
            self.ChineseName = aData.BAS.FutName + aData.BAS.SettleMth

        #endregion

        if aData.HL.HasHL == False: #盤前試撮, 不會有HL
            self.Exchange = "TWF"
        else:
            self.Exchange = aData.HL.Exchange
            self.Category = aData.HL.Market
class ProductTick_Fut(ProductTick):    
    def TranTime(self, aDate:str)->str:
        "時間轉換"    
        try:        
            exTime = datetime.strptime(aDate, "%H%M%S.%f")
            return exTime.strftime("%H:%M:%S.%f")
        except Exception as ex:
            pass
        return aDate
    
    def Upt_TX(self, p_tmpQtTx): #TFutQtTX
        try:        
            import PY_Trade_package.SolPYAPIOB
            tmpQtTx:PY_Trade_package.SolPYAPIOB.TFutQtTX = p_tmpQtTx
            self.TxSeq = tmpQtTx.Get_DealSn()
            self.MatchTime = self.TranTime(tmpQtTx.DealTime)
            self.MatchPrice = tmpQtTx.Get_DealPrice2Str()
            self.MatchQty = tmpQtTx.DealQty
            self.TotalMatchQty = tmpQtTx.TotQty
            self.MatchBuyCount = tmpQtTx.SumBuyDealCount
            self.MatchSellCount = tmpQtTx.SumSellDealCount
            self.DayHigh = str(tmpQtTx.HighPrice)
            self.DayLow = str(tmpQtTx.LowPrice)
            self.IsTrail = tmpQtTx.TryMark = TSolQuoteFutSet.TryMark_Yes

            self.MatchPriceList.clear()
            self.MatchQtyList.clear()
            fDealCount = tmpQtTx.Get_DealCount() #成交價量檔數(一筆行情, 多筆成交價量)
            for fDealIdx in range(fDealCount):
                fDealQty = tmpQtTx.Get_DealQty2IdxVal(fDealIdx) #成交單量
                fDealPrice = tmpQtTx.Get_DealQty2IdxVal(fDealIdx) #成交價
                if fDealQty > 0 and fDealPrice > 0:
                    self.MatchPriceList.append(str(fDealPrice))
                    self.MatchQtyList.append(str(fDealQty))
            if len(self.MatchPriceList) > 0:
                if self.OpenPrice == "":
                    self.OpenPrice = self.MatchPriceList[0]
                elif self.OpenPrice == "0":
                    self.OpenPrice = self.MatchPriceList[0]
            return True
            
        except Exception as ex:
            pass
        return False
    def Upt_5Q(self, p_tmpQt5Q):#TFutQt5Q
    # def Upt_5Q(self, tmpQt5Q):
        try:
            import PY_Trade_package.SolPYAPIOB
            tmpQt5Q:PY_Trade_package.SolPYAPIOB.TFutQt5Q = p_tmpQt5Q
            self.ObSeq = tmpQt5Q.Get_Sn()
            self.OrderBookTime = self.TranTime(tmpQt5Q.DataTime)
            self.IsTrail = tmpQt5Q.TryMark = TSolQuoteFutSet.TryMark_Yes

            for i in range(5):
                price:decimal = 0
                price = tmpQt5Q.Get_S5Q_P2Dec(i + 1) #取得賣5檔價格
                self.SellPrice[i] = str(price)
                self.SellQty[i] = tmpQt5Q.S5Q_QOrg(i + 1) #賣5檔-量-的原始字串內容

                price = tmpQt5Q.Get_B5Q_P2Dec(i + 1) #取得買5檔-價格
                self.BuyPrice[i] = str(price)
                self.BuyQty[i] = tmpQt5Q.B5Q_QOrg(i + 1) #買5檔-量-的原始字串內容

            self.FirstDerivedBuyPrice = tmpQt5Q.Get_FirstDerivedBuyPrice()
            self.FirstDerivedBuyQty = tmpQt5Q.FirstDerivedBuyQty
            self.FirstDerivedSellPrice = tmpQt5Q.Get_FirstDerivedSellPrice()
            self. FirstDerivedSellQty = tmpQt5Q.FirstDerivedSellQty

            return True
        
        except Exception as ex:
            pass
        return False
    def Upt_5QTOT(self, p_tmpQt5QTOT):#TFutQt5QTOT
        try:
            import PY_Trade_package.SolPYAPIOB
            tmpQt5QTOT:PY_Trade_package.SolPYAPIOB.TFutQt5QTOT = p_tmpQt5QTOT
            self.TotalBuyOrder = tmpQt5QTOT.SumBuyOrderCount #委買筆數
            self.TotalBuyQty = tmpQt5QTOT.SumBuyOrderQty #委買口數
            self.TotalSellOrder = tmpQt5QTOT.SumSellOrderCount #委賣筆數
            self.TotalSellQty = tmpQt5QTOT.SumSellOrderQty #委賣口數
            return True
        
        except Exception as ex:
            pass
        return False
        

    # def __init__(self, aData:TFutQuoteData) -> None:
    def __init__(self, aData) -> None:        
        super().__init__()
        if aData is None:
            return
        if aData.HL.HasHL == False:#盤前試撮, 不會有HL
            return
           
        self.Exchange = aData.HL.Exchange#//市場別(TWS/TWF)
        self.Symbol = aData.HL.Symbol#//委託商品代碼(TXFA2)
        self.MatchTime = self.TranTime(aData.HL.DealTime)#撮合時間(成交)(EX:173547.32700)
        self.OrderBookTime = self.MatchTime
        self.TxSeq = aData.HL.Get_DealSn()#//成交序號
        self.ObSeq = aData.HL.Get_Sn_5Q()#//五檔序號

        self.IsTxTrial = aData.HL.TryMark_Deal == TSolQuoteFutSet.TryMark_Yes#//成交試撮註記(試撮=1, 非試撮=0)
        self.Is5QTrial = aData.HL.TryMark_5Q == TSolQuoteFutSet.TryMark_Yes#//五檔試撮註記(試撮=1, 非試撮=0)
        self.IsTrail = self.IsTxTrial if (self.TxSeq >= self.ObSeq) else self.Is5QTrial

        self.DecimalLocator = str(aData.HL.DECIMAL_LOCATOR_Org)#//價格欄位小數位數
        self.MatchPrice = aData.HL.Get_DealPrice2Str()#//成交價
        self.MatchQty = aData.HL.DealQty#//成交單量       

        self.MatchBuyCount = ""
        self.MatchSellCount = ""
        self.TotalMatchQty = aData.HL.TotQty#//成交總量
        self.TotalTradingAmount = aData.HL.TotAmt#//成交總額 //???????????
        self.TradingUnit = ""
        self.DayHigh = aData.HL.Get_HighPrice2Str()#//當日最高價
        self.DayLow = aData.HL.Get_LowPrice2Str()#//當日最低價
        self.RefPrice = aData.BAS.Get_RefPrice2Str()#//參考價
        for i in range(5):#(int i=0;i<5;i++)        
            price:decimal = 0
            price = aData.HL.Get_S5Q_P2Dec(i + 1) #取得賣5檔價格
            self.SellPrice[i] = str(price)
            self.SellQty[i] = aData.HL.S5Q_QOrg(i + 1) #賣5檔-量-的原始字串內容

            price = aData.HL.Get_B5Q_P2Dec(i + 1) #取得買5檔-價格
            self.BuyPrice[i] = str(price)
            self.BuyQty[i] = aData.HL.B5Q_QOrg(i + 1) #//買5檔-量-的原始字串內容
        

        self.AllMarketAmount = ""
        self.AllMarketVolume = ""
        self.AllMarketCnt = ""
        self.AllMarketBuyCnt = ""
        self.AllMarketSellCnt = ""
        self.AllMarketBuyQty = ""
        self.AllMarketSellQty = ""

        self.IsFixedPriceTransaction = ""

        self.OpenPrice = aData.HL.Get_OpenPrice2Str() #//開盤價

        self.FirstDerivedBuyPrice = aData.HL.Get_FirstDerivedBuyPrice() #衍生委託單第一檔買進價格
        self.FirstDerivedBuyQty = aData.HL.FirstDerivedBuyQty #衍生委託單第一檔買進價格數量
        self.FirstDerivedSellPrice = aData.HL.Get_FirstDerivedSellPrice() #衍生委託單第一檔賣出價格數量
        self.FirstDerivedSellQty = aData.HL.FirstDerivedSellQty #衍生委託單第一檔賣出價格數量

        self.TotalBuyOrder = ""
        self.TotalBuyQty = ""
        self.TotalSellOrder = ""
        self.TotalSellQty = ""
        self.Delta = ""
        self.ClosePrice = aData.HL.Get_ClosePrice() #收盤價
        self.SettlePrice = aData.HL.Get_SettlePrice() #結算價

        self.OpenInterest = aData.HL.OpenInterest #未平倉合約數
# ==================================================
# 證券
class ProductBasic_Stk(ProductBasic):
    
        # public ProductBasic_Stk() { }
    # def __init__(self, aData:TStkQuoteData) -> None:
    def __init__(self, aData) -> None:
        super().__init__()
        
        self.ChineseName = aData.BAS.StkName #證券中文
        self.TodayRefPrice = aData.BAS.RefPriceOrg #參考價
        self.RiseStopPrice = aData.BAS.LimitPrice_UpOrg #漲停價
        self.FallStopPrice = aData.BAS.LimitPrice_DownOrg #跌停價
        self.IndustryCategory = aData.BAS.IndustryCategory #產業別
        self.Symbol = aData.BAS.StkNo #證券代碼
        self.StockCategory = aData.BAS.StockCategory #證券別
        self.StockAnomalyCode = aData.BAS.StockAnomalyCode #股票異常代碼
        self.BoardRemark = aData.BAS.BoardRemark #板別註記
        self.ClassRemark = aData.BAS.ClassRemark #類股註記
        self.NonTenParValueRemark = aData.BAS.NonTenFaceValueIndicator #非10元面額註記
        self.AbnormalRecommendationIndicator = aData.BAS.AbnormalRecommendationIndicator #異常推介個股註記
        self.AbnormalSecuritiesIndicator = aData.BAS.AbnormalSecuritiesIndicator #特殊異常證券註記
        self.DayTradingRemark = aData.BAS.DayTradingIndicator #可現股當沖註記

        self.TradingUnit = aData.BAS.TradingUnit #交易單位
        self.TickSize = aData.BAS.TickSizeInfo #跳動點資訊
        self.PreTotalTradingAmount = aData.BAS.TotAmtPre #(前交易日)成交總額
        self.PreTotalMatchQty = aData.BAS.TotQtyPre #(前交易日)成交總量
        self.PreTodayRefPrice = aData.BAS.RefPPre #上一交易日參考價
        self.PreClosePrice = aData.BAS.CPPre #上一交易日收盤價


        self.Exchange = "TWS"
        if aData.HL.HasHL: #盤前試撮, 不會有HL        
            self.Category = aData.HL.StkKind #證券別(S/W/Idx) 
class ProductTick_Stk(ProductTick):
    
    #時間轉換
    def TranTime(self, aDate:str)->str:    
        aDate = aDate + ".000000" if len(aDate) == 6 else aDate #指數時間格式為094500
        try:
            exTime = datetime.strptime(aDate, "%H%M%S.%f")
            return exTime.strftime("%H:%M:%S.%f")
        except Exception as ex:
            pass
        return aDate
    
    # def __init__(self, aData:TStkQuoteData) -> None:
    def __init__(self, aData) -> None:
        super().__init__()
        if aData is None:
            return
        if aData.HL.HasHL == False: #盤前試撮, 不會有HL
            return

        self.Exchange = "TWS" #市場別(TWS/TWF)
        self.Symbol = aData.HL.Symbol #委託商品代碼(TXFA2)
        self.MatchTime = self.TranTime(aData.HL.DealTime) #撮合時間(成交)(EX:173547.32700)
        self.OrderBookTime = self.MatchTime
        self.TxSeq = aData.HL.Get_DealSn() #成交序號
        self.ObSeq = aData.HL.Get_Sn_5Q() #五檔序號

        self.IsTxTrial = aData.HL.TryMark_Deal = TSolQuoteStkSet.TryMark_Yes #成交試撮註記(試撮=1, 非試撮=0)
        self.Is5QTrial = aData.HL.TryMark_5Q = TSolQuoteStkSet.TryMark_Yes #五檔試撮註記(試撮=1, 非試撮=0)
        self.IsTrail = self.IsTxTrial if self.TxSeq >= self.ObSeq else self.Is5QTrial

        self.DecimalLocator = "" #價格欄位小數位數
        self.MatchPrice = aData.HL.DealPriceOrg #成交價
        self.MatchQty = aData.HL.DealQty #成交單量

        self.MatchPriceList.clear()
        self.MatchPriceList.append(self.MatchPrice)
        self.MatchQtyList.clear()
        self.MatchQtyList.append(self.MatchQty)

        self.MatchBuyCount = ""
        self.MatchSellCount = ""
        self.TotalMatchQty = aData.HL.TotQty #成交總量
        self.TotalTradingAmount = aData.HL.TotAmt #成交總額//?????????????????除了IX0001與IX0043其他要自己算?????????
        self.TradingUnit = aData.BAS.TradingUnit #交易單位
        self.DayHigh = aData.HL.HighPriceOrg #當日最高價
        self.DayLow = aData.HL.LowPriceOrg #當日最低價
        self.RefPrice = aData.BAS.RefPriceOrg #參考價
        for i in range(5):        
            self.SellPrice[i] = aData.HL.S5Q_POrg(i + 1) #取得賣5檔價格
            self.SellQty[i] = aData.HL.S5Q_QOrg(i + 1) #賣5檔-量-的原始字串內容

            self.BuyPrice[i] = aData.HL.B5Q_POrg(i + 1) #取得買5檔-價格
            self.BuyQty[i] = aData.HL.B5Q_QOrg(i + 1) #買5檔-量-的原始字串內容
        

        #市場整體總值
        self.AllMarketAmount = aData.HL.WholeTotAmt #整體市場成交總額
        self.AllMarketVolume = aData.HL.WholeTotQty #整體市場成交數量
        self.AllMarketCnt = aData.HL.WholeDealCount #整體市場成交筆數
        self.AllMarketBuyCnt = aData.HL.SumBuyOrderCount #整體市場委託買進筆數
        self.AllMarketSellCnt = aData.HL.SumSellOrderCount #整體市場委託賣出筆數
        self.AllMarketBuyQty = aData.HL.SumBuyOrderQty #整體市場委託買進數量
        self.AllMarketSellQty = aData.HL.SumSellOrderQty #整體市場委託賣出數量
        self.IsFixedPriceTransaction = "" #是否為定盤交易

        self.OpenPrice = aData.HL.OpenPriceOrg #開盤價

        # //aData.HL.Set_FirstDerivedBuyPrice(ref _FirstDerivedBuyPrice) #衍生委託單第一檔買進價格
        # //FirstDerivedBuyQty = aData.HL.FirstDerivedBuyQty #衍生委託單第一檔買進價格數量
        # //aData.HL.Set_FirstDerivedSellPrice(ref _FirstDerivedSellPrice) #衍生委託單第一檔賣出價格數量
        # //FirstDerivedSellQty = aData.HL.FirstDerivedSellQty #衍生委託單第一檔賣出價格數量

        self.TotalBuyOrder = ""
        self.TotalBuyQty = ""
        self.TotalSellOrder = ""
        self.TotalSellQty = ""
        self.Delta = ""
        self.ClosePrice="" #收盤價
        self.SettlePrice="" #結算價

        self.OpenInterest = "" #未平倉合約數
    
    # def Upt_TX(self, tmpQtTx:TStkQtTX)->bool:
    def Upt_TX(self, p_tmpQtTx)->bool:
        sErr:str=""
        try:
            import PY_Trade_package.SolPYAPIOB
            tmpQtTx:PY_Trade_package.SolPYAPIOB.TStkQtTX = p_tmpQtTx
            self.TxSeq = tmpQtTx.Get_DealSn()#成交序號
            self.MatchTime = self.TranTime(tmpQtTx.DealTime) #撮合時間(成交)(EX:173547.32700)
            self.MatchPrice = tmpQtTx.DealPriceOrg #成交價
            self.MatchQty = tmpQtTx.DealQty #成交單量
    
            self.MatchPriceList.clear()
            self.MatchPriceList.append(self.MatchPrice)
            self.MatchQtyList.clear()
            self.MatchQtyList.append(self.MatchQty)

            self.IsTrail = tmpQtTx.TryMark = TSolQuoteStkSet.TryMark_Yes #成交試撮註記(試撮=1, 非試撮=0)

            self.TotalTradingAmount = str(tmpQtTx.HL_TotAmt) #成交總額
            self.DayHigh = str(tmpQtTx.HighPrice) #當日最高價
            self.DayLow = str(tmpQtTx.LowPrice) #當日最低價

            self.TotalMatchQty = tmpQtTx.TotQty
            #this.OrderBookTime = QuoteUtil.GetString(matchData, TWSETickMatchField.MatchTime) #???為何要設定OrderBookTime
            for i in range(5):
                self.SellPrice[i] = tmpQtTx.S5Q_POrg(i + 1) #取得賣5檔價格
                self.SellQty[i] = tmpQtTx.S5Q_QOrg(i + 1) #賣5檔-量-的原始字串內容

                self.BuyPrice[i] = tmpQtTx.B5Q_POrg(i + 1) #取得買5檔-價格
                self.BuyQty[i] = tmpQtTx.B5Q_QOrg(i + 1) #買5檔-量-的原始字串內容

            # //市場整體總值
            # //目前只有IX0001與IX0043 有整體市場資訊
            # //市場整體總值
            self.AllMarketAmount = tmpQtTx.WholeTotAmt #整體市場成交總額
            self.AllMarketVolume = tmpQtTx.WholeTotQty #整體市場成交數量
            self.AllMarketCnt = tmpQtTx.WholeDealCount #整體市場成交筆數
            self.AllMarketBuyCnt = tmpQtTx.SumBuyOrderCount #整體市場委託買進筆數
            self.AllMarketSellCnt = tmpQtTx.SumSellOrderCount #整體市場委託賣出筆數
            self.AllMarketBuyQty = tmpQtTx.SumBuyOrderQty #整體市場委託買進數量
            self.AllMarketSellQty = tmpQtTx.SumSellOrderQty #整體市場委託賣出數量

            self.IsFixedPriceTransaction = str(tmpQtTx.IsFixedPriceTransaction) #是否為定盤交易

            return True,""
        
        except Exception as ex:
            sErr=ex
        return False,sErr
    
    # def Upt_5Q(self, tmpQt5Q:TStkQt5Q)->bool:
    def Upt_5Q(self, p_tmpQt5Q)->bool:
        sErr:str=""
        try:
            import PY_Trade_package.SolPYAPIOB
            tmpQt5Q:PY_Trade_package.SolPYAPIOB.TStkQt5Q = p_tmpQt5Q
            self.IsTrail = tmpQt5Q.TryMark = TSolQuoteStkSet.TryMark_Yes #成交試撮註記(試撮=1, 非試撮=0)
            self.OrderBookTime = self.TranTime(tmpQt5Q.DataTime)
            self.ObSeq = tmpQt5Q.Get_DealSn() #五檔序號

            for i in range(5):
                self.SellPrice[i] = tmpQt5Q.S5Q_POrg(i + 1) #取得賣5檔價格
                self.SellQty[i] = tmpQt5Q.S5Q_QOrg(i + 1) #賣5檔-量-的原始字串內容
                self.BuyPrice[i] = tmpQt5Q.B5Q_POrg(i + 1) #取得買5檔-價格
                self.BuyQty[i] = tmpQt5Q.B5Q_QOrg(i + 1) #買5檔-量-的原始字串內容
            return True,""        
        except Exception as ex:
            sErr = ex
        return False,sErr
    
    # def Upt_IDX(self, tmpQtIDX:TStkQtIDX)->bool: 
    def Upt_IDX(self, p_tmpQtIDX)->bool: 
        "那指數商品的五檔呢?"
        sErr:str=""
        try:       
            import PY_Trade_package.SolPYAPIOB 
            tmpQtIDX:PY_Trade_package.SolPYAPIOB.TStkQtIDX = p_tmpQtIDX
            self.MatchTime = self.TranTime(tmpQtIDX.DealTime) #成交時間
            self.TxSeq = tmpQtIDX.Set_DealSn() #成交序號

            self.TotalMatchQty = tmpQtIDX.TotQty
            self.MatchPrice = tmpQtIDX.DealPriceOrg #成交價
            self.DayHigh = str(tmpQtIDX.HighPrice) #當日最高價
            self.DayLow = str(tmpQtIDX.LowPrice) #當日最低價

            self.TotalTradingAmount = tmpQtIDX.WholeTotAmt #整體市場成交總額//?????????是否只有IX0001與IX0043直接帶入值
            # 市場整體總值
            self.AllMarketAmount = tmpQtIDX.WholeTotAmt #整體市場成交總額
            self.AllMarketVolume = tmpQtIDX.WholeTotQty #整體市場成交數量
            self.AllMarketCnt = tmpQtIDX.WholeDealCount #整體市場成交筆數
            self.AllMarketBuyCnt = tmpQtIDX.SumBuyOrderCount #整體市場委託買進筆數
            self.AllMarketSellCnt = tmpQtIDX.SumSellOrderCount #整體市場委託賣出筆數
            self.AllMarketBuyQty = tmpQtIDX.SumBuyOrderQty #整體市場委託買進數量
            self.AllMarketSellQty = tmpQtIDX.SumSellOrderQty #整體市場委託賣出數量
            return True,""
        
        except Exception as ex:
            sErr=ex
        return False,sErr

class TMapPrdOvs(UserDict):
    "class TMapPrdOvs : ConcurrentDictionary<string, TOvsFutQuoteData>"
    def __init__(self, mapping=None, **kwargs):
        if mapping is not None:
            mapping = {
                str(key).upper(): value for key, value in mapping.items()
            }
        else:
            mapping = {}
        if kwargs:
            mapping.update(
                {str(key).upper(): value for key, value in kwargs.items()}
            )
        self.MapQtProc = {}
        super().__init__(mapping)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    # def NewItem(self, mapQt:TMapOvsFutQuoteData)->bool:
    def NewItem(self, mapQt)->bool:
        try:
            for sSolIce in mapQt.keys():
                if self.data.get(sSolIce) is None:                    
                    self[sSolIce] = mapQt[sSolIce]
            return True
        
        except Exception as ex:
            pass
        return False
    def GetItem(self, aSolICE:str)->bool:
        """return   1.bool
                    2.out TOvsFutQuoteData tmpPrd"""        
        tmpPrd = None
        try:
            if self.data.get(aSolICE) is None:
                return False, tmpPrd
            tmpPrd = self[aSolICE]
            return True, tmpPrd
        except Exception as ex:
            pass
        return False,tmpPrd

class TMapPrdSnapshot(UserDict):
    "TMapPrdSnapshot : ConcurrentDictionary<string, ProductSnapshot>    "
    def __init__(self, mapping=None, **kwargs):        
        if mapping is not None:
            mapping = {
                str(key).upper(): value for key, value in mapping.items()
            }
        else:
            mapping = {}
        if kwargs:
            mapping.update(
                {str(key).upper(): value for key, value in kwargs.items()}
            )
        self.MapQtProc = {}
        super().__init__(mapping)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    # def NewItemFut(self, aSolICE:str, tmpQt:TFutQuoteData)->bool:
    def NewItemFut(self, aSolICE:str, tmpQt)->bool:
        try:          
            if self.data.get(aSolICE) is None:
                tmpPrd:ProductSnapshot = ProductSnapshot()
                tmpPrd.BasicData = ProductBasic_Fut(tmpQt)
                tmpPrd.TickData = ProductTick_Fut(tmpQt)
                self[aSolICE] = tmpPrd
            
            return True
        except Exception as ex:
            pass
        return False
    # def NewItemStk(self, aSolICE:str, tmpQt:TStkQuoteData)->bool:        
    def NewItemStk(self, aSolICE:str, tmpQt)->bool:
        try:        
            if self.data.get(aSolICE) is None:            
                tmpPrd:ProductSnapshot = ProductSnapshot()
                tmpPrd.BasicData = ProductBasic_Stk(tmpQt)
                tmpPrd.TickData = ProductTick_Stk(tmpQt)
                self[aSolICE] = tmpPrd            
            return True        
        except Exception as ex:
            pass
        return False        
    def GetItem(self, aSolICE:str)->bool:
        """return   1.bool
                    2.out ProductSnapshot tmpPrd"""
        tmpPrd = None
        try:
            if self.data.get(aSolICE) is None:
                return False, tmpPrd
            tmpPrd = self[aSolICE]
            return True,tmpPrd            
        except Exception as ex:
            pass
        return False,tmpPrd                
        
class QuoteSessionEvent:
    
    responseCode = -1
    eventInfo = ""
    eventCode=None#SessionEvent
    correlationKey = 0 #object