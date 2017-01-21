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

# fourth graph: grouped bar graph of average sodium for calories, grouped on shelf value
from bokeh.charts import Bar, output_file, save
pal = Pastel1[3]

akaashi = Bar(df, 'calories', values='sodium', agg='mean', group='shelf', title='Average Sodium level per Calorie Amount, grouped by shelf value', color='shelf', palette=pal, background_fill_color='#FFFEBC')

output_file('akaashi.html')
save(akaashi)