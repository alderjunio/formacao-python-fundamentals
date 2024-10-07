contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1111"}
}

#print(contatos["chave"])

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("guilherme@gmail.com", {}))