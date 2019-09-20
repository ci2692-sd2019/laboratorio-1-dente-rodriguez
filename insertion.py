# Semana1Insertion
#
# Descripcion: Programa que implementa el algoritmo Ordenamiento por Insercion
#
# Autores: Giancarlo Dente 15-10395
#          Pedro Rodriguez 15-11264
#
# Fecha: 20/09/2019
#
def InsertionSort(A : [int]):
	for i in range(1,len(A)):
		x = A[i]
		j = i - 1 
		while j>=0 and x<A[j]:
			A[j+1] = A[j]
			j = j - 1
		A[j+1] = x	

