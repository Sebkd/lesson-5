#task4
'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
import os.path

if os.path.isfile(r'text4-2.txt'):
    os.remove('text4-2.txt')

my_translator = {'One': 'Один',
                 'Two' : 'Два',
                 'Three': 'Три',
                 'Four': 'Четыре'}
with open(r'text4-2.txt', 'a+', encoding = 'utf-8') as f_obj_write:
    with open(r'text4-1.txt', encoding = 'utf-8') as f_obj:
        f_obj.seek(0)
        for line in f_obj:
            f_obj_write.write(''.join([my_translator[line.split()[0]], line.strip()[-4:], '\n']))