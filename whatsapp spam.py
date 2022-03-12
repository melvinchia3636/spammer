from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

target = '"your target"'
string = r"Hey I'll spam u with this till ur WhatsApp is out of it's brains"
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

for i in range(1000):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(string)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

