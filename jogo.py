import random;
import time;
print(f"Bem vindo ao RPG Dev");

Boss = 500;
print(f"Um Boss apareceu com {Boss} pontos de vida!");

while Boss > 0:

    time.sleep(2);

    dano = random.randint(10,70);
    
    print(f"O Boss tem {Boss} pontos de vida restantes.");
    Boss -= dano;
    print(f"Você causou {dano} pontos de dano ao Boss.");

    if Boss <= 0:
        print("Parabéns, você derrotou o Boss!");
    else:
        print(f"O Boss ainda tem {Boss} pontos de vida restantes, continue a batalha.");