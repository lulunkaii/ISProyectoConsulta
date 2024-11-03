import datetime

def writeToFile(nombre, correo, fecha):

    posicion_a_insertar = 0
    with open("usuarios.csv", "a+") as file:
        for line in file:
            fecha_agendada = line.split(";")[0]
            if fecha_agendada >= fecha.strftime("%Y-%m-%d %H:%M:%S"):
                break
            
            posicion_a_insertar += 1

    posicion_a_insertar = 2
    fecha.strftime("%Y-%m-%d %H:%M:%S") # 2021-09-01 12:00:00
    with open("usuarios.csv", "a") as file:
        file.seek(posicion_a_insertar)
        file.write(f"{fecha};{nombre};{correo}\n")

    return

