# task6
'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import os.path

def the_sum_item(array):
    the_sum = 0
    for number in array.split ()[1:]:
        x_number = '0'
        for count in range (len (number)):
            if not number[count].isdigit () or number[count] == "-":
                continue
            else:
                x_number = ''.join (x_number + number[count])
        the_sum += int (x_number)
    return the_sum


with open(r'text6.txt', encoding = 'utf-8') as f_obj:
    f_obj.seek (0)
    my_list = {}
    for line in f_obj:
        my_list[line.split()[0]] = the_sum_item(line)
    print(my_list)



