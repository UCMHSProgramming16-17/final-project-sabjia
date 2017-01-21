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

# third graph: bar graph of average sodium for fat values
from bokeh.charts import Bar, output_file, save
suga = Bar(df, 'fat', values='sodium', agg='mean', title='Average Sodium Levels vs. Fat Levels', color='fat', palette=pal)

output_file('suga.html')
save(suga)