import csv

"""
Описание аргументов кода с 8 по 17 стрроку:
S - Открытие файла game.txt.
SS - Преобразование файла game.txt в list, [1:] для того, чтобы не брать первую строк, delimiter разделяет по знаку доллара.
GameName, characters, nameError, date - аргументы столбцов.
el - Перебор элементов строки в каждом столбце.
A - Открытие файла game_new.csv.
AA - Запись файла через функцию writer через делитель: Доллар.
games - лист с играми.
persons - лист с: Персонаж+Игра
bugs - лист отчётов по багам.
"""

games = list()
persons = list()
bugs = list()
print('Задача 1:')
with open('C:/Users/qwerty/Downloads/game.txt', encoding='utf8') as S: # Открываем файл.
    SS = list(csv.reader(S, delimiter='$'))[1:] # Преобразуем в лист.
    for GameName, characters, nameError, date in SS: # Проходимся по каждой строке по элементам.
        if '55' in nameError: # Если есть 55 в ошибке, то печатаем.
            print(f'У персонажа {characters} в игре {GameName} нашлась ошибка с кодом: {nameError} Дата фиксации: {date}')

    # Запись в исправленной таблицы в файл.
    with open('game_new.csv', 'w', encoding='utf8') as A:
        AA = csv.writer(A, delimiter='$')
        AA.writerow(['GameName', 'characters', 'nameError', 'date'])
        AA.writerows(SS)


    for el in SS: # Перебор элементов в строке, -2 элемент - это nameError, -1 - это date, -4 - GameName, -3 - characters
        if '55' in el[-2]:
            # Исправление значений ошибки и даты после выведения отчёта.
            el[-2] = 'Done'
            el[-1] = '0000-00-00'
        games.append(el[-4]) # Добавляем игру в лист для второй задачи.
        persons.append(el[-3])
        persons.append(el[-4]) # Добавляем персонажа+игру в лист для третьей задачи.

    print('\nЗадача 2:')
    for i in range(len(games)): # Перебор элементов листа games.
        bugs.append(f'Игра {games[i]}, количество багов: {games.count(games[i])}') # Ищем количество багов в игре и добавляем текст отчёта.
    for j in sorted(set(bugs)): # Сортируем и удаляем повторы, далее выводим сам отчёт.
        print(j)


    print('\nЗадача 3:')
    for i in range(len(persons) - 1):
        print(f'Персонаж {persons[i]} встречается в игре {persons[i+1]}')






