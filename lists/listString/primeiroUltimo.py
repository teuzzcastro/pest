def primeiro_e_ultimo(string: str):
    primeiro = string[0]
    tamanho_string = len(string)
    ultimo = string[tamanho_string - 1]

    aux = primeiro + ultimo
    return aux

nova_string = primeiro_e_ultimo('Python')
print(nova_string)
