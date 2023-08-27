def is_float(a_string):
    try:
        float(a_string)
        return True
    except ValueError:
        return False


columns = ["ORDEN", "CARNET", "APELLIDOS y NOMBRES", "PTJE APT ACADEM", "PTJE CONOC", "PUNTAJE TOTAL", "PUNTAJE MINIMO",
           "ESCUELA", "OBSERVACIONES", "OPCION"]
