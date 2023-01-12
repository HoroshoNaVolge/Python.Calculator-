# Все связующий и управляющий скрипт

import view
import operations
import log

def button_click():
    value_lst, kind_oper = view.get_value()
    log.logwrite("Ввод: ", value_lst) 
    result = operations.calc(value_lst, kind_oper)
    log.logwrite("Результат: ", result)
    view.output(result)
