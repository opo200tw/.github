import json
import os
import sys

def main():
    json_path = sys.argv[1] if len(sys.argv) > 1 else "repos.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        repos = json.load(f)

    if len(repos) < 10:
        print(f"Error: Only {len(repos)} repositories fetched. Missing private repo permissions? Aborting.")
        sys.exit(1)

    animal_speaker_repos = []
    camera_active_repos = []
    camera_sensor_repos = []
    medical_repos = []
    tool_repos = []
    archived_repos = []
    fork_stream_repos = []
    fork_media_repos = []
    fork_core_repos = []

    # 相機專用感測器與核心模組庫名單
    sensor_repo_names = {
        "ESP32_ApplicationShield",
        "ESP32_ApplicationShield_HTPA",
        "MLX90640-With-STM32",
        "x-cube-tof1",
        "ringbuff",
        "mbedtls"
    }

    # 忽略的展示/內部庫名單
    ignored_repo_names = {".github", "demo-repository"}

    stream_forks = {"RTSPtoWeb", "html5_rtsp_player", "ipchub", "lal", "naza", "jessibuca"}
    media_forks = {"faac", "libg7112aac", "colorbar", "leptonica", "stb"}
    core_forks = {"csv_parser", "crc32", "snagboot", "toolchains-builder", "doc"}

    # 外部開發工具與參考鏡像說明與分類字典
    ref_descriptions = {
        "RTSPtoWeb": ("🎥 音視訊串流", "RTSP 轉 Web 播放伺服器（支援 WebRTC / MSE / HLS 瀏覽器即時預覽）"),
        "html5_rtsp_player": ("🎥 音視訊串流", "HTML5 RTSP 網頁播放器前端組件（免外掛瀏覽器播放）"),
        "ipchub": ("🎥 音視訊串流", "輕量級網路攝影機（IPC）流媒體伺服器與集中管理"),
        "lal": ("🎥 音視訊串流", "高效能音視訊直播流媒體伺服器（RTMP / RTSP / HLS / HTTP-FLV）"),
        "naza": ("🎥 音視訊串流", "Go 語言基礎公用函式庫（lal 串流伺服器依賴）"),
        "jessibuca": ("🎥 音視訊串流", "開源純 H5 跨平台低延遲直播流播放器前端組件"),
        "faac": ("🔊 音訊轉碼", "AAC 音訊壓縮編碼庫（Freeware Advanced Audio Coder）"),
        "libg7112aac": ("🔊 音訊轉碼", "嵌入式音訊轉碼庫（G.711 語音編碼 ➔ AAC 格式轉換）"),
        "colorbar": ("🖼️ 影像測試", "彩色測試圖條生成器（生成 RGB/YUV 各解析度測試圖，用於相機 ISP 除錯）"),
        "leptonica": ("🖼️ 影像演算法", "C 語言高效影像分析與幾何轉換演算法庫"),
        "stb": ("🖼️ 單檔工具庫", "知名 C/C++ Header-only 單檔工具庫（stb_image, stb_truetype 等）"),
        "csv_parser": ("⚙️ 底層參考", "純 C 語言 CSV 表格解析器（用於讀取感測器校準表與設定檔）"),
        "crc32": ("⚙️ 演算法原理", "高效 CRC32 校驗演算法庫（用於封包驗證與 OTA 完整性校驗）"),
        "snagboot": ("⚙️ 燒錄復原", "嵌入式平台通用復原、開機導引與 Flash 燒錄工具"),
        "toolchains-builder": ("⚙️ 工具鏈建置", "嵌入式 GCC 交叉編譯工具鏈建置與自動化腳本"),
        "doc": ("🔐 協定規範", "音視訊 RFC 標準協議規範與測試用音視訊檔案庫"),
    }

    for r in repos:
        name = r.get("name", "")
        desc = r.get("description") or ""
        is_archived = r.get("isArchived", False)
        is_fork = r.get("isFork", False)
        is_private = r.get("isPrivate", True)
        url = r.get("url", f"https://github.com/opo200tw/{name}")

        if name in ignored_repo_names:
            continue

        vis = "🔒 私有" if is_private else ("🌐 參考" if is_fork else "🌐 開源")

        item = {
            "name": name,
            "desc": desc,
            "url": url,
            "vis": vis,
            "is_archived": is_archived,
            "is_fork": is_fork,
            "is_private": is_private
        }

        # 1. 已歸檔專案（獨立專區）
        if is_archived:
            archived_repos.append(item)
            continue

        # 2. 相機感測器與核心模組庫（優先於一般 Fork 判定）
        if name in sensor_repo_names:
            if "ESP32" in name:
                item["tag"] = "Heimann HTPAd"
                item["desc"] = "Heimann HTPAd 熱電堆陣列熱成像感測器驅動與校準計算（ESP32 平台）"
            elif "MLX90640" in name:
                item["tag"] = "MLX90640"
                item["desc"] = "Melexis MLX90640 32×24 像素紅外熱成像陣列感測器驅動（STM32 平台）"
            elif "tof" in name.lower():
                item["tag"] = "VL53L4 TOF"
                item["desc"] = "ST VL53L1 / VL53L4 TOF（Time-of-Flight）雷射測距感測器驅動套件"
            elif "ringbuff" in name.lower():
                item["tag"] = "Lock-Free Buffer"
                item["desc"] = "高效無鎖環形緩衝區（作為 UM-GPM7-camera 內部 lib/RingBuffer Lock-Free SPSC 音視訊緩衝之核心基礎）"
            elif "mbedtls" in name.lower():
                item["tag"] = "SSL/TLS 加密"
                item["desc"] = "輕量級嵌入式 SSL/TLS 加密庫（作為 UM-GPM7-camera 內部 lib/mbedtls 與 lwIP 網路安全連線之核心基礎）"
            camera_sensor_repos.append(item)
            continue

        # 3. 外部 Fork 基礎庫 / 開發除錯工具與協定參考鏡像
        if is_fork:
            category, custom_desc = ref_descriptions.get(name, ("📚 基礎庫", desc))
            item["category"] = category
            item["desc"] = custom_desc
            if name in stream_forks:
                fork_stream_repos.append(item)
            elif name in media_forks:
                fork_media_repos.append(item)
            else:
                fork_core_repos.append(item)
            continue

        # 4. Animal Speaker / GPM4 系列
        if "animalspeaker" in name.lower() or "gpm4" in name.lower():
            if "animalspeaker" in name.lower():
                item["role"] = "產品韌體正本（Canonical）"
            elif "doc" in name.lower():
                item["role"] = "原廠規格與手冊庫"
            elif name == "UM-GPM4":
                item["role"] = "平台對照庫（Platform Umbrella）"
            elif "image-tool" in name.lower():
                item["role"] = "UI 圖像轉換工具"
            else:
                item["role"] = "SDK 歷史快照"
            animal_speaker_repos.append(item)
            continue

        # 5. 相機與影像系統主專案
        if "camera" in name.lower() or "gpm7" in name.lower() or "thermal" in name.lower():
            if name == "UM-GPM7-camera":
                item["role"] = "主要產品正本（Canonical）"
            elif name == "UM-GPM7":
                item["role"] = "平台治理庫（Platform Umbrella）"
            elif "sdk" in name.lower():
                item["role"] = "平台 SDK 對照庫"
            elif "doc" in name.lower():
                item["role"] = "原廠規格與硬體設計庫"
            elif "undistort" in name.lower():
                item["role"] = "鏡頭校準與雙光對齊"
            else:
                item["role"] = "主要專案"
            camera_active_repos.append(item)
            continue

        # 6. 自研開發與量產除錯工具（tutk, agents-serial-term, nrf-command-line-factory）
        if "tutk" in name.lower() or "term" in name.lower() or "tool" in name.lower() or "demo" in name.lower() or "factory" in name.lower() or "serial" in name.lower():
            if "tutk" in name.lower():
                item["role"] = "P2P 串流 SDK 移植與除錯 CLI"
            elif "term" in name.lower():
                item["role"] = "跨平台序列除錯終端（Go TUI）"
            elif "factory" in name.lower():
                item["role"] = "工廠量產自動化燒錄與測試"
            else:
                item["role"] = "開發輔助工具"
            tool_repos.append(item)
            continue

        # 7. 醫療與物聯網韌體（Medical & IoT Systems）
        if "neurotek" in name.lower() or "heartmath" in name.lower() or "emdr" in name.lower():
            if name == "UM-odi-neurotek-ble-system":
                item["role"] = "系統整合工作區（Umbrella Workspace）"
            elif name == "odi-neurotek-ble-system-fw":
                item["role"] = "醫療設備系統韌體（Zephyr / NCS）"
            elif name == "odi-neurotek-ble-system-sw":
                item["role"] = "跨平台應用軟體（Flutter App）"
            elif "heartmath" in name.lower():
                item["role"] = "HeartMath 產品韌體正本"
            elif "emdr" in name.lower():
                item["role"] = "EMDR 產品韌體正本"
            else:
                item["role"] = "醫療韌體專案"
            medical_repos.append(item)
            continue

        medical_repos.append(item)

    # 排序規則
    animal_speaker_repos.sort(key=lambda x: x["name"])
    camera_active_repos.sort(key=lambda x: x["name"])
    camera_sensor_repos.sort(key=lambda x: x["name"])
    medical_repos.sort(key=lambda x: x["name"])
    tool_repos.sort(key=lambda x: x["name"])
    archived_repos.sort(key=lambda x: x["name"])
    fork_stream_repos.sort(key=lambda x: x["name"])
    fork_media_repos.sort(key=lambda x: x["name"])
    fork_core_repos.sort(key=lambda x: x["name"])

    # 渲染 Markdown
    lines = [
        "# opo200tw ⚡",
        "",
        "> **專注於嵌入式系統（Embedded Systems）、晶片平台 SDK 治理、雙光熱成像與智慧相機（Thermal & Vision AI）、BLE 醫療物聯網（Medical IoT）及量產除錯工具開發。**",
        "",
        "<p align=\"left\">",
        "  <img src=\"https://img.shields.io/badge/Status-Active%20Engineering-blue?style=flat-square\" alt=\"Status\" />",
        "  <img src=\"https://img.shields.io/badge/Language-C%20%7C%20C%2B%2B%20%7C%20Go%20%7C%20Python%20%7C%20Dart-green?style=flat-square\" alt=\"Languages\" />",
        "  <img src=\"https://img.shields.io/badge/RTOS-Zephyr%20%7C%20FreeRTOS-purple?style=flat-square\" alt=\"RTOS\" />",
        "  <img src=\"https://img.shields.io/badge/Silicon-Nordic%20nRF%20%7C%20GeneralPlus%20GPM-orange?style=flat-square\" alt=\"Silicon\" />",
        "</p>",
        "",
        "---",
        "",
        "### 🧭 專案領域快速導覽",
        "- 🦌 [**Animal Speaker 系列（GPM4 雙機遊戲呼叫器）**](#-animal-speaker雙機式動物呼叫器--gpm4-系列)",
        "- 📷 [**智慧相機與感測系統（GPM7 雙光熱成像 / TOF）**](#-影像相機與感測系統vision-camera--sensing--gpm7-系列)",
        "- 🧬 [**醫療照護與 BLE 物聯網韌體（Neurotek EMDR / HeartMath）**](#-醫療照護與-ble-物聯網韌體medical--iot-systems)",
        "- 🛠️ [**自研開發與量產除錯工具（Serial Term / nRF Factory / TUTK）**](#-自研開發與量產除錯工具in-house-tools--utilities)",
        "- 📚 [**開源技術與協定參考鏡像（串流 / 播放器 / 演算法 / 工具鏈）**](#-開源技術與協定參考鏡像third-party-mirrors--reference-libraries)",
        "- 📦 [**歷史歸檔專案（已封存原型與分支）**](#-已歸檔專案archived-projects)",
        "",
        "---",
        "",
        "## 🦌 Animal Speaker（雙機式動物呼叫器 / GPM4 系列）",
        "",
        "> **雙機式動物叫聲遊戲呼叫器（Game-Call Device）韌體與晶片平台架構**",
        "",
        "| 專案 / 儲存庫 | 權限 | 角色與定位 | 說明 |",
        "| :--- | :---: | :--- | :--- |"
    ]

    for r in animal_speaker_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | {r['vis']} | **{r.get('role', '專案')}** | {r['desc'] or '韌體專案'} |")

    lines.extend([
        "",
        "---",
        "",
        "## 📷 影像、相機與感測系統（Vision, Camera & Sensing / GPM7 系列）",
        "",
        "### 核心專案與平台規格",
        "",
        "| 專案 / 儲存庫 | 權限 | 角色與定位 | 說明 |",
        "| :--- | :---: | :--- | :--- |"
    ])

    for r in camera_active_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | {r['vis']} | **{r.get('role', '主要專案')}** | {r['desc'] or '相機專案'} |")

    if camera_sensor_repos:
        lines.extend([
            "",
            "### 🔬 感測器驅動與核心模組（Sensors & Core Modules）",
            "",
            "| 模組 / 儲存庫 | 權限 | 適用硬體 / 類型 | 說明 |",
            "| :--- | :---: | :--- | :--- |"
        ])
        for r in camera_sensor_repos:
            lines.append(f"| [**{r['name']}**]({r['url']}) | {r['vis']} | **{r.get('tag', '核心模組')}** | {r['desc']} |")

    if medical_repos:
        lines.extend([
            "",
            "---",
            "",
            "## 🧬 醫療照護與 BLE 物聯網韌體（Medical & IoT Systems）",
            "",
            "| 專案 / 儲存庫 | 權限 | 角色與定位 | 說明 |",
            "| :--- | :---: | :--- | :--- |"
        ])
        for r in medical_repos:
            lines.append(f"| [**{r['name']}**]({r['url']}) | {r['vis']} | **{r.get('role', '醫療韌體專案')}** | {r['desc'] or '嵌入式韌體專案'} |")

    if tool_repos:
        lines.extend([
            "",
            "---",
            "",
            "## 🛠️ 自研開發與量產除錯工具（In-house Tools & Utilities）",
            "",
            "| 專案 / 儲存庫 | 權限 | 角色與定位 | 說明 |",
            "| :--- | :---: | :--- | :--- |"
        ])
        for r in tool_repos:
            lines.append(f"| [**{r['name']}**]({r['url']}) | {r['vis']} | **{r.get('role', '開發與輔助工具')}** | {r['desc'] or '開發與輔助工具'} |")

    lines.extend([
        "",
        "---",
        "",
        "## 📚 開源技術與協定參考鏡像（Third-party Mirrors & Reference Libraries）",
        "",
        "### 🎥 音視訊串流與播放測試",
        "",
        "| 工具 / 參考鏡像 | 領域 / 分類 | 說明與用途 |",
        "| :--- | :--- | :--- |"
    ])
    for r in fork_stream_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | **{r.get('category', '串流測試')}** | {r['desc']} |")

    lines.extend([
        "",
        "### 🔊 音訊轉碼與影像處理",
        "",
        "| 工具 / 參考鏡像 | 領域 / 分類 | 說明與用途 |",
        "| :--- | :--- | :--- |"
    ])
    for r in fork_media_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | **{r.get('category', '媒體處理')}** | {r['desc']} |")

    lines.extend([
        "",
        "### ⚙️ 底層演算法、工具鏈與系統輔助",
        "",
        "| 工具 / 參考鏡像 | 領域 / 分類 | 說明與用途 |",
        "| :--- | :--- | :--- |"
    ])
    for r in fork_core_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | **{r.get('category', '系統輔助')}** | {r['desc']} |")

    if archived_repos:
        lines.extend([
            "",
            "---",
            "",
            "## 📦 已歸檔專案（Archived Projects）",
            "",
            "| 專案 / 儲存庫 | 權限 | 狀態 | 歸檔說明與重構去向 |",
            "| :--- | :---: | :---: | :--- |"
        ])
        for r in archived_repos:
            lines.append(f"| [**{r['name']}**]({r['url']}) | {r['vis']} | 📦 **已歸檔** | {r['desc'] or '歷史專案已歸檔封存'} |")

    lines.extend([
        "",
        "---",
        "",
        "<details>",
        "<summary><b>⚙️ 組織首頁自動同步機制與維護指引（GitHub Actions Automation）</b></summary>",
        "",
        "本首頁目錄由 [**GitHub Actions (`sync-profile.yml`)**](https://github.com/opo200tw/.github/actions/workflows/sync-profile.yml) 搭配 [`generate_readme.py`](https://github.com/opo200tw/.github/blob/main/generate_readme.py) 自動維護與生成：",
        "",
        "### 🔄 預期觸發方式（Trigger Actions）",
        "1. **⏰ 每日自動排程（Scheduled Sync）**：",
        "   - 每天台灣時間 **早上 08:00（UTC 00:00）** 自動巡檢組織內所有 Repositories，自動偵測新增、改名、修改描述或歸檔狀態並同步更新。",
        "2. **🔘 手動一鍵即時觸發（Manual Trigger）**：",
        "   - 若剛完成 Repo 新增、改名或歸檔，可隨時前往 👉 [**Actions 頁面**](https://github.com/opo200tw/.github/actions/workflows/sync-profile.yml) 點擊 **`Run workflow`** 按鈕，約 15 秒內即可完成首頁刷新。",
        "3. **💻 本機 CLI 一行觸發（CLI Trigger）**：",
        "   ```bash",
        "   gh workflow run sync-profile.yml --repo opo200tw/.github",
        "   ```",
        "",
        "### 📝 日常維護方式（Maintenance Guide）",
        "- **修改專案說明**：只需直接在各 Repo 的 GitHub 設定頁（About 齒輪）修改 `Description`，Action 就會自動抓取最新說明並填入表格。",
        "- **專案歸檔**：將 Repo 設為 `Archive` 後，Action 就會自動將該專案移至【📦 已歸檔專案】區塊。",
        "- **安全防護機制**：腳本內建防呆驗證，若權限異常或抓取數量不足，會自動中止執行，防止覆蓋現有完整目錄。",
        "",
        "</details>",
        ""
    ])

    output_content = "\n".join(lines)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(output_content)

    os.makedirs("profile", exist_ok=True)
    with open("profile/README.md", "w", encoding="utf-8") as f:
        f.write(output_content)

    print("Generated README.md and profile/README.md successfully.")

if __name__ == "__main__":
    main()
