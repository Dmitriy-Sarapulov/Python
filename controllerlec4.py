import model_sumlec4 #можно сменить на суммирование
import viewlec4

def button_click():
    value_a = viewlec4.get_value()
    value_b = viewlec4.get_value()
    model_sumlec4.init(value_a, value_b)
    result = model_sumlec4.do_it()
    viewlec4.view(result, "sum")

    