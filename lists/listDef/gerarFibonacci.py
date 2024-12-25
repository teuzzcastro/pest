def gerar_fibonacci(num: int):
    a = 0
    b = 1
    for _ in range(num):
        print(a, ' ') #print(a, end=' ') deixa os números em fileira
        a, b = b, a + b

num = int(input('Digite um número: '))
gerar_fibonacci(num)
