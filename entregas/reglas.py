def elegir_medio(km, kg):
    if kg > 20:
        return "camioneta", "paquete pesado"
    elif km <= 3:
        return "bicicleta", "distancia corta"
    else:
        return "moto", "distancia media y paquete ligero"