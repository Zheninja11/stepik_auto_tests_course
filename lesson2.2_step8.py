from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

inputList1 = browser.find_element(By.XPATH, '//*[@placeholder="Enter first name"]')
inputList1.send_keys('Test')

inputList2 = browser.find_element(By.XPATH, '//*[@placeholder="Enter last name"]')
inputList2.send_keys('Test')

inputList3 = browser.find_element(By.XPATH, '//*[@placeholder="Enter email"]')
inputList3.send_keys('Test@test.ru')

fileButton = browser.find_element(By.ID, 'file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
fileButton.send_keys(file_path)

buttonSubmit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
buttonSubmit.click()

time.sleep(5)
browser.quit()
