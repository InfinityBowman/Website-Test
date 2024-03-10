import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import Div, Spinner, TextInput, Slider
from bokeh.layouts import column, row
import pandas as pd
# # Generate Bokeh plot
# N = 4000
# x = np.random.random(size=N) * 100
# y = np.random.random(size=N) * 100
# radii = np.random.random(size=N) * 1.5
# colors = ["#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(np.floor(50 + 2 * x), np.floor(30 + 2 * y))]

# plot = figure()
# plot.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

# # Specify the output file
# output_file("bokeh_plot.html")

# # Save and show the plot
# show(plot)
url = 'https://raw.githubusercontent.com/InfinityBowman/Website-Test/main/InfinityBowman.csv'

# Read the CSV file with pandas
df = pd.read_csv(url, delimiter=",")

x = np.random.random(50)
y = np.random.random(50)

p = figure()
points = p.circle(x, y)

# Create a Div with styled text
div_text = "<p style='color: orange; font-size: 24px; font-weight: bold;'>Select Size</p>"
div_size = Div(text=div_text)

div_text = "<p style='color: orange; font-size: 24px; font-weight: bold;'>Select Color</p>"
div_color = Div(text=div_text)

slider_styles = {'color': 'orange', 'font-size': '16px'}
slider = Slider(start=0, end=100, value=50, step=1, title="Slider", 
                bar_color='#e043ff', styles=slider_styles)
slider.js_link('value', points.glyph, 'size')

spinner_styles = {'color': 'orange', 'font-size': '16px'}
spinner = Spinner(title='', low=0, high=20, step=1,
                  value=points.glyph.size, width=200, styles=spinner_styles)
spinner.js_link("value", points.glyph, "size")

textinput = TextInput(value=points.glyph.fill_color, width=200)
textinput.js_link("value", points.glyph, "fill_color")

# Arrange the widgets in a specific layout
# row1 = row(div_size, spinner, align='start')
# row2 = row(div_color, textinput, align='start')
# layout = column(row1, row2, p, sizing_mode="stretch_both", )
layout = column(row(column(div_size, spinner), column(div_color, textinput), align='center'), slider, p)

# Specify the output file and show the plot
output_file("bokeh_plot.html")
show(layout)
