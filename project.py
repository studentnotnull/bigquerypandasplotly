import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "lesson2/key.json"

import plotly.graph_objects as go
from plotly.offline import plot

from google.cloud import bigquery



client = bigquery.Client()



query_job = client.query("select tag_name, count from bigquery-public-data.stackoverflow.tags LIMIT 1000")


dataset =dict()
for row in query_job:
    dataset[row[0]] = row[1]


plot(go.Figure( data=[go.Pie(labels=list(dataset.keys()), values=list(dataset.values()))]))