import re

# шаблон регулярного выражения для допустимой записи действительного числа
pattern = r'^([+-]?\d+(\.\d+)?([eE][+-]?\d+)?)$'

# примеры ввода
input_str = [
    '1.2', 
    '1.',
    '1.0e-55', 
    'e-12',
    '6.5E',
    '1e-12', 
    '+4.1234567890E-99999',
    '7.6e+12.5',
    '99'
]

# проверяем каждую строку
for s in input_str:
    # удаляем пробелы из строки
    s = s.replace(' ', '')
    
    # проверяем, соответствует ли строка шаблону регулярного выражения
    if re.match(pattern, s):
        print(f'{s} is legal.')
    else:
        print(f'{s}. is illegal.')