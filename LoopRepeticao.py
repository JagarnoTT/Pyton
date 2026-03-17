import time;
dados_sensores = [
    {"equipamento": "Caldeira_A", "temperatura": 85, "status": "operacional"},
    {"equipamento": "Caldeira_B", "status": "manutencao"}, 
    {"equipamento": "Caldeira_C", "temperatura": 105, "status": "operacional"},
    {"equipamento": "Caldeira_D", "temperatura": "ERRO_LEITURA", "status": "operacional"}
]

def analisar_caldeiras(dados_sensores):
        
    while True:
        try:
            
            for dados in dados_sensores:
                
                equipamento = dados['equipamento'];
                status = dados['status'];
                
                time.sleep(4)
            
                print("-" * 50);
                if status == 'manutencao':
                    print(f"{equipamento} este dispositivo está em manutenção, vamos para o próximo!")
                    continue
            
                elif status == 'operacional':
                    temperatura = dados.get["temperatura"]
                try:
                    temperatura = dados['temperatura']
                    print(f"{equipamento} está {status}");
                    if temperatura > 90:
                        print(f"{temperatura}°C' + ' A temperatura excedeu o limite, comece o procedimento de resfriamento");
                        continue
                    elif temperatura < 90:
                        print(f"{dados['temperatura']}°C estão normais os niveis, podemos seguir!")
                        continue
                    else:
                        print("Erro de leitura do sensor")
                        continue
                except Exception as e:
                    print(f"Um erro inesperado aconteceu! {e}")
        except Exception as e:
            print(f"Um erro inesperado aconteceu! {e}")
            
analisar_caldeiras(dados_sensores);