# terminar *

def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
def dias_mes(ano, mes):
    if mes == 2:
        if ano_bissexto(ano):
            return 29
        else:
            return 28
    elif mes in [4, 6, 9, 11]:
        return 30
