import os
import re
import sys

def process_files(input_files):
    """Обрабатывает файлы, извлекая строки с </link> или </color>"""
    extracted_lines = []
    
    for file_path in input_files:
        if not os.path.isfile(file_path):
            print(f"Файл не найден, пропускаем: {file_path}")
            continue
            
        if not file_path.lower().endswith('.txt'):
            print(f"Не TXT-файл, пропускаем: {file_path}")
            continue

        print(f"Обработка: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Ошибка чтения: {e}")
            continue

        tag_lines = []
        clean_lines = []
        pattern = re.compile(r'(</link>|</color>)', re.IGNORECASE)
        
        for line in lines:
            if pattern.search(line):
                tag_lines.append(line)
            else:
                clean_lines.append(line)

        if tag_lines:
            extracted_lines.extend(tag_lines)
            
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(clean_lines)
                print(f"Удалено строк: {len(tag_lines)}")
            except Exception as e:
                print(f"Ошибка записи: {e}")
        else:
            print("Совпадений нет")

    if extracted_lines:
        output_file = "extracted_tags.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(extracted_lines)
            print(f"\nСохранено в: {output_file}")
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

def main():
    if len(sys.argv) < 2:
        print("Перетащите TXT-файлы на скрипт")
        input("\nНажмите Enter...")
        return

    process_files(sys.argv[1:])
    input("\nГотово. Нажмите Enter...")

if __name__ == "__main__":
    main()