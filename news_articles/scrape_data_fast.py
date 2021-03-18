from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import pandas as pd
import os
import numpy as np
##proxy_list = ["107.189.13.143:3199", "196.16.230.16:3199", "104.233.54.105:3199", "104.249.3.167:3199", "181.177.65.16:3199"]


keyword = "kodak"
    
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
    
url = 'https://www.bloomberg.com/search?query={}'.format(keyword)
browser.visit(url)

##input("press enter")

headline_list = []
publish_date_list = []
author_list = []
eyebrow_list = []
link_list = []


rotate_num = int(2)
ranger_num = 10
for x in range(ranger_num):
    print(str((int(x)/int(ranger_num))*100)+"% Completed")
    rotate_num = rotate_num + int(10)
    
    try:
        browser.find_by_xpath('//*[@id="root"]/div/section[2]/div[3]/div['+str(rotate_num)+']/button').click()
    except:
        input('Error')
        browser.find_by_xpath('//*[@id="root"]/div/section[2]/div[3]/div['+str(rotate_num)+']/button').click()

    time.sleep(1.5)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)
    
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

headlines = soup.find_all('a', {'class': re.compile(r'^headline')})

publish_dates = soup.find_all('div', {'class': re.compile(r'^publishedAt')})
authors = soup.find_all('div', {'class': re.compile(r'^authors')})

eyebrows = soup.find_all('div', {'class': re.compile(r'^eyebrow')})




for headline in headlines:
##        print('page:', x, '-------------')
##        print(headline.text)
    headline_list.append(headline.text)
##        print(headline.get('href'))
    link_list.append(headline.get('href'))

for publish_date in publish_dates:
##        print(publish_date.text)
    publish_date_list.append(publish_date.text)
    
for author in authors:
##        print(author.text)
    author_list.append(author.text)

for eyebrow in eyebrows:
##        print(eyebrow.text)
    eyebrow_list.append(eyebrow.text)
    


columns = ["Date", "Headline", "Author", "Eyebrow", "Link"]
news_articles_df = pd.DataFrame(list(zip(publish_date_list, headline_list,
                                             author_list, eyebrow_list, link_list)), columns = columns)

news_articles_df.to_csv("raw_download/headline_scrape_to_page_{}.csv".format(keyword))


browser.quit()








