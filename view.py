def choice_calc():
    global my_calc
    my_calc = int(input('тип калькулятора (1 кнопочный, 2 строчный): '))
    return my_calc

def input_number():
    number = input('Введите число:  ')
    if number.isdigit():
        number = int(number)
        return number
    else:
        number = str(number)
        return number


def input_operation():
    operation = input('Введите операцию(+, -, *, /, = :  ')
    return operation

def print_result(smth):
    print(smth)