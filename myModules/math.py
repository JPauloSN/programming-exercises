#função para calcular fatorial
def factorial(number:int):

    #evita erro de infinitas chamadas, caso a função receba um valor flutuante
    number = int(number)
    
    if number == 0: #interrompe o loop ao alcançar nossa última chamada
        return 1 
    
    # entra em um loop de chamadas recursivas 
    return number * factorial(number-1)