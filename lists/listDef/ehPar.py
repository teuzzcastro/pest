def eh_par(num: int):
    if num % 2 == 0:
        return True
    else: 
        return False
    
num = int(input('Digite um número: '))
resultado = eh_par(num)
print(resultado)
