import matplotlib.pyplot as plt
import numpy as np

horas_estudio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
puntuaciones = np.array([55, 58, 63, 67, 70, 72, 75, 78, 82, 85])  

plt.scatter(horas_estudio, puntuaciones, color='blue', label='Horas de Estudio vs Puntuaciones', edgecolors='black')

plt.title("Relación entre Horas de Estudio y Puntuaciones", fontsize=14)
plt.xlabel("Horas de Estudio", fontsize=12)
plt.ylabel("Puntuaciones Obtenidas", fontsize=12)

for i in range(len(horas_estudio)):
    plt.text(horas_estudio[i], puntuaciones[i] + 1, f'{puntuaciones[i]}', ha='center', va='bottom', fontsize=10)

plt.legend()
plt.tight_layout()
plt.show()

