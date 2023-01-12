# Все связующий и управляющий скрипт

import view
import operations

def button_click():
    value_lst, kind_oper = view.get_value()
    result = operations.calc(value_lst, kind_oper)
    view.output(result)
