from collections import defaultdict, Counter

# 1. Crear un defaultdict para contar visitas
visitas = defaultdict(int)

# Simular registros
usuarios = ["ana", "juan", "ana", "pedro", "juan", "ana"]

for usuario in usuarios:
    visitas[usuario] += 1

print("Visitas por usuario:")
for usuario, cantidad in visitas.items():
    print(f"{usuario}: {cantidad}")

# 2. Crear una lista con elementos repetidos
colores = ["rojo", "azul", "verde", "rojo", "rojo", "azul"]

# 3. Usar Counter para contar automáticamente
conteo_colores = Counter(colores)

print("\nConteo de colores:")
print(conteo_colores)

# 4. Iterar sobre los resultados
print("\nReporte de colores:")
for color, cantidad in conteo_colores.items():
    print(f"{color}: {cantidad}")
