import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv", encoding = "utf8")
fig = px.bar(df,x="Country", y = "InternetUsers")
fig.show()