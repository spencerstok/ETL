from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import pandas as pd
import os
import numpy as np
import glob
import requests

import json
import time
import requests
import pandas as pd
from selenium import webdriver
from requests.auth import HTTPBasicAuth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import tkinter as tk
##proxy_list = ["107.189.13.143:3199", "196.16.230.16:3199", "104.233.54.105:3199", "104.249.3.167:3199", "181.177.65.16:3199"]
##
##
##username = "sp99f49bfc"
##password = "Yung$avage2"
##
##
##url = "https://whatismyipaddress.com/"
##
##PROXY = f'http://user-sp99f49bfc-sessionduration-10:Developer1*@gate.smartproxy.com:10000'
##opts = Options()
##opts.add_argument("--start-maximized")
##opts.add_argument('--proxy-server=http://%s' % PROXY)
##opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
##driver_path = "chromedriver.exe"
##
##driver = webdriver.Chrome(executable_path=driver_path, options=opts)
##driver.get(url)




##//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[151]/button
##//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[200]/button
##
##
##//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]


for filepath in glob.glob("initial_filter/*.csv"):
    
    control_df = pd.read_csv(filepath)
##    print(control_df)
    control_df['Timestamp'] = ''
    control_df['Contents'] = '' 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    for x in range(len(control_df)):
        try:
            time.sleep(1)
            html2 = browser.html
            soup2 = BeautifulSoup(html2, 'html.parser')
            warning = soup.find('h2', {'class': re.compile(r'^main__heading')})
            if "detected unusual activity" in str(warning.text):
                input("Solve Captcga to continue")
            else:
                input("Check Error Code")
        except:
            pass
        
        print(str((int(x)/(len(control_df)))*100)+"%")
        
        url = control_df["Link"].iat[x]
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        try:
            timestamp = soup.find('time', {'class': re.compile(r'^article-timestamp')})
##            print(timestamp.text)
            middle_column = soup.find('div', {'class': re.compile(r'^middle-column')})
##            print(middle_column.text)
            control_df["Timestamp"].iat[x] = timestamp.text
            control_df["Contents"].iat[x] = middle_column.text
        except:
            
                
            control_df["Timestamp"].iat[x] = "Other_Media"
            control_df["Contents"].iat[x] = "Other_Media"
##            pass
        

        newfilepath = str(filepath).replace("initial_filter", "secondary_filter")
        control_df.to_csv(newfilepath)
##
##        
##
##
##
##
####input("press enter")
##
####headline_list = []
####publish_date_list = []
####author_list = []
####eyebrow_list = []
####link_list = []
####
####
####rotate_num = int(2)
####ranger_num = 10
####for x in range(ranger_num):
####    print(str((int(x)/int(ranger_num))*100)+"% Completed")
####    rotate_num = rotate_num + int(10)
####    
####    try:
####        browser.find_by_xpath('//*[@id="root"]/div/section[2]/div[3]/div['+str(rotate_num)+']/button').click()
####    except:
####        input('Error')
####        browser.find_by_xpath('//*[@id="root"]/div/section[2]/div[3]/div['+str(rotate_num)+']/button').click()
####
####    time.sleep(1.5)
####
####    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
####
####    time.sleep(2)
####    
####html = browser.html
####soup = BeautifulSoup(html, 'html.parser')
####
####headlines = soup.find_all('a', {'class': re.compile(r'^headline')})
####
####publish_dates = soup.find_all('div', {'class': re.compile(r'^publishedAt')})
####authors = soup.find_all('div', {'class': re.compile(r'^authors')})
####
####eyebrows = soup.find_all('div', {'class': re.compile(r'^eyebrow')})
####
####
####
####
####for headline in headlines:
######        print('page:', x, '-------------')
######        print(headline.text)
####    headline_list.append(headline.text)
######        print(headline.get('href'))
####    link_list.append(headline.get('href'))
####
####for publish_date in publish_dates:
######        print(publish_date.text)
####    publish_date_list.append(publish_date.text)
####    
####for author in authors:
######        print(author.text)
####    author_list.append(author.text)
####
####for eyebrow in eyebrows:
######        print(eyebrow.text)
####    eyebrow_list.append(eyebrow.text)
####    
####
####
####columns = ["Date", "Headline", "Author", "Eyebrow", "Link"]
####news_articles_df = pd.DataFrame(list(zip(publish_date_list, headline_list,
####                                             author_list, eyebrow_list, link_list)), columns = columns)
####
####news_articles_df.to_csv("raw_download/headline_scrape_to_page_{}.csv".format(keyword))
####
####
####browser.quit()
####
####
####
####
####
####
####
####
####
##
