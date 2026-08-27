# opo200tw

歡迎來到 **opo200tw** 組織專案總覽。本組織主要維護嵌入式韌體、晶片平台 SDK 鏡像、影像與熱成像系統及相關周邊開發工具。

---

## 🦌 Animal Speaker（雙機式動物呼叫器）

> **雙機式動物叫聲遊戲呼叫器（Game-Call Device）韌體與平台架構**

| 專案 / 儲存庫 | 角色與定位 | 說明 |
| :--- | :--- | :--- |
| [**AnimalSpeaker**](https://github.com/opo200tw/AnimalSpeaker) | **產品韌體正本（Canonical）** | 包含 HandUnit（發射端）、Speaker（接收端）、Bootloader 與 BLE 通訊協定。日常開發與維護的核心儲存庫。 |
| [**UM-GPM4**](https://github.com/opo200tw/UM-GPM4) | **平台對照庫（Platform Umbrella）** | GeneralPlus GPM47XXA 原廠 SDK 多版本（`v1.0.3`、`v1.0.4-release`、`v1.0.4-2ndboot`）鏡像與 Meson 工具鏈對照。 |

---

## 📷 影像、相機與感測系統（Vision, Camera & Sensing）

| 專案 / 儲存庫 | 狀態 / 角色 | 說明 |
| :--- | :--- | :--- |
| [**camera**](https://github.com/opo200tw/camera) | **主要專案** | A7 影像系統主程式韌體 |
| [**camera-docs**](https://github.com/opo200tw/camera-docs) | **技術手冊** | 相機相關技術手冊與 PDF 規格文件庫（1:1 路徑對照） |
| [**ThermalCAM-TOF**](https://github.com/opo200tw/ThermalCAM-TOF) | **Sensor 模組** | 用於 `UM-GPM7-camera` 的 Sensor（TOF 測距與感測器模組） |
| [**ThermalCAM**](https://github.com/opo200tw/ThermalCAM) | ⚠️ **已廢棄（Deprecated）** | 早期 GPA7 / Wi-Fi / P2P 原型專案。因架構重組、功能已解耦拆分並由後續專案（如 `camera` 與獨立 sensor 模組）取代，僅保留歷史參考。 |

---

## 🛠️ 開發工具與周邊（Tools & Utilities）

| 專案 / 儲存庫 | 說明 |
| :--- | :--- |
| [**agents-serial-term**](https://github.com/opo200tw/agents-serial-term) | 跨平台序列埠除錯終端工具（TUI + Headless），支援 FTDI / CDC 設備 |
| [**image_tool**](https://github.com/opo200tw/image_tool) | 影像處理與格式轉換輔助工具 |

---

## 📚 常用通訊與基礎庫鏡像（Reference & Libraries）

- **音訊與串流**：`faac`、`libg7112aac`、`lal`、`ipchub`、`RTSPtoWeb`、`html5_rtsp_player`
- **安全與通用**：`mbedtls`、`ringbuff`、`csv_parser`、`stb`、`leptonica`
