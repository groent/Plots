import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots() 
x = [1, 2, 3, 4]
y = [1, 4, 2, 3]
y_err = [0.9, 1.2, 0.5, 0.3]
ax.plot(x, y, color="blue")
ax.errorbar(x, y, y_err, fmt="o", linewidth=2, capsize=6, color="blue")

ax.set_title("Desplasamiento vs Tiempo")
ax.set_xlabel("Time(s)")
ax.set_ylabel("Velocity(m/s)")

plt.show()                           