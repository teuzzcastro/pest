def calcular_perimetro(lado: float):
    calc = lado * 4
    return calc

lado = float(input('Digite o lado: '))
resultado = calcular_perimetro(lado)
print('Seu perimêtro é', resultado)
