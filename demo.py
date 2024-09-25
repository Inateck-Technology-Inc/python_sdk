
from time import sleep
from InateckScannerBle import InateckScannerBle, DeviceType

def scan_callback(mac):
    mac = mac.decode('utf-8')
    print("mac: %s" % (mac))

def code_callback(code):
    code = code.decode('utf-8')
    print("code: %s" % (code))


if __name__ == '__main__':
    inateck = InateckScannerBle()
    status = inateck.registerEvent(scan_callback)
    if status != 0:
        print("init failed: %d" % (status))
        exit(1)
    print("init success")
    print("version: %s" % (inateck.sdkVersion()))
    print("you can input command: > scan, > stop, > devices, > connect, > disconnect, > version, > battery, > software, > settingInfo, > closeVolume, > openVolume, > destroy")
    while True:
        input_str = input("")
        cmd = input_str.split(' ')
        start = cmd[0]
        if start != '>':
            print("Invalid command, example: > scan")
            continue
        method = cmd[1]
        if method == None:
            print("Invalid command, example: > scan")
            continue
        if method == 'scan':
            status = inateck.startScan()
            print("status: %d" % (status))
        elif method == 'stop':
            status = inateck.stopScan()
            print("status: %d" % (status))
        elif method == 'devices':
            devices = inateck.getDevices()
            print("devices: %s" % (devices))
        elif method == 'connect':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > connect fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            device = inateck.connect(mac, code_callback)
            inateck.auth(mac)
            print("device: %s" % (device))
        elif method == 'disconnect':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > disconnect fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            device = inateck.disconnect(mac)
            print("device: %d" % (device))
        elif method == 'version':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > version fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            version = inateck.getHardwareVersion(mac)
            print("version: %s" % (version))
        elif method == 'battery':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > battery fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            battery = inateck.getBattery(mac)
            print("battery: %s" % (battery))
        elif method == 'software':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > software fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            software = inateck.getSoftwareVersion(mac)
            print("software: %s" % (software))
        elif method == 'settingInfo':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > settingInfo fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            settingInfo = inateck.getSettingInfo(mac)
            print("settingInfo: %s" % (settingInfo))
        elif method == 'closeVolume':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > closeVolume fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            closeVolume = '[{"flag":1001,"value":0}]'
            status = inateck.setSettingInfo(mac, closeVolume, DeviceType.ST75)
            inateck.beeOrShake(mac)
            print("settingInfo: %s" % (status))
        elif method == 'openVolume':
            mac = cmd[2]
            if mac == None:
                print("Invalid command, example: > closeVolume fb556f1d-f919-2d4d-c98c-fcbe246af2e4")
                continue
            closeVolume = '[{"flag":1001,"value":4}]'
            status = inateck.setSettingInfo(mac, closeVolume, DeviceType.ST75)
            inateck.beeOrShake(mac)
            print("settingInfo: %s" % (status))
        elif method == 'destroy':
            inateck.destroy()
        else:
            print("Invalid command, example: > scan")

