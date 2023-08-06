import numpy as np
import matplotlib.pyplot as plt

# Определение диапазона значений параметра t
t_values = np.linspace(0, 5*np.pi, 500)

# Вычисление значений x и y
x = t_values * np.sin(t_values)
y = t_values * np.cos(t_values)

# Построение графика спирали
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Спираль: x = t * sin(t), y = t * cos(t)')
plt.grid(True)
plt.show()
