import requests

url = 'http://localhost:8050/render.jpeg?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('j.jpg', 'wb') as f:
    f.write(response.content)