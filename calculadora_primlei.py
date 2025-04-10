def calcular_variação(calor_recebido, trabalho_realizado, energia_inicial):
    calor_total = calor_recebido - trabalho_realizado
    energia_final = calor_total + energia_inicial

    return energia_final



calor_recebido = float(input("Qual é o calor recebido?: "))
trabalho_realizado = float(input("Qual é o trabalho realizado?: "))
energia_inicial = float(input("Qual é a energia inicial?: "))

calcular_energia=calcular_variação(calor_recebido, trabalho_realizado, energia_inicial)

print(f'A energia interna final é {calcular_energia}')1


