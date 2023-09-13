import numpy as np
import math as m
import matplotlib.pyplot as pt
x = 0
x1 = np.empty(1)
while x <= 100:
    x = x + 0.1
    np.append (x1 , x)
    y = 4*np.sin(x)

pt.plot (x1 , y)
pt.show()


