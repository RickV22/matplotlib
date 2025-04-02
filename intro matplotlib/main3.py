import matplotlib.pyplot as plt
import numpy as np

meses =["Ene","Feb","Mar"]
naranjas=[80,75,90]
uvas=[50,60,55]
manzanas=[100,85,95]

plt.figure(figsize=(12,6))
ancho_barras=0.25
x=np.arange(len(meses))

barras_naranjas=plt.bar(x-ancho_barras,naranjas,width=ancho_barras, label="Naranjas",color="#ffa500",edgecolor="black")
barras_uvas=plt.bar(x, uvas,width=ancho_barras, label="Uvas",color="#800080",edgecolor="black")
barras_manzanas=plt.bar(x+ancho_barras,manzanas,width=ancho_barras, label="Manzanas",color="#00ff00",edgecolor="black")

plt.title("Ventas Mensuales de Frutas (Primer Trimestre)",fontweight="bold", pad=20,fontsize=14)
plt.xlabel("Mes",fontsize=12,labelpad=10)
plt.ylabel("Ventas (kg)",fontsize=12,labelpad=10)
plt.xticks(x,meses)
plt.grid(axis="y",linestyle="--",alpha=0.4)

for barra in barras_naranjas:
  altura=barra.get_height()
  plt.text(barra.get_x()+barra.get_width()/2, altura+1, f"{altura} kg", ha="center", va="bottom",fontsize=10)

for barras in barras_uvas:
  altura=barras.get_height()
  plt.text(barras.get_x()+barras.get_width()/2, altura+1, f"{altura} kg", ha="center", va="bottom",fontsize=10)

for barras in barras_manzanas:
  altura=barras.get_height()
  plt.text(barras.get_x()+barras.get_width()/2, altura+1, f"{altura} kg", ha="center", va="bottom",fontsize=10)

plt.legend(loc="upper left", framealpha=1)
plt.ylim(0,max(max(naranjas),max(uvas),max(manzanas))*1.15)
plt.tight_layout()
plt.grid(axis="y",linestyle="--",alpha=0.7)

plt.show()
