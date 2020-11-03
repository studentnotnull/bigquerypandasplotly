import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import pandas as pd
from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','stackoverflow')



query = "select * from bigquery-public-data.stackoverflow.stackoverflow_posts "

df = client.query_to_pandas(query)

df.sort_values('answer_count',ascending=False, inplace=True)
result = df.iloc[:2]


# VS


query = "select * from bigquery-public-data.stackoverflow.stackoverflow_posts order by answer_count desc limit 2"

df = client.query_to_pandas(query)

print(df)