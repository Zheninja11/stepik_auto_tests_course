from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.XPATH, '//button[text()="I want to go on a magical journey!"]').click()

alert_confirm = browser.switch_to.alert.accept()

number = browser.find_element(By.XPATH, '//span[@id="input_value"]')
x = calc(int(number.text))

inputPole = browser.find_element(By.ID, 'answer')
inputPole.send_keys(x)

buttonSubmit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
buttonSubmit.click()

time.sleep(5)
browser.quit()
