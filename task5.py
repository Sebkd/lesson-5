# task5
'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
import os.path
import random

if os.path.isfile(r'text5.txt'):
    os.remove('text5.txt')

original_list = [element for element in range(random.randint(1, 10))]
random.shuffle(original_list)
print(f'Случайный набор чисел списка: {original_list}')

with open(r'text5.txt', 'a+', encoding = 'utf-8') as f_obj:
    for line in original_list:
        f_obj.write(''.join(str(line) + ' '))
    f_obj.seek(0)
    print(f'Сумма чисел в файле = {sum(map(int, f_obj.readline().split()))}')