# Semana1InsertionPrueba
#
# Descripcion: Programa que prueba el algoritmo Ordenamiento por Insercion, dado un archivo que en cada linea 
# contiene un entero.
#
# Autores: Giancarlo Dente 15-10395
#          Pedro Rodriguez 15-11264
#
# Fecha: 20/09/2019b
#
import insertion

f = open('Secuencia.txt','r')
lines = f.readlines()

A = []

for line in lines:
	A.append(int(line))

print("Secuencia a ordenar: " + str(A))
insertion.InsertionSort(A)
print("Secuencia ya ordenado: " + str(A))	