def inverter_esquerda(string: str):
    metade = len(string) // 2
    return string[:metade][::-1] + string[metade:]

saida = inverter_esquerda('Python')
print(saida)
