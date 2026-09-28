class Producto:
	def __init__(self, nombre:str, precio:float, cantidad:int):
		if not nombre.strip():
			raise ValueError("Nombre incorrecto.")
		else:
			self.nombre=nombre.strip()
			
		if precio>=0:
			self.precio=precio
		else:
			raise ValueError("Precio incorrecto. No puede ser menor que 0.")
		if cantidad>=0:
			self.cantidad=cantidad
		else:
			raise ValueError("Cantidad incorrecta.")
	
	def actualizar_cantidad(self, nueva_cantidad:int):
		if nueva_cantidad>=0:
			self.cantidad=nueva_cantidad
		else:
			raise ValueError("Nueva cantidad no puede ser menor que 0.")
	
	def actualizar_precio(self, nuevo_precio:float):
		if nuevo_precio>=0:
			self.precio=nuevo_precio
		else:
			raise ValueError("Nuevo precio no puede ser menor que 0.")

	def calcular_valor_total(self)->float:
		return self.precio * self.cantidad
	
	def __str__(self):
		print(f"Producto: {self.nombre}")
		print(f"Cantidad: {self.cantidad}")
		print(f"Precio: {self.precio}")
		return ''
		
class Inventario:
	def __init__(self):
		self.lista_productos=[]
		
	def agregar_producto(self, producto:Producto):
		if not isinstance(producto, Producto):
			raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
		else:
			self.lista_productos.append(producto)
		
	def buscar_producto(self, nombre:str)->Producto | None:
		for i in range(len(self.lista_productos)):
			if self.lista_productos[i].nombre.lower()==nombre.lower(): 
				return self.lista_productos[i]
		return None
	
	def calcular_valor_inventario(self):
		total=0
		for i in range(len(self.lista_productos)):
			total+=self.lista_productos[i].calcular_valor_total()
		return total
	
	def listar_productos(self):
		if len(self.lista_productos)==0:
			print("El inventario está vacío.")
			return
		else:
			print("En este inventario, hay los siguientes productos:")
			for i in range(len(self.lista_productos)):
				print(f" Producto {i+1}")
				print("-----------------")
				print(self.lista_productos[i])
		
def imprimir_menu():
	print("\nMENU DE OPCIONES")
	print("------------------------")
	print("1. Agregar producto")
	print("2. Buscar producto")
	print("3. Listar productos")
	print("4. Calcular valor total del inventario")
	print("5. Salir")
	print("------------------------")
	
def menu_principal(inventario: Inventario)->None:
	while True:
		imprimir_menu()
		try:
			opcion = input("Ingrese una opcion: ")
		except ValueError:
			print("ERROR. Opcion incorrecta")
			continue
			
		match opcion:
			case "1":
				print("Ingrese los datos del nuevo producto:")
				try: 
					nombre=input("Nombre: ")
					precio=float(input("Precio: "))
					cantidad=int(input("Cantidad: "))
					producto= Producto(nombre,precio,cantidad)
					inventario.agregar_producto(producto)
					print("EXITO. Producto agregado correctamente")
				except ValueError as error:
					print(f"ERROR: {error}")
				
			case "2":
				nombre=input("Ingrese el nombre del producto a buscar: ")
				producto=inventario.buscar_producto(nombre)
				if producto is None:
					print("Lo siento, producto no encontrado")
				else:
					print("EXITO, se encontro el producto")
					print(producto)
			case "3":
				inventario.listar_productos()
			case "4":
				total = inventario.calcular_valor_inventario()
				print(f"EXITO. Valor total: {round(total,2)}")
			case "5":
				print("Hasta luego!")
				break
			case _:
				print("ERROR. Opcion incorrecta")
				continue
		
if __name__=="__main__":
	inventario=Inventario()
	menu_principal(inventario)
	
