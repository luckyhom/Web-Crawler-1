import tesserocr
from PIL import Image

image = Image.open('code.jpg')
result = tesserocr.image_to_text(image)
print(result)
# tesserocr另一个简单的方法，将图片文件转为字符串
print(tesserocr.file_to_text('code.jpg'))
