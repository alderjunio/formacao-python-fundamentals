def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia")

def depositar(valor):
    saldo = 500
    saldo += valor

    print(saldo)

sacar(100)