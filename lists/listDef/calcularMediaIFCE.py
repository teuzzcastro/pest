print('Etapa 1 (N1)')

def calcular_media_ifce_n1(soma_notas: float, quantidade_notas: int):
    return soma_notas / quantidade_notas if quantidade_notas > 0 else 0

quantidade_notas_n1 = int(input("Quantas notas você deseja inserir para a N1? "))

soma_notas_n1 = 0

for i in range(quantidade_notas_n1):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota para a N1 (de 0 a 10): '))
        if 0 <= nota <= 10:
            soma_notas_n1 += nota
            break
        else:
            print('Nota inválida! A nota deve estar entre 0 e 10.')

if quantidade_notas_n1 > 0:
    resultado1 = calcular_media_ifce_n1(soma_notas_n1, quantidade_notas_n1)
    print(f'- Sua média da N1 é {resultado1}')
else:
    print('Você não inseriu nenhuma nota para a N1.')

print(' ' * 100)
print('Etapa 2 (N2)')

def calcular_media_ifce_n2(soma_notas: float, quantidade_notas: int):
    return soma_notas / quantidade_notas if quantidade_notas > 0 else 0

quantidade_notas_n2 = int(input("Quantas notas você deseja inserir para a N2? "))

soma_notas_n2 = 0

for i in range(quantidade_notas_n2):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota para a N2 (de 0 a 10): '))
        if 0 <= nota <= 10:
            soma_notas_n2 += nota
            break
        else:
            print('Nota inválida! A nota deve estar entre 0 e 10.')

if quantidade_notas_n2 > 0:
    resultado2 = calcular_media_ifce_n2(soma_notas_n2, quantidade_notas_n2)
    print(f'- Sua média da N2 é {resultado2}')
else:
    print('Você não inseriu nenhuma nota para a N2.')

print(' ' * 100)
print('Média Final')

def calcular_media_ifce_mf(resultado1: float, resultado2: float):
    return (resultado1 + resultado2) / 2

if quantidade_notas_n1 > 0 and quantidade_notas_n2 > 0:
    resultado3 = calcular_media_ifce_mf(resultado1, resultado2)
    print(f'- Sua média final é {resultado3}')
else:
    print('Não é possível calcular a média final. Verifique se as médias de N1 e N2 foram corretamente calculadas.')
