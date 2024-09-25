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
        if platform.system() == 'Darwin':
            self.lib = cdll.LoadLibrary('./lib/libscanner_ble_x86_64-apple-darwin.dylib')
        elif platform.system() == 'Linux':
            self.lib = cdll.LoadLibrary('./libscanner_ble.so')
        elif platform.system() == 'Windows':
            self.lib = cdll.LoadLibrary('./libscanner_ble.dll')
        else:
            print("Unsupported OS")

    def registerEvent(self, callback):
        CallbackType = CFUNCTYPE(None, c_char_p)
        self.eventCallback = CallbackType(callback)
        status = self.lib.inateck_scanner_ble_init(self.eventCallback)
        return status
    
    def destroy(self):
        status = self.lib.inateck_scanner_ble_destroy()
        return status
    
    def startScan(self):
        status = self.lib.inateck_scanner_ble_start_scan()
        return status
    
    def stopScan(self):
        status = self.lib.inateck_scanner_ble_stop_scan()
        return status
    
    def getDevices(self):
        get_devices = self.lib.inateck_scanner_ble_get_devices
        get_devices.restype = c_char_p
        char_ptr = get_devices()
        return char_ptr.decode('utf-8')
    
    def connect(self, mac, callback):
        mac = c_char_p(bytes(mac, 'utf-8'))
        CallbackType = CFUNCTYPE(None, c_char_p)
        self.connectCallback = CallbackType(callback)
        connect = self.lib.inateck_scanner_ble_connect
        connect.restype = c_char_p
        char_ptr = connect(mac, self.connectCallback)
        return char_ptr.decode('utf-8')
    
    def auth(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_auth(mac)
        return status
    
    def disconnect(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_disconnect(mac)
        return status
    
    def getBattery(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        get_battery = self.lib.inateck_scanner_ble_get_battery
        get_battery.restype = c_char_p
        char_ptr = get_battery(mac)
        return char_ptr.decode('utf-8')
    
    def getHardwareVersion(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        get_hardware_version = self.lib.inateck_scanner_ble_get_hardware_version
        get_hardware_version.restype = c_char_p
        char_ptr = get_hardware_version(mac)
        return char_ptr.decode('utf-8')
    
    def getSoftwareVersion(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        get_software_version = self.lib.inateck_scanner_ble_get_software_version
        get_software_version.restype = c_char_p
        char_ptr = get_software_version(mac)
        return char_ptr.decode('utf-8')
    
    def beeOrShake(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        bee_or_shake = self.lib.inateck_scanner_ble_bee_or_shake
        bee_or_shake.restype = c_char_p
        char_ptr = bee_or_shake(mac)
        return char_ptr.decode('utf-8')
    
    def getSettingInfo(self, mac, device_type):
        mac = c_char_p(bytes(mac, 'utf-8'))
        device_type = c_int(device_type.value)
        get_setting_info = self.lib.inateck_scanner_ble_get_setting_info
        get_setting_info.restype = c_char_p
        char_ptr = get_setting_info(mac, device_type)
        return char_ptr.decode('utf-8')
    
    def setSettingInfo(self, mac, cmd, device_type):
        mac = c_char_p(bytes(mac, 'utf-8'))
        cmd = c_char_p(bytes(cmd, 'utf-8'))
        device_type = c_int(device_type.value)
        setting_info = self.lib.inateck_scanner_ble_set_setting_info
        setting_info.restype = c_char_p
        char_ptr = setting_info(mac, cmd, device_type)
        return char_ptr.decode('utf-8')
    
    def setName(self, mac, name):
        mac = c_char_p(bytes(mac, 'utf-8'))
        name = c_char_p(bytes(name, 'utf-8'))
        status = self.lib.inateck_scanner_ble_set_name(mac, name)
        return status
    
    def setTime(self, mac, time):
        mac = c_char_p(bytes(mac, 'utf-8'))
        time = c_long(time)
        status = self.lib.inateck_scanner_ble_set_time(mac, time)
        return status
    
    def inventoryClearCache(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_inventory_clear_cache(mac)
        return status
    
    def inventoryUploadCache(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_inventory_upload_cache(mac)
        return status
    
    def inventoryUploadCacheNumber(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_inventory_upload_cache_number(mac)
        return status
    
    def reset(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_reset(mac)
        return status
    
    def restart(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_restart(mac)
        return status
    
    def closeAllCode(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_close_all_code(mac)
        return status
    
    def openAllCode(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_open_all_code(mac)
        return status
    
    def resetAllCode(self, mac):
        mac = c_char_p(bytes(mac, 'utf-8'))
        status = self.lib.inateck_scanner_ble_reset_all_code(mac)
        return status
    
    def sdkVersion(self):
        sdk_version = self.lib.inateck_scanner_ble_sdk_version
        sdk_version.restype = c_char_p
        char_ptr = sdk_version()
        return char_ptr.decode('utf-8')