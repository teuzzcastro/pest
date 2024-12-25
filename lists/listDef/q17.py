def classificar_nota(nota: int):
    if nota < 0 or nota > 10:
        print('Nota Inválida.')

    elif nota <= 6:
       print('Reprovado.')
    elif nota > 6:
        print('Aprovado.')

nota = int(input('Digite sua nota: '))
classificar_nota(nota)