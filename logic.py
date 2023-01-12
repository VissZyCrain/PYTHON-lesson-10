import calcylator, convertor

def button_click(text):
    primer = convertor.convert_expression(text)
    result = calcylator.Calc(primer)
    return result