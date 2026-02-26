
def convertir_temperatura(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k

c = float(input("ingrese temperatura en celsius: "))
f, k = convertir_temperatura(c)

print("fahrenheit:", f)
print("kelvin:", k)