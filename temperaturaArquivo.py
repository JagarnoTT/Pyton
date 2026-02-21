with open("temperatura.txt", "r", encoding="utf-8") as arquivo:
    dado_lido = arquivo.read();

    temperatura = float(dado_lido);

    print(f"A temperatura é de {temperatura}°C");

    if temperatura > 90:
        print("Temperatura alta, a maquina está superaquecendo!");

    else:
        print("Temperatura normal, não é necessário ligar o ar-condicionado!");