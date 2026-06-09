import numpy as np
import matplotlib.pyplot as plt

# 1. Definir los valores de 'x'
# Vamos a graficar desde 0 hasta 10 productos vendidos.
x = np.linspace(0, 10, 100)

# 2. Definir nuestra función de ganancias f(x)
y = (- x ** 2 + 10*x - 15)

# 3. Configurar y dibujar el gráfico principal
plt.figure(figsize=(8,5))
plt.plot(x, y, label = "f(x) = -x^2 + 10x - 15", color = "blue", linewidth = 2)

# 4. Resaltar el punto máximo (x=5) que calculamos a mano
# Si reemplazamos x=5 en la función original: y = -(5)^2 + 10(5) - 15 = 10
plt.plot(5, 10, 'ro', markersize = 8, label = "Punto Optimo (5, 10)")

# Agregamos unas líneas punteadas para mostrar las coordenadas del punto máximo
plt.axvline(x=5, color = 'red', linestyle = '--', alpha = 0.5)
plt.axhline(y=10, color = 'red', linestyle = '--', alpha = 0.5)

# 5. Agregar detalles estéticos y etiquetas
plt.title("Grafico De Ganancias De La Empresa", fontsize = 14)
plt.xlabel("Cantidad de productos vendidos (x)", fontsize = 12)
plt.ylabel("Ganancia f(x)",  fontsize = 12)

# Dibujar el eje X en cero para ver dónde hay pérdidas (valores negativos) y ganancias
plt.axhline(0, color = 'black', linewidth = 1.2)

plt.grid(True, linestyle = ':', alpha = 0.7)
plt.legend()

# Mostrar en Pantalla
plt.show()
