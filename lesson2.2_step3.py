from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def summa(x, y):
    x = int(x)
    y = int(y)
    sum1 = x + y
    return str(sum1)

link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link)

find_number_one = browser.find_element(By.ID, 'num1')
find_number_two = browser.find_element(By.ID, 'num2')
numberOne = find_number_one.text
numberTwo = find_number_two.text

sumNumber = summa(numberOne, numberTwo)

selectList = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
selectList.select_by_value(f'{sumNumber}')

buttonSubmit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
buttonSubmit.click()

time.sleep(5)
browser.quit()
