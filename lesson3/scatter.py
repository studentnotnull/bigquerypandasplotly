import plotly.graph_objects as go
from plotly.offline import plot

x =[1,2,3,4,5,6,7,8,9,10]

y= list(map(lambda  x:x*x, x) )

trace1 =go.Scatter(x =x , y=y, mode="lines")

trace2 =go.Scatter(x =[1,2,3,4] , y=[11,7,4,1])

layout = go.Layout(title='Scatter' )

fig = go.Figure(data=[trace1,trace2], layout = layout)

plot(fig)
