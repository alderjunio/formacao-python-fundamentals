class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando bicicleta....")
        print("bicicleta parada")

    def correr(self):
        print("Vrum....") 

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
b1 = Bicicleta("vermelha", "barra forte", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta("verde", "montain bike", 2012, 1500)
print(b2)
b2.correr()

    

