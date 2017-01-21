# NOTE: this is a master file that includes the coding for all four of the visualizations. Individual codes are under their respective names (ex. boxplot.py)
# import the modules
import csv
import pandas as pd
import numpy as np
import bokeh

# create file
df = pd.read_csv('cereal.csv')

# import palette
from bokeh.palettes import Pastel1
pal = Pastel1[5]        #choose amount of palette needed

# first graph: Box Plot of calories vs. fat in cereal
from bokeh.charts import BoxPlot, output_file, save
kayleen = BoxPlot(df, label='calories', values='fat', title="Calories vs. Fat", color='calories',palette=pal)

output_file('kayleen.html')
save(kayleen)

# second graph: Scatter plot of carbs vs. sugars
from bokeh.charts import Scatter, output_file, save
hoshi = Scatter(df, x='carbo', y='sugars', title='Carbs vs. Sugars', xlabel='Total Carbohydrates per serving (g)', ylabel='Total Sugar per serving (g)', color='#CAA2F9')

output_file('hoshi.html')
save(hoshi)

# third graph: bar graph of average sodium for fat values
from bokeh.charts import Bar, output_file, save
suga = Bar(df, 'fat', values='sodium', agg='mean', title='Average Sodium Levels vs. Fat Levels', color='fat', palette=pal)

output_file('suga.html')
save(suga)

# fourth graph: grouped bar graph of average sodium for calories, grouped on shelf value
from bokeh.charts import Bar, output_file, save
pal = Pastel1[3]

akaashi = Bar(df, 'calories', values='sodium', agg='mean', group='shelf', title='Average Sodium level per Calorie Amount, grouped by shelf value', color='shelf', palette=pal, background_fill_color='#FFFEBC')

output_file('akaashi.html')
save(akaashi)