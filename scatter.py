import matplotlib.pyplot as plt
import numpy as np

a = np.arange(50)
c = np.random.randint(0, 50, 50)
d = np.random.randn(50) * 100
b = a + 10 * np.random.randn(50)


plt.grid(True)
plt.scatter(a, b, c=c, s=d)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.colorbar()
plt.show()