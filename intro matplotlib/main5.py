import matplotlib.pyplot as plt
import numpy as np

# Configuración reproducible
np.random.seed(19680801)

# Generación de datos
data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.abs(np.random.randn(50)) * 100
}
data['b'] = data['a'] + 10 * np.random.randn(50)

# Creación de figura
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f5f5f5')

# Gráfico de dispersión
scatter = ax.scatter(
    'a', 'b', 
    c='c', 
    s='d', 
    data=data,
    cmap='viridis',
    alpha=0.7,
    edgecolors='w',
    linewidths=0.5
)

ax.set_xlabel('Variable A (unidades)', fontsize=12)  # Tamaño de fuente individual
ax.set_ylabel('Variable B (unidades)', fontsize=12)
ax.set_title('Relación entre Variables A y B\n(Tamaño = Magnitud D, Color = Variable C)', 
             fontsize=14, pad=20, fontweight='bold')  # Tamaño y estilo para título

# Barra de colores
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Valores de C', rotation=270, labelpad=15, fontsize=10)

# Leyenda de tamaños
sizes = [20, 40, 60, 80, 100]
legend_elements = [plt.Line2D([0], [0], 
                   marker='o', 
                   color='w', 
                   label=f'Tamaño: {size}',
                   markersize=np.sqrt(size), 
                   markerfacecolor='#404040') 
                   for size in sizes]
ax.legend(handles=legend_elements, title='Escala de Tamaños', loc='upper right', fontsize=9)

# Grid y estilo
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_facecolor('#f9f9f9')

plt.tight_layout()
plt.show()