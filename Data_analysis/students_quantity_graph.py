import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from graphs_stylesheet import color_palette
from graphs_stylesheet import plot_settings, legend_settings
def draw_graph(years, students, accepted, graduated):
	
	# graph config
	x_label = str(years)
	bar_width = 1
	
	#bars position
	x_position = []
	x_position2 = []
	x_position3 = []
	for i in range(0,len(years)):
		x_position.append(1.1*i)
		x_position2.append(i*1.1-0.25)
		x_position3.append(i*1.1+0.25)

	title='Quantity of students in different years'
	xlabel='YEARS'
	ylabel='QUANTITY'
	plot_settings(plt, title, xlabel, ylabel)

	plt.bar(x_position, students, color=color_palette['light_grey'], edgecolor='white', width=bar_width, label='recruited')
	plt.bar(x_position2, accepted, color=color_palette['dark_grapefruit'], edgecolor='white', width=0.5, label='accepted')
	plt.bar(x_position3, graduated, color=color_palette['dark_basil'], edgecolor='white', width=0.5, label='graduated')
	
	ax = plt.gca()
	count = 0
	for i in ax.patches:
		if count >= len(years):
			ax.text(i.get_x()+0.05, i.get_height()+60, \
            		str(i.get_height()), fontsize=9,
                		color=color_palette['dark_dark_grey'], rotation=50, fontweight='heavy')
		else:
			ax.text(i.get_x()+0.05, i.get_height()+20, \
            		str(i.get_height()), fontsize=9,
                		color=color_palette['dark_dark_grey'], fontweight='heavy')
		count = count + 1

	legend_settings(plt)
	plt.xticks(x_position, years, rotation=60, fontsize=12, color=color_palette['dark_dark_grey'])
	plt.yticks(np.arange(0, 2500, 250),fontsize=12, color=color_palette['dark_dark_grey'])
	plt.savefig("./Graphs/students_quantity_graph.png",dpi=400)
	plt.show()



	
