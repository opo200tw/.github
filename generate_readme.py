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

    # 分類容器
    animal_speaker_repos = []
    camera_active_repos = []
    camera_archived_repos = []
    embedded_repos = []
    tool_repos = []
    other_archived_repos = []
    fork_repos = []

    for r in repos:
        name = r.get("name", "")
        desc = r.get("description") or ""
        is_archived = r.get("isArchived", False)
        is_fork = r.get("isFork", False)
        url = r.get("url", f"https://github.com/opo200tw/{name}")

        if name == ".github":
            continue

        item = {
            "name": name,
            "desc": desc,
            "url": url,
            "is_archived": is_archived,
            "is_fork": is_fork
        }

        # 1. 外部 Fork 基礎庫
        if is_fork:
            fork_repos.append(item)
            continue

        # 2. 已歸檔專案分類
        if is_archived:
            if "camera" in name.lower() or "thermal" in name.lower() or "gpa7" in name.lower():
                camera_archived_repos.append(item)
            else:
                other_archived_repos.append(item)
            continue

        # 3. Animal Speaker / GPM4 系列
        if "animalspeaker" in name.lower() or name == "UM-GPM4":
            item["role"] = "產品韌體正本（Canonical）" if "animalspeaker" in name.lower() else "平台對照庫（Platform Umbrella）"
            animal_speaker_repos.append(item)
            continue

        # 4. 相機與感測系統
        if "camera" in name.lower() or "gpm7" in name.lower() or "thermal" in name.lower():
            item["role"] = "技術手冊" if "docs" in name.lower() else "主要專案"
            camera_active_repos.append(item)
            continue

        # 5. 工具類
        if "term" in name.lower() or "tool" in name.lower() or "demo" in name.lower():
            tool_repos.append(item)
            continue

        # 6. 其他嵌入式
        embedded_repos.append(item)

    # 排序
    animal_speaker_repos.sort(key=lambda x: x["name"])
    camera_active_repos.sort(key=lambda x: x["name"])
    camera_archived_repos.sort(key=lambda x: x["name"])
    embedded_repos.sort(key=lambda x: x["name"])
    tool_repos.sort(key=lambda x: x["name"])
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
        "| 專案 / 儲存庫 | 狀態 / 角色 | 說明 |",
        "| :--- | :--- | :--- |"
    ])

    for r in camera_active_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | **{r.get('role', '主要專案')}** | {r['desc'] or '相機專案'} |")
    for r in camera_archived_repos:
        lines.append(f"| [**{r['name']}**]({r['url']}) | 📦 **已歸檔（Archived）** | {r['desc'] or '歷史專案已歸檔'} |")

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

    lines.append("")
    output_content = "\n".join(lines)

    # 輸出至檔案
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(output_content)

    os.makedirs("profile", exist_ok=True)
    with open("profile/README.md", "w", encoding="utf-8") as f:
        f.write(output_content)

    print("Generated README.md and profile/README.md successfully.")

if __name__ == "__main__":
    main()
