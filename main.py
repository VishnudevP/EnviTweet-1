#importing modules needed
import csv
import requests
from bs4 import BeautifulSoup
#URL of website
URL = "https://www.ucsusa.org/resources/each-countrys-share-co2-emissions"
#creating CSV file with certain parameters 
csvfile = open("currentemissions.csv", "w")
csv_writer = csv.writer(csvfile)
csv_writer.writerow(["rank", "country", "emissions"])
#condesing code
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#accessing list of baby names
results = soup.find("tbody")
baby_names = results.find_all("tr")
#going through list, accessing all elements of list
for name in baby_names:
  name_details = name.find_all("td")
  rank = name_details[0].text.strip()
  country = name_details[1].text.strip()
  emissions = name_details[2].text.strip()
#if one of these parameters does not exist, skip it
  if None in (rank, country, emissions):
    continue
#put these parameters into your CSV file
  csv_writer.writerow([rank, country, emissions])
#close your file
csvfile.close()
