import datetime
def sort_dates(lines):
        
        # definir una función que recibe una línea de texto y retorna la fecha formateada como objeto datetime
        def date_key(line_string):
            fecha_str = line_string.split(";")[0]
            fecha_format = datetime.datetime.strptime(fecha_str, '%Y-%m-%d %H:%M')
            return fecha_format
        
        # sortear segun la fecha
        return sorted(lines, key=date_key)
     
def escribir_a_archivo(nombre, correo, fecha_cita, rut, motivo):

    fecha_cita = fecha_cita.strftime("%Y-%m-%d %H:%M") # 2021-09-01 12:00:00

    with open("usuarios.csv", "a") as file:
        file.write(f"{fecha_cita};{nombre};{correo};{rut};{motivo}\n")
    
    lines = []
    with open("usuarios.csv", "r") as file:
        lines = file.readlines()
    
    lines = sort_dates(lines)
    
    with open("usuarios.csv", "w") as file:
        for line in lines:
            file.write(line)
    
    return
