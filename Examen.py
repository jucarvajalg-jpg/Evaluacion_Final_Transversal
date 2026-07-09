# =====================================================================
# ASIGNATURA: Fundamentos de Programación (FPY1101)
# EVALUACIÓN: Evaluación Final Transversal (EFT) - PetMarket
# =====================================================================

#----------------------------------------------------------------------
# 1. Funcion de Validacion Independiente
#----------------------------------------------------------------------

def validar_codigo(codigo, productos):
    if not codigo or codigo.scrip() == "":
        return False
    if codigo.strip().upper() in [k.upper( for k in productos.keys()]:
        return False
    return True

def validar_nombre(nombre):
    return bool(nombre and nombre.strip() != "")

def validar_categoria(categoria):
    return bool(categoria and categoria.strip() != "")

def validar_marca(marca):
    return bool(marca and marca.strip() != "")

def validar_peso(peso):
    try:
        val = float(peso)
        return val > 0
    except ValueError:
        return False

def validar_es_importado(opcion):
    return opcion.strip().lower() in ["s", "n"]

def validar_es_para_cachorros(opcion):
    return opcion.strip().lower() in ["s", "n"]