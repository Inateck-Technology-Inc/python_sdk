# Inateck 扫码枪SDK

## 支持平台

| OS | Support |
| ------- | ------- |
| iOS | &#x2705; |
| Android | &#x2705; |
| Windows | &#x2705; |
| Linux | &#x2705; |
| Mac | &#x2705; |

## 支持语言
   
| Language | Support | Link |
| ------- | ------- | ------- |
| Swift | &#x2705; | https://github.com/Inateck-Technology-Inc/ios_sdk |
| Kotlin | &#x2705; | https://github.com/Inateck-Technology-Inc/android_sdk |
| Java | &#x2705; | https://github.com/Inateck-Technology-Inc/java_sdk |
| C# | &#x2705; | https://github.com/Inateck-Technology-Inc/csharp_sdk |
| C++ | &#x2705; | https://github.com/Inateck-Technology-Inc/cpp_sdk |
| Python | &#x2705; | https://github.com/Inateck-Technology-Inc/python_sdk |
| C | &#x2705; | https://github.com/Inateck-Technology-Inc/cpp_sdk |

## 用法
1. 将相应操作系统平台 `libscanner_ble` 库文件拷贝到项目中
2. 运行Demo

## 普通API  

初始化SDK，`callback` 为设备连接状态的回调

```python
registerEvent(`callback`)

```

<br>

开始扫描设备

```python
startScan()
```

<br>

停止扫描设备

```python
stopScan()
```

<br>

连接设备，`mac` 为设备的唯一标识, `callback` 为连接设备扫码内容的回调。扫码内容为UTF-8编码，如果扫码内容为非UTF-8编码，需要自行转换，自定义编码参考[文档](./code.md)

```python
connect(`mac`, `callback`)
```

<br>

断开设备，`mac` 为设备的唯一标识

```python
disconnect(`mac`)
```

<br>

授权设备，`mac` 为设备的唯一标识，当设备连接成功后，需要授权设备才能正常使用
```python
auth(`mac`)
```

<br>

获取电量，`mac` 为设备的唯一标识

```python
getBattery(`mac`)
```

<br>

获取固件版本，`mac` 为设备的唯一标识

```python
getFirmwareVersion(`mac`)
```

<br>

获取软件版本，`mac` 为设备的唯一标识

```python
getSoftwareVersion(`mac`)
```

<br>

设置设备名称，`mac` 为设备的唯一标识

```python
setName(`mac`, `name`)
```

<br>

设置设备时间，`mac` 为设备的唯一标识

```python
setTime(`mac`, `time`)
```

恢复出厂设置，`mac` 为设备的唯一标识

```python
reset(`mac`)
```

<br>

重启设备，`mac` 为设备的唯一标识

```python
restart(`mac`)
```

<br>

库存模式设置，`mac` 为设备的唯一标识

```python
// 清除库存缓存
inventoryClearCache(`mac`)

// 当 USB 有线连接时，上传库存数据
inventoryUploadCache(`mac`)

// 当 USB 有线连接时，上传库存缓存数量
inventoryUploadCacheNumber(`mac`)
```

<br>

条码打开设置，`mac` 为设备的唯一标识

```python
// 打开所有条码
openAllCode(`mac`)

// 关闭所有条码
closeAllCode(`mac`)

// 条码恢复出厂设置
resetAllCode(`mac`)
```

<br>

SDK 版本

```python
sdkVersion()
```

<br>

## 设置API

设置配置信息，`mac` 为设备的唯一标识，`cmd` 为 json 字符串，具体配置信息参考[文档](./zh_info.md)

```python
setSettingInfo(`mac`, `cmd`)

// Example
// 设置扫码枪声音大小
// `cmd` 为 json 字符串
setSettingInfo(`mac`, "[{ "value" : "0","area" : "3","name" : "volume" }]")
```

<br>


获取配置信息，`mac` 为设备的唯一标识

```python
getSettingInfo(`mac`)
```






