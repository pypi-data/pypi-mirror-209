import socket
import ctypes
import os


# Define the ctypes functions and their arguments
GetPrivateProfileSectionNames = ctypes.windll.kernel32.GetPrivateProfileSectionNamesW
GetPrivateProfileSectionNames.argtypes = (ctypes.c_void_p, ctypes.c_uint, ctypes.c_wchar_p)
GetPrivateProfileString = ctypes.windll.kernel32.GetPrivateProfileStringW
GetPrivateProfileString.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.Array, ctypes.c_int, ctypes.c_wchar_p)
GetPrivateProfileInt = ctypes.windll.kernel32.GetPrivateProfileIntW
GetPrivateProfileInt.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_wchar_p)
WritePrivateProfileString = ctypes.windll.kernel32.WritePrivateProfileStringW
WritePrivateProfileString.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p)


class MQCSHelper:
    @staticmethod
    def extractIp():
        localIP = ''
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            """ original code
            socket.Connect("10.255.255.255", 1);
            IPEndPoint endPoint = socket.LocalEndPoint as IPEndPoint;
            localIP = endPoint.Address.ToString();
            """
            s.connect(('10.255.255.255', 1))
            localIP = s.getsockname()[0]
        return localIP


# Define the NativeMethods class with ctypes functions
class NativeMethods:
    GetPrivateProfileSectionNames = GetPrivateProfileSectionNames
    GetPrivateProfileString = GetPrivateProfileString
    GetPrivateProfileInt = GetPrivateProfileInt
    WritePrivateProfileString = WritePrivateProfileString


class IniFile:

    MaxSectionSize:int = 32767
    m_path:str
    def __init__(self, path: str):
        """
        Initializes a new instance of the IniFile class.

        Args:
            path (str): The path of the INI file.
        """
        # Convert to the full path. Because of backward compatibility,
        # the win32 functions tend to assume the path should be the
        # root Windows directory if it is not specified. By calling
        # abspath, we make sure we are always passing the full path
        # to the win32 functions.
        if not os.path.exists(path):
            with open(path, 'w') as f:
                pass
        self.m_path = os.path.abspath(path)

    @property
    def Path(self) -> str:
        """
        Gets the full path of the INI file this object instance is operating on.

        Returns:
            str: A file path.
        """
        return self.m_path
    def GetString(self, section_name: str, key_name: str, default_value: str) -> str:
        if section_name is None:
            raise ValueError("sectionName cannot be None")
        if key_name is None:
            raise ValueError("keyName cannot be None")
        retval = ctypes.create_string_buffer(IniFile.MaxSectionSize)
        result = NativeMethods.GetPrivateProfileString(section_name, key_name, default_value, retval, IniFile.MaxSectionSize, self.m_path)
        # Convert the buffer to a Python string
        retval2 = ctypes.wstring_at(retval)
        # print(result2)
        return retval2 if len(retval2) > 0 else default_value
    
    def GetInt16(self, section_name, key_name, default_value):
        retval = self.GetInt32(section_name, key_name, default_value)
        return int(retval) & 0xFFFF

    def GetInt32(self, sectionName: str, keyName: str, defaultValue: int) -> int:
        if sectionName is None:
            raise ValueError("sectionName cannot be None.")
        if keyName is None:
            raise ValueError("keyName cannot be None.")

        return NativeMethods.GetPrivateProfileInt(sectionName, keyName, defaultValue, self.m_path)
    
    def GetDouble(self, section_name: str, key_name: str, default_value: float) -> float:
        retval = self.GetString(section_name, key_name, "")

        if not retval:
            return default_value

        return float(retval)
    
    def GetSectionValuesAsList(self, section_name):
        if section_name is None:
            raise ValueError("section_name cannot be None")

        # Allocate a buffer for the returned section names.
        ptr = ctypes.c_char_p(bytes(IniFile.MaxSectionSize))

        try:
            # Get the section key/value pairs into the buffer.
            len = NativeMethods.GetPrivateProfileSection(section_name.encode('utf-8'),
                                                        ptr,
                                                        IniFile.MaxSectionSize,
                                                        self.m_path.encode('utf-8'))

            keyValuePairs = self.convert_null_separated_string_to_string_array(ptr.value, len)
        finally:
            # Free the buffer
            ctypes.windll.kernel32.GlobalFree(ptr)

        # Parse keyValue pairs and add them to the list.
        retval = []

        for i in range(len(keyValuePairs)):
            # Parse the "key=value" string into its constituent parts
            equalSignPos = keyValuePairs[i].find(b'=')

            key = keyValuePairs[i][:equalSignPos].decode('utf-8')

            value = keyValuePairs[i][equalSignPos+1:].decode('utf-8')

            retval.append((key, value))

        return retval
    
    def GetSectionValues(self, sectionName):
        keyValuePairs = self.GetSectionValuesAsList(sectionName)
        retval = {}
        for keyValuePair in keyValuePairs:
            if keyValuePair[0] not in retval:
                retval[keyValuePair[0]] = keyValuePair[1]
        return retval

    def GetKeyNames(self, sectionName):
        if sectionName is None:
            raise ValueError("sectionName cannot be None")

        # Allocate a buffer for the returned section names.
        ptr = ctypes.create_string_buffer(IniFile.MaxSectionSize)
        try:
            # Get the section names into the buffer.
            len = NativeMethods.GetPrivateProfileString(sectionName,
                                                        None,
                                                        None,
                                                        ptr,
                                                        IniFile.MaxSectionSize,
                                                        self.m_path)
            # retval2 = ctypes.wstring_at(ptr)
            retval = self.ConvertNullSeperatedStringToStringArray(ptr, len)
            
        finally:
            # Free the buffer
            # ctypes.windll.kernel32.GlobalFree(ptr)
            pass

        return retval    

    def GetSectionNames(self):
        retval = []
        buffer_size = 1024
        buffer = ctypes.create_unicode_buffer(buffer_size)
        while True:
            length = ctypes.windll.kernel32.GetPrivateProfileSectionNamesW(buffer, buffer_size, self.path)
            if length == 0:
                error_code = ctypes.windll.kernel32.GetLastError()
                if error_code == 0x2: # ERROR_FILE_NOT_FOUND
                    return []
                elif error_code == 0x7A: # ERROR_INSUFFICIENT_BUFFER
                    buffer_size *= 2
                    buffer = ctypes.create_unicode_buffer(buffer_size)
                    continue
                else:
                    raise WindowsError(error_code, "Failed to get section names from INI file")
            elif length == buffer_size - 2:
                buffer_size *= 2
                buffer = ctypes.create_unicode_buffer(buffer_size)
                continue
            else:
                section_names = buffer.value[:length].split("\x00")
                return [name for name in section_names if name != ""]


    def ConvertNullSeperatedStringToStringArray(self, ptr, val_length):
        if val_length == 0:
            return []
        retval2 = ctypes.wstring_at(ptr, val_length - 1)
        # Convert the buffer into a string. 
        # buff = ctypes.string_at(retval2, val_length*2 - 1).decode('utf-8')
        # buff = ctypes.string_at(ptr, val_length*2 - 1)

        # Parse the buffer into an array of strings by searching for nulls.
        return retval2.split('\0')
    
    def WriteValueInternal(self, section_name, key_name, value):
        success = NativeMethods.WritePrivateProfileString(section_name, key_name, value, self.m_path)
        if not success:
            raise Exception("Failed to write value to INI file.")

    def WriteValue(self, sectionName, keyName, value):
        if sectionName is None:
            raise ValueError("sectionName cannot be None")

        if keyName is None:
            raise ValueError("keyName cannot be None")

        if value is None:
            raise ValueError("value cannot be None")

        self.WriteValueInternal(sectionName, keyName, value)

    def WriteValue(self, sectionName, keyName, value):
        self.WriteValue(sectionName, keyName, int(value))

    def WriteValue(self, sectionName, keyName, value):
        self.WriteValue(sectionName, keyName, str(value))

    def WriteValue(self, sectionName, keyName, value):
        self.WriteValue(sectionName, keyName, str(value))

    def DeleteKey(self, sectionName, keyName):
        if sectionName is None:
            raise ValueError("sectionName cannot be None")

        if keyName is None:
            raise ValueError("keyName cannot be None")

        self.WriteValueInternal(sectionName, keyName, None)

    def DeleteSection(self, sectionName):
        if sectionName is None:
            raise ValueError("sectionName cannot be None")    
        self.WriteValueInternal(sectionName, None, None)