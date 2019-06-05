import json

data = [
{
    "name": "BOb",
    "gender": "male",
    "birthday": "1992-10-18"
},
{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}
]

with open('dumps_data.json', 'w') as file:
    # file.write(json.dumps(data))
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    # indent参数的值为缩进格式，这样文件json内容会自带缩进，格式清晰。
    # 如果data中带有中文需要将ensure_ascii设置为False
