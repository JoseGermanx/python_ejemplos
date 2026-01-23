#procedimientos

def saludar_usuario(nombre):
    print(f"Hola, {nombre}. Bienvenido/a.")


def imprimir_numeros():
    for numero in range(1, 11):
        print(numero)


# Ejemplo de uso
saludar_usuario("María")
imprimir_numeros()


# mas complejo

menu = {
    "Pizza": 8000,
    "Hamburguesa": 6500,
    "Ensalada": 5000,
    "Bebida": 2000
}


def mostrar_menu(menu):
    print("Menú del restaurante:")
    for plato, precio in menu.items():
        print(f"{plato}: ${precio}")


def mostrar_pedido(cliente, platos):
    print(f"Pedido de {cliente}:")
    for plato in platos:
        print(f"- {plato}")


def calcular_total(menu, platos):
    total = 0
    for plato in platos:
        total += menu.get(plato, 0)
    print(f"Total a pagar: ${total}")


# Ejemplo de uso
mostrar_menu(menu)

pedido_cliente = ["Pizza", "Bebida", "Ensalada"]
mostrar_pedido("Carlos", pedido_cliente)
calcular_total(menu, pedido_cliente)

