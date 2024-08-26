import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#imports

driver = webdriver.Chrome()

sources = []
list_roles = []
joblist = []

start_date = time.strftime("2024-08-20")

workbook = openpyxl.Workbook()
sheet = workbook.active

with open('sources.txt', 'r') as file:
  for line in file:
    sources.append(line.strip())
    
with open('roles.txt', 'r') as file:
  for line in file:
    list_roles.append(line.strip())
    

for role in list_roles:
  current_tab = workbook.create_sheet(role)
  
  for source in sources:
    url = f"https://www.google.com/search?q=site:{source}+%22{role}%22+%22remote%22+-%22remote+in+the+US%22+%22brazil\"+after:{start_date}"
    driver.get(url)
    input("Please complete the CAPTCHA and then press Enter to continue...")
    result_content = driver.find_elements(By.CSS_SELECTOR, '#search div > div h3')
    if(result_content):
      for position in result_content:
        job_title = position.text
        job_url = position.find_element(By.XPATH, '..').get_attribute('href')
        current_tab.append([job_title, job_url])

if 'Sheet' in workbook.sheetnames:
  workbook.remove(workbook['Sheet'])
workbook.save('jobs.xlsx')