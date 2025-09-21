#!/usr/bin/env python3
import os, re, textwrap, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, ".."))

def first_heading(p):
    if not os.path.exists(p): return ""
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                return re.sub(r'^#+\s*', '', s)  # "# Title" -> "Title"
    return ""

def read_tistory_url(dirpath):
    u = os.path.join(dirpath, "tistory.url")
    if os.path.exists(u):
        with open(u, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

def collect_weeks():
    items = []
    for name in sorted(os.listdir(REPO)):
        if re.match(r"^\d+_", name) and os.path.isdir(os.path.join(REPO, name)):
            week_dir = os.path.join(REPO, name)
            title = first_heading(os.path.join(week_dir, "README.md"))
            tistory = read_tistory_url(week_dir)
            items.append((name, title, tistory))
    return items

def make_table(rows):
    out = ["| Week | Topic | Notes | Tistory |", "|---|---|---|---|"]
    for name, title, tistory in rows:
        week_no = re.match(r"^(\d+)_", name).group(1)
        topic = title if title else name
        notes_link = f"[{name}](./{name}/README.md)" if os.path.exists(os.path.join(REPO, name, "README.md")) else f"./{name}/"
        tistory_link = f"[바로가기]({tistory})" if tistory else ""
        out.append(f"| {week_no} | {topic} | {notes_link} | {tistory_link} |")
    return "\n".join(out) + "\n"

def render_readme(table_md):
    body = f"""# Operating System

강의·과제·팀프로젝트 산출물을 **주차별 폴더**로 정리합니다.  
아래 주차 표는 푸시 시 자동으로 갱신됩니다.

## 주차 인덱스 (Auto)
{table_md}
## 바로가기
- 주차 폴더 루트: [./](./)
- 과제: [assignments/](./assignments/)
- 팀프로젝트: [team/](./team/)

## 규칙
- 주차: `번호_주제/README.md`, `sql/`, `tistory.url` (선택)

> 이 README는 GitHub Actions로 자동 갱신됩니다.
"""
    return textwrap.dedent(body)

def main():
    rows = collect_weeks()
    table = make_table(rows)
    out = render_readme(table)
    path = os.path.join(REPO, "README.md")
    old = ""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()
    if old != out:
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)

if __name__ == "__main__":
    sys.exit(main())
