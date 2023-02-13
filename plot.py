import matplotlib.pyplot as plt
import numpy as np
import glob
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MaxNLocator

def plot_slice(sharkdata,var,scalar_args={"cmap":'viridis'},cbar_args=None):
	im=plt.pcolormesh(sharkdata.xx,sharkdata.yy,getattr(sharkdata,var),**scalar_args)
	if(cbar_args is not None):
		plt.colorbar(im,**cbar_args)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.legend()
	plt.show()

  