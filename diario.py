from datetime import datetime

mi_ruta = "C:\\Users\\Dell\\Documents\\archivo\\"
dato = input("Texto: ")
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
mi_archivo = open(mi_ruta + "diario.txt", "a")
mi_archivo.write(f"{fecha} - {dato}")
mi_archivo.close()