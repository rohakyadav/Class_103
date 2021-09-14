Topic Capstone class: Data visualization

● Learn to use plotly and pandas for data visualization 

● Visualize internet users data from different countries and compare it with their per capita income using line graph, histograms and scatter plots

What are the data types that we use while writing code? We know about the use of -dictionary -list -float -integer -string.

There is another data object which is called a dataframe. In the data frame the data is aligned in tabular form

 [i.e.](https://i.e./),

 rows and columns. And these rows and columns can have any type of data such as string or integer or float.

To create a data frame we need a python library called pandas. pandas library helps us with data manipulation and analysis. First we need to install this library to our system.

Using pip3 the python package manager. We'll write a command pip3 install pandas.

mport pandas as pd data = [1,2,3,4,5] df = pd.DataFrame(data) print (df)

So graphs use data from dataframe. Python has a library called Ploty Express which is a visualization library. “Plotly Express” is actually a high-level wrapper for Plotly, and provides a much simpler syntax to draw complex charts in no time.

plotly is a Python library which is used to design graphs, especially interactive graphs

let's install the ploty express to our system. We'll install it using pip3, the python package manager.

Now let's see how to plot the line chart. To plot the chart, we first need to import ploty.express as px and also import pandas as pd.

import pandas as pd import plotly.express as px

Then we use a read_csv method provided by pandas to read the csv file and store the data in the df variable. Code:- df =

 pd.read_csv("[line_chart.csv](https://line_chart.csv/)")

We use the line() method to create the line chart. Line charts are often used to see how the value of one parameter (y) changes compared to another parameter (x).

For example-> How do profits change for different days in the month? How does stock market price change for different days of the week?

Normally one value which varies independently is called an independent variable. Here days in the month and days of the week are independent variables.

The other value which varies as the independent variable changes is called the dependent variable. Here profits and stock price are dependent variables

Independent variables are denoted by x while dependent variables are denoted by y.

The line chart takes parameters such as the data, value for x and y, color and the title for the chart. Code: fig =

 [px.line(df](https://px.line(df/),

 x="Year", y="Per capita income", color="Country", title='Per Capita Income')

Using the show() method we show the graph. Code:

 [fig.show()](https://fig.show()/)

The lines show drop and growth over the years indicating growth or drop in per capita income of the countries. Different colors indicate different countries On the x axis there are years plotted and on y axis we have the per capita income.

This is one form of graphical representation. There is another chart called a bar chart. Bar charts are a type of graph that are used to display and compare the number, frequency or other measure for different categories of data.

To create a bar chart we use bar() method . This bar method takes parameters such as the data, value for x and y, color and the title for the chart. Code: fig =

 [px.bar(df](https://px.bar(df/),

 x='Country', y='InternetUsers')

Using the show() method we show the graph. Code:

 [fig.show()](https://fig.show()/)

There is another form of representing data that is using a scatter plot. Scatter plot is used to plot data points

on a horizontal and a vertical axis in the attempt to show how much one variable is affected by another.

To create a scatter chart we use scatter() method . This scatter method takes parameters such as the data, value for x and y, color and the size for the markers.

fig = px.scatter(df, x="Population", y="Per capita", size="Percentage",color="Country" , size_max=60)