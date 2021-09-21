import pandas as pd
import plotly.express as px
df = pd.read_csv("Data-visualization-master\csv files\line_chart.csv", encoding = "utf8")
fig = px.line(df,x="Year", y = "Per capita income", color = "Country", title = "per capita income")
fig.show()