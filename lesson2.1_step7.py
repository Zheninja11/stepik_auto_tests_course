from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

valuex = browser.find_element(By.ID, 'treasure')
xChecked = valuex.get_attribute("valuex")

x = calc(xChecked)

inputX = browser.find_element(By.ID, 'answer')
inputX.send_keys(x)

checkboxRobot = browser.find_element(By.ID, 'robotCheckbox')
checkboxRobot.click()

radioButtonRobot = browser.find_element(By.ID, 'robotsRule')
radioButtonRobot.click()

buttonSubmit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
buttonSubmit.click()

time.sleep(5)
browser.quit()
