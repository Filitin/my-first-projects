import os

action = input("Укажите действие(encrypt/decrypt):\n").strip().lower()

x = input("Укажите локацию своего файла:\n").strip().strip('"')

key = int(input("Укажите ключ:\n"))

name = input("Укажите название файла:\n")

location = input("Укажите локацию для сохранения файла:\n").strip().strip('"')

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
    
    elif action == "decrypt":
        # дешифруем данные  
        for i in range(len(data)):
            enc[i] = (data[i] - key) % 256
    else:
        raise ValueError("Неправильное действие.")
    #Запись резултата
    folder = location
    os.makedirs(folder, exist_ok=True)
    out_path = os.path.join(folder, name)
    with open(out_path, "wb") as f_out:
        f_out.write(enc)


    # пишем итоговый резютат
    print("Файл успешно обработан.")
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print("Что-то пошло не так:", e)