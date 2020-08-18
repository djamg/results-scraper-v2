from soup import loaded
from soup import resultCheck
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time


op = webdriver.ChromeOptions()
op.add_argument('headless')
op.page_load_strategy = 'eager'
op.add_argument('--log-level=3')

driver = webdriver.Chrome(options=op)
driver.get("http://results.drait.in/")

# select student
student = driver.find_element_by_xpath('//*[@id="myDIV"]/button[3]')
student.click()
time.sleep(1)  # seconds
usn = input("Enter you USN: ")

# select from dropdown
searchButton = driver.find_element_by_xpath('//*[@id="ugpg"]/option[2]')
searchButton.click()

# enters the USN
searchbox = driver.find_element_by_xpath("//*[@id='usn']")
searchbox.send_keys(usn)

# submit
submitButton = driver.find_element_by_xpath('//*[@id="submit"]')
submitButton.click()
time.sleep(3.5)  # seconds


# saves the updated page source
url = driver.page_source

loaded(url)

# time.sleep(6)
# driver.quit()
