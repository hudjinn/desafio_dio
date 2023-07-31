import locale

locale.setlocale(locale.LC_ALL, '')

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3


def validar_valor_positivo(valor):
    return valor > 0


def depositar():
    global SALDO, EXTRATO
    valor = float(input("Informe o valor do depósito: "))
    if validar_valor_positivo(valor):
        SALDO += valor
        EXTRATO += f"Depósito: {locale.currency(valor)}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar():
    global SALDO, EXTRATO, NUMERO_SAQUES
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > SALDO
    excedeu_limite = valor > LIMITE
    excedeu_saques = NUMERO_SAQUES >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif validar_valor_positivo(valor):
        SALDO -= valor
        EXTRATO += f"Saque: {locale.currency(valor)}\n"
        NUMERO_SAQUES += 1
    else:
        print("Operação falhou! O valor informado é inválido.")


def extrato():
    global EXTRATO, SALDO
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not EXTRATO else EXTRATO)
    print(f"\nSaldo: {locale.currency(SALDO)}")
    print("==========================================")


while True:
    opcao = input(MENU)

    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
