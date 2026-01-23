def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def clasificar_temperatura(t):
    if t < 5:
        return "Muy frío"
    elif t < 15:
        return "Frío"
    elif t < 25:
        return "Agradable"
    elif t < 35:
        return "Caluroso"
    else:
        return "Extremo"


def clasificar_edad(edad):
    if edad > 60:
        return "Adulto mayor"
    else:
        return "No adulto mayor"
