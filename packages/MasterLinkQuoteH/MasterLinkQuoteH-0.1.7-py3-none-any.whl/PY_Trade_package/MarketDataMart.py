# from Product import *
from PY_Trade_package.Product import ProductBasic, ProductSnapshot, ProductTick
# from SolPYAPI import TMapOvsFutQuoteData, TOvsFutQuoteData
from PY_Trade_package.SolPYAPI_Model import RCode
from enum import Enum

class SystemEvent:
    
    rcode:RCode
    msg:str
    def __init__(self, rcode:RCode, msg:str):
        self.rcode = rcode
        self.msg = msg
    def __str__(self) -> str:
        return f"RCode:{self.rcode} msg:{self.msg}"

class MarketDataMart:
    
    #region 系統訊息通知    
    OnSystemEvent:callable = None
    def Fire_OnSystemEvent(self, data:SystemEvent):
        if self.OnSystemEvent == None:
            return
        if self.OnSystemEvent != None:
            self.OnSystemEvent(data)         
    #endregion

    #region 系統連線狀態    
    OnConnectState:callable = None
    def Fire_MarketDataMart_ConnectState(self, aIsConnected:bool, aMsg:str):    
        if self.OnConnectState == None:
            return
        if self.OnConnectState != None:
            self.OnConnectState(aIsConnected, aMsg)
        
    #endregion    

    #region 國內商品

    #region 商品基本資料更新    
    OnUpdateBasic:callable=None
    def Fire_OnUpdateBasic(self, data:ProductBasic):    
        if self.OnUpdateBasic == None:
            return
        if self.OnUpdateBasic != None:
            self.OnUpdateBasic(data)       
    
    # For List    
    OnUpdateBasicList:callable=None
    def Fire_OnUpdateProductBasicList(self, data:list):
        "List<ProductSnapshot> data"    
        if self.OnUpdateBasicList == None:
            return
        if self.OnUpdateBasicList != None:
            self.OnUpdateBasicList(data)
    #endregion

    #region 商品最新快照更新    
    OnUpdateLastSnapshot:callable=None
    def Fire_OnUpdateLastSnapshot(self, data:ProductSnapshot):    
        if self.OnUpdateLastSnapshot == None:
            return
        if self.OnUpdateLastSnapshot != None:
            self.OnUpdateLastSnapshot(data)    
    #endregion

    #region 商品成交訊息    
    OnMatch:callable=None
    def Fire_OnMatch(self, data:ProductTick):    
        if self.OnMatch == None:
            return
        if self.OnMatch != None:
            self.OnMatch(data)
    #endregion

    #region 商品委託簿訊息    
    OnOrderBook:callable=None
    def Fire_OnOrderBook(self, data:ProductTick):    
        if self.OnOrderBook == None:
            return
        if self.OnOrderBook != None:
            self.OnOrderBook(data)
    #endregion

    #region 商品委託量累計更新    
    OnUpdateTotalOrderQty:callable=None
    def Fire_OnUpdateTotalOrderQty(self, data:ProductTick):    
        if self.OnUpdateTotalOrderQty == None:
            return        

        if self.OnUpdateTotalOrderQty != None:
            self.OnUpdateTotalOrderQty(data)
    #endregion

    #region 選擇權商品Greeks更新    
    OnUpdateOptionGreeks:callable=None
    def Fire_OnUpdateOptionGreeks(self, data:ProductTick):    
        if  self.OnUpdateOptionGreeks == None:
            return
        if self.OnUpdateOptionGreeks != None:        
            self.OnUpdateOptionGreeks(data)
    #endregion

    #endregion


    #region 海外商品

    #region 海外商品基本資料更新    
    OnUpdateOvsBasic:callable=None    
    def Fire_OnUpdateOvsBasic(self, data):
        if self.OnUpdateOvsBasic == None:
            return
        if self.OnUpdateOvsBasic != None:
            self.OnUpdateOvsBasic(data)        
    #endregion

    #region 海外商品成交資料更新    
    OnUpdateOvsMatch:callable=None    
    def Fire_OnUpdateOvsMatch(self, data):
        if self.OnUpdateOvsMatch == None:
            return        
        if self.OnUpdateOvsMatch != None:
            self.OnUpdateOvsMatch(data)
    #endregion

    #region 海外商品五檔資料更新    
    OnUpdateOvsOrderBook:callable=None    
    def Fire_OnUpdateOvsOrderBook(self, data):
        if self.OnUpdateOvsOrderBook == None:
            return
        if self.OnUpdateOvsOrderBook != None:
            self.OnUpdateOvsOrderBook(data)
    #endregion

    #endregion






    
