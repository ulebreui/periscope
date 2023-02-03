import matplotlib.pyplot as plt
import numpy as np
import glob
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MaxNLocator

def plot_slice(sharkdata,var,levels=100,scalar_args={"cmap":'viridis'},cbar_args=None):
	plt.contourf(sharkdata.xx,sharkdata.yy,getattr(sharkdata,var),levels=levels,**scalar_args)
	#plt.colorbar(cbar_args)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()

  