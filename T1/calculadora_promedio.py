def main():
	asignaturas, calificaciones = ingresar_calificaciones()
	if calificaciones:
		try:
			umbral = float(input("Ingresa el valor del umbral (predeterminado=5): "))
		except ValueError:
			print("Umbral incorrecto, valor predeterminado del umbral: 5")
			umbral = 5.0
		aprobados, desaprobados = determinar_estado(calificaciones, umbral)
		promedio = calcular_promedio(calificaciones)
		mostrar_resumen(aprobados, desaprobados, asignaturas,calificaciones)
		print(f"\nPromedio de asignaturas: {round(promedio,2)}")
		indiceMax,indiceMin = encontrar_extremos(calificaciones)
		print(f"Materia con mayor nota: {asignaturas[indiceMax]} / {calificaciones[indiceMax]}")
		print(f"Materia con menor nota: {asignaturas[indiceMin]} / {calificaciones[indiceMin]}")
	else:
		print("No se ingresaron datos!")

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
				auxCalificacion = float(input("Ingresa la calificacion: "))
				if (10 >= auxCalificacion >= 0):
					calificaciones.append(auxCalificacion)
					break
				else:
					print("ERROR. Ingresa una calificacion valida: ")
					continue
			except ValueError:
				print("ERROR. Ingresa una calificacion valida: ")
				continue
		#print(f"Asignatura N{numAsignatura+1}: {asignaturas[numAsignatura]} / {calificaciones[numAsignatura]}\n")
		numAsignatura+=1
	return asignaturas,calificaciones
	
def calcular_promedio(calificaciones: list[float]) -> float:
	if calificaciones:
		return sum(calificaciones)/(len(calificaciones))
	else:
		return 0
	
def determinar_estado(calificaciones: list[float], umbral=5.0):
	aprobados=[]
	desaprobados=[]
	for i in range(len(calificaciones)):
		if calificaciones[i]<umbral:
			desaprobados.append(i)
		else:
			aprobados.append(i)
	return aprobados, desaprobados

def encontrar_extremos(calificaciones: list[float]):
	maximo=max(calificaciones)
	indiceMax=calificaciones.index(maximo)
	minimo=min(calificaciones)
	indiceMin=calificaciones.index(minimo)
	return indiceMax, indiceMin
	
def mostrar_resumen(aprobados: list[int], desaprobados: list[int], asignaturas: list[str], calificaciones: list[float]):
	print("\nRESUMEN DE MATERIAS")
	print("-----------------------")
	estado=""
	for i in range(len(asignaturas)):
		if i in desaprobados: estado="DESAPROBADO"
		if i in aprobados: estado="APROBADO"
		print(f"A{i+1}: {asignaturas[i]} / {calificaciones[i]}, Estado: {estado}")
	print("-----------------------")

if __name__ == '__main__':
	main()
	print("Hasta luego!")
