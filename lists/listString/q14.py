def inverter_direita(string):
    metade = len(string) // 2
    return string[:metade] + string[metade:][::-1]

saida = inverter_direita('Pythonista')
print(saida)