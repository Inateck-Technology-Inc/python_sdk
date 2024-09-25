# 扫码枪配置 cmd

## 设置扫码枪声音大小


| 声音大小 | 状态值 | 状态  | cmd                        |
| ---- | --- | --- | -------------------------- |
| 声音大小 | 0   | 静音  | {"flag": 1001, "value": 0} |
| 声音大小 | 2   | 小   | {"flag": 1001, "value": 2} |
| 声音大小 | 4   | 中   | {"flag": 1001, "value": 4} |
| 声音大小 | 8   | 大   | {"flag": 1001, "value": 8} |



<br>

## 设置扫码枪震动强度

| 震动强度 | 状态值 | 状态  | cmd                        |
| ---- | --- | --- | -------------------------- |
| 震动强度 | 0   | 弱   | {"flag": 1002, "value": 0} |
| 震动强度 | 1   | 强   | {"flag": 1002, "value": 1} |
| 震动强度 | 2   | 关   | {"flag": 1002, "value": 2} |


<br>


## 照明灯控制
  
| 照明灯控制 | 状态值 | 状态   | cmd                        |
| ----- | --- | ---- | -------------------------- |
| 照明灯控制 | 0   | 识读时亮 | {"flag": 1003, "value": 0} |
| 照明灯控制 | 1   | 常亮   | {"flag": 1003, "value": 1} |
| 照明灯控制 | 2   | 常灭   | {"flag": 1003, "value": 2} |

<br>

## 定位灯控制

| 定位灯控制 | 状态值 | 状态   | cmd                        |
| ----- | --- | ---- | -------------------------- |
| 定位灯控制 | 0   | 识读时亮 | {"flag": 1004, "value": 0} |
| 定位灯控制 | 1   | 常亮   | {"flag": 1004, "value": 1} |
| 定位灯控制 | 2   | 常灭   | {"flag": 1004, "value": 2} |

<br>

## 键盘语言设置

| 键盘语言 | 状态值 | 状态                 | cmd                         |
| ---- | --- | ------------------ | --------------------------- |
| 键盘语言 | 1   | US Windows         | {"flag": 1005, "value": 1}  |
| 键盘语言 | 2   | Italian Windows    | {"flag": 1005, "value": 2}  |
| 键盘语言 | 3   | German Windows     | {"flag": 1005, "value": 3}  |
| 键盘语言 | 4   | Spanish Windows    | {"flag": 1005, "value": 4}  |
| 键盘语言 | 5   | French Windows     | {"flag": 1005, "value": 5}  |
| 键盘语言 | 6   | UK Windows         | {"flag": 1005, "value": 6}  |
| 键盘语言 | 7   | Japanese Windows   | {"flag": 1005, "value": 7}  |
| 键盘语言 | 8   | Canadian Windows   | {"flag": 1005, "value": 8}  |
| 键盘语言 | 9   | Lithuania Windows  | {"flag": 1005, "value": 9}  |
| 键盘语言 | 10  | Srbija Windows     | {"flag": 1005, "value": 10} |
| 键盘语言 | 11  | Swedish Windows    | {"flag": 1005, "value": 11} |
| 键盘语言 | 12  | Dutch Windows      | {"flag": 1005, "value": 12} |
| 键盘语言 | 13  | Danish Windows     | {"flag": 1005, "value": 13} |
| 键盘语言 | 14  | Norwegian Windows  | {"flag": 1005, "value": 14} |
| 键盘语言 | 16  | Portuguese Windows | {"flag": 1005, "value": 16} |
| 键盘语言 | 17  | Polish Windows     | {"flag": 1005, "value": 17} |
| 键盘语言 | 33  | US MAC             | {"flag": 1005, "value": 33} |
| 键盘语言 | 34  | Italian MAC        | {"flag": 1005, "value": 34} |
| 键盘语言 | 35  | German MAC         | {"flag": 1005, "value":35}  |
| 键盘语言 | 36  | Spanish MAC        | {"flag": 1005, "value": 36} |
| 键盘语言 | 37  | French MAC         | {"flag": 1005, "value": 37} |
| 键盘语言 | 38  | UK MAC             | {"flag": 1005, "value": 38} |
| 键盘语言 | 39  | Japanese MAC       | {"flag": 1005, "value": 39} |
| 键盘语言 | 40  | Canadian MAC       | {"flag": 1005, "value": 40} |
| 键盘语言 | 41  | Lithuania MAC      | {"flag": 1005, "value": 41} |
| 键盘语言 | 42  | Srbija MAC         | {"flag": 1005, "value": 42} |
| 键盘语言 | 43  | Swedish MAC        | {"flag": 1005, "value": 43} |
| 键盘语言 | 44  | Dutch MAC          | {"flag": 1005, "value": 44} |
| 键盘语言 | 45  | Danish MAC         | {"flag": 1005, "value": 45} |
| 键盘语言 | 46  | Norwegian MAC      | {"flag": 1005, "value": 46} |
| 键盘语言 | 48  | Portuguese MAC     | {"flag": 1005, "value": 48} |
| 键盘语言 | 49  | Polish MAC         | {"flag": 1005, "value": 49} |

<br>

## 扫描模式

| 扫描模式 | 状态值 | 状态     | cmd                        |
| ---- | --- | ------ | -------------------------- |
| 扫描模式 | 1   | 连续扫描   | {"flag": 1006, "value": 1} |
| 扫描模式 | 2   | 自动关闭红光 | {"flag": 1006, "value": 2} |
| 扫描模式 | 3   | 自动感应   | {"flag": 1006, "value": 3} |
| 扫描模式 | 5   | 免提     | {"flag": 1006, "value": 5} |


<br>

## 蓝牙模式

| 蓝牙模式 | 状态值 | 状态      | cmd                        |
| ---- | --- | ------- | -------------------------- |
| 蓝牙模式 | 0   | HID模式   | {"flag": 1007, "value": 0} |
| 蓝牙模式 | 1   | SPP模式   | {"flag": 1007, "value": 1} |
| 蓝牙模式 | 2   | GATT模式  | {"flag": 1007, "value": 2} |
| 蓝牙模式 | 3   | 蓝牙接收器模式 | {"flag": 1007, "value": 3} |

<br>

## 大小写转换

| 大小写转换 | 状态值 | 状态   | cmd                        |
| ----- | --- | ---- | -------------------------- |
| 大小写转换 | 0   | 不转换  | {"flag": 1008, "value": 0} |
| 大小写转换 | 1   | 全部小写 | {"flag": 1008, "value": 1} |
| 大小写转换 | 2   | 全部大写 | {"flag": 1008, "value": 2} |
<br>


## 条码输出日期
  
| 条码输出日期 | 状态值 | 状态  | cmd                        |
| ------ | --- | --- | -------------------------- |
| 条码输出日期 | 0   | 关闭  | {"flag": 1009, "value": 0} |
| 条码输出日期 | 1   | 开启  | {"flag": 1009, "value": 1} |

<br>

## 条码输出时间

| 条码输出时间 | 状态值 | 状态  | cmd                        |
| ------ | --- | --- | -------------------------- |
| 条码输出时间 | 0   | 关闭  | {"flag": 1010, "value": 0} |
| 条码输出时间 | 1   | 开启  | {"flag": 1010, "value": 1} |

<br>

## 后缀

| 后缀  | 状态值 | 状态    | cmd                        |
| --- | --- | ----- | -------------------------- |
| 后缀  | 0   | Tab   | {"flag": 1011, "value": 0} |
| 后缀  | 1   | Enter | {"flag": 1011, "value": 1} |
| 后缀  | 2   | 不加后缀  | {"flag": 1011, "value": 2} |

<br>

## 自动休眠

| 自动休眠 | 状态值 | 状态  | cmd                        |
| ---- | --- | --- | -------------------------- |
| 自动休眠 | 0   | 关闭  | {"flag": 1012, "value": 0} |
| 自动休眠 | 1   | 开启  | {"flag": 1012, "value": 1} |

<br>

## 库存模式

| 库存模式 | 状态值 | 状态  | cmd                        |
| ---- | --- | --- | -------------------------- |
| 库存模式 | 0   | 关闭  | {"flag": 1013, "value": 0} |
| 库存模式 | 1   | 开启  | {"flag": 1013, "value": 1} |

<br>

## 双击上传
  
| 双击上传 | 状态值 | 状态  | cmd                        |
| ---- | --- | --- | -------------------------- |
| 双击上传 | 0   | 关闭  | {"flag": 1014, "value": 0} |
| 双击上传 | 1   | 开启  | {"flag": 1014, "value": 1} |

<br>

## 条码设置

| 条码设置        | 状态值 | 状态  | cmd                        |
| ----------- | --- | --- | -------------------------- |
| Codabar码    | 1   | 开启  | {"flag": 2001, "value": 1} |
| Codabar码    | 0   | 关闭  | {"flag": 2001, "value": 0} |
| IATA25码     | 1   | 开启  | {"flag": 2002, "value": 1} |
| IATA25码     | 0   | 关闭  | {"flag": 2002, "value": 0} |
| 交叉25码       | 1   | 开启  | {"flag": 2003, "value": 1} |
| 交叉25码       | 0   | 关闭  | {"flag": 2003, "value": 0} |
| 矩阵25码       | 1   | 开启  | {"flag": 2004, "value": 1} |
| 矩阵25码       | 0   | 关闭  | {"flag": 2004, "value": 0} |
| 标准25码       | 1   | 开启  | {"flag": 2005, "value": 1} |
| 标准25码       | 0   | 关闭  | {"flag": 2005, "value": 0} |
| Code39码     | 1   | 开启  | {"flag": 2006, "value": 1} |
| Code39码     | 0   | 关闭  | {"flag": 2006, "value": 0} |
| Code93码     | 1   | 开启  | {"flag": 2007, "value": 1} |
| Code93码     | 0   | 关闭  | {"flag": 2007, "value": 0} |
| Code128码    | 1   | 开启  | {"flag": 2008, "value": 1} |
| Code128码    | 0   | 关闭  | {"flag": 2008, "value": 0} |
| EAN-8码      | 1   | 开启  | {"flag": 2009, "value": 1} |
| EAN-8码      | 0   | 关闭  | {"flag": 2009, "value": 0} |
| EAN-13码     | 1   | 开启  | {"flag": 2010, "value": 1} |
| EAN-13码     | 0   | 关闭  | {"flag": 2010, "value": 0} |
| UPC-A码      | 1   | 开启  | {"flag": 2011, "value": 1} |
| UPC-A码      | 0   | 关闭  | {"flag": 2011, "value": 0} |
| UPC-E0码     | 1   | 开启  | {"flag": 2012, "value": 1} |
| UPC-E0码     | 0   | 关闭  | {"flag": 2012, "value": 0} |
| MSI码        | 1   | 开启  | {"flag": 2013, "value": 1} |
| MSI码        | 0   | 关闭  | {"flag": 2013, "value": 0} |
| Code11码     | 1   | 开启  | {"flag": 2014, "value": 1} |
| Code11码     | 0   | 关闭  | {"flag": 2014, "value": 0} |
| 中国邮政码       | 1   | 开启  | {"flag": 2015, "value": 1} |
| 中国邮政码       | 0   | 关闭  | {"flag": 2015, "value": 0} |
| UPC-E1码     | 1   | 开启  | {"flag": 2016, "value": 1} |
| UPC-E1码     | 0   | 关   | {"flag": 2016, "value": 0} |
| USPS/FedEx码 | 1   | 开启  | {"flag": 2017, "value": 1} |
| USPS/FedEx码 | 0   | 关闭  | {"flag": 2017, "value": 0} |
| Aztec码      | 1   | 开启  | {"flag": 2018, "value": 1} |
| Aztec码      | 0   | 关闭  | {"flag": 2018, "value": 0} |
| MaxiCode码   | 1   | 开启  | {"flag": 2019, "value": 1} |
| MaxiCode码   | 0   | 关闭  | {"flag": 2019, "value": 0} |
| 汉信码         | 1   | 开启  | {"flag": 2020, "value": 1} |
| 汉信码         | 0   | 关闭  | {"flag": 2020, "value": 0} |
| DataMatrix  | 1   | 开启  | {"flag": 2021, "value": 1} |
| DataMatrix  | 0   | 关闭  | {"flag": 2021, "value": 0} |
| QRCode      | 1   | 开启  | {"flag": 2022, "value": 1} |
| QRCode      | 0   | 关闭  | {"flag": 2022, "value": 0} |
| PDF417      | 1   | 开启  | {"flag": 2023, "value": 1} |
| PDF417      | 0   | 关闭  | {"flag": 2023, "value": 0} |
| GS1-128     | 1   | 开启  | {"flag": 2024, "value": 1} |
| GS1-128     | 0   | 关闭  | {"flag": 2024, "value": 0} |
| RSS14复合码    | 1   | 开启  | {"flag": 2025, "value": 1} |
| RSS14复合码    | 0   | 关闭  | {"flag": 2025, "value": 0} |
| plesey码     | 1   | 开启  | {"flag": 2026, "value": 1} |
| plesey码     | 0   | 关闭  | {"flag": 2026, "value": 0} |
| telepen码    | 1   | 开启  | {"flag": 2027, "value": 1} |
| telepen码    | 0   | 关闭  | {"flag": 2027, "value": 0} |
| RSS-14码     | 1   | 开启  | {"flag": 2028, "value": 1} |
| RSS-14码     | 0   | 关闭  | {"flag": 2028, "value": 0} |

<br>