def conversor_em_horas12(horas, minutos):
    periodo = "A.M." if horas < 12 else "P.M."

    horas12 = horas % 12
    horas12 = 12 if horas12 == 0 else horas12

    return f"{horas12}:{minutos:02d} {periodo}"


while True:
    print("Para encerrar o programa digite um valor negativo (-HH:MM) \n")

    Hrs = input("Olá, digite as horas no modelo 'HH:MM': \n")
    horas24, minutos24 = map(int,Hrs.split(":"))

    if horas24 < 0:
        print("Encerrando...")
        break

    conversao = conversor_em_horas12(horas24, minutos24)
    print(f"Horário convertido: {conversao}")



