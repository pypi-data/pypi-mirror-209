from threading import Lock
from time import sleep
import logging
from  logging.config import fileConfig
import os
import pathlib
import queue
from enum import Enum
import threading
# LOGGING_LEVEL = getattr(logging, LOG_LEVEL)
# LOGGING_FORMAT = '%(asctime)-15s %(filename)s:%(lineno)d:%(funcName)s %(levelname)s - %(message)s'

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M',
#                     handlers=[logging.FileHandler('my.log', 'w', 'utf-8'), ])
 
# logging.debug('Hello debug!')
# logging.info('Hello info!')
# logging.warning('Hello warning!')
# logging.error('Hello error!')
# logging.critical('Hello critical!')

class SolLogType(Enum):
    Info=0
    Warning=1
    Error=2
    Debug=3

class SolaceLog:

    def create_logger(log_path):
        # config
        logging.captureWarnings(True)   # 捕捉 py waring message
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        my_logger = logging.getLogger('py.warnings')    # 捕捉 py waring message
        my_logger.setLevel(logging.INFO)
    
        # 若不存在目錄則新建
        # if not os.path.exists(dir_path+log_folder):
        #     os.makedirs(dir_path+log_folder)
    
        # file handler
        # fileHandler = logging.FileHandler(dir_path+log_folder+'/'+filename, 'w', 'utf-8')        
        path = os.path.join(pathlib.Path(log_path).parent.absolute(), 'SolPY.log')        
        fileHandler = logging.FileHandler(path, 'a', 'utf-8')
        fileHandler.setFormatter(formatter)
        my_logger.addHandler(fileHandler)
    
        # console handler
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(formatter)
        my_logger.addHandler(consoleHandler)
    
        return my_logger
    

    def __init__(self, log_path:str, loglv = logging.INFO, conlv = logging.INFO):

        self._lock = Lock()
        self._run = True
        self._queue = queue.Queue()

         # config
        logging.captureWarnings(True)   # 捕捉 py waring message
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.my_logger = logging.getLogger('py.warnings')    # 捕捉 py waring message
        self.my_logger.setLevel(loglv)
    
        # 若不存在目錄則新建
        # if not os.path.exists(dir_path+log_folder):
        #     os.makedirs(dir_path+log_folder)
    
        # file handler
        # fileHandler = logging.FileHandler(dir_path+log_folder+'/'+filename, 'w', 'utf-8')
        path = os.path.join(pathlib.Path(log_path).parent.absolute(), 'SolPY.log')
        fileHandler = logging.FileHandler(path, 'a', 'utf-8')
        fileHandler.setFormatter(formatter)
        self.my_logger.addHandler(fileHandler)
    
        # console handler
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(conlv)
        consoleHandler.setFormatter(formatter)
        self.my_logger.addHandler(consoleHandler)
        thrd = threading.Thread(target=self.OnThread, name="SolaceLog")
        thrd.start()
        
    
    def Wrtie_log(self, type_info:SolLogType,msg:str):
        try:
            if type_info==SolLogType.Error:
                self.my_logger.error(msg)
            elif type_info==SolLogType.Warning:
                self.my_logger.warning(msg)
            elif type_info==SolLogType.Info:
                self.my_logger.info(msg)
            elif type_info==SolLogType.Debug:
                self.my_logger.debug(msg)
        except Exception as ex:
            pass

    def OnThread(self):
        while self._run:
            try:
                with self._lock:
                    while not self._queue.empty():
                        para = self._queue.get()
                        self.Wrtie_log(para["arg1"],para["arg2"])
            except Exception as ex:
                pass
            finally:
                sleep(0.001)
    def Add(self, **para):
        with self._lock:
            self._queue.put(para)    