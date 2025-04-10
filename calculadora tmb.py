def calcular_tmb(peso, altura, idade, sexo):
    if sexo.lower() == 'masculino':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * idade)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * idade)
    return tmb


def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite seu sexo (Masculino/Feminino): ")

        tmb = calcular_tmb(peso, altura, idade, sexo)

        print(f"Sua Taxa Metabólica Basal (TMB) é {tmb:.2f} calorias/dia.")
    except ValueError:
        print("Por favor, insira valores válidos para peso, altura e idade.")


if __name__ == "__main__":
    main()