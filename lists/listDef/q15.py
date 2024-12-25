def imc(peso: float, altura: float):
    return peso / (altura * 2)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
resultado = imc(peso, altura)
print(resultado)