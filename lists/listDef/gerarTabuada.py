def gerar_tabuada(num: int):
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

num = int(input('Digite um número: '))
gerar_tabuada(num)
