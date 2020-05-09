import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)    
    answer = browser.find_element_by_id('answer')
    x = browser.find_element_by_id('input_value')
    answer.send_keys(calc(x.text))
    robot_cb = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    robot_cb.click()
    robot_rb = browser.find_element_by_css_selector('[for="robotsRule"]')
    robot_rb.click()
    submit_btn = browser.find_element_by_tag_name('button')
    submit_btn.click()
finally:
    time.sleep(10)
    browser.quit()