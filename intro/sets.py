# Demo: Usuarios en plataformas usando sets

# Listas con usuarios (hay repetidos)
plataforma_a = ["ana", "juan", "maria", "ana", "pedro"]
plataforma_b = ["lucas", "maria", "juan", "juan", "sofia"]

# Convertir a sets (elimina duplicados)
set_a = set(plataforma_a)
set_b = set(plataforma_b)

print("Usuarios únicos plataforma A:", set_a)
print("Usuarios únicos plataforma B:", set_b)

# Intersección
print("Usuarios en ambas plataformas:", set_a & set_b)

# Unión
print("Todos los usuarios:", set_a | set_b)

# Diferencia
print("Solo en plataforma A:", set_a - set_b)
print("Solo en plataforma B:", set_b - set_a)

# Modificar sets
set_a.add("carlos")
set_b.remove("lucas")

# Recorrer un set
print("\nUsuarios plataforma A:")
for usuario in set_a:
    print(usuario)
