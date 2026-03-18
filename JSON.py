import json;

try:
    Dicionario = {
    "Equipamento_1": {"Nome": "Bomba", "Status": "Ativo", "Temperadura": 85},
    "Equipamento_2": {"Nome": "Redentor", "Status": "Bloquado", "Temperadura": 40},
    "Equipamento_3":{"Nome": "Filtro", "Status": "Ativo", "Temperadura": 65}
    }
    

    with open("status_maquina.json", "w", encoding="utf-8") as arquivo:
        json.dump(Dicionario, arquivo, ensure_ascii = False, indent=4);

        print("Arquivo criado com sucesso!");

except FileNotFoundError:
    print("Ocorreu um erro ao tentar acessar o arquivo");
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}");

