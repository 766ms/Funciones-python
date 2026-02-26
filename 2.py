
def agregar_estudiante(lista, nombre, nota):
    estudiante = {"nombre": nombre, "nota": nota}
    lista.append(estudiante)

def mostrar_estudiantes(lista):
    for e in lista:
        print("nombre:", e["nombre"], "nota:", e["nota"])

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    suma = 0
    for e in lista:
        suma += e["nota"]
    return suma / len(lista)

estudiantes = []

cantidad = int(input("cuantos estudiantes desea agregar: "))

for i in range(cantidad):
    nombre = input("nombre del estudiante: ")
    nota = float(input("nota del estudiante: "))
    agregar_estudiante(estudiantes, nombre, nota)

print("lista de estudiantes")
mostrar_estudiantes(estudiantes)

promedio = calcular_promedio(estudiantes)
print("promedio general:", promedio)