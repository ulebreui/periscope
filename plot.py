import matplotlib.pyplot as plt
import numpy as np
import glob
import dune
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import ListedColormap
from matplotlib.ticker import MaxNLocator

def plot_slice(sharkdata,var,scalar_args={"cmap":'viridis'},cbar_args=None):
	plt.contourf(sharkdata.xx,sharkdata.yy,getattr(sharkdata,var))#,scalar_args=scalar_args)
	#plt.colorbar(cbar_args)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()

  