def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print(f"Você já atingiu o limite de {limite_saques} saques diários. Por favor, selecione uma das opções abaixo:")
        return saldo, extrato, numero_saques

    if valor > 0 and valor <= saldo and valor <= limite:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado com sucesso, seu saldo atual é de R${saldo:.2f}. Selecione uma das opções abaixo:")
    else:
        print(f"O valor de seu saque deve ser igual ou inferior ao seu saldo, que atualmente é de R${saldo}, além disso deverá respeitar o limite de R${limite}. Selecione uma das opções abaixo:")
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print(f"O valor será depositado e seu saldo após o saque será de R${saldo:.2f}. Selecione uma das opções abaixo:")
    else:
        print("O valor informado não pode ser depositado por, por favor informe um opção válida.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================")


def criar_usuario(usuarios):
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Já existe usuário com esse CPF!")
        return
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print("Conta criada com sucesso!")
        return conta
    else:
        print("Usuário não encontrado, por favor crie um usuário antes de criar uma conta.")
        return None


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []
numero_conta = 1

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input(" Qual valor será depositado?"))
        saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == "s":
        print("Sacar")
        saque = float(input("Qual valor deseja sacar? "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
            numero_conta += 1

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços! Até breve!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")