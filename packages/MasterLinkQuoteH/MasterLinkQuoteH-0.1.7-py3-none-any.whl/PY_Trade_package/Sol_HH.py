from PY_Trade_package.MarketDataMart import MarketDataMart
from PY_Trade_package.SolPYAPIOB import SolAPIHH,TQryStkProdMap,TQryStkProdRec,TObjFutComList,TObjBaseFutMap,TFutCom,TObjBaseFutList,TFutQtBase,TObjBaseOptMap,TObjBaseOptMthList,TObjBaseOptCallPutList
from PY_Trade_package.SolPYAPI_Model import RCode


class Sol_HH():
    def __init__(self,mdm: MarketDataMart,pypath:str):        
        self.__solace = SolAPIHH(mdm,pypath)
        super().__init__()

    def Logon(self, host:str, username:str, password:str, aCompressLevel:int = 5)->RCode:
        return self.__solace.Logon(host, username, password, aCompressLevel)
    
    def DisConnect(self):
        return self.__solace.DisConnect()
    

    def Set_OnLogEvent(self, func:callable):        
        self.__solace.Set_OnLogEvent(func)
    
    def Subscribe(self, exchange:str, symbol:str)->RCode:
        return self.__solace.Subscribe(exchange,symbol)
    
    def Unsubscribe(self, exchange:str, symbol:str)->RCode:
        return self.__solace.Unsubscribe(exchange, symbol)  
    
    def QryProdID_NormalStock(self):
        """取個一般上市上櫃股票商品檔(不含零股/權證)
        return  1:RCode
                2:out TQryStkProdMap mapProd"""
        ret, mapProd =  self.__solace.QryProdID_NormalStock()
        return ret, mapProd
    
    def QryProd_FutCom2(self):
        """取複式期貨商品檔
        out TObjFutComList aProdList"""
        ret, aProdList = self.__solace.QryProd_FutCom2()
        return ret,aProdList
    
    def QryProd_Fut(self,aIsNormal: bool, aIsFutStk: bool, aIsSmall: bool):
        """取期貨商品檔(不含選擇權)
            aIsNormal:取一般期貨
            aIsFutStk:取個股期
            aIsSmall:個股期是否包含小型
            return  1. RCode
                    2.out TObjBaseFutMap aMapProdBase"""
        ret,aMapProdBase = self.__solace.QryProd_Fut(aIsNormal, aIsFutStk, aIsSmall)
        return ret,aMapProdBase

    def QryProd_Opt(self,aIsNormal: bool, aIsOptStk: bool, aIsSmall: bool): 
        """取選擇權商品檔
            aIsNormal:取一般選擇權
            aIsOptStk:取個股選
            aIsSmall:個股期是否包含小型
            out TObjBaseOptMap aMapProdBase"""   
        ret, aMapProdBase = self.__solace.QryProd_Opt(aIsNormal, aIsOptStk, aIsSmall)
        return ret,aMapProdBase

class TQryStkProdMapX(TQryStkProdMap):
    def __init__(self, mapping=None, **kwargs):
        super().__init__(mapping, **kwargs)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)
    
class TQryStkProdRecX(TQryStkProdRec):
    def __init__(self) -> None:
        super().__init__()

class TObjFutComListX(TObjFutComList):
    def __init__(self, mapping=None, **kwargs):
        super().__init__(mapping, **kwargs)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)
    
class TObjBaseFutMapX(TObjBaseFutMap):    
    def __init__(self, mapping=None, **kwargs):
        super().__init__(mapping, **kwargs)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)
    
class TFutComX(TFutCom):
    def __init__(self) -> None:
        super().__init__()

class TObjBaseFutListX(TObjBaseFutList):
    pass

class TFutQtBaseX(TFutQtBase):
    def __init__(self) -> None:
        super().__init__()
class TObjBaseOptMapX(TObjBaseOptMap):
    def __init__(self, mapping=None, **kwargs):
        super().__init__(mapping, **kwargs)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

class TObjBaseOptMthListX(TObjBaseOptMthList):
    def __init__(self, mapping=None, **kwargs):
        super().__init__(mapping, **kwargs)
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)
class TObjBaseOptCallPutListX(TObjBaseOptCallPutList):
    def __init__(self, mapping=None, **kwargs):
        super().__init__(mapping, **kwargs)
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)