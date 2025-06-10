mi_ruta = "C:\\Users\\Dell\\Documents\\archivo\\"
mi_archivo = open(mi_ruta + "compras.txt", "w")
while True:
    producto = input("Ingresa un producto (o escribe 'fin' para terminar): ")
    if producto.lower() == "fin":
        break
    mi_archivo.write(producto + "\n")
    print("Tu lista de compras ha sido guardada en compras.txt.")