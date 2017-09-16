tipo_string = "este es una variable string"

tipo_entero_positivo = 2 # numero
tipo_entero_negativo = -2 # numero

# lista
# todas las listas empiezan de 0
tipo_lista_productos = ["pan", "huevos", "mantequilla"]
tipo_lista_precios = [0.50, 0.7, 1.5]

tipo_flotante = 3.2

tipo_decimal = 87263281763872163872163712.2

tipo_boolean = True # o False

tipo_tupla = ("pan", "huevos", "mantequila", )


tipo_diccionario = {
	"nombres":"Marcelino Pariapaza",
    "apellidos":"Caballero Garcia",
    "cedula":"14522590",
    "fecha_nacimiento":"03121980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Complicado"
    }

print(tipo_diccionario['nombres'])
print(type(tipo_diccionario))

if tipo_boolean:
	print("el %s esta a %f" % (tipo_lista_productos[0], 
		tipo_lista_precios[0]))
else:
	print("no hay pan")