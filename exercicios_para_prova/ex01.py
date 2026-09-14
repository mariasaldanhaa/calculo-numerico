nota = float(input("Informe a nota do aluno de 0 a 100: "))

if nota < 0 or nota > 100:
    print("Ops! Digite novamente.")
elif nota >= 60:
    print("Aprovado!")
elif nota >= 40:
    print("Reavaliação!")
else:
    print("Reprovado!")