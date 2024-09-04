import openpyxl
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#imports

driver = webdriver.Chrome()

sources = []
list_roles = []
total_vacancies = 0

input_locale = input("Deseja buscar vagas no BR ou Exterior? (br/ext) [Deixe em branco para buscar no Exterior]")

if input_locale == "BR":
  sources_path = "br/sources.txt"
  string_search = "%22remoto%22"
else :
  sources_path = "ext/sources.txt"
  string_search = "%22remote%22+-%22remote+in+the+US%22"

input_start_date = input("Qual a data de início da busca? (AAAA-MM-DD) [Deixe em branco para buscar vagas dos últimos 7 dias]")

if input_start_date != "":
  start_date = input_start_date
else:
  today = datetime.now().date().strftime('%Y-%m-%d')
  start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

workbook = openpyxl.Workbook()
sheet = workbook.active

with open(sources_path, 'r') as file:
  for line in file:
    sources.append(line.strip())
    
with open('roles.txt', 'r') as file:
  for line in file:
    list_roles.append(line.strip())
    

for role in list_roles:
  current_tab = workbook.create_sheet(role)
  
  for source in sources:
    url = f"https://www.google.com/search?q=site:{source}+%22{role}%22+{string_search}+\"+after:{start_date}"
    url_result = driver.get(url)
    if "https://www.google.com/sorry/index" in driver.current_url:
      print("Please complete the CAPTCHA and then press Enter to continue...")
      input()
    else :
      result_content = driver.find_elements(By.CSS_SELECTOR, '#search div > div h3')
      if(result_content):
        for position in result_content:
          job_title = position.text
          job_url = position.find_element(By.XPATH, '..').get_attribute('href')
          current_tab.append([job_title, job_url])
          total_vacancies += 1

if(total_vacancies != 0):
  if 'Sheet' in workbook.sheetnames:
    workbook.remove(workbook['Sheet'])
    workbook.save(f"vagas_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx")
  else :
    print("Nenhuma vaga encontrada")
    driver.quit()