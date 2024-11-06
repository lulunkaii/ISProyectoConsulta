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
    path_directorio = f"./src/base_de_datos/medicos/{medico_ID}"  
    if not os.path.exists(f"./src/base_de_datos/medicos/{medico_ID}"):
        f = open('./src/log.txt', 'a')
        f.write(f'<{datetime.datetime.now()}> Error. La ID de medico no existe.\n')
        f.close()
        return False
    else:
        return True

def comprobar_formato_fecha(fecha):
    try:
        if type(fecha) == str:
            datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M')
            return True
        elif type(fecha) == datetime.datetime:
            return True
        else:
            f = open('./src/log.txt', 'a')
            f.write(f'<{datetime.datetime.now()}> Error. Formato de fecha incorrecto.\n')
            f.close()
            return False
    
    except ValueError:
        f = open('./src/log.txt', 'a')
        f.write(f'<{datetime.datetime.now()}> Error. Formato de fecha incorrecto.\n')
        f.close()
        return False
    
def comprobar_rut(rut): 

    correcto = True
    rut_digitos = rut.replace(".", "")
    rut_digitos = rut.replace("-", "")

    if (not rut_digitos.isdigit()) and (len(rut_digitos) != 9):
        correcto = False


    if rut.count(".") == 2:
        
        if rut[2] != "." or rut[6] != ".":
            correcto = False
            
    elif rut.count(".") != 0:
        correcto = False

    if not rut[-2] == "-":
        correcto = False
    
    if not correcto:
        f = open('./src/log.txt', 'a')
        f.write(f'<{datetime.datetime.now()}> Error. Formato de rut incorrecto.\n')
        f.close()
        return False
    else:
        return True


def escribir_a_archivo(medico_ID, nombre, correo, fecha_cita, rut, motivo):
    
    path_archivo = ""

    if comprobar_directorio(medico_ID) and comprobar_formato_fecha(fecha_cita) and comprobar_rut(rut):
        path_archivo = f"./src/base_de_datos/medicos/{medico_ID}/citas.csv"
        fecha_cita = fecha_cita.strftime("%Y-%m-%d %H:%M") # 2021-09-01 12:00:00
    else:
        return
    

    with open(f"./src/base_de_datos/medicos/{medico_ID}/citas.csv", "a") as file:
        estado = False # al momento de creacion de la cita esta no ha sido confirmada
        file.write(f"{fecha_cita};{nombre};{correo};{rut};{motivo};{estado}\n")
    
    lines = []
    with open(path_archivo, "r") as file:
        lines = file.readlines()
    
    lines = sort_dates(lines)
    
    with open(path_archivo, "w") as file:
        for line in lines:
            file.write(line)
    
    return
