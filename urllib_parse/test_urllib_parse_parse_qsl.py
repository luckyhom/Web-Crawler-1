from urllib.parse import parse_qsl

query = 'name=germy&age=22'
print(parse_qsl(query))