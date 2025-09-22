import re

def transform_tags_in_file(input_file_path, output_file_path):
    try:
     
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        text = re.sub(r'<(link)="([^"]+)">', r'<\1\="\2">', text)
      
        text = re.sub(r'<(size)=([^>]+)>', r'<\1\=\2>', text)
     
        text = re.sub(r'<(color)=#([^>]+)>', r'<\1\=#\2>', text)

       
        text = re.sub(r'<(sprite)=([^>]+)>', r'<\1\=\2>', text)

        
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f"Теги успешно преобразованы и сохранены в '{output_file_path}'.")
    
    except Exception as e:
        print(f"Ошибка при обработке файлов: {e}")


input_file_path = 'translated_output.txt'  # путь к исходному файлу
output_file_path = 'ver2.1_RU1.txt'  # путь для преобразованного файла
transform_tags_in_file(input_file_path, output_file_path)
