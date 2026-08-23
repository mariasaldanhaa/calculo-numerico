somaNota = 0
quantidadeAlunos = 0

for cont in range(10):
    print(f"--- ALUNO {cont + 1} ---")

    while True:
        n1 = float(input("Informe a nota da primeira prova: "))
        n2 = float(input("Informe a nota da segunda prova: "))
        n3 = float(input("Informe a nota da terceira prova: "))
        notas = [n1, n2, n3]

        if any(x < 0 for x in notas):
            print("Nota inválida! Alguma nota é negativa. Digite todas novamente.")
        else:
            break

    notaFinal = (n1 + n2) * 0.3 + n3 * 0.4
    somaNota = somaNota + notaFinal
    quantidadeAlunos += 1

    print(f"Nota Final: {notaFinal:.2f}")

    if (notaFinal >= 0 and notaFinal <= 60):
        print(f"Reprovado! Lamento.")
    else:
        print(f"Parabéns! Aprovadíssimo.")

print(f"Média Final:  {(somaNota / quantidadeAlunos):.2f}")