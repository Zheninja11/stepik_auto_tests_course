from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

number = browser.find_element(By.ID, 'input_value').text
y = calc(number)

browser.execute_script("window.scrollBy(0, 150);")

inputPole = browser.find_element(By.ID, 'answer')
inputPole.send_keys(y)

checkboxRobot = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
checkboxRobot.click()

radioButtonRobot = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
radioButtonRobot.click()

buttonSubmit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
buttonSubmit.click()

time.sleep(5)
browser.quit()
