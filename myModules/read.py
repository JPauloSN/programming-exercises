#função para receber o input do usuário, considerando o caso de ValueError

def read(mType:str = "str", msg:str = "Insira o valor: "):

    while True:
        try:
            match mType:

                case 'int':
                    return int(input(msg))
                
                case 'float':
                    return float(input(msg))
                
                case 'str':
                    return input(msg)
                case _:
                    print("undefined type")
                    return
        
        except ValueError:
            print(f"{'='*15}ERROR{'='*15}")
            print("Valor inválido! Por favor, insira um valor válido.")
