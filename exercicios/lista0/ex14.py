qtd_trechos = int(input('Digite a quantidade de trechos da viagem (1 a 50)'))

if not (1 <= qtd_trechos <= 50):
    print("Erro! O número de trechos deve estar entre 1 e 50.")
else:
    distancias = []
    velocidades = []

    for i in range(qtd_trechos):
        print(f"\n-- Dados do trecho {i + 1} --")
        distancias.append(float(input(f"Distância do trecho {i + 1} (em km): ")))
        velocidades.append(float(input(f"Velocidade do trecho {i + 1} (em km/h): ")))

numerador = sum(d * v for d, v in zip(distancias, velocidades))
denominador = sum(distancias)

media = numerador / denominador

print(f"Velocidade média: {media:.2f} km/h")

print("\nTrechos com velocidade acima da média: ")
acima = False

for i, (dist, vel) in enumerate(zip(distancias, velocidades), start=1):
    if vel > media:
        print(f"Trecho {i}: Velocidade de {vel:.2f} km/h (Distância: {dist} km)")
        acima = True

if not acima:
    print("Nenhum trecho ficou acima da média geral.")