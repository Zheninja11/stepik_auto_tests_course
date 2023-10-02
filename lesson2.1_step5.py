from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

xElement = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = xElement.text
y = calc(x)

inputText = browser.find_element(By.XPATH, '//*[@id="answer"]')
inputText.send_keys(y)

checkboxRobot = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
checkboxRobot.click()

radioButtonRobot = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
radioButtonRobot.click()

buttonSubmit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
buttonSubmit.click()

time.sleep(5)
browser.quit()
