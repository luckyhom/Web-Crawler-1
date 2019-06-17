from selenium import webdriver

browser = webdriver.Chrome()
url = "https://www.zhihu.com/explore"
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
browser.close()

# 获取文本
browser = webdriver.Chrome()
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
browser.close()

# 获取id、位置、标签名和大小
browser = webdriver.Chrome()
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
browser.close()

