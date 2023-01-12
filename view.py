# Интерфейс

def get_value():
    print("Запущен калькулятор.")
    kind_operation = input("Для комплексных чисел введите 1, для обычных введите 2: ")
    
    while True:
        inp = input("Введите операцию. Отделите числа от знака операции пробелом: ")
        try_act = inp
        data = try_act.split()

        if len(data) == 3:
            if data[1] == "+" or data[1] == "-" or data[1] == "*" or data[1] == "/":
                print("Спасибо")
                break

        print("Неверный ввод. Попробуйте снова")

    return inp, kind_operation


def output(result):
    try:
        if result.is_integer():
            print(f"Результат", int(result))
        elif isinstance(result, float):
            print(f"Результат:", result)
        else: print(result)
    except:
        print(f"Результат", result)
