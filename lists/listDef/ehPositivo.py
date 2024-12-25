def eh_positivo(num: int): 
    if num == 0:
        print('Neutro!')
    if num > 0: 
        return True
    if num < 0:
        return False
    
num = int(input('Digite o número: '))
resultado = eh_positivo(num)
print(resultado)
