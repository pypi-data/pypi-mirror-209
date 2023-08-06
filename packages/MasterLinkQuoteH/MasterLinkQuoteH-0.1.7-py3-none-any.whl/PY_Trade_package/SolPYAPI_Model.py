from enum import Enum

class RCode(Enum):
    # 成功
    OK = 0
    # An API call would block, but non-blocking was requested.
    SOLCLIENT_WOULD_BLOCK = 1
    # The API call is in progress (non-blocking mode).
    SOLCLIENT_IN_PROGRESS = 2
    # The API could not complete because the object is not ready (for example, the session is not connected).
    SOLCLIENT_NOT_READY = 3
    # A get next operation on structured container returned End-of-Stream.
    SOLCLIENT_EOS = 4
    # A get for a named field in a MAP was not found.
    SOLCLIENT_NOT_FOUND = 5
    # The context had no events to process.
    SOLCLIENT_NOEVENT = 6
    # The API call completed some, but not all, of the requested function.
    SOLCLIENT_INCOMPLETE = 7
    # Commit() returns this when the transaction has already been rolled back.
    SOLCLIENT_ROLLBACK = 8
    # SolClient Session Event
    SOLCLIENT_EVENT = 9
    # 連線已建立
    CLIENT_ALREADY_CONNECTED = 10
    # 連線已斷線
    CLIENT_ALREADY_DISCONNECTED = 11
    # 公告訊息
    ANNOUNCEMENT = 12
    # 失敗
    FAIL = -1
    # 拒絕連線
    CONNECTION_REFUSED = -2
    # 連線失敗
    CONNECTION_FAIL = -3
    # 目標物件已存在
    ALREADY_EXISTS = -4
    # 目標物件不存在
    NOT_FOUND = -5
    # 連線尚未準備好
    CLIENT_NOT_READY = -6
    # 超過訂閱數上限
    USER_SUBSCRIPTION_LIMIT_EXCEEDED = -7
    # 尚未申請
    USER_NOT_APPLIED = -8
    # 尚未驗證
    USER_NOT_VERIFIED = -9
    # 驗證失敗
    USER_VERIFICATION_FAIL = -10
    # 訂閱商品失敗
    SUBSCRIPTION_FAIL = -11
    # 回補失敗
    RECOVERY_FAIL = -12
    # 下載基本資料檔失敗
    DOWNLOAD_PRODUCT_FAIL = -13
    # 訊息處理錯誤
    MESSAGE_HANDLER_FAIL = -14
    # 功能訂閱數超過上限
    FUNCTION_SUBSCRIPTION_LIMIT_EXCEEDED = -15
    #尚未驗證 TWSE
    USER_NOT_VERIFIED_TWSE = -16
    #尚未驗證 TAIFEX
    USER_NOT_VERIFIED_TAIFEX = -17
    #尚未驗證 TWSE&TAIFEX
    USER_NOT_VERIFIED_TWSE_TAIFEX = -18
    # 未知錯誤
    UNKNOWN_ERROR = -9999

class TSolQuoteStkSet():        
    N1 = 1
    N2 = 2
    N3 = 3
    N4 = 4
    N5 = 5
        
    TryMark_Yes = "1"
    """盤前試撮"""
    TryMark_No = "0"
    """盤中交易"""
    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")

class TSolQuoteFutSet():
    
    N1:int = 1
    N2:int = 2
    N3:int = 3
    N4:int = 4
    N5:int = 5

    MarketPriceOrder_Buy:str = "999999999"
    """市價買進委託,行情以9個9來表達"""
    MarketPriceOrder_Sell:str = "-999999999"
    "市價賣出委託,行情以9個9來表達"        
    TryMark_Yes:str = "1"
    "盤前試撮"
    TryMark_No:str = "0"
    "盤中交易"
    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")

class TSolQuoteOvsFutSet:
    N1:int = 1
    N2:int = 2
    N3:int = 3
    N4:int = 4
    N5:int = 5
    
    TryMark_Yes:str = "1"
    "盤前試撮"
    TryMark_No:str = "0"
    "盤中交易"
    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")

class TFutProdKind(Enum):
    pkNone = 0
    pkNormal = 10
    "一般期貨"
    pkIndex = 20
    "指數商品(EX:TAIWANVIX)"

class TOvsFutProdKind(Enum):
    pkNone = 0
    pkNormal = 10
    "一般期貨"
    pkIndex = 20
    "指數商品(EX:TAIWANVIX)"
    
class TOvsFutQtRcvKind(Enum):
    pkQtRcv_BAS = 10
    "回補契約基本資料"
    
class SubscriptionCategory:
    """分類訂閱"""
    
    STOCK = "S"
    "證券"    
    ODD = "Z"
    "零股"    
    WARRANT = "W"
    "權證"    
    INDEX = "Idx"
    "指數"    
    FUTURE = "FUT"
    "期貨"
    OPTION = "OPT"
    "選擇權"
    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")

class SubscriptionCategoryOvs:
    """分類訂閱"""
    FUTURE = "FUT"
    "期貨"
    OPTION = "OPT"
    "選擇權"
    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")

class RequestType(Enum):
    "API授權請求類型"
    QuoteAPI = 0
    "報價API"
    TradeQPI = 1
    "交易API"

class AccountStatus(Enum):
    "API授權狀態"
        
    NotApplied = 0
    "尚未申請"
    NotVerified = 1
    "尚未認證"        
    Verified = 2
    "已認證"

class EXCHANGE:
    TWF:str = "TWF"
    TWS:str = "TWS"
    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")


class UserLoginReply:
    def __init__(self):
        self.result = False # SSO verification
        self.uid = ''
        self._accountStatus = [None] * 3
        self.accountStatus = self._accountStatus
        self.requestType = 0
        self.typeName = ''
        self.hostName = ''
        self.vpnName = ''
        self.userName = ''
        self.password = ''
        self.message = ''
        "公告訊息"
        self.announcement = ''
        self.compressLevel = 0
        "Solace行情壓縮Level"
        self.twsPsaStatus = 1
        "證券公告驗證狀態(1=未驗證, 2=已驗證)" 
        self.twfPsaStatus = 1
        "期貨公告驗證狀態(1=未驗證, 2=已驗證)"

class UserLogin:
    def __init__(self, username, password, source, requestType, ip, isSIM):
        self.uid:str = username
        self.password:str = password
        self.source:str = source
        self.requestType:int = requestType
        self.ip:str = ip
        self.isSIM:bool = isSIM
    def __str__(self) -> str:
        return f"uid:{self.uid} password:{self.password} source:{self.source} reqtype:{self.requestType} ip:{self.ip} isSIM:{self.isSIM}"
    
class TSolClientConnData:
    
    Host:str = ""
    Username:str = ""
    Password:str = ""
    MessageVPN:str = ""
    TLPath:str = ""
    CacheName:str = "dc01"
    
    CompressLevel:int = 1
    "壓縮等級"

class TStkCat:
    S:str="S"
    "一般股票"
    W:str="W"
    "權證類"
    Idx:str="Idx"
    "指數類"

    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")

class TFutCat:
    FUT:str="FUT"
    "期貨類"
    OPT:str="OPT"
    "選擇權類"
    def __setattr__(self, *_):
        raise Exception("Tried to change the value of a constant")
    

