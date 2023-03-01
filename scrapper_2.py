from selenium import webdriver
from bs4 import BeautifulSoup

import time
import csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser   = webdriver.Chrome("chromedriver.exe")

browser.get(START_URL)
time.sleep(10)

headers       = ["vmag" , 'proper_name' , 'bayer_designation' , 'disttance_ly' , 'spectral_class' , 'mass' , 'radius' , 'lunimosity']
star_data     = []
new_star_data = []

def scrape():
    for i in range(0, 98):

        soup = BeautifulSoup(browser.page_source, "html.parser")

        for tl_tag in soup.find_all("td", attrs={"class", "bright_star"}):
            td_tags = tl_tag.find_all("td")
            temp_list = []
            for index, li_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tags.find_all("a")[0].contents[0])

def scrape_more_data(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content , "html.parser")
    for tr_tag in soup.find_all("tr" , attrs = {"class" : "fact_row"}):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div" , attrs = {"class" : "value"})[0].contents[0])
                
            
            except:
                temp_list.append("")

        new_star_data.app(temp_list)

scrape()
for data in star_data:
    scrape_more_data(data[5])

final_star_data = []
for index , data in enumerate(star_data):
    final_star_data.append(data + new_star_data[index])

    with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_star_data)
