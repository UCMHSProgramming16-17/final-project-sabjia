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

# second graph: Scatter plot of carbs vs. sugars
from bokeh.charts import Scatter, output_file, save
hoshi = Scatter(df, x='carbo', y='sugars', title='Carbs vs. Sugars', xlabel='Total Carbohydrates per serving (g)', ylabel='Total Sugar per serving (g)', color='#CAA2F9')

output_file('hoshi.html')
save(hoshi)