import csv
import pandas as pd

with open('data.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)  # 没一行都是列表形式

# 还可以使用pandas中的read_csv()，读取csv文件
df = pd.read_csv('data.csv')
print(df)