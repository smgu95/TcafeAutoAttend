from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
url = 'http://tcafe2a.com/'
driver.get(url)


id=driver.find_element_by_id('ol_id')
id.send_keys('아이디 입력')
pw=driver.find_element_by_id('ol_pw')
pw.send_keys('패스워드 입력')

loginbutton = driver.find_element_by_tag_name('button')
loginbutton.click()


driver.get(url+'/community/attendance')

driver.find_element_by_xpath('//*[@id="cnftjr"]/div/form/table/tbody/tr/td/img').click()

