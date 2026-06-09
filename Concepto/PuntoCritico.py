import sympy as sp

x = sp.Symbol("x") # variable x

f = (-x ** 2 + 10*x - 15) # definicion de funcion

derivada = sp.diff(f, x) # se calcula la derivada
print(f"La derivada es: {derivada}")

puntosCriticos = sp.solve(derivada, x) # se almacenan los puntos criticos

# Itera el arreglo de puntosCriticos
for i in range(len(puntosCriticos)):
	puntosCrit = puntosCriticos[i]
	print(f"Punto Critico[{i+1}]: {puntosCrit}")

