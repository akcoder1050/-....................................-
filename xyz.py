import pandas as pan
import csv 
import plotly.graph_objects as plo

#imortant line from pandas liberary(5 and 6 line)data file.
ggc =  pan.read_csv("xyz.csv")
print(ggc.groupby("level")["attempt"].mean())
fig = plo.Figure(plo.Bar(
            x=ggc.groupby("level")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation='h'))
fig.show() 