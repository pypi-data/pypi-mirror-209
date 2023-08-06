import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение диапазонов переменных u и v
u_values = np.linspace(0, 3*np.pi, 100)
v_values = np.linspace(-np.pi, np.pi, 100)

# Создание сетки значений u и v
u, v = np.meshgrid(u_values, v_values)

# Вычисление значений x, y и z
x = u * np.cos(u) * (np.cos(v) + 1)
y = u * np.sin(u) * (np.cos(v) + 1)
z = u * np.sin(v)

# Создание каркасного графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, color='blue', linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Создание сплошного графика
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

# Отображение графиков
plt.show()
