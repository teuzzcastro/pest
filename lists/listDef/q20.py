print('Etapa 1 (N1)')
def calcular_media_ifce_n1(nota1: float, nota2: float):
    return (nota1 + nota2) // 2

nota1 = float(input('Digite sua primeira nota da N1: '))
nota2 = float(input('Digite sua segunda nota da N1: '))
resultado1 = calcular_media_ifce_n1(nota1, nota2)
print(f'- Sua média da N1 é {resultado1}')

print(' ' * 100)
print('Etapa 2 (N2)')
def calcular_media_ifce_n2(nota1: float, nota2: float, nota3: float):
    return (nota1 + nota2 + nota3) // 3
    
nota1 = float(input('Digite sua primeira nota da N2: '))
nota2 = float(input('Digite sua segunda nota da N2: '))
nota3 = float(input('Digite sua terceira nota da N2: '))
resultado2 = calcular_media_ifce_n2(nota1, nota2, nota3)
print(f'- Sua média da N2 é {resultado2}')

print(' ' * 100)
print('Média Final')
def calcular_media_ifce_mf(resultado1: float, resultado: float):
    return (resultado1 + resultado2) / 2

resultado3 = calcular_media_ifce_mf(resultado1, resultado2)
print(f'- Sua média final é {resultado3}')