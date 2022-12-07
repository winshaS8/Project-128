from bs4 import BeautifulSoup
from selenium import webdriver

from selinium.webdriver.common.by import BY
import timeimport pandas as pd 
import requests

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
page = requests.get()
scraped_data = []


    

soup  = BeautifulSoup(page.text, 'html.parsel')
    
bright_star_table = soup.find_all('ul', attrs = {'class', 'wikitable'})
total_table = len(bright_star_table)
table_rows = bright_star_table[1].find_all('tr')
temp_list = []

for row in table_rows:
   td = row.find_all('td')
   temp_list.append(row)
   

   
headers = ['Star_name','Distance','Mass','Radius','Luminosity']
planet_df_1 = pd.DataFrame(planets_data, columns=headers)
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")    

