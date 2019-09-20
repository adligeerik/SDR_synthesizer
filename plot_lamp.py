import numpy as np
import matplotlib.pyplot as plt
import os
import sys


f= open(sys.argv[1],"r")


data = np.fromfile(f,dtype=np.float32)


fig = plt.figure()
plt.ylim((-0.2,1.2))
plt.plot(data)

plt.show()


f.close()





