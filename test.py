from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('https://passport.liepin.com/h/account/?default=1')
driver.implicitly_wait(5)
pnum = driver.find_element_by_xpath('//div[@class="ui-tab-toggle loginforphonecode"]//div[@class="account"]//input[@class]')
pnum.send_keys('15603057947')
inp_cap = input('Input CAPTCHA:')
captcha = driver.find_element_by_xpath('//div[@class="valid-code"]/input')
captcha.send_keys(inp_cap)
button = driver.find_element_by_xpath('//div[@class="clearfix"]/a')
button.click()
inp_pcap = input('Input phone CAPTCHA:')
pcap = driver.find_element_by_xpath('//div[@class="clearfix"]/input')
pcap.send_keys(inp_pcap)
log_button = driver.find_element_by_xpath('//div[@class="actions"]/input')
log_button.click()

driver.refresh()
cookies = driver.get_cookies()
print(cookies)

