def trocar_metades(string: str):
    metade = len(string) // 2
    return string[metade:] + string[:metade] 

saida = trocar_metades('Python')
print(saida)
