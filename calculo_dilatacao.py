def calcular_dilatacao(temperatura_comeco, temperatura_final, coeficiente_dilatacao, comprimento_inicial):
    """
Calcula a dilatação linear de um material com base na fórmula da dilatação térmica linear.
    A formula é:	∆L = L° * a * ∆T
    onde:
        ∆L = variação do comprimento (dilatação)
        L° = comprimento inicial
        a = coeficiente de dilatação linear
        ∆T = variação de temperatura (temperatura_final - temperatura_inicial)
    """

    # Calcula a variação de temperatura
    variacao_temperatura = temperatura_final - temperatura_comeco

    # Calcula a dilatação linear
    # Dilatação volumetrica = 3 * coeficiente
    # Dilatação superficial = 2 * coeficiente
    dilatacao_final = comprimento_inicial * coeficiente_dilatacao * variacao_temperatura

    return dilatacao_final


temperatura_comeco = float(input("Qual a temperatura inicial?: "))
temperatura_final = float(input("Qual a temperatura final?: "))
comprimento_inicial = float(input("Qual o comprimento inicial?: ").replace(",","."))
coeficiente_dilatacao = float(input("Qual é o coeficiente de dilatação?: "))

calculo = calcular_dilatacao(temperatura_comeco, temperatura_final, comprimento_inicial, coeficiente_dilatacao)

print(f'O comprimento final é {comprimento_inicial+calculo}')