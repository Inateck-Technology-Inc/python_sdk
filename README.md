# Inateck Scanner SDK

## Supported Platforms

| OS | Support |
| ------- | ------- |
| iOS | &#x2705; |
| Android | &#x2705; |
| Windows | &#x2705; |
| Linux | &#x2705; |
| Mac | &#x2705; |

## Supported Languages
   
| Language | Support | Link |
| ------- | ------- | ------- |
| Swift | &#x2705; | https://github.com/Inateck-Technology-Inc/ios_sdk |
| Kotlin | &#x2705; | https://github.com/Inateck-Technology-Inc/android_sdk |
| Java | &#x2705; | https://github.com/Inateck-Technology-Inc/java_sdk |
| C# | &#x2705; | https://github.com/Inateck-Technology-Inc/csharp_sdk |
| C++ | &#x2705; | https://github.com/Inateck-Technology-Inc/cpp_sdk |
| Python | &#x2705; | https://github.com/Inateck-Technology-Inc/python_sdk |
| C | &#x2705; | https://github.com/Inateck-Technology-Inc/cpp_sdk |

## Usage
1. Copy the corresponding `libscanner_ble` library file for your operating system platform to your project.
2. Run the demo.


## General API  

Initialize the SDK, `callback` is the callback for device connection status.

```python
registerEvent(`callback`)
```

<br>

Start scanning devices

```python
startScan()
```

<br>

Stop scanning devices

```python
stopScan()
```

<br>

Connect the device, `mac` is the unique identifier of the device, `callback` is the callback for scanning content of the connected device. The scanning content is encoded in UTF-8. If the scanning content is not encoded in UTF-8, it needs to be converted manually. For custom encoding, refer to the [documentation](./code.md).

```python
connect(`mac`, `callback`)
```

<br>

Disconnect the device, `mac` is the unique identifier of the device.

```python
disconnect(`mac`)
```

<br>

Authorize the device, `mac` is the unique identifier of the device. After successful device connection, the device needs to be authorized in order to use it properly.
```python
auth(`mac`)
```

<br>
Get the battery level, `mac` is the unique identifier of the device.

```python
getBattery(`mac`)
```

<br>

Get the firmware version, `mac` is the unique identifier of the device.

```python
getFirmwareVersion(`mac`)
```

<br>
Get the software version, `mac` is the unique identifier of the device.

```python
getSoftwareVersion(`mac`)
```

<br>
Set the device name, `mac` is the unique identifier of the device.

```python
setName(`mac`, `name`)
```

<br>

Set the device time, `mac` is the unique identifier of the device.

```python
setTime(`mac`, `time`)
```

Reset to factory settings, `mac` is the unique identifier of the device.

```python
reset(`mac`)
```

<br>

Restart the device, `mac` is the unique identifier of the device.

```python
restart(`mac`)
```

<br>

Inventory mode settings, `mac` is the unique identifier of the device.

```python
// Clear inventory cache
inventoryClearCache(`mac`)

// Upload inventory data when connected via USB
inventoryUploadCache(`mac`)

// Upload the number of inventory cache when connected via USB
inventoryUploadCacheNumber(`mac`)
```

<br>

Barcode open settings, `mac` is the unique identifier of the device.

```python
// Open all barcodes
openAllCode(`mac`)

// Close all barcodes
closeAllCode(`mac`)

// Reset all barcodes to factory settings
resetAllCode(`mac`)
```

<br>

SDK Version

```python
sdkVersion()
```

<br>

## Setting API

Set the configuration information, `mac` is the unique identifier of the device, `cmd` is a JSON string. For specific configuration information, refer to the [documentation](./info.md).

```python
setSettingInfo(`mac`, `cmd`)

// Example
// Set the volume of the scanner
// `cmd` is a JSON string
setSettingInfo(`mac`, "[{ "value" : "0","area" : "3","name" : "volume" }]")
```

<br>


Get the configuration information, `mac` is the unique identifier of the device.

```python
getSettingInfo(`mac`)
```


