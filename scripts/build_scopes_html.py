import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
md_path = ROOT / "docs" / "index.md"
out_path = ROOT / "docs" / "_includes" / "scopes.html"

md = md_path.read_text(encoding="utf-8")
start = md.index('<details markdown="1">')
end = md.index("</details>\n\n<h2 id=\"step-7\">")
block = md[start:end]

parts = block.split("</summary>", 1)[1]
inners = re.findall(
    r'<details markdown="1">\s*<summary>(.*?)</summary>\s*(.*?)</details>',
    parts,
    re.S,
)


def md_table_to_html(table_md: str) -> str:
    lines = [line.strip() for line in table_md.strip().splitlines() if line.strip()]
    rows = []
    for line in lines:
        if re.fullmatch(r"\|[-:\s|]+\|", line):
            continue
        rows.append([cell.strip() for cell in line.strip("|").split("|")])

    if not rows:
        return ""

    chunks = ["<table>", "<thead><tr>"]
    for header in rows[0]:
        chunks.append(f"<th>{header}</th>")
    chunks.append("</tr></thead><tbody>")

    for row in rows[1:]:
        chunks.append("<tr>")
        for cell in row:
            cell = re.sub(r"`([^`]+)`", r"<code>\1</code>", cell)
            chunks.append(f"<td>{cell}</td>")
        chunks.append("</tr>")

    chunks.append("</tbody></table>")
    return "".join(chunks)


lines = [
    '<details class="scopes-outer">',
    "<summary><strong>Полный список доступных данных и scopes</strong></summary>",
    '<div class="scopes-list">',
]

for title, table_md in inners:
    lines.extend(
        [
            "<details>",
            f"<summary>{title.strip()}</summary>",
            md_table_to_html(table_md),
            "</details>",
        ]
    )

lines.extend(["</div>", "</details>"])
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {len(inners)} sections to {out_path}")
