import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

arquivo_excel = 'C:\\Users\\thaya\\Downloads\\robo\\challenge.xlsx'

df = pd.read_excel(arquivo_excel)

driver = webdriver.Chrome()

url = 'https://www.rpachallenge.com/'
driver.get(url)

start = driver.find_element(By.CSS_SELECTOR, '[class="waves-effect col s12 m12 l12 btn-large uiColorButton"]')
start.click()
time.sleep(2) 



for index, row in df.iterrows():    
    
    FirstName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]')
    FirstName.clear()
    FirstName.send_keys(row['First Name'])
    
    
    LastName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]')
    LastName.clear()
    LastName.send_keys(row['Last Name '])
    
    CompanyName = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]')
    CompanyName.clear()
    CompanyName.send_keys(row['Company Name'])
    
    RoleInComapany = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]')
    RoleInComapany.clear()
    RoleInComapany.send_keys(row['Role in Company'])
    
    Address = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]')
    Address.clear()
    Address.send_keys(row['Address'])
 
    Email = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]')
    Email.clear()
    Email.send_keys(row['Email'])
 
    PhoneNumber = driver.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]')
    PhoneNumber.clear()
    PhoneNumber.send_keys(row['Phone Number'])
 
    time.sleep(3) 
    botao_submit = driver.find_element(By.CSS_SELECTOR, '[class="btn uiColorButton"]')
    botao_submit.click()

    time.sleep(5)

driver.quit()