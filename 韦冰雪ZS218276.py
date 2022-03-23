import pandas as pd
from matplotlib import pyplot as plt

# 没有列名进行重命名
new_columns = ["user_id", "event_id"]
df = pd.read_csv('F:/韦冰雪/研一下/大数据与云计算/0322/user_event.csv', names=new_columns, squeeze=True)
# print(df)
df50=df['user_id'].value_counts().head(50)
print(df50)
df50_dict=df50.to_dict()
print(df50_dict)

