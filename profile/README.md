# opo200tw

歡迎來到 **opo200tw** 組織專案總覽。本組織主要維護嵌入式韌體、晶片平台 SDK 鏡像、影像與熱成像系統及相關周邊開發工具。

---

## 🦌 Animal Speaker（雙機式動物呼叫器）

> **雙機式動物叫聲遊戲呼叫器（Game-Call Device）韌體與平台架構**

| 專案 / 儲存庫 | 角色與定位 | 說明 |
| :--- | :--- | :--- |
| [**UM-GPM4**](https://github.com/opo200tw/UM-GPM4) | **平台對照庫（Platform Umbrella）** | GeneralPlus GPM47XXA 原廠 SDK 多版本（v1.0.3, v1.0.4-release）鏡像與 Meson 工具鏈對照庫 |
| [**UM-GPM4-AnimalSpeaker**](https://github.com/opo200tw/UM-GPM4-AnimalSpeaker) | **產品韌體正本（Canonical）** | 雙機式動物呼叫器產品韌體正本（HandUnit + Speaker + Bootloader + BLE 通訊協定） |

---

## 📷 影像、相機與感測系統（Vision, Camera & Sensing）

| 專案 / 儲存庫 | 狀態 / 角色 | 說明 |
| :--- | :--- | :--- |
| [**UM-GPM7-camera**](https://github.com/opo200tw/UM-GPM7-camera) | **主要專案** | GeneralPlus GPM7 / GPA7XXXA 智慧相機主程式韌體（熱成像 + TOF + RTSP + TUTK P2P） |
| [**UM-GPM7-camera-docs**](https://github.com/opo200tw/UM-GPM7-camera-docs) | **技術手冊** | GPM7 相機專案 1:1 PDF 原廠手冊、晶片暫存器與感測器規格書封存庫 |
| [**GPA7XXXA_V1.2**](https://github.com/opo200tw/GPA7XXXA_V1.2) | 📦 **已歸檔（Archived）** | 歷史專案已歸檔 |
| [**ThermalCAM**](https://github.com/opo200tw/ThermalCAM) | 📦 **已歸檔（Archived）** | [Deprecated] 早期原型專案已廢棄，功能由 camera 與獨立 sensor 模組取代 |
| [**ThermalCAM-TOF**](https://github.com/opo200tw/ThermalCAM-TOF) | 📦 **已歸檔（Archived）** | [Deprecated] 原為 UM-GPM7-camera 的 sensor，現已廢棄停用，僅供歷史參考 |
| [**UM-GPM4-camera**](https://github.com/opo200tw/UM-GPM4-camera) | 📦 **已歸檔（Archived）** | [Deprecated] 早期 GPM4 相機 RTSP 原型專案，因升級至 GPM7 (UM-GPM7-camera) 已廢棄 |

---

## 🔬 其他嵌入式與硬體專案（Other Embedded Projects）

| 專案 / 儲存庫 | 說明 |
| :--- | :--- |
| [**EMDR**](https://github.com/opo200tw/EMDR) | EMDR 相關專案韌體 |
| [**UM-ND52L15-HeartMath**](https://github.com/opo200tw/UM-ND52L15-HeartMath) | Nordic nRF52832（ND52L15）晶片之 HeartMath 專案韌體 |
| [**caller_and_remote**](https://github.com/opo200tw/caller_and_remote) | 早期呼叫器與遙控器歷史專案保存 |
| [**faaclib**](https://github.com/opo200tw/faaclib) | GPM4 |
| [**sdk_ref_v1.3.1**](https://github.com/opo200tw/sdk_ref_v1.3.1) | 嵌入式韌體專案 |

---

## 🛠️ 開發工具與周邊（Tools & Utilities）

| 專案 / 儲存庫 | 說明 |
| :--- | :--- |
| [**agents-serial-term**](https://github.com/opo200tw/agents-serial-term) | Cross-platform serial debug terminal (TUI + headless) for FTDI/CDC devices |
| [**demo-repository**](https://github.com/opo200tw/demo-repository) | A code repository designed to show the best GitHub has to offer. |
| [**image_tool**](https://github.com/opo200tw/image_tool) | OpenCV 相機校準輔助工具（熱成像與可見光 Homography 對齊、凌通專用畸變表生成） |

---

## 📚 常用通訊與基礎庫鏡像（Reference & Libraries）

- `ESP32_ApplicationShield`、`ESP32_ApplicationShield_HTPA`、`MLX90640-With-STM32`、`RTSPtoWeb`、`colorbar`、`crc32`、`csv_parser`、`doc`、`faac`、`html5_rtsp_player`、`ipchub`、`lal`、`leptonica`、`libg7112aac`、`mbedtls`、`naza`、`ringbuff`、`stb`、`stm32cube-platformio-freertos`、`x-cube-tof1`
