def divisao_segura(num1: int, num2: int):
    if num2 == 0:
        return 'Inválida!'
    
    return num1 // num2
            
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
resultado = divisao_segura(num1, num2)
print(resultado)

