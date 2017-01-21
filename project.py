# import the modules
import csv
import pandas as pd
import numpy as np
import bokeh

# create file
df = pd.read_csv('population.csv')

# first graph: bar graph of the number of total asian population in each borough
from bokeh.charts import Bar, output_file, save
kayleen = Bar(df, 'Borough', values='Total Asian Only', title='Asian Population in NYC Boroughs (2010)', color='#DEAAF8')

output_file('kayleen.html')
save(kayleen)           #save file!!!

# second graph: pie chart of how many chinese people in each borough
from bokeh.charts import Donut, output_file, save

hoshi = Donut(df, label=['Borough','Total Asian - Chinese and Taiwanese'], values='Total Asian - Chinese and Taiwanese', text_font_size='7pt', 
title='Total Chinese and Taiwanese in NYC Boroughs (2010)', color=['#A4EED7','#C7EEA4','#FBF37C','#F9AAA2','#CAA2F9'])


output_file('hoshi.html')
save(hoshi)             #save the file!

# third graph: 