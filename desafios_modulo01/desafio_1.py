# Solicita ao usuário um número inteiro
numero = int(input())

resultado = numero % 2

if resultado == 0:
    print("Par")
elif resultado != 0:
    print("Ímpar")

    