import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import pandas as pd
from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','stackoverflow')

# query = "select * from bigquery-public-data.stackoverflow.users"
#
#
# print(client.estimate_query_size(query))

query = "select * from bigquery-public-data.stackoverflow.users where age is not null limit 1000"

df1 = client.query_to_pandas(query)

print(df1.head(10))

print(df1.size)

query = "select * from bigquery-public-data.stackoverflow.users  limit 1000"

df2 = client.query_to_pandas(query)
print(df2.head(10))

print(df1.size)

# df = client.query_to_pandas(query)
#
# print(df.head(10))
#
# print(df.columns)
#
#
# print(df.age>10)
#
# new_df = df[ ['display_name', 'age']  ] [df.age>10]

# print(new_df.head(10))