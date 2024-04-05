#funções pré-instaladas do Python
from os import system

#funções próprias
from myModules.read import read
from myModules.math import factorial

#main
while True:
    #limpa tela do terminal
    system("cls")
    
    print("\n\tBem-vindo! Esse programa calcula o fatorial de um número!")
    number = read("int", "Digite o número que deseja fatorar (Digite 0 para parar a execução): ")
    
    #encerra o programa, caso satisfaça a condição
    if number==0:
        print("\nAgradecemos a preferência! Volte sempre :)")
        break

    #imprime os resultados no terminal
    print(f"\n{'-'*10} RESULTADO {'-'*10}")
    print(f"\nO fatorial de {number}! é {factorial(number)}\n")

    #interrompe a execução antes de reiniciar
    system("pause")