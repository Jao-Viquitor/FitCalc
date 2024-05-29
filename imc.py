def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        
        imc = calcular_imc(peso, altura)

        interpretacao = interpretar_imc(imc)
        
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Interpretação: {interpretacao}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    main()
