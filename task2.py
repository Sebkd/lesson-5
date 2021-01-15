# task2
'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''
import os.path

with open(r'text2.txt', 'a+', encoding = 'utf-8') as f_obj:
    f_obj.seek(0)
    print(f'Число строк в файле = {len(f_obj.readlines())}')
    f_obj.seek(0)
    for index, line in enumerate (f_obj, start = 1):
        print(f'Строка = {index}, Количество слов в строке = {len(line.split())}')
