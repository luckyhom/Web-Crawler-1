from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

# 访问页面
browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
    print(browser.page_source)
finally:
    browser.close()


# 查找结点
browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
    input_first = browser.find_element_by_id('q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third)
finally:
    browser.close()

# 使用find_element()方法
browser = webdriver.Chrome()
try:
    browser.get("https://www.taobao.com")
    input_first = browser.find_element(By.ID, 'q')
    print('使用find_element()方法')
    print(input_first)
finally:
    browser.close()

# 查找多个节点使用find_elements_xx()方法或find_elements()方法
browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
    print('使用find_elements_by_css_selector()')
    lis = browser.find_elements_by_css_selector('.service-bd li')
    # 等效的写法
    print('使用find_elements()方法')
    lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
    print(lis)
finally:
    browser.close()
