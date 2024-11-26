#======calculadora IMC======

def calculaIMC(kg, altura):
    IMC = kg/(altura * altura)
    return IMC

peso = input("qual seu peso: ")
altura = input("qual a sua altura: ")
print("\n")
if peso  and altura:
    peso = float(peso)
    altura = float(altura)

    result = float(calculaIMC(peso, altura))
    print(f"seu IMC e de: {result:.2f}")

    if result<25.5:
        print("voce esta abaixo do peso normal\n")
    elif result<=70.9:
        print("voce esta cpm o peso normal\n")
    elif result<=110.9:
        print("cuidado excesso de peso\n")
    elif result<=120.9:
        print("cuidado obesidade classe 1\n")
    elif result<=130.9:
        print("cuidado obesidade classe 2\n")
    else:
        print("cuidado obesidade classe 3\n")
    
else:
    print("por favor, preencha todos os campos!")