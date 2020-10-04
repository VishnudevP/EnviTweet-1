import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

with open("modi.csv", "w") as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(["Quote by prime minister Modi of India: "])
  driver.get("https://quotefancy.com/quote/1619575/Narendra-Modi-We-the-present-generation-have-the-responsibility-to-act-as-a-trustee-of")
  x = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/div/div[1]/h1').text
  print(x)
  csv_writer.writerow([x])
csvfile.close()
