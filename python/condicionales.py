# condicionales
# http://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/condicional_if.html

stock = 4
cantidad_requerida = 4
precio = 21


if cantidad_requerida > stock:
	print("no hay stock suficicente para su pedido")
else:
	print("El total de su pedido es %f" % (cantidad_requerida * precio))


