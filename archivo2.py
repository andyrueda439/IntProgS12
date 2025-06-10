mi_ruta = "C:\\Users\\Dell\\Documents\\archivo\\"
mi_archivo = open(mi_ruta + "notas.txt", "w")
texto = input("Dime algo: ")
mi_archivo.write(texto)
mi_archivo.close()