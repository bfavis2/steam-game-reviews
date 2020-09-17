#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:17:44 2020

@author: brianf
"""


import json
import requests
import pathlib
import json
import time

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
        
    def parse_data(self):
        total = 0
        json_text = self.make_request().json()
        while json_text['success'] == 1:
            num_reviews = int(json_text['query_summary']['num_reviews'])
            for _ in range(num_reviews):
                total += 1
            self.cursor = json_text['cursor']
            json_text = self.make_request().json()
            
        return total
            
    
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
        r = requests.get(start, params)
        return r


s = steamAPI(427520) # Factorio appid
a = s.parse_data()

