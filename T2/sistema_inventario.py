class Producto:
	def __init__(self, nombre:str, precio:float, cantidad:int):
		if not nombre.strip():
			self.nombre=nombre.strip()
		else:
			raise ValueError("El nombre no puede estar vacío.")
		if precio>=0:
			self.precio=precio
		else:
			raise ValueError("Precio incorrecto. No puede ser menor que 0")
		if cantidad>=0:
			self.cantidad=cantidad
		else:
			raise ValueError("Cantidad incorrecto. No puede ser menor que 0")
	
	def actualizar_cantidad(nueva_cantidad:int):
		if nueva_cantidad>=0:
			self.cantidad=nueva_cantidad
		else:
			raise ValueError("Nueva cantidad no puede ser menor que 0")
	
	def actualizar_precio(nuevo_precio:float):
		if nuevo_precio>=0:
			self.precio=nuevo_precio
		else:
			raise ValueError("Nuevo precio no puede ser menor que 0")

	def calcular_valor_total()->float:
		return self.precio * self.cantidad
	
	def __str__():
		print(f"Producto {self.nombre}:")
		print(f"Cantidad: {self.cantidad}")
		print(f"Precio: {self.precio}")
		
class Inventario:
	def __init__():
		self.lista_productos= list[Producto]
		
	def agregar_producto(producto:Producto):
		self.lista_productos.append(producto)
		
	def buscar_producto(nombre:str):
		for i in range(len(self.lista_productos)):
			if self.lista_productos[i].nombre==nombre: self.lista_productos[i]
		return None
	
	def calcular_valor_inventario():
		total=0
		for i in range(len(self.lista_productos)):
			total+=self.lista_productos[i].calcular_valor_total()
		return total
	
	def listar_productos():
		print("En este inventario, hay los siguientes productos:")
		for i in range(len(self.lista_productos)):
			print(f"Producto {i+1}")
			print("-----------------")
			self.lista_productos[i].__str__()
		
def imprimir_menu():
	print("1. Agregar producto")
	print("2. Buscar producto")
	print("3. Listar productos")
	print("4. Calcular valor total del inventario")
	print("5. Salir")
	
def menu_principal():
	while True:
		imprimir_menu()
		try:
			opcion = int(input("Ingrese una opcion: "))
		except:
			print("ERROR. Opcion incorrecta")
			continue
		return
		
if __name__=="__main__":
	inventario=Inventario()
	menu_principal()
	
