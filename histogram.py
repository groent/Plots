import matplotlib.pyplot as plt
import numpy as np

#np.arrange returns an array of random integers within 8
x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)


plt.show()