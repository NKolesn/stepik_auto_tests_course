from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return int(x) + int(y)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_number = browser.find_element(By.CSS_SELECTOR, "#num1")
    b_number = browser.find_element(By.CSS_SELECTOR, "#num2")
    x = a_number.text
    y = b_number.text
    summ = calc(x, y)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ)) 

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
