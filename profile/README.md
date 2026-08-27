# opo200tw

歡迎來到 **opo200tw** 組織專案總覽。本組織主要維護嵌入式韌體、晶片平台 SDK 鏡像、影像與熱成像系統及相關周邊開發工具。

---

## 🦌 Animal Speaker（雙機式動物呼叫器）

> **雙機式動物叫聲遊戲呼叫器（Game-Call Device）韌體與平台架構**

| 專案 / 儲存庫 | 角色與定位 | 說明 |
| :--- | :--- | :--- |
| [**UM-GPM4-AnimalSpeaker**](https://github.com/opo200tw/UM-GPM4-AnimalSpeaker) | **產品韌體正本（Canonical）** | 雙機式動物呼叫器產品韌體（HandUnit 發射端 + Speaker 接收端 + Bootloader + BLE 通訊協定）。日常開發正本。 |
| [**UM-GPM4**](https://github.com/opo200tw/UM-GPM4) | **平台對照庫（Platform Umbrella）** | GeneralPlus GPM47XXA 原廠 SDK 多版本（`v1.0.3`、`v1.0.4-release`、`v1.0.4-2ndboot`）鏡像與 Meson 工具鏈對照。 |

---

## 📷 影像、相機與感測系統（Vision, Camera & Sensing）

| 專案 / 儲存庫 | 狀態 / 角色 | 說明 |
| :--- | :--- | :--- |
| [**UM-GPM7-camera**](https://github.com/opo200tw/UM-GPM7-camera) | **主要專案** | GeneralPlus GPM7 / GPA7XXXA 智慧相機主程式韌體（熱成像 + TOF + RTSP + TUTK P2P）。 |
| [**UM-GPM7-camera-docs**](https://github.com/opo200tw/UM-GPM7-camera-docs) | **技術手冊** | GPM7 相機專案 1:1 PDF 原廠手冊、晶片暫存器與感測器規格書封存庫。 |
| [**ThermalCAM-TOF**](https://github.com/opo200tw/ThermalCAM-TOF) | 📦 **已歸檔（Archived）** | 原為 `UM-GPM7-camera` 的 Sensor（TOF 測距與感測器模組），現已廢棄停用。 |
| [**ThermalCAM**](https://github.com/opo200tw/ThermalCAM) | 📦 **已歸檔（Archived）** | 早期 GPA7 原型專案，功能已被 `UM-GPM7-camera` 等專案取代。 |

---

## 🔬 其他嵌入式與硬體專案（Other Embedded Projects）

| 專案 / 儲存庫 | 說明 |
| :--- | :--- |
| [**UM-ND52L15-HeartMath**](https://github.com/opo200tw/UM-ND52L15-HeartMath) | Nordic nRF52832（ND52L15）晶片之 HeartMath 專案韌體。 |
| [**EMDR**](https://github.com/opo200tw/EMDR) | EMDR 相關專案韌體。 |
| [**caller_and_remote**](https://github.com/opo200tw/caller_and_remote) | 早期呼叫器與遙控器歷史專案保存。 |

---

## 🛠️ 開發工具與周邊（Tools & Utilities）

| 專案 / 儲存庫 | 說明 |
| :--- | :--- |
| [**agents-serial-term**](https://github.com/opo200tw/agents-serial-term) | 跨平台序列埠除錯終端工具（TUI + Headless），支援 FTDI / CDC 設備。 |
| [**image_tool**](https://github.com/opo200tw/image_tool) | OpenCV 相機校準輔助工具（熱成像與可見光 Homography 對齊、凌通專用畸變表生成）。 |
| [**rtsp_demo**](https://github.com/opo200tw/rtsp_demo) | RTSP 串流測試與驗證 Demo。 |

---

## 📚 常用通訊與基礎庫鏡像（Reference & Libraries）

- **音訊與串流**：`faac`、`faaclib`、`libg7112aac`、`lal`、`ipchub`、`RTSPtoWeb`、`html5_rtsp_player`
- **感測與平台**：`x-cube-tof1`、`MLX90640-With-STM32`、`ESP32_ApplicationShield`、`ESP32_ApplicationShield_HTPA`
- **安全與通用**：`mbedtls`、`ringbuff`、`csv_parser`、`stb`、`leptonica`
