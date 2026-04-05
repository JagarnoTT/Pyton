import time;
def Automação():
    try:
        with open('LogAutomacao.txt','r', encoding='utf-8') as arquivo:
            LerArquivo = arquivo.read();
            print(LerArquivo);

    except FileNotFoundError:
        print('Ocorreu um erro ao tentar acessar o arquivo');
        time.sleep(2);
        print("Criando arquivo de log...");
        with open('LogAutomacao.txt','w', encoding='utf-8') as arquivo:
            arquivo.write(f"Bem vindo!");
Automação();



