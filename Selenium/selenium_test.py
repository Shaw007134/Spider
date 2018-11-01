from selenium import webdriver
import os

chromedriver = "./chromedriver"
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.quit()