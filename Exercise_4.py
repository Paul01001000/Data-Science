import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math

N = 50
vals = np.zeros([N,4])
vals[:,0] = np.linspace(0,131/255,N)
vals[:,1] = np.linspace(132/255,184/255,N)
vals[:,2] = np.linspace(26/255,77/255,N)
vals[:,3] = np.linspace(1,0.2,N)

my_map = ListedColormap(vals)

x = np.linspace(0,2*math.pi,50)
y = [math.sin(i) for i in x]
fig = plt.figure()
plt.scatter(x,y, c=np.linspace(0,1,N), cmap=my_map, marker="s",s=np.linspace(10,(20**2)*10,N))
fig.show()
