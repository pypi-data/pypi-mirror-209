import numpy as np

# Генерация массива случайных чисел
arr = np.random.randint(1, 21, size=(5, 5))
print("Исходный массив:")
print(arr)

# Замена чисел от 3 до 8 на 0
arr[(arr >= 3) & (arr <= 8)] = 0
print("\nМассив после замены:")
print(arr)
