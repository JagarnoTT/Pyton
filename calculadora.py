print("Conversão de reais para dólares");

SalarioReal = float(input("Digite o valor do seu salário em reais: "));

def convert(SalarioReal):
    SalarioDolar = SalarioReal / 5.22;
    return SalarioDolar;

SalarioDolar = convert(SalarioReal);

def SalarioAnual(SalarioDolar):
    SalarioDolarAnual = SalarioDolar * 12;
    return SalarioDolarAnual;

print('-' * 50);
print(f"Seu Salário convertido de real para doláres é de ${convert(SalarioReal):.2f}");
print(f"Seu salário anual é de ${SalarioAnual(SalarioDolar):.2f}");