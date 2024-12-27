def trocar_primeira_letra(string: str,):
    resultado = string[:-1] + '#'  
    return resultado

saida = trocar_primeira_letra('Porra')
print(saida)
