import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,7)
y1=np.array([15,23,18,37,27,35])
y2=np.array([10,20,25,18,30,22])

plt.figure(figsize=(10,6))

plt.plot(x,y1,label='producto A', color='r', marker='o', linewidth=2)
plt.plot(x,y2,label='producto B', color='b', linestyle='--', marker='s', linewidth=2)
plt.title("Comparacion de ventas: producto A VS producto B", fontweight="bold",pad=20)
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Ventas (miles de USD)", fontsize=12)
plt.xticks(x)
plt.grid(axis="y", linestyle="--", alpha=0.4)

for xi,yi in zip(x,y1):
    plt.text(xi, yi+1, f"{yi}", ha="center", va="bottom", fontsize=10)
    
for xi,yi in zip(x,y2):
    plt.text(xi, yi+1, f"{yi}", ha="center", va="bottom", fontsize=10)

plt.ylim(0, max(max(y1), max(y2))*1.2)

plt.legend(loc="upper left", framealpha=1)
plt.tight_layout()
plt.show()    

