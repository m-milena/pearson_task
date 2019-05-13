import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

def draw_graph(years, students, accepted, graduated):
	
	plt.style.use('seaborn-muted')
	# graph config
	x_label = str(years)
	bar_width = 1
	
	#bars position
	x_position = []
	for i in range(0,len(years)):
		x_position.append(i)

	plt.figure(figsize=(15,10))
	plt.bar(x_position, students, color='#8391a8', edgecolor='white', width=bar_width, label='recruited')
	plt.bar(x_position, accepted, color='#b24908', edgecolor='white', width=bar_width, label='accepted')
	plt.bar(x_position, graduated, color='#3b7c1b', edgecolor='white', width=bar_width, label='graduated')
	ax = plt.gca()
	plt.legend(fontsize=10)
	plt.xticks(x_position, years, rotation=60, fontsize=10)
	plt.yticks(fontsize=10)
	plt.xlabel("years", fontsize=10)
	plt.ylabel("students", fontsize=10)
	plt.title("Quantity of students in different years", fontweight="bold", fontsize=15)
	

	plt.show()
	
