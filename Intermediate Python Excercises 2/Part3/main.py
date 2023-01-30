#For this part of the assignment, I had to figure out how to create a virtual environment within Visual Studio Code, which I learned how to do from this video: https://www.youtube.com/watch?v=1w6zUrVx4to&ab_channel=PythonInOffice

import numpy as np
from numpy import random

a = random.rand(10)
print("Random numbers: " + str(a))
print("Mean: " + str(np.mean(a)))
print("Median: " + str(np.median(a)))
print("Standard Deviation: " + str(np.std(a)))