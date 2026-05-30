
# Importamos las bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset de ventas
df = pd.read_csv("datos/dataset.csv")

# Calculamos el importe total de cada venta
df["ventas_total"] = df["cantidad"] * df["precio"]
# Calculamos ventas totales
ventas_totales = df["ventas_total"].sum()

# Obtenemos el producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Convertimos la columna fecha al formato datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# Extraemos el mes de cada venta
df["mes"] = df["fecha"].dt.month

# Agrupamos las ventas por mes
ventas_por_mes = df.groupby("mes")["ventas_total"].sum()

# Mostramos resultados por consola
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Generamos el gráfico de evolución de ventas
plt.figure(figsize=(8,5))
ventas_por_mes.plot(marker="o")

plt.title("Evolución de ventas por mes")
plt.xlabel("mes")
plt.ylabel("ventas")
plt.grid(True)

# Guardamos el gráfico en la carpeta resultados
plt.savefig("resultados/grafico_resultados.png")

plt.show()
