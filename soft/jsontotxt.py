import json
import sys
import os
from collections import defaultdict

if len(sys.argv) < 2:
    print("Перетащи один или несколько JSON-файлов на этот скрипт.")
    input("Нажми Enter для выхода...")
    sys.exit(1)

for input_path in sys.argv[1:]:
    print(f"\nОбработка файла: {input_path}")

    if not input_path.lower().endswith('.json'):
        print(f"Пропущен (не JSON): {input_path}")
        continue

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка при чтении {input_path}: {e}")
        continue

    grouped_strings = defaultdict(set)  

    for item in data:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    escaped_value = value.encode('unicode_escape').decode('utf-8')
                    grouped_strings[key].add(escaped_value)  

    output_lines = []
    for key in sorted(grouped_strings.keys()):
        output_lines.append(f"=== {key} ===")
        output_lines.extend(sorted(grouped_strings[key]))  
        output_lines.append("")  

    output_text = "\n".join(output_lines)
    output_file = os.path.splitext(input_path)[0] + "_unique_strings.txt" 

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_text)
        print(f"Готово: {output_file} (уникальных значений: {sum(len(v) for v in grouped_strings.values())})")
    except Exception as e:
        print(f"Ошибка при сохранении {output_file}: {e}")

input("\nВсе файлы обработаны. Нажми Enter для выхода...")