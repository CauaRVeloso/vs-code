def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def calcular_tmb(peso, altura, idade, sexo):
    if sexo.lower() == 'masculino':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * idade)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * idade)
    return tmb


def calcular_calorias_diarias(tmb, nivel_atividade):
    niveis = {
        'sedentario': 1.2,
        'levemente ativo': 1.375,
        'moderadamente ativo': 1.55,
        'muito ativo': 1.725,
        'extremamente ativo': 1.9
    }
    return tmb * niveis.get(nivel_atividade.lower(), 1.2)


def main():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): ").replace(",","."))
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu gênero (masculino/feminino): ")
    nivel_atividade = input(
        "Digite seu nível de atividade (sedentario, levemente ativo, moderadamente ativo, muito ativo, extremamente ativo): ")

    imc = calcular_imc(peso, altura)
    tmb = calcular_tmb(peso, altura, idade, sexo)
    calorias_diarias = calcular_calorias_diarias(tmb, nivel_atividade)

    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Sua TMB é: {tmb:.2f} calorias/dia")
    print(f"Para manter seu peso, você precisa de aproximadamente {calorias_diarias:.2f} calorias/dia")


if __name__ == "__main__":
    main()
