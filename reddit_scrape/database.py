# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import glob
import os
import pandas as pd

##
##path = "initial_filter//"
##
##all_files = glob.glob(os.path.join(path, "*.csv"))
##
##all_df = []
##for f in all_files:
##    df = pd.read_csv(f, sep=',')
##    df['file'] = f.split('/')[-1]
##    all_df.append(df)
##    
##merged_df = pd.concat(all_df, ignore_index=True, sort=True)
##
##
##merged_df.to_csv("databaseupload//merged_news_scrape.csv")
##
##

##path = "stock_dfs//"
##
##all_files = glob.glob(os.path.join(path, "*.csv"))
##
##all_df = []
##for f in all_files:
##    df = pd.read_csv(f, sep=',')
##    df['file'] = f.split('/')[-1]
##    all_df.append(df)
##    
##merged_df = pd.concat(all_df, ignore_index=True, sort=True)
##
##
##merged_df.to_csv("databaseupload//merged_redditt_scrape.csv")


path = "Comb//"

all_files = glob.glob(os.path.join(path, "*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_df = pd.concat(all_df, ignore_index=True, sort=True)


merged_df.to_csv("databaseupload//merged_stock_data.csv")


# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


db = client.stock_info
collection = db.news
