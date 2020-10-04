import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

with open("trump.csv", "w") as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(["Quote by president Trump of USA: "])
  driver.get("https://www.msnbc.com/rachel-maddow-show/trumps-approach-the-climate-crisis-gets-even-more-embarrassing-msna1203751")
  y = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div/div/article/div/div[2]/div[1]/div/section/blockquote/p').text
  print(y)
  csv_writer.writerow([y])
csvfile.close()
