# task3
'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

import os.path
print(f'Фамилии сотрудников, зарплата которых больше 20 000 руб:')
with open(r'salary.txt', 'a+', encoding = 'utf-8') as f_obj:
    f_obj.seek(0)
    average_salary, count = 0, 0
    for line in f_obj:
        if float(line.split ()[1]) > 20000:
            count +=1
            average_salary +=float(line.split()[1])
            print(line.split()[0])
print(f'Средняя зарплата этих сотрудников: {round((average_salary / count), 2)}')
