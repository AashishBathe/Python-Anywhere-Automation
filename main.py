from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
service = Service('C:\development\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=opt)

username = os.environ.get('Pyanyuser')  # Saved as env var
password = os.environ.get('Pyanypass')  # Saved as env var

driver.get('https://www.pythonanywhere.com/login/?next=/')
time.sleep(1)
name = driver.find_element(By.NAME, 'auth-username')
name.send_keys(username)
passw = driver.find_element(By.NAME, 'auth-password')
passw.send_keys(password)
login_button = driver.find_element(By.ID, 'id_next')
login_button.click()
time.sleep(2)
tasks_button = driver.find_element(By.ID, 'id_tasks_link')
tasks_button.click()
time.sleep(1)
extend_button = driver.find_element(By.XPATH, '//*[@id="id_scheduled_tasks_table"]/div/div/table/tbody/tr/td[6]/button[4]')
extend_button.click()
driver.quit()
