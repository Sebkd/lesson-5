# task7
'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''
import json

with open(r'text7.txt', encoding = 'utf-8') as f_obj:
    f_obj.seek(0)
    average_profit, count = 0, 0
    average_dict, my_dict = {}, {}
    for line in f_obj:
        difference = float(line.split()[2]) - float(line.split()[3])
        if (difference):
            count += 1
            average_profit += difference
        my_dict[line.split()[0]] = difference
    average_dict['average_profit'] = round(average_profit / count, 2)
    print(f'{[my_dict, average_dict]}')
with open(r'text7.json', 'a+', encoding = 'utf-8') as f_obj:
    json.dump([my_dict, average_dict], f_obj)
