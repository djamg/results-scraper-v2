from bs4 import BeautifulSoup

from soup import loaded
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

heading = ["Subject", "Credits", "CIE 1", "CIE 1 Attendance", "CIE 2", "CIE 2 Attendance",
           "CIE M", "Final Attendance", "Assignment", "Group Activity", "Final CIE", "SEE Grade"]

driver = webdriver.Chrome()
driver.get("http://results.drait.in/")

# select student
student = driver.find_element_by_xpath('//*[@id="myDIV"]/button[3]')
student.click()
time.sleep(1)

# select from dropdown
searchButton = driver.find_element_by_xpath('//*[@id="ugpg"]/option[2]')
searchButton.click()

# enters the USN
searchbox = driver.find_element_by_xpath("//*[@id='usn']")
searchbox.send_keys("1da17im006")

# submit
submitButton = driver.find_element_by_xpath('//*[@id="submit"]')
submitButton.click()

time.sleep(4)

# saves the updated page source
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
selectionForSoup = soup.select('tbody tr')
print(selectionForSoup)

for head in soup.select('thead tr'):
    row_text = [x.text for x in head.find_all('th')]
    print(', '.join(row_text))


for row in soup.select('tbody tr'):
    row_text = [x.text for x in row.find_all('td')]
    print(', '.join(row_text))
