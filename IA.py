#  -*- coding: utf-8 -*-

#CALCULO DE PROBABILIDADES

cantidad_de_ganancia1 = int(input("Digite la primer cantidad de ganancia: "))
probabilidad_de_cantidad_ganancia1 = int(input("Digite el primer porcentaje de ganancia: "))


perdida_cantidad1 = int(input("Digite la primer perdida: "))
probabilidad_perdida_de_cantidad1 = int(input("DIgite la primer probabilidad de perdida: "))

#SEGUNDA OPCION

cantidad_de_ganancia2 = int(input("\n\n\nDigite la segunda cantidad de ganancia: "))
probabilidad_de_cantidad_ganancia2 = int(input("Digite el segundo porcentaje de ganancia: "))

perdida_cantidad2 = int(input("Digite la segunda perdidad: "))
probabilidad_perdida_de_cantidad2 = int(input("Digite la segunda probabilidad de perdida: "))

#CALCULO DE LA MEJOR OPCION
#PRIMERA OPCION

rest1 = cantidad_de_ganancia1*(probabilidad_de_cantidad_ganancia1/100)
rest2 = perdida_cantidad1*(probabilidad_perdida_de_cantidad1/100)

referencia1 = rest1-rest2
print(referencia1)

#SEGUNDA OPCION

rest3 = cantidad_de_ganancia2*(probabilidad_de_cantidad_ganancia2/100)
rest4 = perdida_cantidad2*(probabilidad_perdida_de_cantidad2/100)

referencia2 = rest3-rest4
print(referencia2)

#CONDICIONALES PARA LA ELECION DE LA MEJOR OPCION
if referencia1 >= referencia2:
	print("\nLA PRIMERA OPCION ES MEJOR QUE LA SEGUNDA")
else:
	print("\neLA SEGUNDA OPCION ES MEJOR QUE LA PRIMERA")
