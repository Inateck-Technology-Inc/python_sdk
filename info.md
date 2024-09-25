# cmd

## Set Scanner Volume

| Volume | Status Value | Status | cmd                        |
| ------ | ------------- | ------ | -------------------------- |
| Volume | 0             | Mute   | {"flag": 1001, "value": 0} |
| Volume | 2             | Low    | {"flag": 1001, "value": 2} |
| Volume | 4             | Medium | {"flag": 1001, "value": 4} |
| Volume | 8             | High   | {"flag": 1001, "value": 8} |

<br>

## Set Scanner Vibration Intensity

| Vibration Intensity | Status Value | Status | cmd                        |
| ------------------- | ------------- | ------ | -------------------------- |
| Vibration Intensity | 0             | Weak   | {"flag": 1002, "value": 0} |
| Vibration Intensity | 1             | Strong | {"flag": 1002, "value": 1} |
| Vibration Intensity | 2             | Off    | {"flag": 1002, "value": 2} |

<br>

## Illumination Control

| Illumination Control | Status Value | Status       | cmd                        |
| -------------------- | ------------- | ------------ | -------------------------- |
| Illumination Control | 0             | On when reading | {"flag": 1003, "value": 0} |
| Illumination Control | 1             | Always on    | {"flag": 1003, "value": 1} |
| Illumination Control | 2             | Always off   | {"flag": 1003, "value": 2} |

<br>

## Aiming Light Control

| Aiming Light Control | Status Value | Status       | cmd                        |
| -------------------- | ------------- | ------------ | -------------------------- |
| Aiming Light Control | 0             | On when reading | {"flag": 1004, "value": 0} |
| Aiming Light Control | 1             | Always on    | {"flag": 1004, "value": 1} |
| Aiming Light Control | 2             | Always off   | {"flag": 1004, "value": 2} |

<br>

## Keyboard Language Settings

| Keyboard Language | Status Value | Status            | cmd                         |
| ----------------- | ------------- | ----------------- | --------------------------- |
| Keyboard Language | 1             | US Windows        | {"flag": 1005, "value": 1}  |
| Keyboard Language | 2             | Italian Windows   | {"flag": 1005, "value": 2}  |
| Keyboard Language | 3             | German Windows    | {"flag": 1005, "value": 3}  |
| Keyboard Language | 4             | Spanish Windows   | {"flag": 1005, "value": 4}  |
| Keyboard Language | 5             | French Windows    | {"flag": 1005, "value": 5}  |
| Keyboard Language | 6             | UK Windows        | {"flag": 1005, "value": 6}  |
| Keyboard Language | 7             | Japanese Windows  | {"flag": 1005, "value": 7}  |
| Keyboard Language | 8             | Canadian Windows  | {"flag": 1005, "value": 8}  |
| Keyboard Language | 9             | Lithuanian Windows| {"flag": 1005, "value": 9}  |
| Keyboard Language | 10            | Serbian Windows   | {"flag": 1005, "value": 10} |
| Keyboard Language | 11            | Swedish Windows   | {"flag": 1005, "value": 11} |
| Keyboard Language | 12            | Dutch Windows     | {"flag": 1005, "value": 12} |
| Keyboard Language | 13            | Danish Windows    | {"flag": 1005, "value": 13} |
| Keyboard Language | 14            | Norwegian Windows | {"flag": 1005, "value": 14} |
| Keyboard Language | 16            | Portuguese Windows| {"flag": 1005, "value": 16} |
| Keyboard Language | 17            | Polish Windows    | {"flag": 1005, "value": 17} |
| Keyboard Language | 33            | US MAC            | {"flag": 1005, "value": 33} |
| Keyboard Language | 34            | Italian MAC       | {"flag": 1005, "value": 34} |
| Keyboard Language | 35            | German MAC        | {"flag": 1005, "value": 35} |
| Keyboard Language | 36            | Spanish MAC       | {"flag": 1005, "value": 36} |
| Keyboard Language | 37            | French MAC        | {"flag": 1005, "value": 37} |
| Keyboard Language | 38            | UK MAC            | {"flag": 1005, "value": 38} |
| Keyboard Language | 39            | Japanese MAC      | {"flag": 1005, "value": 39} |
| Keyboard Language | 40            | Canadian MAC      | {"flag": 1005, "value": 40} |
| Keyboard Language | 41            | Lithuanian MAC    | {"flag": 1005, "value": 41} |
| Keyboard Language | 42            | Serbian MAC       | {"flag": 1005, "value": 42} |
| Keyboard Language | 43            | Swedish MAC       | {"flag": 1005, "value": 43} |
| Keyboard Language | 44            | Dutch MAC         | {"flag": 1005, "value": 44} |
| Keyboard Language | 45            | Danish MAC        | {"flag": 1005, "value": 45} |
| Keyboard Language | 46            | Norwegian MAC     | {"flag": 1005, "value": 46} |
| Keyboard Language | 48            | Portuguese MAC    | {"flag": 1005, "value": 48} |
| Keyboard Language | 49            | Polish MAC        | {"flag": 1005, "value": 49} |

<br>

## Scanning Mode

| Scanning Mode | Status Value | Status         | cmd                        |
| ------------- | ------------- | -------------- | -------------------------- |
| Scanning Mode | 1             | Continuous Scan| {"flag": 1006, "value": 1} |
| Scanning Mode | 2             | Auto Close Red Light | {"flag": 1006, "value": 2} |
| Scanning Mode | 3             | Auto Sensing   | {"flag": 1006, "value": 3} |
| Scanning Mode | 5             | Hands-Free     | {"flag": 1006, "value": 5} |

<br>

## Bluetooth Mode

| Bluetooth Mode | Status Value | Status              | cmd                        |
| -------------- | ------------- | ------------------- | -------------------------- |
| Bluetooth Mode | 0             | HID Mode            | {"flag": 1007, "value": 0} |
| Bluetooth Mode | 1             | SPP Mode            | {"flag": 1007, "value": 1} |
| Bluetooth Mode | 2             | GATT Mode           | {"flag": 1007, "value": 2} |
| Bluetooth Mode | 3             | Bluetooth Receiver Mode | {"flag": 1007, "value": 3} |

<br>

## Case Conversion

| Case Conversion | Status Value | Status     | cmd                        |
| --------------- | ------------- | ---------- | -------------------------- |
| Case Conversion | 0             | No Conversion | {"flag": 1008, "value": 0} |
| Case Conversion | 1             | All Lowercase | {"flag": 1008, "value": 1} |
| Case Conversion | 2             | All Uppercase | {"flag": 1008, "value": 2} |

<br>

## Barcode Output Date

| Barcode Output Date | Status Value | Status | cmd                        |
| ------------------- | ------------- | ------ | -------------------------- |
| Barcode Output Date | 0             | Off    | {"flag": 1009, "value": 0} |
| Barcode Output Date | 1             | On     | {"flag": 1009, "value": 1} |

<br>

## Barcode Output Time

| Barcode Output Time | Status Value | Status | cmd                        |
| ------------------- | ------------- | ------ | -------------------------- |
| Barcode Output Time | 0             | Off    | {"flag": 1010, "value": 0} |
| Barcode Output Time | 1             | On     | {"flag": 1010, "value": 1} |

<br>

## Suffix

| Suffix | Status Value | Status | cmd                        |
| ------ | ------------- | ------ | -------------------------- |
| Suffix | 0             | Tab    | {"flag": 1011, "value": 0} |
| Suffix | 1             | Enter  | {"flag": 1011, "value": 1} |
| Suffix | 2             | No Suffix | {"flag": 1011, "value": 2} |

<br>

## Auto Sleep

| Auto Sleep | Status Value | Status | cmd                        |
| ---------- | ------------- | ------ | -------------------------- |
| Auto Sleep | 0             | Off    | {"flag": 1012, "value": 0} |
| Auto Sleep | 1             | On     | {"flag": 1012, "value": 1} |

<br>

## Inventory Mode

| Inventory Mode | Status Value | Status | cmd                        |
| -------------- | ------------- | ------ | -------------------------- |
| Inventory Mode | 0             | Off    | {"flag": 1013, "value": 0} |
| Inventory Mode | 1             | On     | {"flag": 1013, "value": 1} |

<br>

## Double Click Upload

| Double Click Upload | Status Value | Status | cmd                        |
| ------------------- | ------------- | ------ | -------------------------- |
| Double Click Upload | 0             | Off    | {"flag": 1014, "value": 0} |
| Double Click Upload | 1             | On     | {"flag": 1014, "value": 1} |

<br>

## Barcode Settings

| Barcode Settings | Status Value | Status | cmd                        |
| ---------------- | ------------- | ------ | -------------------------- |
| Codabar          | 1             | On     | {"flag": 2001, "value": 1} |
| Codabar          | 0             | Off    | {"flag": 2001, "value": 0} |
| IATA25           | 1             | On     | {"flag": 2002, "value": 1} |
| IATA25           | 0             | Off    | {"flag": 2002, "value": 0} |
| Interleaved 25   | 1             | On     | {"flag": 2003, "value": 1} |
| Interleaved 25   | 0             | Off    | {"flag": 2003, "value": 0} |
| Matrix 25        | 1             | On     | {"flag": 2004, "value": 1} |
| Matrix 25        | 0             | Off    | {"flag": 2004, "value": 0} |
| Standard 25      | 1             | On     | {"flag": 2005, "value": 1} |
| Standard 25      | 0             | Off    | {"flag": 2005, "value": 0} |
| Code39           | 1             | On     | {"flag": 2006, "value": 1} |
| Code39           | 0             | Off    | {"flag": 2006, "value": 0} |
| Code93           | 1             | On     | {"flag": 2007, "value": 1} |
| Code93           | 0             | Off    | {"flag": 2007, "value": 0} |
| Code128          | 1             | On     | {"flag": 2008, "value": 1} |
| Code128          | 0             | Off    | {"flag": 2008, "value": 0} |
| EAN-8            | 1             | On     | {"flag": 2009, "value": 1} |
| EAN-8            | 0             | Off    | {"flag": 2009, "value": 0} |
| EAN-13           | 1             | On     | {"flag": 2010, "value": 1} |
| EAN-13           | 0             | Off    | {"flag": 2010, "value": 0} |
| UPC-A            | 1             | On     | {"flag": 2011, "value": 1} |
| UPC-A            | 0             | Off    | {"flag": 2011, "value": 0} |
| UPC-E0           | 1             | On     | {"flag": 2012, "value": 1} |
| UPC-E0           | 0             | Off    | {"flag": 2012, "value": 0} |
| MSI              | 1             | On     | {"flag": 2013, "value": 1} |
| MSI              | 0             | Off    | {"flag": 2013, "value": 0} |
| Code11           | 1             | On     | {"flag": 2014, "value": 1} |
| Code11           | 0             | Off    | {"flag": 2014, "value": 0} |
| China Post       | 1             | On     | {"flag": 2015, "value": 1} |
| China Post       | 0             | Off    | {"flag": 2015, "value": 0} |
| UPC-E1           | 1             | On     | {"flag": 2016, "value": 1} |
| UPC-E1           | 0             | Off    | {"flag": 2016, "value": 0} |
| USPS/FedEx       | 1             | On     | {"flag": 2017, "value": 1} |
| USPS/FedEx       | 0             | Off    | {"flag": 2017, "value": 0} |
| Aztec            | 1             | On     | {"flag": 2018, "value": 1} |
| Aztec            | 0             | Off    | {"flag": 2018, "value": 0} |
| MaxiCode         | 1             | On     | {"flag": 2019, "value": 1} |
| MaxiCode         | 0             | Off    | {"flag": 2019, "value": 0} |
| Han Xin          | 1             | On     | {"flag": 2020, "value": 1} |
| Han Xin          | 0             | Off    | {"flag": 2020, "value": 0} |
| DataMatrix       | 1             | On     | {"flag": 2021, "value": 1} |
| DataMatrix       | 0             | Off    | {"flag": 2021, "value": 0} |
| QRCode           | 1             | On     | {"flag": 2022, "value": 1} |
| QRCode           | 0             | Off    | {"flag": 2022, "value": 0} |
| PDF417           | 1             | On     | {"flag": 2023, "value": 1} |
| PDF417           | 0             | Off    | {"flag": 2023, "value": 0} |
| GS1-128          | 1             | On     | {"flag": 2024, "value": 1} |
| GS1-128          | 0             | Off    | {"flag": 2024, "value": 0} |
| RSS14 Composite  | 1             | On     | {"flag": 2025, "value": 1} |
| RSS14 Composite  | 0             | Off    | {"flag": 2025, "value": 0} |
| Plessey          | 1             | On     | {"flag": 2026, "value": 1} |
| Plessey          | 0             | Off    | {"flag": 2026, "value": 0} |
| Telepen          | 1             | On     | {"flag": 2027, "value": 1} |
| Telepen          | 0             | Off    | {"flag": 2027, "value": 0} |
| RSS-14           | 1             | On     | {"flag": 2028, "value": 1} |
| RSS-14           | 0             | Off    | {"flag": 2028, "value": 0} |

<br>

