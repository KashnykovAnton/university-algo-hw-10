import numpy as np
import scipy.integrate as spi
import random
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

a = 0
b = 2

n = 1000000
x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, f(b), n)

points_under_curve = sum(y_rand <= f(x_rand))

integral_mc = points_under_curve / n * (b - a) * f(b)

integral_scipy, error = spi.quad(f, a, b)

print("Значення інтеграла за методом Монте-Карло:   ", integral_mc)
print("Значення інтеграла за допомогою функції quad:", integral_scipy)

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
