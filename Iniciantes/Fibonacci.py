limite = int(input("Digite o número limite para a sequência de Fibonacci: "))

morango, abacaxi = 0, 1

while abacaxi <= limite:
    print(abacaxi)
    morango, abacaxi = abacaxi, morango + abacaxi