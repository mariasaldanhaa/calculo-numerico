def juros(capital, taxa, tempo =  12):
    return(capital * taxa * tempo) / 100

print('Cálculo de juros')
cap = float(input('Capital: '))
tax = float(input('Taxa: '))
escolha = input('Tempo diferente de 12 meses? (S/N)')
if escolha.lower() == 's':
    temp = int(input('Tempo: '))
    jur = juros(taxa = tax, capital =cap, tempo= temp)
else:
    jur = juros(cap, tax)
print('O valor dos juros é ', jur)