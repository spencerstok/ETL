from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import pandas as pd
import os
import numpy as np
import glob



for file in glob.glob("raw_download/*.csv"):
    df = pd.read_csv(file)
    print(file)
    #Initial filter to only include 2021 this will reduce our scrape load
    filt1_df = df[df["Date"].str.contains("2021")]
    print(str(len(df) - len(filt1_df)) + " Outside Dates Removed")

    
##    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
##    start_date = '01-25-2021'
##    end_date = '03-17-2021'
##
##    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
##
##    df = df.loc[mask]
##
    oldlen = len(df)
    df.drop_duplicates(subset="Link", keep='last', inplace=True)
    print(str(oldlen - len(df)) + " Duplicates Removed")

    

    

    filename_stripped = str(file).replace("raw_download\\", "")

    

    df.to_csv("initial_filter/{}".format(filename_stripped), index=False)

    
