def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def test(a,b):
    return (a * 2) + (b * 3)


def exbir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é = {resultado}")

exbir_resultado(10,10, somar)
exbir_resultado(10,10, subtrair)
exbir_resultado(10,10, test)