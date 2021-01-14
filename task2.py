# task2
'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''
import os.path

if os.path.isfile(r'text2.txt'):
    os.remove('text2.txt')

with open(r'text2.txt', 'a+', encoding = 'utf-8') as f_obj:
    f_obj.write('12334223\n')
    f_obj.write('vdbvabdvkb\n')

    f_obj.seek (0)
    for line in f_obj:
        print (line.strip())
