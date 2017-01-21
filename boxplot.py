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