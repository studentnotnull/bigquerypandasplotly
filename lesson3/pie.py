import plotly.graph_objects as go
from plotly.offline import plot

fig = go.Figure( data=[go.Pie(labels=['bob','boba','boban'], values=[1000,1000,1000])])
plot(fig)