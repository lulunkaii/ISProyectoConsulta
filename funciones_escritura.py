import datetime
import os
def sort_dates(lines):
        
        # definir una función que recibe una línea de texto y retorna la fecha formateada como objeto datetime
        def date_key(line_string):
            fecha_str = line_string.split(";")[0]
            fecha_format = datetime.datetime.strptime(fecha_str, '%Y-%m-%d %H:%M')
            return fecha_format
        
        # sortear segun la fecha
        return sorted(lines, key=date_key)


def comprobar_directorio(medico_ID):
    path_directorio = f"./src/medicos/{medico_ID}"
    if not os.path.exists(path_directorio):
        f = open('log.txt', 'a')
        f.write('La id de medico no existe.')
        f.close()
    else:
        return True
     
def escribir_a_archivo(medico_ID, nombre, correo, fecha_cita, rut, motivo):
    
    path_archivo = f"./src/medicos/{medico_ID}/citas.csv"
    
    fecha_cita = fecha_cita.strftime("%Y-%m-%d %H:%M") # 2021-09-01 12:00:00

    with open(f"./src/medicos/{medico_ID}/citas.csv", "a") as file:
        file.write(f"{fecha_cita};{nombre};{correo};{rut};{motivo}\n")
    
    lines = []
    with open(path_archivo, "r") as file:
        lines = file.readlines()
    
    lines = sort_dates(lines)
    
    with open(path_archivo, "w") as file:
        for line in lines:
            file.write(line)
    
    return
