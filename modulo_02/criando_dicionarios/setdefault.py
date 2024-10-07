contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

print(contato.setdefault("nome", "Giovanna"))
print(contato)

print(contato.setdefault("idade", 28))
print(contato)