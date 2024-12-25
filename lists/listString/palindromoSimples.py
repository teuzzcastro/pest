def palindromo_simples(string):
    resuldado = string == string[::-1]
    return resuldado

saida = palindromo_simples('arara')
print(saida)
