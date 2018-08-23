from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)
driver.get('http://www.baidu.com/')
title = driver.title
print(title)