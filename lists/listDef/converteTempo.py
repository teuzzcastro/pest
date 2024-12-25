def converte_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60

    return horas, minutos, segundos

segundos = int(input("Digite a quantidade de segundos: "))
horas, minutos, segundus = converte_tempo(segundos)
print(f"{segundos} segundos = {horas} horas, {minutos} minutos e {segundus} segundos.")
