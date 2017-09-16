precio = "45"

if type(precio) == str:
	# convertir a float
	precio = float(precio)

precio_con_impuesto = precio * 1.19

cantidad = "3"

if type(cantidad) == str:
	# convertir a entero
	cantidad = int(cantidad)

print("total de la venta: %f " % (precio_con_impuesto * cantidad))