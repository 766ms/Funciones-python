
def analizar_ventas(ventas):
    mayor = max(ventas)
    menor = min(ventas)
    promedio = sum(ventas) / len(ventas)
    return mayor, menor, promedio

ventas = []
cantidad = int(input("cuantas ventas desea ingresar: "))

for i in range(cantidad):
    venta = float(input("ingrese valor de la venta: "))
    ventas.append(venta)

mayor, menor, promedio = analizar_ventas(ventas)

print("venta mayor:", mayor)
print("venta menor:", menor)
print("promedio de ventas:", promedio)