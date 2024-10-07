#metodo union()
conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))
print("==================")

#metodo intersection()
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b))
print("==================")

#metodo difference()
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#metodo symmetric_difference()
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.symmetric_difference(conjunto_b))
print("==================")


#metodo issubset()
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
print("==================")


#metodo issuperset()
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
print("==================")


#metodo isdisjoint()
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
print("==================")



#metodo add()
sorteio = {1,23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)
print("==================")



#metodo clear()
sorteio = {1,23}

print(sorteio)
sorteio.clear()
print(sorteio)
print("==================")



#metodo copy()
sorteio = {1,23}

print(sorteio)
sorteio.copy()
print(sorteio)
print("==================")




#metodo discard
numeros2 = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros2)
numeros2.discard(1)
numeros2.discard(45)
print(numeros2)
print("==================")



#metodo poppop
numeros3 = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros3)
numeros3.pop()
numeros3.pop()
print(numeros3)
print("==================")



#metodo remove
numeros4 = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros4)
numeros4.remove(0)
print(numeros4)
print("==================")


#metodo len
numeros5 = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(len(numeros5))
print("==================")


#metodo len
numeros6 = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(1 in numeros6)
print(10 in numeros6)
print("==================")


