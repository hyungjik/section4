import pandas as pd
import csv


csv2 = "d:/inflearn/crawling/section4/csv_s2.csv"
df2 = pd.read_csv(csv2, sep=';', skiprows=[0], header=None,
                  names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
print(df2)

df2.to_csv('d:/inflearn/crawling/section4/result_s1.csv', index=False)
