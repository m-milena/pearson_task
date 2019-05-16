import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from graphs_stylesheet import color_palette
from graphs_stylesheet import plot_settings, legend_settings, subplots_settings

def draw_graph(x1, y1, x2, y2, x3, y3, x4, y4, titles, fig_title, xlabel, ylabel, savename):
	
	
	f, axarr = plt.subplots(2,2)
	axarr[0,0].scatter(x1, y1, label = 'graduated', color=color_palette['dark_basil'], alpha=0.3)
	axarr[0,1].scatter(x2, y2, label = "didn't graduated", color=color_palette['dark_grapefruit'], alpha=0.3)
	axarr[1,0].scatter(x3, y3, label = 'graduated', color=color_palette['dark_basil'], alpha=0.3)
	axarr[1,1].scatter(x4, y4, label = "didn't graduated", color=color_palette['dark_grapefruit'], alpha=0.3)
	
	f.suptitle(fig_title, fontweight="bold", fontsize=20, color=color_palette['dark_dark_grey']) 
	subplots_settings(plt, axarr, 2, 2, titles, xlabel, ylabel)
	

	plt.savefig("./Graphs/Scores_in_different_years/"+savename+".png",dpi=400)
	plt.close()
	#plt.show()
