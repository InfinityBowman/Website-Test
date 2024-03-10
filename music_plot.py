import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

url = 'https://raw.githubusercontent.com/InfinityBowman/Website-Test/main/InfinityBowman.csv'
# Read the CSV file with pandas
df = pd.read_csv(url, delimiter=",")

df['Date'] = pd.to_datetime(df['Date'])
start_date = pd.to_datetime('2022-01-01')
filtered_df = df[(df['Date'] >= start_date)]
df = filtered_df

df.set_index('Date', inplace=True)

# Group by 'Artist' and resample by month, counting the plays
artist_monthly_plays = df.groupby('Artist').resample('M').size().reset_index(name='PlayCount')
artist_monthly_plays = artist_monthly_plays.drop(artist_monthly_plays.loc[artist_monthly_plays['PlayCount'] == 0].index)

# Group by 'Date' and get the top 5 artists for each month
top_artists_per_month = artist_monthly_plays.groupby('Date').apply(lambda group: group.nlargest(5, 'PlayCount')).reset_index(drop=True)
df = top_artists_per_month

# Create a Bokeh ColumnDataSource
source = ColumnDataSource(df)
TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

# Create a Bokeh figure
p = figure(title='Scatter Plot', x_axis_label='Date', x_axis_type='datetime', y_axis_label='PlayCount', width=800, height=400, tools=TOOLS)

# Add a scatter glyph to the figure
scatter = p.circle(x='Date', y='PlayCount', source=source, size=8, color='blue', alpha=0.6, legend_label='Artist')

# Add HoverTool to display artist name on hover
p.hover.tooltips = [('Artist', '@Artist'), ('Date', '@Date{%F}'), ('PlayCount', '@PlayCount')]
p.hover.formatters = {'@Date': 'datetime'}

# Customize the plot appearance if needed
p.title.text_font_size = '16pt'
p.legend.location = "top_left"
p.legend.title = "Legend"

output_file("music_plot.html")
show(p)
