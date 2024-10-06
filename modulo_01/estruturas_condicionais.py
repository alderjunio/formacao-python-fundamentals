MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, já pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer aulas praticas")
else:
    print("Menor de idade, ainda não pode tirar a CNH")
