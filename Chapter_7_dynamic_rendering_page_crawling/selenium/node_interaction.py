from selenium import webdriver
import time

# 节点交互就是使用selenium，驱动浏览器来执行一些操作
# 让浏览器模拟执行一些操作

browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
    input = browser.find_element_by_id('q')
    input.send_keys('iPhone')
    time.sleep(1)
    input.clear()
    input.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()
    time.sleep(2)
finally:
    browser.close()