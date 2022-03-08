#Калькулятор работает с вещественными числами. При введении целого числа он преобразует его в число с плавающей точкой.
#При ввеедение формата, не приводимого к числу с плавающей точкой, выдается ошибка и предложение повторного введения числа.
#Калькулятор поддерживает следующие действия: + сложение, - вычитание, * умножение, / деление, ** возведение в степень, **/ извлечение корня.
# Округление до 4 знаков после завпятой.
while True:
    try:
        num1 = float(input('Введите первое число: '))
        break
    except: print("Это не число. Введите первое число: ")
while True:
    oper = input('Ввведите действие (оператор): ')
    if oper in ('+', '-', '*','/', '**', '**/'):
        oper = oper
        break
    else: print ("""Вы ввели действие (оператор), не поддерживаемый калькулятором!
    Поддерживаемые действия:
    + сложение
    - вычитание
    * умножение
    / деление 
    ** возведение в степень (следующее значение - это степень, в которую требуется возвести)
    **/ извлечение корня (следующее значение - это корень какой степени требуется найти)). """)
while True:
    try:
        num2 = float(input('Введите второе число: '))
        break
    except: print("Это не число. Введите второе число: ")
if oper == '+': result = num1+num2
elif oper == '-': result = num1-num2
elif oper == '*': result = num1*num2
elif oper == '/': result = num1/num2
elif oper == '**': result = num1**num2
elif oper == '**/': result = num1**(1/num2)
else: print ('Ошибка! Что-то пошло не так. Запустите калькулятор заново!')
#print('Итого: {}. '.format(result))
result = round(result,4)
print(f"Итого (c округлением до 4 знаков после запятой): {result}. ")
# перевод в пропись
dict_zifra = {0: 'ноль', 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять',
    6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять'}
dict_20 = {11 : 'одиннадцать', 12 : 'двенадцать', 13 : 'тринадцать',
    14 : 'четырнадцать', 15 : 'пятнадцать', 16 : 'шестнадцать',
    17 : 'семнадцать', 18 : 'восемнадцать', 19 : 'девятнадцать'}
dict_dozens = {10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок',
    50 : 'пятьдесят', 60 : 'шестьдесят', 70 : 'семьдесят',
    80 : 'восемьдесят', 90 : 'девяносто'}
dict_hundrets = {0: '', 100: 'сто', 200: 'двести', 300: 'триста', 400:'четыреста', 500:'пятьсот', 600:'шестьсот', 700:'семьсот', 800:'восемьсот', 900:'девятьсот'}
fl_result = int(round((round(result,2)*100)%100,0))
if fl_result < 10: fl_result_propis = f'/0{fl_result}. '
else: fl_result_propis = f'/{fl_result}. '
result = int(result)
if 0 < result <= 1000:
    result_propis3 = (result // 100) * 100
    result_propis0 = result - result_propis3
    result_propis1 = result_propis0 % 10
    result_propis2 = result_propis0 - result_propis1
    result_propis3 = dict_hundrets.get(result_propis3)
    if result_propis0 == 0:
        result_propis2 = ""
        result_propis1 = ""
    elif 0 < result_propis0 < 10:
        result_propis2 = ""
        result_propis1 = dict_zifra.get(result_propis1)
    elif 10 <= result_propis0 < 20:
        result_propis2 = dict_20.get(result_propis0)
        result_propis1 = ""
    elif result_propis0 >= 20 and result_propis1 == 0:
        result_propis2 = dict_dozens.get(result_propis2)
        result_propis1 = ""
    elif result_propis0 >= 20 and result_propis1 != 0:
        result_propis2 = dict_dozens.get(result_propis2)
        result_propis1 = dict_zifra.get(result_propis1)
    else : result = result
    print(f'Прописью (дробная часть c округление до 2 знаков после /) :{result_propis3} {result_propis2} {result_propis1} {fl_result_propis}')
elif result ==0: print(f'Прописью (дробная часть c округление до 2 знаков после /) :ноль {fl_result_propis}')
else: print ('Калькулятор пока не поддерживает перевод такого чила в пропись!')



