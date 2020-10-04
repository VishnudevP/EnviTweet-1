import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

with open("marshallislands.csv", "w") as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(["Quote by climate refugee: "])
  driver.get("https://mashable.com/2018/02/25/marshall-islands-climate-refugees/")
  x = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/article/div/div[21]/div/p[2]').text
  print(x)
  csv_writer.writerow([x])
csvfile.close()
