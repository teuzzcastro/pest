def classificar_idade(idade: int):
    if idade <= 0:
        print('Idade Inválida!')
    if idade == 1:
        print('Bebê.')
    if idade >= 2 and idade < 12:
        print('Criança.')
    if idade >= 12 and idade <= 17:
        print('Adolescente.')
    elif idade >= 18:
        print('Adulto.')

idade = int(input('Digite sua idade: '))
classificar_idade(idade)
