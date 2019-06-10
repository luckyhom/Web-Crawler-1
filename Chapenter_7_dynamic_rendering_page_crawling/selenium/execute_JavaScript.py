from selenium import webdriver

# 下拉进度条使用execute_script()方法即可实现

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert(("To Bottom")')
browser.close()