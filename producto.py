try:
    mi_ruta = "C:\\Users\\Dell\\Documents\\archivo\\"
    mi_archivo = open(mi_ruta + "compras.txt", "r")
    for linea in mi_archivo:
            linea = linea.strip
            partes = linea.split(",")
            if len(partes) == 3:
                nombre, precio, cantidad = partes
                print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")
    else:
                print("Línea con formato incorrecto:", linea)
except FileNotFoundError:
    print("Error: El archivo 'productos.csv' no fue encontrado.")
    mi_archivo.close()