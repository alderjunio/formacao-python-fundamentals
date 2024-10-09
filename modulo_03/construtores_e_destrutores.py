# metodo construtor __init__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def falar(self):
        print("au au")

    def __del__(self):
        print("Removendo a instancia da classe")

c = Cachorro("Nico", "Caramelo")
c.falar()


# metodo destrutor __del__

# class Cachorro:
#     def __del__(self):
#         print("Destruindo a instancia")

# c = Cachorro()
# del c


