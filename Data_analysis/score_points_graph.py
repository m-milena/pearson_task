import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import seaborn as sns
from graphs_stylesheet import color_palette
from graphs_stylesheet import plot_settings, legend_settings

def draw_graph(years, minimum_score, maximum_score, average_score):
# graph config
	x_label = str(years)
	bar_width = 1
	
	#bars position
	x_position = []

	for i in range(0,len(years)):
		x_position.append(i)

	title='Score of accepted students in different years'
	xlabel='YEARS'
	ylabel='SCORE'
	plot_settings(plt, title, xlabel, ylabel)
	plt.bar(x_position, maximum_score, color=sns.color_palette("bone", len(x_position)*3), edgecolor='white', width=bar_width, label='score of accepted students')
	plt.bar(x_position, minimum_score, color='white', edgecolor='white', width=bar_width)
	
	plt.plot(x_position, average_score, '^', color=color_palette['dark_grass'], label='average score of accepted students')
	ax = plt.gca()
	count = 0
	for i in ax.patches:
		if count >= len(x_position):
			ax.text(i.get_x()+0.05, i.get_height()-15, \
            		str(i.get_height()), fontsize=9,
                		color=color_palette['light_dark_grey'], fontweight='heavy')
		else:
			ax.text(i.get_x()+0.05, i.get_height()+5, \
            		str(i.get_height()), fontsize=9,
                		color=color_palette['light_dark_grey'], fontweight='heavy')
		count = count + 1
	
	for i,j in zip(x_position,average_score):
    		corr = 0.4
    		ax.annotate(str(j),  xy=(i-corr, j+corr*15), color=color_palette['dark_grass'], fontweight="bold", fontsize=10)

	legend_settings(plt)
	plt.xticks(x_position, years, rotation=60, fontsize=12, color=color_palette['dark_dark_grey'])
	plt.yticks(fontsize=12, color=color_palette['dark_dark_grey'])
	ax=plt.gca()
	ax.set_ylim(500, 1200)
	plt.savefig("./Graphs/score_points_graph.png",dpi=400)
	plt.show()
