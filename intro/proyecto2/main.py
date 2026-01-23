from modulos.datos_basicos import leer_str, leer_int, leer_float

usuarios = []

nombre = leer_str("Nombre: ")
edad = leer_int("Edad: ")
tipo = leer_str("Tipo de usuario (admin/cliente): ")
saldo = leer_float("Saldo disponible: ")

es_mayor = edad >= 18
tiene_descuento = saldo > 0 and edad < 25
saldo_final = saldo - 5 if tiene_descuento else saldo

usuario = {
    "nombre": nombre,
    "edad": edad,
    "tipo": tipo,
    "saldo": saldo_final,
    "mayor_edad": es_mayor,
    "descuento": tiene_descuento
}

usuarios.append(usuario)

print("\nRegistro creado:")
print(usuario)
