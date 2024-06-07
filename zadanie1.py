import numpy as np
import matplotlib.pyplot as plt

# Параметры
alpha = 1.75
beta = 3 / 5

# Определение функции розы
def rose(t, alpha, beta):
    return alpha * np.abs(np.cos(beta * t))

# Генерация параметра t
t = np.linspace(0, 50 * np.pi, 50000)
z = rose(t, alpha, beta) * np.exp(1j * t)

# Конформное отображение
def f(z):
    return (2 * z - 1j) / (2 + 1j * z)

w = f(z)

# Визуализация
plt.figure(figsize=(14, 7))

# Оригинальный образ розы
plt.subplot(1, 2, 1)
plt.plot(z.real, z.imag, label='Прообраз розы')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Прообраз розы в декартовой системе')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Образ розы после конформного отображения
plt.subplot(1, 2, 2)
plt.plot(w.real, w.imag, label='Образ розы', color='r')
plt.xlabel('Re(w)')
plt.ylabel('Im(w)')
plt.title('Образ розы в декартовой системе')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.tight_layout()
plt.show()