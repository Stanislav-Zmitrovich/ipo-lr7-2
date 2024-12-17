import json  # Подключаем json

lines = '-' * 22  # Добавляем элемент дизайна
with open("dump.json", 'r', encoding='utf-8') as file:  # Открываем файл, выдав имя файл
    dump = json.load(file)  # Загружаем в перменную дамп содержимое json
while True:  # Пока истинно(программа выполняется, пока не будет завершена извне)
    status = False
    find = input("Введите номер квалификации: ")  # Просим ввести номер квалификации
    for item in dump:  # Для  каждого предмета
        if item['model'] == 'data.skill':  # Если имеет значение квалификации в поле модель
            if item["fields"]['code'] == find:  # Если код равен
                for specialty in dump: # Для каждой специальности в файле
                    if specialty['model'] == 'data.specialty': # Если модель специальности равна data.specialty
                        if specialty['pk'] == item['fields']['specialty']: # Если pk равен нужному
                            print(f'{lines} Найдено {lines}') # Выводим
                            print( # Найденную специальность
                                f'{specialty["fields"]["code"]} >> Специальность' # С
                                f' {specialty["fields"]["title"]}, {specialty["fields"]["c_type"]}') # Красивым
                            print(f"{item['fields']['code']} >> Квалификация {item['fields']['title']}") # Оформлением
                            print(lines + lines) # А также
                            status = True # Устанавливаем статус
    if not status: # Который воспрепятствует
        print(f'{lines} Не найдено {lines}') # Выводу сообщения
        print("Не получилось ничего найти по вашей квалификации") # Об отсутствии соответствия
        print(lines + lines) # В файле