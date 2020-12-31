# Selenium tutorial #1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
PATH = '/Users/user/Desktop/selenium/chromedriver'
driver = webdriver.Chrome(PATH)
# open browser
driver.get('https://tenshoku.mynavi.jp/')
print(driver.title)
time.sleep(3)
# close popup
try:
  driver.execute_script('document.querySelector(".karte-close").click()')
  time.sleep(3)
# close popup
  driver.execute_script('document.querySelector(".karte-close").click()')
except:
# go to next process if error and exception
  pass
# get element search box's name
search_box = driver.find_element_by_name('srFreeSearchKeyword')
# input keyboard process
search_box.send_keys('未経験')
# get element search button's class
search_btn = driver.find_element_by_class_name('js__searchRecruitTop')
# push search button return
search_btn.send_keys(Keys.RETURN)
#############until here home work 2-1####################
try:
    cassetteRecruit__main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cassetteRecruit__main"))
    )

    # articles = cassetteRecruit__main.find_elements_by_class_name("tableCondition")
    # for tableCondition in articles:
    #   t_head = articles.find_elements_by_class_name('tableCondition')
    #   print(tableCondition.text)

finally:
    driver.quit()