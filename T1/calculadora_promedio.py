def main():
	ingresar_calificaciones()

def ingresar_calificaciones():
	asignaturas=[]
	calificaciones=[]
	numAsignatura=0
	while True:
		print("Ingresa el nombre de la asignatura")		
		auxAsignatura=input()
		asignaturas.append(auxAsignatura)
		while True:
			print("Ingresa la calificacion")
			auxCalificacion=input()
			if (10 >= auxCalificacion >= 0):
				auxCalificacion=input()
				calificaciones.append(auxCalificacion)
				break
			else:
				print("ERROR. Ingresa una calificacion valida")
				continue
		numAsignatura+=1
		
if __name__ == '__main__':
	main()
