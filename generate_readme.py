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
    embedded_repos = []
    tool_repos = []
    archived_repos = []
    fork_repos = []

    # 4 個感測器專用庫名單
    sensor_repo_names = {
        "ESP32_ApplicationShield",
        "ESP32_ApplicationShield_HTPA",
        "MLX90640-With-STM32",
        "x-cube-tof1"
    }

    # 忽略的展示/內部庫名單
    ignored_repo_names = {".github", "demo-repository"}

    for r in repos:
        name = r.get("name", "")
        desc = r.get("description") or ""
        is_archived = r.get("isArchived", False)
        is_fork = r.get("isFork", False)
        url = r.get("url", f"https://github.com/opo200tw/{name}")

        if name in ignored_repo_names:
            continue

        item = {
            "name": name,
            "desc": desc,
            "url": url,
            "is_archived": is_archived,
            "is_fork": is_fork
        }

        # 1. 已歸檔專案（獨立專區）
        if is_archived:
            archived_repos.append(item)
            continue

        # 2. 相機與感測器參考庫（優先於一般 Fork 判定）
        if name in sensor_repo_names:
            if "ESP32" in name:
                item["desc"] = "Heimann HTPAd 熱電堆陣列熱成像感測器驅動與校準計算（ESP32 平台）"
            elif "MLX90640" in name:
                item["desc"] = "Melexis MLX90640 32×24 像素紅外熱成像陣列感測器驅動（STM32 平台）"
            elif "tof" in name.lower():
                item["desc"] = "ST VL53L1 / VL53L4 TOF（Time-of-Flight）雷射測距感測器驅動套件"
            camera_sensor_repos.append(item)
            continue

        # 3. 外部 Fork 基礎庫
        if is_fork:
            fork_repos.append(item)
            continue

        # 4. Animal Speaker / GPM4 系列
        if "animalspeaker" in name.lower() or name == "UM-GPM4":
            item["role"] = "產品韌體正本（Canonical）" if "animalspeaker" in name.lower() else "平台對照庫（Platform Umbrella）"
            animal_speaker_repos.append(item)
            continue

        # 5. 相機與影像系統主專案
        if "camera" in name.lower() or "gpm7" in name.lower() or "thermal" in name.lower():
            item["role"] = "技術手冊" if "docs" in name.lower() else ("平台 SDK 對照庫" if "sdk" in name.lower() else ("校準工具" if "undistort" in name.lower() else "主要專案"))
            camera_active_repos.append(item)
            continue

        # 6. 工具類
        if "term" in name.lower() or "tool" in name.lower() or "demo" in name.lower():
            tool_repos.append(item)
            continue

        # 7. 其他嵌入式
        embedded_repos.append(item)

    # 排序
    animal_speaker_repos.sort(key=lambda x: x["name"])
    camera_active_repos.sort(key=lambda x: x["name"])
    camera_sensor_repos.sort(key=lambda x: x["name"])
    embedded_repos.sort(key=lambda x: x["name"])
    tool_repos.sort(key=lambda x: x["name"])
    archived_repos.sort(key=lambda x: x["name"])
    fork_repos.sort(key=lambda x: x["name"])

    # 渲染 Markdown
    lines = [
        "# opo200tw",
        "",
        "歡迎來到 **opo200tw** 組織專案總覽。本組織主要維護嵌入式韌體、晶片平台 SDK 鏡像、影像與熱成像系統及相關周邊開發工具。",
        "",
        "---",
        "",
        "## 🦌 Animal Speaker（雙機式動物呼叫器）",
        "",
        "> **雙機式動物叫聲遊戲呼叫器（Game-Call Device）韌體與平台架構**",
        "",
        "| 專案 / 儲存庫 | 角色與定位 | 說明 |",
        "| :--- | :--- | :--- |"
    ]

    for r in animal_speaker_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | **{r.get('role', '專案')}** | {r['desc'] or '韌體專案'} |")

    lines.extend([
        "",
        "---",
        "",
        "## 📷 影像、相機與感測系統（Vision, Camera & Sensing）",
        "",
        "### 核心專案與文件",
        "",
        "| 專案 / 儲存庫 | 狀態 / 角色 | 說明 |",
        "| :--- | :--- | :--- |"
    ])

    for r in camera_active_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | **{r.get('role', '主要專案')}** | {r['desc'] or '相機專案'} |")

    if camera_sensor_repos:
        lines.extend([
            "",
            "### 🔬 感測器驅動與硬體參考（Sensors & Hardware Reference）",
            "",
            "| 感測器 / 儲存庫 | 適用感測器型號 | 說明 |",
            "| :--- | :--- | :--- |"
        ])
        for r in camera_sensor_repos:
            sensor_tag = "Heimann HTPAd" if "ESP32" in r["name"] else ("MLX90640" if "MLX" in r["name"] else "VL53L4 TOF")
            lines.append(f"| [**{r['name']}**]({r['url']}) | **{sensor_tag}** | {r['desc']} |")

    if embedded_repos:
        lines.extend([
            "",
            "---",
            "",
            "## 🔬 其他嵌入式與硬體專案（Other Embedded Projects）",
            "",
            "| 專案 / 儲存庫 | 說明 |",
            "| :--- | :--- |"
        ])
        for r in embedded_repos:
            lines.append(f"| [**{r['name']}**]({r['url']}) | {r['desc'] or '嵌入式韌體專案'} |")

    if tool_repos:
        lines.extend([
            "",
            "---",
            "",
            "## 🛠️ 開發工具與周邊（Tools & Utilities）",
            "",
            "| 專案 / 儲存庫 | 說明 |",
            "| :--- | :--- |"
        ])
        for r in tool_repos:
            lines.append(f"| [**{r['name']}**]({r['url']}) | {r['desc'] or '開發與輔助工具'} |")

    if archived_repos:
        lines.extend([
            "",
            "---",
            "",
            "## 📦 已歸檔專案（Archived Projects）",
            "",
            "| 專案 / 儲存庫 | 狀態 | 歸檔說明 |",
            "| :--- | :--- | :--- |"
        ])
        for r in archived_repos:
            lines.append(f"| [**{r['name']}**]({r['url']}) | 📦 **已歸檔** | {r['desc'] or '歷史專案已歸檔封存'} |")

    if fork_repos:
        lines.extend([
            "",
            "---",
            "",
            "## 📚 常用通訊與基礎庫鏡像（Reference & Libraries）",
            ""
        ])
        fork_links = [f"`{r['name']}`" for r in fork_repos]
        lines.append("- " + "、".join(fork_links))

    # 加入 Action 自動化維護與觸發說明區塊
    lines.extend([
        "",
        "---",
        "",
        "## ⚙️ 組織首頁自動同步機制（GitHub Actions Automation）",
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
        "- **專案歸檔**：將 Repo 設為 `Archive` 後，Action 會自動將該專案移至【📦 已歸檔專案】區塊。",
        "- **安全防護機制**：腳本內建防呆驗證，若權限異常或抓取數量不足，會自動中止執行，防止覆蓋現有完整目錄。"
    ])

    lines.append("")
    output_content = "\n".join(lines)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(output_content)

    os.makedirs("profile", exist_ok=True)
    with open("profile/README.md", "w", encoding="utf-8") as f:
        f.write(output_content)

    print("Generated README.md and profile/README.md successfully.")

if __name__ == "__main__":
    main()
