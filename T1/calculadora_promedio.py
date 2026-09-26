def main():
	asignaturas=[]
	calificaciones=[]
	aprobados=[]
	desaprobados=[]
	asignaturas, calificaciones = ingresar_calificaciones()
	try:
		umbral = int(input("Ingresa el valor del umbral: "))
	except ValueError:
		print("Umbral incorrecto, valor predeterminado del umbral: 5")
		umbral=5
	aprobados, desaprobados = determinar_estado(calificaciones,umbral)
	promCalififaciones = calcular_promedio(calificaciones)
	imprimirMaterias(aprobados, desaprobados, asignaturas,calificaciones)
	print(f"\nPromedio de asignaturas: {promCalififaciones:.2}")
	indiceMax,indiceMin = encontrar_extremos(calificaciones)
	print(f"Materia con mayor nota: {asignaturas[indiceMax]} / {calificaciones[indiceMax]}")
	print(f"Materia con menor nota: {asignaturas[indiceMin]} / {calificaciones[indiceMin]}")

def ingresar_calificaciones():
	asignaturas=[]
	calificaciones=[]
	numAsignatura=0
	while True:	
		auxAsignatura = input("Ingresa el nombre de la asignatura (Enter para finalizar):\n")
		if auxAsignatura=="":
			break
		asignaturas.append(auxAsignatura)
		while True:
			try: 
				auxCalificacion = int(input("Ingresa la calificacion: "))
				if (10 >= auxCalificacion >= 0):
					calificaciones.append(auxCalificacion)
					break
				else:
					print("ERROR. Ingresa una calificacion valida: ")
					continue
			except ValueError:
				print("ERROR. Ingresa una calificacion valida: ")
				continue
		print(f"Asignatura N{numAsignatura+1}: {asignaturas[numAsignatura]} / {calificaciones[numAsignatura]}\n")
		numAsignatura+=1
	return asignaturas,calificaciones
	
def calcular_promedio(calificaciones: list[int]) -> int:
	return sum(calificaciones)/(len(calificaciones))
	
def determinar_estado(calificaciones: list[int], umbral:int):
	aprobados=[]
	desaprobados=[]
	for i in range(len(calificaciones)):
		if calificaciones[i]<umbral:
			desaprobados.append(i)
		else:
			aprobados.append(i)
	return aprobados, desaprobados

def encontrar_extremos(calificaciones: list[int]):
	maximo=0
	indiceMax=0
	minimo=calificaciones[0]
	indiceMin=0
	for i in range(len(calificaciones)):
		if calificaciones[i] < minimo: 
			minimo=calificaciones[i]
			indiceMin=i
		if calificaciones[i] > maximo: 
			maximo=calificaciones[i]
			indiceMax=i
	return indiceMax, indiceMin
	
def imprimirMaterias(aprobados: list[int], desaprobados: list[int], asignaturas: list[str], calificaciones: list[int]):
	print("\nRESUMEN DE MATERIAS")
	print("-----------------------")
	status=""
	for i in range(len(asignaturas)):
		if i in desaprobados: status="DESAPROBADO"
		if i in aprobados: status="APROBADO"
		print(f"A{i+1}: {asignaturas[i]} / {calificaciones[i]}, Estado: {status}")
	print("-----------------------")

if __name__ == '__main__':
	main()
