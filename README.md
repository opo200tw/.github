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

### 核心專案與文件

| 專案 / 儲存庫 | 狀態 / 角色 | 說明 |
| :--- | :--- | :--- |
| [**UM-GPM7-SDK-v1.3.1**](https://github.com/opo200tw/UM-GPM7-SDK-v1.3.1) | **平台 SDK 對照庫** | GeneralPlus GPM7 / GPA7XXXA 原廠 SDK v1.3.1 平台對照庫 |
| [**UM-GPM7-camera**](https://github.com/opo200tw/UM-GPM7-camera) | **主要專案** | GeneralPlus GPM7 / GPA7XXXA 智慧相機主程式韌體（熱成像 + TOF + RTSP + TUTK P2P） |
| [**UM-GPM7-camera-docs**](https://github.com/opo200tw/UM-GPM7-camera-docs) | **技術手冊** | GPM7 相機專案 1:1 PDF 原廠手冊、晶片暫存器與感測器規格書封存庫 |
| [**UM-GPM7-camera-undistort**](https://github.com/opo200tw/UM-GPM7-camera-undistort) | **校準工具** | GPM7 相機鏡頭畸變校正表生成與雙光單應性對齊工具（OpenCV） |

### 🔬 感測器驅動與硬體參考（Sensors & Hardware Reference）

| 感測器 / 儲存庫 | 適用感測器型號 | 說明 |
| :--- | :--- | :--- |
| [**ESP32_ApplicationShield**](https://github.com/opo200tw/ESP32_ApplicationShield) | **Heimann HTPAd** | Heimann HTPAd 熱電堆陣列熱成像感測器驅動與校準計算（ESP32 平台） |
| [**MLX90640-With-STM32**](https://github.com/opo200tw/MLX90640-With-STM32) | **MLX90640** | Melexis MLX90640 32×24 像素紅外熱成像陣列感測器驅動（STM32 平台） |
| [**x-cube-tof1**](https://github.com/opo200tw/x-cube-tof1) | **VL53L4 TOF** | ST VL53L1 / VL53L4 TOF（Time-of-Flight）雷射測距感測器驅動套件 |

---

## 🔬 其他嵌入式與硬體專案（Other Embedded Projects）

| 專案 / 儲存庫 | 說明 |
| :--- | :--- |
| [**UM-ND52L15-EMDR**](https://github.com/opo200tw/UM-ND52L15-EMDR) | Nordic nRF52832（ND52L15）晶片之 EMDR 專案韌體 |
| [**UM-ND52L15-HeartMath**](https://github.com/opo200tw/UM-ND52L15-HeartMath) | Nordic nRF52832（ND52L15）晶片之 HeartMath 專案韌體 |
| [**faaclib**](https://github.com/opo200tw/faaclib) | GPM4 |

---

## 🛠️ 開發工具與周邊（Tools & Utilities）

| 專案 / 儲存庫 | 說明 |
| :--- | :--- |
| [**agents-serial-term**](https://github.com/opo200tw/agents-serial-term) | Cross-platform serial debug terminal (TUI + headless) for FTDI/CDC devices |

---

## 📦 已歸檔專案（Archived Projects）

| 專案 / 儲存庫 | 狀態 | 歸檔說明 |
| :--- | :--- | :--- |
| [**ESP32_ApplicationShield_HTPA**](https://github.com/opo200tw/ESP32_ApplicationShield_HTPA) | 📦 **已歸檔** | [Deprecated] Heimann HTPAd 熱成像感測器舊版驅動快照，已被 ESP32_ApplicationShield 最新版取代封存 |
| [**GPA7XXXA_V1.2**](https://github.com/opo200tw/GPA7XXXA_V1.2) | 📦 **已歸檔** | [Deprecated] 早期 GeneralPlus GPA7 原廠 SDK V1.2 歷史版本，已由 UM-GPM7-SDK-v1.3.1 與 UM-GPM7-camera 取代封存 |
| [**ThermalCAM**](https://github.com/opo200tw/ThermalCAM) | 📦 **已歸檔** | [Deprecated] 早期熱成像原型，已重構為 UM-GPM7-camera 獨立 Demo (sensorProject/HTPA，Target: HTPA) |
| [**ThermalCAM-TOF**](https://github.com/opo200tw/ThermalCAM-TOF) | 📦 **已歸檔** | [Deprecated] 早期 TOF 測距原型，已重構為 UM-GPM7-camera 獨立 Demo (sensorProject/TOF，Target: TOF) |
| [**UM-GPM4-camera**](https://github.com/opo200tw/UM-GPM4-camera) | 📦 **已歸檔** | [Deprecated] 早期 GPM4 相機 RTSP 原型專案，因升級至 GPM7 (UM-GPM7-camera) 已廢棄 |
| [**caller_and_remote**](https://github.com/opo200tw/caller_and_remote) | 📦 **已歸檔** | [Deprecated] 早期 Bitbucket 託管之動物呼叫器舊版原始碼備份，已被 UM-GPM4-AnimalSpeaker 取代封存 |

---

## 📚 常用通訊與基礎庫鏡像（Reference & Libraries）

| 儲存庫 / 鏡像 | 領域 / 分類 | 說明與用途 |
| :--- | :--- | :--- |
| [**crc32**](https://github.com/opo200tw/crc32) | **⚙️ 嵌入式底層與工具** | 高效 CRC32 校驗演算法庫（用於封包驗證與 OTA 完整性校驗） |
| [**csv_parser**](https://github.com/opo200tw/csv_parser) | **⚙️ 嵌入式底層與工具** | 純 C 語言 CSV 表格解析器（用於讀取感測器校準表與設定檔） |
| [**ringbuff**](https://github.com/opo200tw/ringbuff) | **⚙️ 嵌入式底層與工具** | 高效無鎖環形緩衝區（作為 UM-GPM7-camera 內部 lib/RingBuffer Lock-Free SPSC 音視訊與通訊緩衝之核心基礎） |
| [**stm32cube-platformio-freertos**](https://github.com/opo200tw/stm32cube-platformio-freertos) | **⚙️ 嵌入式底層與工具** | STM32Cube 結合 PlatformIO 與 FreeRTOS 專案環境參考 |
| [**RTSPtoWeb**](https://github.com/opo200tw/RTSPtoWeb) | **🎥 音視訊串流** | RTSP 轉 Web 播放伺服器（支援 WebRTC / MSE / HLS 瀏覽器即時預覽） |
| [**html5_rtsp_player**](https://github.com/opo200tw/html5_rtsp_player) | **🎥 音視訊串流** | HTML5 RTSP 網頁播放器前端組件（免外掛瀏覽器播放） |
| [**ipchub**](https://github.com/opo200tw/ipchub) | **🎥 音視訊串流** | 輕量級網路攝影機（IPC）流媒體伺服器與集中管理 |
| [**lal**](https://github.com/opo200tw/lal) | **🎥 音視訊串流** | 高效能音視訊直播流媒體伺服器（RTMP / RTSP / HLS / HTTP-FLV） |
| [**naza**](https://github.com/opo200tw/naza) | **🎥 音視訊串流** | Go 語言基礎公用函式庫（lal 串流伺服器依賴） |
| [**faac**](https://github.com/opo200tw/faac) | **🔊 音訊編碼與轉碼** | AAC 音訊壓縮編碼庫（Freeware Advanced Audio Coder） |
| [**libg7112aac**](https://github.com/opo200tw/libg7112aac) | **🔊 音訊編碼與轉碼** | 嵌入式音訊轉碼庫（G.711 語音編碼 ➔ AAC 格式轉換） |
| [**doc**](https://github.com/opo200tw/doc) | **🔐 網路安全與協定文件** | 音視訊 RFC 標準協議規範與測試用音視訊檔案庫 |
| [**mbedtls**](https://github.com/opo200tw/mbedtls) | **🔐 網路安全與協定文件** | 輕量級嵌入式 SSL/TLS 加密與安全演算法庫（Arm 原廠開源） |
| [**colorbar**](https://github.com/opo200tw/colorbar) | **🖼️ 影像處理與測試** | 彩色測試圖條生成器（生成 RGB/YUV 各解析度測試圖，用於相機 ISP 除錯） |
| [**leptonica**](https://github.com/opo200tw/leptonica) | **🖼️ 影像處理與測試** | C 語言高效影像分析與幾何轉換演算法庫 |
| [**stb**](https://github.com/opo200tw/stb) | **🖼️ 影像處理與測試** | 知名 C/C++ Header-only 單檔工具庫（stb_image, stb_truetype 等） |

---

## ⚙️ 組織首頁自動同步機制（GitHub Actions Automation）

本首頁目錄由 [**GitHub Actions (`sync-profile.yml`)**](https://github.com/opo200tw/.github/actions/workflows/sync-profile.yml) 搭配 [`generate_readme.py`](https://github.com/opo200tw/.github/blob/main/generate_readme.py) 自動維護與生成：

### 🔄 預期觸發方式（Trigger Actions）
1. **⏰ 每日自動排程（Scheduled Sync）**：
   - 每天台灣時間 **早上 08:00（UTC 00:00）** 自動巡檢組織內所有 Repositories，自動偵測新增、改名、修改描述或歸檔狀態並同步更新。
2. **🔘 手動一鍵即時觸發（Manual Trigger）**：
   - 若剛完成 Repo 新增、改名或歸檔，可隨時前往 👉 [**Actions 頁面**](https://github.com/opo200tw/.github/actions/workflows/sync-profile.yml) 點擊 **`Run workflow`** 按鈕，約 15 秒內即可完成首頁刷新。
3. **💻 本機 CLI 一行觸發（CLI Trigger）**：
   ```bash
   gh workflow run sync-profile.yml --repo opo200tw/.github
   ```

### 📝 日常維護方式（Maintenance Guide）
- **修改專案說明**：只需直接在各 Repo 的 GitHub 設定頁（About 齒輪）修改 `Description`，Action 就會自動抓取最新說明並填入表格。
- **專案歸檔**：將 Repo 設為 `Archive` 後，Action 會自動將該專案移至【📦 已歸檔專案】區塊。
- **安全防護機制**：腳本內建防呆驗證，若權限異常或抓取數量不足，會自動中止執行，防止覆蓋現有完整目錄。
