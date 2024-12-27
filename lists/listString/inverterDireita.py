def inverter_direita(string: str):
    metade = len(string) // 2
    return string[:metade] + string[metade:][::-1]

saida = inverter_direita('Python')
print(saida)
