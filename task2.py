# task2
'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''
import os.path

if os.path.isfile(r'text2.txt'):
    os.remove('text2.txt')

with open(r'text2.txt', 'a+', encoding = 'utf-8') as f_obj:
    f_obj.write('1234525252556789\n')
    f_obj.write('q355125545werty\n')
    f_obj.seek (0)
    for index, line in enumerate(f_obj, start = 1):
        print(f'Строка = {index}, Количество букв строке = {len(line)-1}')
