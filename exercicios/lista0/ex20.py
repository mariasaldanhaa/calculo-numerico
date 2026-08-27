# corrigido em sala

def mdc(num1, num2):
    while True:
        resto = num1 % num2
        
        if resto == 0:
            return num2
        num1 = num2
        num2 =  resto

def mmc(num1, num2):
    return (num1 * num2) // mdc(num1, num2)

def mdc_lista(lista):
    resultado = list[0]

    for num in lista[1:]:
        resultado = mdc(resultado, num)
    return resultado

def mmc_lista(lista):
    resultado = lista[0]

    for num in lista[1:]:
        resultado = mmc(resultado, num)
    return resultado

print('-- TESTE DAS FUNÇÕES --')
lista = input("Digite uma lista de números separando por espaços: ")
lista = [int(num) for num in lista.split()]

print('Lista: ', lista)
print('MDC: ', mdc_lista)
print('MMC: ', mmc_lista)
