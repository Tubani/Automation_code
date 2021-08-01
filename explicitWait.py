from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import wait

def type_and_enter(element,text):
    element.send_keys(text + Keys.ENTER)    

Source = "Dhaka (DAC - Shahjalal Intl.)" 
Destination = "New York (NYC - All Airports)"


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.expedia.com/")
print(driver.title)
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="wizardMainRegionV2"]/div/div/div[2]/div/div/ul/li[2]/a/span').click()

driver.find_element(By.XPATH,'//*[@id="uitk-tabs-button-container"]/div[1]/li[2]/a/span').click()

origin = driver.find_element(By.XPATH,'//*[@id="location-field-leg1-origin-menu"]/div[1]/button[1]')
type_and_enter(origin,Source)

destination = driver.find_element(By.XPATH,'//*[@id="location-field-leg1-destination-menu"]/div[1]/button[1]')
type_and_enter(destination, Destination)

date = driver.find_element(By.XPATH,'//*[@id="d1-btn"]')
date.click()
num = driver.find_element(By.XPATH,'//*[@id="wizard-flight-tab-oneway"]/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[7]/button').click()
done = driver.find_element(By.XPATH,'//*[@id="wizard-flight-tab-oneway"]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/button').click()
search = driver.find_element(By.XPATH,'//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()

wait = wait.WebDriverWait(driver,10)
driver.quit()

