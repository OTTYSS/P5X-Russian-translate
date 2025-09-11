import json

# читаем JSON
with open("skills.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lines = []
for item in data:
    # берём desc и заменяем настоящие переносы строк на текст "\n"
    desc = item.get("desc", "").replace("\n", "\\n")
    content = item.get("contentBG", "")
    if content:
        block = f'{desc}\\n<b><size=28><color=#850101>"{content}"</color></size></b>'
    else:
        block = desc
    lines.append(block)

# сохраняем в txt
with open("skills1.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
