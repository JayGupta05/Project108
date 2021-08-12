import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("data.csv")

avg = df["Avg Rating"].tolist()
graph = pf.create_distplot([avg],["Average Rating"],show_hist=False)
graph.show()