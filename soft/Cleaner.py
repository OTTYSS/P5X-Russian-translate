# coding: utf-8

def clean_file(file1, file2, output_file):

    with open(file1, "r", encoding="utf-8") as f1:
        lines1 = set(line.strip() for line in f1 if line.strip())


    with open(file2, "r", encoding="utf-8") as f2:
        lines2 = f2.readlines()

    result = []
    for line in lines2:
        if "=" in line:
            eng, rus = line.split("=", 1)
            if eng.strip() not in lines1:
                result.append(line)
        else:
            result.append(line)


    with open(output_file, "w", encoding="utf-8") as out:
        out.writelines(result)

    print(f"Готово ✅ Файл сохранён как: {output_file}")



clean_file("yumi_content.txt", "ConfDialog_RU_split.txt", "cleaned_file2.txt")
