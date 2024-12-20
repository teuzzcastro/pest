def trocar_metade(string):
    metade = len(string) // 2
    return string[metade:] + string[:metade]

saida = trocar_metade('Pythonista')
print(saida)