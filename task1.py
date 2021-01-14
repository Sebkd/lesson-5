# task1
'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
import os.path
#C:\Users\sebkd\PycharmProjects\lesson-5\
if os.path.isfile(r'text.txt'):
    os.remove('text.txt')
with open('text.txt', 'a+') as f_obj:
    while True:
        if not f_obj.write(input()):
            break
        else:
            continue
    f_obj.seek(0)
    for line in f_obj:
        print(line)
