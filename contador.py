try:
    mi_ruta = "C:\\Users\\Dell\\Documents\\archivo\\"
    nombre = input("Nombre del archivo (Ejemplo: poema.txt): ")
    mi_archivo = open(mi_ruta + 'contador', 'r')
    contenido = mi_archivo.read()
    lineas = mi_archivo.readlines()
    numero_lineas = len(lineas)
    print(f"El archivo tiene {numero_lineas} lineas.")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre}' no fue encontrado.")