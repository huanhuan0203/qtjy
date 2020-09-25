# coding: utf-8
from selenium import webdriver
from time import sleep
#引入浏览器启动
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(5)  #停5秒
driver.quit()#关掉driver

