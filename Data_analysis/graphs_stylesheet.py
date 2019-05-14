# Color palette
color_palette = {
'light_ruby' : '#db3247', 'dark_ruby' : '#c02537',
'light_grapefruit' : '#f05462', 'dark_grapefruit' : '#e04356',
'light_bittersweet' : '#ff6d48', 'dark_bittersweet' : '#ec5536',
'light_sunflower' : '#ffcc40', 'dark_sunflower' : '#fbba28',
'light_straw' : '#ebce32', 'dark_straw' : '#dfc220',
'light_grass' : '#9ed45c', 'dark_grass' : '#8cbf46',
'light_basil' : '#19cb69', 'dark_basil' : '#19b95f',
'light_mint' : '#3ecfe', 'dark_mint' : '#2abb9a',
'light_teal' : '#9dcdcd', 'dark_teal' : '#7bb1b1',
'light_aqua' : '#44c1ef', 'dark_aqua' : '#2baedc',
'light_blue_jeans' : '#579df2', 'dark_blue_jeans' : '#448ae2',
'light_lavender' : '#ac93ef', 'dark_lavender' : '#967be2',
'light_plum' : '#8068bc', 'dark_plum' : '#6a51ac',
'light_pink_rose' : '#ef87c2', 'dark_ink_rose' : '#d971b0',
'light_beaver' : '#bca385', 'dark_beaver' : '#ab8e66',
'light_chocolate' : '#8f8272', 'dark_chocolate' : '#7a7162',
'light_light_grey' : '#f7f8fc', 'dark_light_grey' : '#e8e9ee',
'light_grey' : '#cdd1da', 'dark_grey' : '#acb2c0',
'light_dark_grey' : '#656b77', 'dark_dark_grey' : '#434957',
'light_charcoal' : '#3d3c41', 'dark_charcoal' : '#323136'}

# default plot settings
def plot_settings(plt, title, xlabel, ylabel):

	plt.figure(figsize=(20,10), facecolor='white')

	ax = plt.gca()
	ax.set_facecolor('white')
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
	plt.setp(ax.spines.values(), color=color_palette['dark_dark_grey'])

	plt.xlabel(xlabel, fontsize=12, color=color_palette['dark_dark_grey'])
	plt.ylabel(ylabel, fontsize=12, color=color_palette['dark_dark_grey'])
	plt.title(title, fontweight="bold", fontsize=20, color=color_palette['dark_dark_grey'])

def legend_settings(plt):
	legend = plt.legend(fontsize=12, loc=1)
	plt.setp(legend.get_texts(), color=color_palette['dark_dark_grey'], alpha=0.8)

	
