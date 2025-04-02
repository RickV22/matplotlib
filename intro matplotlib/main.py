import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
ventas = [120, 150, 100, 135, 210, 195] 

plt.figure(figsize=(10,6))
plt.plot(meses, ventas, marker='o', linestyle='-', linewidth=2.5, color='r', label='Ventas')

plt.title('Ventas primer semestre del año')
plt.xlabel('Meses del Año')
plt.ylabel('Ventas')
plt.legend()

for i in range(len(meses)):
    plt.text(meses[i], ventas[i], f'${ventas[i]}'"K", ha='center', va='bottom', fontsize=10)
    
plt.grid(axis='y', alpha=0.10, linestyle='--', color='white')
plt.gca().set_facecolor('gray')    
plt.xticks(rotation=25)

plt.show()







