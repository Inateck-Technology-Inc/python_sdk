from ctypes import *
from enum import Enum
import platform

class DeviceType(Enum):
    NONE = 0
    Pro8 = 1
    ST45 = 2
    ST23 = 3
    ST91 = 4
    ST42 = 5
    ST54 = 6
    ST55 = 7
    ST73 = 8
    ST75 = 9
    ST43 = 10
    P7 = 11
    ST21 = 12
    ST60 = 13
    ST70 = 14
    P6 = 15
    ST35 = 16

class InateckScannerBle:
    def __init__(self):
        if platform.system() == 'Windows':
            self.lib = cdll.LoadLibrary('./scanner_ble_x86_64-pc-windows-msvc.dll')
        else:
            print("Unsupported OS")

    def init(self):
        func = self.lib.inateck_scanner_ble_init
        func.restype = c_char_p
        char_ptr = func()
        return char_ptr.decode('utf-8')

    def setDiscoverCallback(self, callback):
        CallbackType = CFUNCTYPE(None, c_char_p)
        self.eventCallback = CallbackType(callback)
        func = self.lib.inateck_scanner_ble_set_discover_callback
        func.restype = c_char_p
        char_ptr = func(self.eventCallback)
        return char_ptr.decode('utf-8')
    
    def waitAvailable(self):
        func = self.lib.inateck_scanner_ble_wait_available
        func.restype = c_char_p
        char_ptr = func()
        return char_ptr.decode('utf-8')
    
    def startScan(self):
        func = self.lib.inateck_scanner_ble_start_discover
        func.restype = c_char_p
        char_ptr = func()
        return char_ptr.decode('utf-8')
    
    def stopScan(self):
        func = self.lib.inateck_scanner_ble_stop_discover
        func.restype = c_char_p
        char_ptr = func()
        return char_ptr.decode('utf-8')
    
    def getDevices(self):
        func = self.lib.inateck_scanner_ble_get_devices
        func.restype = c_char_p
        char_ptr = func()
        return char_ptr.decode('utf-8')
    
    def connect(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_connect
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def checkCommunication(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_check_communication
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def auth(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_auth
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def setCodeCallback(self, deviceId, callback):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        CallbackType = CFUNCTYPE(None, c_char_p)
        self.codeCallback = CallbackType(callback)
        func = self.lib.inateck_scanner_ble_set_code_callback
        func.restype = c_char_p
        char_ptr = func(deviceId, self.codeCallback)
        return char_ptr.decode('utf-8')
    
    def setDisconnectCallback(self, deviceId, callback):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        CallbackType = CFUNCTYPE(None, c_char_p)
        self.disconnectCallback = CallbackType(callback)
        func = self.lib.inateck_scanner_ble_set_disconnect_callback
        func.restype = c_char_p
        char_ptr = func(deviceId, self.disconnectCallback)
        return char_ptr.decode('utf-8')
    
    def disconnect(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_disconnect
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def getBattery(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_get_battery
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def getHardwareVersion(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        get_hardware_version = self.lib.inateck_scanner_ble_get_hardware_version
        get_hardware_version.restype = c_char_p
        char_ptr = get_hardware_version(deviceId)
        return char_ptr.decode('utf-8')
    
    def getSoftwareVersion(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        get_software_version = self.lib.inateck_scanner_ble_get_software_version
        get_software_version.restype = c_char_p
        char_ptr = get_software_version(deviceId)
        return char_ptr.decode('utf-8')
    
    def beeOrShake(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        bee_or_shake = self.lib.inateck_scanner_ble_bee_or_shake
        bee_or_shake.restype = c_char_p
        char_ptr = bee_or_shake(deviceId)
        return char_ptr.decode('utf-8')
    
    def getSettingInfo(self, deviceId, device_type):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        device_type = c_int(device_type.value)
        get_setting_info = self.lib.inateck_scanner_ble_get_setting_info
        get_setting_info.restype = c_char_p
        char_ptr = get_setting_info(deviceId, device_type)
        return char_ptr.decode('utf-8')
    
    def setSettingInfo(self, deviceId, cmd, device_type):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        cmd = c_char_p(bytes(cmd, 'utf-8'))
        device_type = c_int(device_type.value)
        setting_info = self.lib.inateck_scanner_ble_set_setting_info
        setting_info.restype = c_char_p
        char_ptr = setting_info(deviceId, cmd, device_type)
        return char_ptr.decode('utf-8')
    
    def setName(self, deviceId, name):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        name = c_char_p(bytes(name, 'utf-8'))
        func = self.lib.inateck_scanner_ble_set_name
        func.restype = c_char_p
        char_ptr = func(deviceId, name)
        return char_ptr.decode('utf-8')
    
    def setTime(self, deviceId, time):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        time = c_long(time)
        func = self.lib.inateck_scanner_ble_set_time
        func.restype = c_char_p
        char_ptr = func(deviceId, time)
        return char_ptr.decode('utf-8')
    
    def inventoryClearCache(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_inventory_clear_cache
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def inventoryUploadCache(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_inventory_upload_cache
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def inventoryUploadCacheNumber(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_inventory_upload_cache_number
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def reset(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_reset
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def restart(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_restart
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def closeAllCode(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_close_all_code
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def openAllCode(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_open_all_code
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def resetAllCode(self, deviceId):
        deviceId = c_char_p(bytes(deviceId, 'utf-8'))
        func = self.lib.inateck_scanner_ble_reset_all_code
        func.restype = c_char_p
        char_ptr = func(deviceId)
        return char_ptr.decode('utf-8')
    
    def sdkVersion(self):
        sdk_version = self.lib.inateck_scanner_ble_sdk_version
        sdk_version.restype = c_char_p
        char_ptr = sdk_version()
        return char_ptr.decode('utf-8')
    
    def debug(self, enable):
        enable = c_int(enable)
        status = self.lib.inateck_scanner_ble_set_debug(enable)
        return status