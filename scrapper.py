from selenium import webdriver
from bs4 import BeautifulSoup

import time 
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser   = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")

browser.get(START_URL)
time.sleep(10)

def scrape():
    headers   = ["vmag" , 'proper_name' , 'bayer_designation' , 'disttance_ly' , 'spectral_class' , 'mass' , 'radius' , 'lunimosity']
    star_data = []
    for i in range(0,98):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for tl_tags in soup.find_all('td' , attrs={"class", "brightstar"}):
            temp_list = []
            for index, li_tag in enumerate(tl_tags):
                if index == 0:
                    temp_list.append(tl_tags.find_all("a")[0].contents[0])
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()