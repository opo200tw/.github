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
| [**UM-GPM7-camera**](https://github.com/opo200tw/UM-GPM7-camera) | **主要專案** | GeneralPlus GPM7 / GPA7XXXA 智慧相機主程式韌體（熱成像 + TOF + RTSP + TUTK P2P） |
| [**UM-GPM7-camera-docs**](https://github.com/opo200tw/UM-GPM7-camera-docs) | **技術手冊** | GPM7 相機專案 1:1 PDF 原廠手冊、晶片暫存器與感測器規格書封存庫 |

### 🔬 感測器驅動與核心模組（Sensors & Core Modules）

| 模組 / 儲存庫 | 適用硬體 / 類型 | 說明 |
| :--- | :--- | :--- |
| [**ESP32_ApplicationShield**](https://github.com/opo200tw/ESP32_ApplicationShield) | **Heimann HTPAd** | Heimann HTPAd 熱電堆陣列熱成像感測器驅動與校準計算（ESP32 平台） |
| [**ESP32_ApplicationShield_HTPA**](https://github.com/opo200tw/ESP32_ApplicationShield_HTPA) | **Heimann HTPAd** | Heimann HTPAd 熱電堆陣列熱成像感測器驅動與校準計算（ESP32 平台） |
| [**MLX90640-With-STM32**](https://github.com/opo200tw/MLX90640-With-STM32) | **MLX90640** | Melexis MLX90640 32×24 像素紅外熱成像陣列感測器驅動（STM32 平台） |
| [**mbedtls**](https://github.com/opo200tw/mbedtls) | **SSL/TLS 加密** | 輕量級嵌入式 SSL/TLS 加密庫（作為 UM-GPM7-camera 內部 lib/mbedtls 與 lwIP 網路安全連線之核心基礎） |
| [**ringbuff**](https://github.com/opo200tw/ringbuff) | **Lock-Free Buffer** | 高效無鎖環形緩衝區（作為 UM-GPM7-camera 內部 lib/RingBuffer Lock-Free SPSC 音視訊與通訊緩衝之核心基礎） |
| [**x-cube-tof1**](https://github.com/opo200tw/x-cube-tof1) | **VL53L4 TOF** | ST VL53L1 / VL53L4 TOF（Time-of-Flight）雷射測距感測器驅動套件 |

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
| [**image_tool**](https://github.com/opo200tw/image_tool) | OpenCV 相機校準輔助工具（熱成像與可見光 Homography 對齊、凌通專用畸變表生成） |

---

## 📦 已歸檔專案（Archived Projects）

| 專案 / 儲存庫 | 狀態 | 歸檔說明 |
| :--- | :--- | :--- |
| [**GPA7XXXA_V1.2**](https://github.com/opo200tw/GPA7XXXA_V1.2) | 📦 **已歸檔** | 歷史專案已歸檔封存 |
| [**ThermalCAM**](https://github.com/opo200tw/ThermalCAM) | 📦 **已歸檔** | [Deprecated] 早期原型專案已廢棄，功能由 camera 與獨立 sensor 模組取代 |
| [**ThermalCAM-TOF**](https://github.com/opo200tw/ThermalCAM-TOF) | 📦 **已歸檔** | [Deprecated] 原為 UM-GPM7-camera 的 sensor，現已廢棄停用，僅供歷史參考 |
| [**UM-GPM4-camera**](https://github.com/opo200tw/UM-GPM4-camera) | 📦 **已歸檔** | [Deprecated] 早期 GPM4 相機 RTSP 原型專案，因升級至 GPM7 (UM-GPM7-camera) 已廢棄 |

---

## 🛠️ 開發除錯工具與協定參考鏡像（Tools & Reference Mirrors）

| 工具 / 參考鏡像 | 領域 / 分類 | 說明與用途 |
| :--- | :--- | :--- |
| [**csv_parser**](https://github.com/opo200tw/csv_parser) | **⚙️ 嵌入式底層參考** | 純 C 語言 CSV 表格解析器（用於讀取感測器校準表與設定檔） |
| [**crc32**](https://github.com/opo200tw/crc32) | **⚙️ 演算法原理參考** | 高效 CRC32 校驗演算法庫（用於封包驗證與 OTA 完整性校驗） |
| [**RTSPtoWeb**](https://github.com/opo200tw/RTSPtoWeb) | **🎥 音視訊串流測試** | RTSP 轉 Web 播放伺服器（支援 WebRTC / MSE / HLS 瀏覽器即時預覽） |
| [**html5_rtsp_player**](https://github.com/opo200tw/html5_rtsp_player) | **🎥 音視訊串流測試** | HTML5 RTSP 網頁播放器前端組件（免外掛瀏覽器播放） |
| [**ipchub**](https://github.com/opo200tw/ipchub) | **🎥 音視訊串流測試** | 輕量級網路攝影機（IPC）流媒體伺服器與集中管理 |
| [**lal**](https://github.com/opo200tw/lal) | **🎥 音視訊串流測試** | 高效能音視訊直播流媒體伺服器（RTMP / RTSP / HLS / HTTP-FLV） |
| [**naza**](https://github.com/opo200tw/naza) | **🎥 音視訊串流測試** | Go 語言基礎公用函式庫（lal 串流伺服器依賴） |
| [**stm32cube-platformio-freertos**](https://github.com/opo200tw/stm32cube-platformio-freertos) | **📚 基礎庫** |  |
| [**faac**](https://github.com/opo200tw/faac) | **🔊 音訊轉碼參考** | AAC 音訊壓縮編碼庫（Freeware Advanced Audio Coder） |
| [**libg7112aac**](https://github.com/opo200tw/libg7112aac) | **🔊 音訊轉碼參考** | 嵌入式音訊轉碼庫（G.711 語音編碼 ➔ AAC 格式轉換） |
| [**doc**](https://github.com/opo200tw/doc) | **🔐 網路協定文件** | 音視訊 RFC 標準協議規範與測試用音視訊檔案庫 |
| [**stb**](https://github.com/opo200tw/stb) | **🖼️ 單檔工具庫參考** | 知名 C/C++ Header-only 單檔工具庫（stb_image, stb_truetype 等） |
| [**colorbar**](https://github.com/opo200tw/colorbar) | **🖼️ 影像測試工具** | 彩色測試圖條生成器（生成 RGB/YUV 各解析度測試圖，用於相機 ISP 除錯） |
| [**leptonica**](https://github.com/opo200tw/leptonica) | **🖼️ 影像演算法參考** | C 語言高效影像分析與幾何轉換演算法庫 |

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
- **專案歸檔**：將 Repo 設為 `Archive` 後，Action 就會自動將該專案移至【📦 已歸檔專案】區塊。
- **安全防護機制**：腳本內建防呆驗證，若權限異常或抓取數量不足，會自動中止執行，防止覆蓋現有完整目錄。
