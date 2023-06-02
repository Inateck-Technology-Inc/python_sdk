import sys
import ctypes
import time

from pathlib import Path

def loadIndirect():
    if sys.platform == "darwin":
        libname = ""
    elif sys.platform.startswith("win"):
        libname = "lib/scanner_windows.dll"
    else:
        libname = ""

    lib = libname.format("scanner")
    path = str(Path(__file__).parent / lib)
    return ctypes.cdll.LoadLibrary(path)

_Lib = loadIndirect()

def callback(data):
    print("Received data:", data.decode())

def scan():
    scan_func = _Lib.scan
    scan_func.argtypes = []
    scan_func.restype = ctypes.c_char_p
    return scan_func()

callback_type = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
my_callback_ptr = callback_type(callback)

def connect(device_id,app_id,developer_id,app_key):
    connect_func = _Lib.connect
    connect_func.argtypes = [ctypes.c_char_p,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_void_p]
    connect_func.restype = ctypes.c_char_p
    #null_pointer = ctypes.c_void_p()
    return connect_func(device_id,app_id,developer_id,app_key,my_callback_ptr)

def disconnect(device_id):
    disconnect_func = _Lib.disconnect
    disconnect_func.argtypes = [ctypes.c_char_p]
    disconnect_func.restype = ctypes.c_char_p
    return disconnect_func(device_id)

def get_properties_info_by_key(device_id,key):
    info_func = _Lib.get_properties_info_by_key
    info_func.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
    info_func.restype = ctypes.c_char_p
    return info_func(device_id,key)

def get_basic_properties(device_id,key):
    edit_func = _Lib.get_basic_properties
    edit_func.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
    edit_func.restype = ctypes.c_char_p
    return edit_func(device_id,key)

def edit_properties_info_by_key(device_id,key,value):
    edit_func = _Lib.edit_properties_info_by_key
    edit_func.argtypes = [ctypes.c_char_p,ctypes.c_char_p,ctypes.c_char_p]
    edit_func.restype = ctypes.c_char_p
    return edit_func(device_id,key,value)

def get_all_barcode_properties(device_id):
    info_func = _Lib.get_all_barcode_properties
    info_func.argtypes = [ctypes.c_char_p]
    info_func.restype = ctypes.c_char_p
    return info_func(device_id)


if __name__ == '__main__':
    print(scan())
    print(connect(b"7B:AA:8C:98:10:71",b"**",b"**",b"**"))
    print(get_properties_info_by_key(b"7B:AA:8C:98:10:71",b"lighting_lamp_control"))
    print(edit_properties_info_by_key(b"7B:AA:8C:98:10:71",b"GS1-128",b"1"))
    print(get_basic_properties(b"7B:AA:8C:98:10:71",b"firmware_version"))
    print(get_all_barcode_properties(b"7B:AA:8C:98:10:71"))
    time.sleep(10)
    print(disconnect(b"7B:AA:8C:98:10:71"))
