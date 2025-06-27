import os
import sys

# выбор между языками

PROMPTS = {
    'en': {
        'select_lang': "Select language [en/ru/uk]: ",
        'action': "Select action (encrypt/decrypt): ",
        'file_location': "Enter the path to your file: ",
        'key': "Enter the key (integer): ",
        'output_name': "Enter the name for the output file: ",
        'output_location': "Enter the directory to save the file: ",
        'success': "File processed successfully.",
        'error': "Something went wrong: {}",
        'not_found': "File not found.",
        'invalid_action': "Invalid action. Use 'encrypt' or 'decrypt'.",
    },
    'ru': {
        'select_lang': "Выберите язык [en/ru/uk]: ",
        'action': "Укажите действие (encrypt/decrypt или шифровать/расшифровать): ",
        'file_location': "Укажите путь к файлу: ",
        'key': "Укажите ключ (целое число): ",
        'output_name': "Укажите имя выходного файла: ",
        'output_location': "Укажите папку для сохранения: ",
        'success': "Файл успешно обработан.",
        'error': "Что-то пошло не так: {}",
        'not_found': "Файл не найден.",
        'invalid_action': "Неправильное действие. Используйте 'encrypt'/'decrypt' или 'шифровать'/'расшифровать'.",
    },
    'uk': {
        'select_lang': "Оберіть мову [en/ru/uk]: ",
        'action': "Вкажіть дію (encrypt/decrypt або шифрувати/розшифрувати): ",
        'file_location': "Вкажіть шлях до файлу: ",
        'key': "Вкажіть ключ (ціле число): ",
        'output_name': "Вкажіть ім'я вихідного файлу: ",
        'output_location': "Вкажіть папку для збереження: ",
        'success': "Файл успішно оброблено.",
        'error': "Щось пішло не так: {}",
        'not_found': "Файл не знайдено.",
        'invalid_action': "Неправильна дія. Використайте 'encrypt'/'decrypt' або 'шифрувати'/'розшифрувати'.",
    }
}

ACTION_MAP = {
    'encrypt': 'encrypt', 'decrypt': 'decrypt',
    'шифровать': 'encrypt', 'расшифровать': 'decrypt',
    'шифрувати': 'encrypt', 'розшифрувати': 'decrypt'
}


# выбираем язык 
while True:
    lang_input = input(PROMPTS['en']['select_lang']).strip().lower()
    if lang_input in PROMPTS:
        lang = lang_input
        break
    print(f"Invalid language: {lang_input}")

p = PROMPTS[lang]

# выбираем действие
while True:
    action_input = input(p['action']).strip().lower()
    if action_input in ACTION_MAP:
        action = ACTION_MAP[action_input]
        break
    print(p['invalid_action'])

# выбираем файл 
x = input(p['file_location']).strip().strip('"')
try:
    key = int(input(p['key']))
except ValueError:
    print(p['error'].format("Invalid key format."))
    sys.exit(1)

# создаем новое имя файла и выбираем его путь
name = input(p['output_name'])
location = input('output_location:').strip().strip('"')

try:
    # Читаем исходный текстовый файлы в байтах
    with open(x, "rb") as f_in:
        data = f_in.read()
    # создаём новый массив той же длины   
    enc = bytearray(len(data))

    if action == "encrypt":
        # шифруем данные 
        for i in range(len(data)):
            enc[i] = (data[i] + key) % 256
    
    else:
        # дешифруем данные  
        for i in range(len(data)):
            enc[i] = (data[i] - key) % 256
    os.makedirs(location, exist_ok=True)
    out_path = os.path.join(location, name)
    with open(out_path, 'wb') as f_out:
        f_out.write(enc)

    #Запись резултата
    folder = location
    os.makedirs(folder, exist_ok=True)
    out_path = os.path.join(folder, name)
    with open(out_path, "wb") as f_out:
        f_out.write(enc)


    # пишем итоговый резютат
    print(p['success'])
except FileNotFoundError:
    print(p['not_found'])
except Exception as e:
    print(p['error'].format(e))