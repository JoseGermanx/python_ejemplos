class CuentaCorreo:
    def __init__(self, usuario, dominio, password):
        self.usuario = usuario          # atributo público
        self._dominio = dominio          # atributo protegido
        self.__password = password      # atributo privado

    def mostrar_cuenta(self):
        print(f"Correo: {self.usuario}@{self._dominio}")


# Crear una instancia
cuenta = CuentaCorreo("juan", "correo.com", "1234segura")

# Acceso a atributos
print(cuenta.usuario)        # público: acceso directo
print(cuenta._dominio)       # protegido: accesible, pero no recomendado

# print(cuenta.__password)   # ❌ error: no es accesible directamente

# Acceso indirecto (name mangling)
print(cuenta._CuentaCorreo__password)


