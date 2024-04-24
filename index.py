## Define o menu do sistema
menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

## Define as váriavéis utilizadas no sistema
saldo = 0
Limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3
quantidade_saque = 0

## Loop do programa o qual as operações serão realizadas
while True:
    opcao = input(menu)

    ## Define a operação de depósitos de acordo com as regras do sistemas
    if opcao == "d":
        print("Qual valor deseja depositar:")
        valor = float(input())
        if valor < 0:
            print("Não foi possível realizar operação, valor de depósito inválido")
        else:
            saldo += valor
            print("Depósito realizado com sucesso")
            extrato += f"Déposito de: R$ {valor:.2f} \n"

    
    ## Define a operação de saque de acordo com as regras do sistemas
    elif opcao == "s":
        print("Qual valor deseja sacar:")
        valor = float(input())
        if valor >Limite:
            print("Não foi possível realizar operação, saque excede limite")
        elif quantidade_saque >= LIMITES_SAQUES:
            print("Você excedeu seu limite de saque diário")
        elif valor < 0:
            print("Não foi possível realizar operação, valor de saque inválido")
        elif saldo < valor:
            print("Não foi possível sacar, saldo em conta insuficiente")
        else:
            saldo -= valor
            print("Saque realizado com sucesso")
            extrato += f"Saque de: R$ {valor:.2f} \n"
            quantidade_saque +=1


    ## Define a operação de extrato da conta de acordo com as regras do sistemas
    elif opcao == "e":
        if extrato == "":
            print("########## Extrato ##########")
            print("Não foi realizada movimentações")
            print("#############################")
        else:
            print("########## Extrato ##########")
            print(f"{extrato} \n Saldo total = R$ {saldo:.2f}")
            print("#############################")
    

    ## Define a opção para sair do sistemas
    elif opcao == "q":
        break
    
    ## Exibe uma mnesagem caso nenhuma operação válida seja selecionada
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")