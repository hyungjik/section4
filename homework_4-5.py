import pandas as pd
import numpy as np

example = "d:/inflearn/crawling/section4/FL_insurance_sample.csv"
df = pd.read_csv(example)
print(df.head())
print(df.loc[:, 'county'])
print(df.loc[:, ['county', 'line']])
print(df.iloc[0, 0])
print(df.query('point_granularity <= 2'))
df2 = df.query('statecode == "FL" and construction == "Masonry"')

df2.to_csv("d:/inflearn/crawling/section4/FL_csv.csv")



#
# # df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
# df = pd.DataFrame(np.random.randn(100,4), columns=list('ABCD'))
# print(df)
#
# df.to_csv('d:/inflearn/crawling/section4/result_s2.csv', index=False, header=False)
