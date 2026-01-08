import os
import re

# --- НАСТРОЙКИ ---
folder_path = './text'
master_file = 'master.txt'
encoding = 'utf-8'

def split_by_equal(line):
    """
    Разбивает строку по первому знаку '=', перед которым нет '\'.
    Использует негативный просмотр назад (negative lookbehind).
    """
    # Ищем знак =, перед которым нет символа \
    parts = re.split(r'(?<!\\)=', line.strip(), maxsplit=1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return None

def update_translations():
    master_path = os.path.join(folder_path, master_file)
    if not os.path.exists(master_path):
        print(f"Ошибка: Мастер-файл {master_file} не найден.")
        return

    # 1. Читаем большой файл
    master_data = {}
    with open(master_path, 'r', encoding=encoding) as f:
        for line in f:
            result = split_by_equal(line)
            if result:
                eng_key, rus_val = result
                master_data[eng_key] = rus_val

    keys_to_remove = set()

    # 2. Обходим файлы
    for filename in os.listdir(folder_path):
        if filename == master_file or not filename.endswith('.txt'):
            continue
        
        file_path = os.path.join(folder_path, filename)
        updated_lines = []
        file_changed = False

        with open(file_path, 'r', encoding=encoding) as f:
            lines = f.readlines()

        for line in lines:
            result = split_by_equal(line)
            if result:
                eng, rus = result
                if eng in master_data:
                    new_rus = master_data[eng]
                    # Меняем только если русский текст отличается
                    if new_rus != rus:
                        print(f"[{filename}] Замена для: {eng}")
                        line = f"{eng}={new_rus}\n"
                        file_changed = True
                        keys_to_remove.add(eng)
                    else:
                        # Приводим к стандарту без пробелов, даже если нет правок
                        line = f"{eng}={rus}\n"
            
            updated_lines.append(line if line.endswith('\n') else line + '\n')

        if file_changed:
            with open(file_path, 'w', encoding=encoding) as f:
                f.writelines(updated_lines)

    # 3. Обновляем мастер-файл (удаляем только те, что применились)
    remaining_lines = []
    with open(master_path, 'r', encoding=encoding) as f:
        for line in f:
            result = split_by_equal(line)
            if result:
                eng, _ = result
                if eng in keys_to_remove:
                    continue
            remaining_lines.append(line)

    with open(master_path, 'w', encoding=encoding) as f:
        f.writelines(remaining_lines)

    print(f"\nГотово! Обновлено уникальных строк: {len(keys_to_remove)}")

if __name__ == "__main__":
    update_translations()