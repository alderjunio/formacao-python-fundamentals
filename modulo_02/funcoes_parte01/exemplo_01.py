def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem2(nome="Alder")
exibir_mensagem2("Alder Junio")
exibir_mensagem3()
exibir_mensagem3(nome="Helen")
