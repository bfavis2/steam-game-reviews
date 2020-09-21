#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:17:44 2020

@author: brianf
"""


import json
import pandas as pd
import requests
import pathlib
import json
import time
import csv

class steamAPI():
    
    def __init__(self, appid, filter_='recent', language='english', day_range=None,
                 cursor='*', review_type='all', purchase_type='steam', num_per_page='20'):
        self.filter = filter_
        self.language = language
        self.day_range = day_range
        self.cursor = cursor
        self.review_type = review_type
        self.purchase_type = purchase_type
        self.num_per_page = num_per_page
        self.appid = appid
        
        self.df = [[
                    'index',
                    'appid', 
                    'review',
                    'playtime', 
                    'time_created',
                    'recommend',
                    'liked_votes',
                    'funny_votes',
                    'helpfullness_score',
                    'comment_count'
                    ]]
  
    def get_all_reviews(self, filename):
        total = 0
        batch_size = 100
        json_text = self.make_request().json()
        num_reviews = int(json_text['query_summary']['num_reviews'])
        while json_text['success'] == 1 and num_reviews > 0:
            for review in json_text['reviews']:
                total += 1
                self.parse_json_review(review, total)
                if total % batch_size == 0:
                    self.export_to_csv(filename)
            self.cursor = json_text['cursor']
            print(f'Processed:{total} cursor:{self.cursor})')
            json_text = self.make_request().json()
            num_reviews = int(json_text['query_summary']['num_reviews']) 
        
        self.export_to_csv(filename)
        print(f'Processed and exported {total} reviews')
        return
    
    def parse_json_review(self, review, index):
        new_row = [
                    index,
                    self.appid,
                    review['review'],
                    review['author']['playtime_at_review'],
                    review['timestamp_created'],
                    review['voted_up'],
                    review['votes_up'],
                    review['votes_funny'],
                    review['weighted_vote_score'],
                    review['comment_count']
                    ]
        self.df.append(new_row)
        return
    
    def export_to_csv(self, filename):
        with open(filename, 'a') as f:
            csv_writer = csv.writer(f)
            for row in self.df:
                csv_writer.writerow(row)
        print(f'Successfully wrote {len(self.df)-1} lines to {filename}')      
        self.clear_df()
        return
    
    def clear_df(self):
        self.df = []
        return
        
    def call_api(self):
        pass
    
    def set_parameters(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print('There is no attribute named {}'.format(key))
    
    def get_appid(self, product):
        'http://api.steampowered.com/ISteamApps/GetAppList/v2'
    
    def make_request(self):
        'Builds the request URL and returns a response object'
        start = f'https://store.steampowered.com/appreviews/{self.appid}?json=1'
        params = vars(self).copy()
        params['appid'] = None
        params['df'] = None
        r = requests.get(start, params)
        return r


# s = steamAPI(427520) # Factorio appid
# a = s.get_all_reviews('factorio_20200920.csv')

s = steamAPI(766040) # Gloom appid
a = s.get_all_reviews('gloom_20200920.csv')

