# corrigido em sala
from tempo import ano_bissexto, dias_mes, nome_mes

ano = int(input('Digite um ano: '))
mes = int(input('Digite um mês (1 - 12): '))

if 1 <= mes <= 12:
    print(f"\nResultados para a data {mes}/{ano}:")
    print(f"* O ano {ano} é bissexto? {ano_bissexto(ano)}")
    print(f"* Nome do mês digitado: {nome_mes(mes)}")
    print(f"* Quantidade de dias neste mês: {dias_mes(ano, mes)} dias.")
else:
    print("\nErro: Mês inválido! Digite um valor entre 1 e 12.")