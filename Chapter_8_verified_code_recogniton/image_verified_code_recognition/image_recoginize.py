import tesserocr
from PIL import Image

image = Image.open('code1.jpg')
result = tesserocr.image_to_text(image)
print(result)
# 上面的识别结果并不准确，若要加强识别准确度可以采用转灰值、二值化等操作，下面进行二值化处理
# 将图像转化为灰度图像
image = image.convert('L')
image.show()
result = tesserocr.image_to_text(image)
print(result)
# 将图片进行二值化处理
image = image.convert('1')
image.show()
# 自定义二值化阈值
image = Image.open('code1.jpg')
image = image.convert('L')
threshold = 80
table = []
for i in range(256):
    if i < threshold or i > 200:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)
