import matplotlib.pyplot as plt
import numpy as np

from geometry import Circle, Point

center = Point(0,0)
circle = Circle(center=center, radius=1)
alpha = np.linspace(-2*np.pi, 2*np.pi, 721)
X = circle.center.x + circle.radius * np.cos(alpha)
Y = circle.center.y + circle.radius * np.sin(alpha)

fig,axs=plt.subplots(3,1)
fig.suptitle('Связь единичной окружности с синусом и косинусом', fontsize=14)

#окружность
axs[0].plot(X, Y, color='blue', label='окружность')
axs[0].axis('equal')
axs[0].grid(True)
axs[0].legend()
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

#косинус
axs[1].plot(alpha, X, color='blue', label='cos(α)')
axs[1].grid(True)
axs[1].legend()
axs[1].set_xlabel('Угол α (радианы)')
axs[1].set_ylabel('cos(α)')

#синус
axs[2].plot(alpha, Y, color='blue', label='sin(α)')
axs[2].grid(True)
axs[2].legend()
axs[2].set_xlabel('Угол α (радианы)')
axs[2].set_ylabel('sin(α)')

#пример
angle = np.pi/3 #60 градусов
example_point = Point(np.cos(angle), np.sin(angle))

axs[0].plot(example_point.x, example_point.y, 'ro', markersize=8, label=f'α={angle:.2f}')
axs[0].plot([0, example_point.x], [0, example_point.y], 'r--', alpha=0.5)
axs[1].plot(angle, example_point.x, 'ro', markersize=8)
axs[2].plot(angle, example_point.y, 'ro', markersize=8)

plt.show()