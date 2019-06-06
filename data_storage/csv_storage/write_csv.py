import csv

with open('data.csv', 'w', newline='',encoding='utf-8') as csvfile:
    # newline='' 为了取消写入数据后每行下面的空行
    # encoding 用于指定编码，有中文时指定为utf-8

    writer = csv.writer(csvfile, delimiter=",")  # delimiter参数定义分隔符
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
    writer.writerows([['10004', 'Tom', 24], ['10005', 'Jerry', 22]])  # writerows()方法同时写入多行，参数为二维列表
    # 字典的写入方法
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10006', 'name': 'Jenny', 'age': 22})
    writer.writerow({'id': '10007', 'name': 'Taylor', 'age': 22})
