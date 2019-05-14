import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from graphs_stylesheet import color_palette
from graphs_stylesheet import plot_settings, legend_settings

def draw_graph(x1, y1, x2, y2, title, xlabel, ylabel, savename):

	plot_settings(plt, title, xlabel, ylabel)
	plt.scatter(x1, y1, label = 'graduated', color=color_palette['dark_basil'])
	plt.scatter(x2, y2, label = "didn't graduated", color=color_palette['dark_grapefruit'])


	legend_settings(plt)
	plt.xticks(fontsize=12, color=color_palette['dark_dark_grey'])
	plt.yticks(fontsize=12, color=color_palette['dark_dark_grey'])
	#plt.savefig("./Graphs/"+savename+".png",dpi=400)
	plt.show()
