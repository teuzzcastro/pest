def palindromo_simples(string: str):
    resultado = string == string[::-1]
    return resultado

saida = palindromo_simples('arara')
print(saida)
