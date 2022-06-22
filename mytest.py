# from samila import *
# import numpy as np
# import math
# import random
# import matplotlib.pyplot as plt

# GI = GenerativeImage()
# GI.generate()
# GI.plot(color='red', bgcolor='black', projection=Projection.POLAR)
# print(GI.function1_str)
# print(GI.function2_str)
# print(GI.seed)
# print(GI.fig)
# for f in dir(GI.fig):
#     print(f, GI.fig.f)
# plt.show()
# print(GI.fig)


# -------------------

# from samila import *
# import numpy as np
# import math
# import random
# import matplotlib.pyplot as plt

# # # def f1(x, y):
# # #     return y + random.uniform(-1, 1) * math.cos(x)

# # # def f2(x, y):
# # #     return random.uniform(-abs(x), abs(x)) * abs(x) * math.sin(y) + random.uniform(-0.5, 0.5) * math.sin(x)
# def f1(x, y):
#     return random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
# def f2(x, y):
#     return random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x

import matplotlib.pyplot as plt
import math
import random
from samila import GenerativeImage, Projection

def f1(x, y):
    return y + random.uniform(-1, 1) * math.cos(x)

def f2(x, y):
    return random.uniform(-abs(x), abs(x)) * abs(x) * math.sin(y) + random.uniform(-0.5, 0.5) * math.sin(x)

def color_f(x, y):
    return y**2 + x**2

GI = GenerativeImage(f1, f2)
GI.generate(seed=813200)
GI.plot(color_function=color_f)
# GI.save_image("test.png", depth=3)
plt.show()
