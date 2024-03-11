import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file, curdoc
from bokeh.models import ColumnDataSource
from bokeh.models import Div, Spinner, TextInput, Slider
from bokeh.layouts import column, row
from bokeh.themes import Theme

# Create a Bokeh theme from the JSON definition
custom_theme = Theme(filename="./custom_plot_theme.json")

# Apply the custom theme to the current document
curdoc().theme = custom_theme #131313 is cool red
# curdoc().theme = 'dark_minimal'

url = 'https://raw.githubusercontent.com/InfinityBowman/Website-Test/main/InfinityBowman.csv'
# Read the CSV file with pandas
df = pd.read_csv(url, delimiter=",")

# Fix Dates
df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%y %H:%M")
start_date = pd.to_datetime('2022-01-01')
filtered_df = df[(df['Date'] >= start_date)]
df = filtered_df
df.set_index('Date', inplace=True)

# Group by 'Artist' and resample by month, counting the plays
artist_monthly_plays = df.groupby('Artist').resample('ME').size().reset_index(name='PlayCount')
artist_monthly_plays = artist_monthly_plays.drop(artist_monthly_plays.loc[artist_monthly_plays['PlayCount'] == 0].index)

# Group by 'Date' and get the top 5 artists for each month
top_artists_per_month = artist_monthly_plays.groupby('Date', group_keys=False).apply(lambda group: group.nlargest(5, 'PlayCount')).reset_index(drop=True)
df = top_artists_per_month

# Create a Bokeh ColumnDataSource
source = ColumnDataSource(df)
TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

# Create a Bokeh figure
p = figure(title='Top 5 Music Artists Per Month', x_axis_label='Date', x_axis_type='datetime', y_axis_label='Plays', width=800, height=600, tools=TOOLS)

# Add a scatter glyph to the figure
points = p.circle(x='Date', y='PlayCount', source=source, size=12, color='white', alpha=0.6, legend_label='Artist')

# Add HoverTool to display artist name on hover
p.hover.tooltips = [('Artist', '@Artist'), ('Date', '@Date{%F}'), ('PlayCount', '@PlayCount')]
p.hover.formatters = {'@Date': 'datetime'}

# Customize the plot appearance if needed
p.title.text_font_size = '16pt'
p.legend.location = "top_left"
p.legend.title = "Legend"

# Select Size
div_text = "<p style='color: orange; font-size: 24px; font-weight: bold;'>Select Size</p>"
div_size = Div(text=div_text)

# Select Color
div_text = "<p style='color: orange; font-size: 24px; font-weight: bold;'>Select Color</p>"
div_color = Div(text=div_text)

# Spinner Bar
spinner_styles = {'color': 'orange', 'font-size': '16px'}
spinner = Spinner(title='', low=0, high=40, step=1,
                  value=points.glyph.size, width=200, styles=spinner_styles)
spinner.js_link("value", points.glyph, "size")

# Text Input Bar
textinput = TextInput(value=points.glyph.fill_color, width=200)
textinput.js_link("value", points.glyph, "fill_color")

# Set Layout
layout = column(row(column(div_size, spinner), column(div_color, textinput), align='center'), p, align='center')

output_file("music_plot.html")
show(layout)
