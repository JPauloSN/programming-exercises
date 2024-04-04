from os import system

#função para calcular fatorial
def factorial(number):
    if number == 0:
        return 1; 
    return number * factorial(number-1)

#função para receber o input do usuário, considerando o caso de ValueError
def readInteger(msg):
    while True:
        try:
            number = int(input(msg))
            return  number # O loop para se o valor for válido
        except ValueError:
            system("cls")
            print(f"{'='*5}ERROR{'='*5}")
            print("Valor inválido! Por favor, insira um número.")

while True:
    system("cls")
    
    print("\n\tBem-vindo! Esse programa calcula o fatorial de um número!")
    number = readInteger("\nInforme o número que deseja calcular (para encerrar a execução digite 0):")
    
    if number==0:
        print("\nAgradecemos a preferência! Volte sempre :)")
        break

    print(f"\n{'-'*10} RESULTADO {'-'*10}")
    print(f"\nO fatorial de {number}! é {factorial(number)}\n")

    system("pause")


