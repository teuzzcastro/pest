def maior_numero(num1: int, num2: int):
    if num1 == num2:
        return num1 or num2
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2
    
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
resultado = maior_numero(num1, num2)
print(resultado)
