# bucle while
# while = http://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/bucle_while.html
# for = http://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/bucle_for.html

suma = 0
numero = 1

while numero <= 10:
    suma = numero + suma
    numero = numero + 1

print("La suma es %s" % str(suma))

# bucle for
lista_animales = ["gato", "perro", "elefante"] # i=3

for animal in lista_animales:
	print(animal)

lista_productos = [{"nombre": "pan", "precio": 0.5, "cantidad": 21}, 
					{"nombre": "leche", "precio": 1.5, "cantidad": 2},
					{"nombre": "mantequila", "precio": 2.5, "cantidad": 2}
					]


for producto in lista_productos:
	print("total del producto %s es igual a %f" 
		% (producto["nombre"], producto["precio"]*producto["cantidad"]) )
	# if producto["nombre"] == "pan":
		# break




