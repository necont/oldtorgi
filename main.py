from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

for year in years:
    if year % 4 == 0:
        months_dict = {'01': '31', '02': '29', '03': '31', '04': '30',
                       '05': '31', '06': '30', '07': '31', '08': '31',
                       '09': '30', '10': '31', '11': '30', '12': '31'}
    else:
        months_dict = {'01': '31', '02': '28', '03': '31', '04': '30',
                       '05': '31', '06': '30', '07': '31', '08': '31',
                       '09': '30', '10': '31', '11': '30', '12': '31'}
    for month in months_dict:
        link = f'http://old.torgi.gov.ru/opendata/7710349494-torgi/data-2-{str(year)}{month}01T0000-{str(year)}{month}{months_dict[month]}T0000-structure-20130401T0000.xml'
        try:
            driver.get(link)
            print(1)
            time.sleep(3)
            print(11)
            try:
                r = driver.page_source
                # print(21)
                # print(r)
                # soup = BeautifulSoup(r, 'lxml.parser')
                # print(2)
                # data = ET.tostring(str(soup))
                # print(3)
                myfile = open(f'{str(year)}{month}', 'w')
                print(4)
                myfile.write(r)

            except:
                print('Eror2')
        except:
            print('Eror1')
