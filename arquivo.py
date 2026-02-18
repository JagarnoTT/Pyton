with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Escrevendo dentro de um arquivo de texto\n");
    arquivo.write("Acentuação correta: á, é, í, ó, ú, ç\n");
    arquivo.write("-" * 50 + "\n");

print("Arquivo salvo com sucesso!");