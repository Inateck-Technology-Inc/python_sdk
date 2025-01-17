
from time import sleep
from InateckScannerBle import InateckScannerBle, DeviceType

def scan_callback(mac):
    mac = mac.decode('utf-8')
    print("mac: %s" % (mac))

def code_callback(code):
    code = code.decode('utf-8')
    print("code: %s" % (code))

def connect(inateck, device_id):
    inateck.connect(device_id)
    inateck.checkCommunication(device_id)
    inateck.auth(device_id)
    inateck.setCodeCallback(device_id, code_callback)

def get_hardware_version(inateck, device_id):
    hardware_version = inateck.getHardwareVersion(device_id)
    print("Hardware Version: %s" % (hardware_version))

def get_software_version(inateck, device_id):
    software_version = inateck.getSoftwareVersion(device_id)
    print("Software Version: %s" % (software_version))

def get_setting_info(inateck, device_id):
    setting_info = inateck.getSettingInfo(device_id, DeviceType.ST75)
    print("Setting Info: %s" % (setting_info))

def quiet_mode(inateck, device_id):
    close_volume = "[{\"flag\":1001,\"value\":0}]"
    info = inateck.setSettingInfo(device_id, close_volume, DeviceType.ST75)
    inateck.beeOrShake(device_id)
    print("Quiet Mode: %s" % (info))

def loud_mode(inateck, device_id):
    open_volume = "[{\"flag\":1001,\"value\":4}]"
    info = inateck.setSettingInfo(device_id, open_volume, DeviceType.ST75)
    inateck.beeOrShake(device_id)
    print("Loud Mode: %s" % (info))


if __name__ == '__main__':
    inateck = InateckScannerBle()
    inateck.debug(True)
    sdk_version = inateck.sdkVersion()
    print("SDK Version: %s" % (sdk_version))

    inateck.init()
    inateck.waitAvailable()

    inateck.setDiscoverCallback(scan_callback)
    inateck.startScan()
    sleep(10)
    inateck.stopScan()

    device_id = "BluetoothLE#BluetoothLEf4:4e:fc:89:ee:4a-aa:2b:00:03:95:83"

    connect(inateck, device_id)

    sleep(10)

    inateck.beeOrShake(device_id)

    sleep(5)

    get_hardware_version(inateck, device_id)

    get_software_version(inateck, device_id)

    get_setting_info(inateck, device_id)

    quiet_mode(inateck, device_id)

    sleep(5)

    loud_mode(inateck, device_id)

    sleep(5)



