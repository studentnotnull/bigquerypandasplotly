import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import plotly.graph_objects as go
from plotly.offline import plot

from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','stackoverflow')


query = """ select 
                    *
            from bigquery-public-data.stackoverflow.stackoverflow_posts 
            
         
            limit 1000
        """

df = client.query_to_pandas(query)

print(df.head(10))

df_filter = df[['id', 'title', 'comment_count', 'answer_count']][ (df.comment_count>=2) & (df.answer_count>=1) ]

print(df_filter.comment_count.max())

print(df_filter[['comment_count']].min())

print(df_filter.head(10))
print(df_filter.size)
print(df_filter.count)


# trace = go.Scatter(x = df.creation_date, y= df.count_of_posts)
#
# fig = go.Figure(data=[trace])
#
# plot(fig)
# VS
# fig_dict={
#
#     "data":[
#
#                     {
#                         "x":df.creation_date,
#                         "y":df.count_of_post,
#                         "type":"scatter"
#                     }
#             ],
#     "layout":
#         {
#             "title":"Information"
#         }
# }
#
# plot(fig_dict)






