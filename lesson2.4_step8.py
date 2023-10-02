from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

priceCheck = WebDriverWait(browser, 12).until(
    expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
buttonBook = browser.find_element(By.ID, 'book').click()

number = browser.find_element(By.XPATH, '//span[@id="input_value"]')
x = calc(int(number.text))

inputPole = browser.find_element(By.ID, 'answer')
inputPole.send_keys(x)

buttonSubmit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
buttonSubmit.click()

time.sleep(5)
browser.quit()
