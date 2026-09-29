# T2: Sistema de inventario

Aplicación de consola desarrollada con Python para gestionar productos mediante programación orientada a objetos.

## Conceptos utilizados

- Clases, objetos, atributos y métodos.
- Constructores mediante `__init__`.
- Representación de objetos mediante `__str__`.
- Encapsulación de datos y comportamiento.
- Composición: un inventario contiene objetos `Producto`.
- Validación de tipos con `isinstance`.
- Excepciones `TypeError`, `ValueError` y `LookupError`.
- Anotaciones de tipos y retornos opcionales.
- Menú interactivo con `match-case`.
- Punto de entrada `if __name__ == "__main__":`.

## Funcionalidades

- Creación de productos con nombre, precio y cantidad.
- Validación de nombres vacíos, tipos incorrectos y valores negativos.
- Actualización de precio y cantidad.
- Cálculo del valor total de cada producto y del inventario.
- Búsqueda de productos sin distinguir mayúsculas y minúsculas.
- Listado de productos y gestión de inventarios vacíos.

## Ejecución

```bash
python3 sistema_inventario.py
```
