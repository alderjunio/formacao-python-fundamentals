contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-5151"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "0505-2221"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3224-2221"}
}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave,valor)