import time;
import random;

def relatorio(historico):

    historicoMAximo = max(historico);
    historicoDano = len(historico);

    for i in range (len(historico)):
        print(f"Dano {i + 1}: {historico[i]} pontos ao HP do boss");
    
    print(f"Parabéns, você derrotou o Boss! Com um total de {historicoDano} ataques! Com seu maior dano sendo de {historicoMAximo} pontos!");

def AtacarEspada():
    print("Ataque com espada");
    corteEspada = random.randint(20, 100);
    return corteEspada; #Return está devolvendo o valor para quem chamar a funcao atacarEspada;

def AtacarMachado():
    print("Ataque com machado");
    destruirMachado = random.randint(50,150);
    return destruirMachado;

ataque_aleatorio = [AtacarEspada, AtacarMachado];
    

print(f"Bem vindo ao segundo RPG Dev");
print(f"Prepare-se para uma batalha épica contra um Boss mais poderoso!");
print(f"Para sair do jogo digite 'sair' quando for solicitado a inserir um dano crítico.");
print('_' * 50);

boss = 2000; #HP do Boss;
print(f"Você vai enfrentar um Boss com {boss} HP!");
print('_' * 50);
time.sleep(3);
historico = [];

while boss > 0:
    time.sleep(2);

    TrocadeArmas = random.choice(ataque_aleatorio);
    dano = TrocadeArmas();

    if dano > 80:
        print(f"Você causou {dano} de dano ao Boss, agora você pode inserir um dano crítico! O dano causado será dobrado.");

        print(f"-" * 50);
        critico = input("Deseja usar o dano crítico? (s/n): ").strip().lower();
        print(f"-" * 30);

        if critico == 'sair':
            print(f"Já vai sair? Tudo bem, até a próxima!");
            break;

        if critico == 's':
            dano *= 2;
            print(f"Você causou um dano crítico de {dano} pontos ao Boss!");

        elif critico == 'n':
            print(f"Você causou {dano} de dano ao Boss, mas não usou o dano crítico.");
        else:
            print(f"opcao invalida, voce causou {dano} de dano ao Boss, mas perdeu a chance de usar o dano crítico.");

    else:
        print(f"Você causou {dano} pontos de dano ao Boss.");

    boss -= dano;

    historico.append(dano);
    print('-' * 50);

    if boss <= 0:

        relatorio(historico);
    else:
        print(f"O Boss ainda tem {boss} pontos de vida restantes, continue a batalha.");