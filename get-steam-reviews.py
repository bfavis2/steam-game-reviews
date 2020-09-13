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

class steam_api():
    
    def __init__(self, appid, filter_=None, language=None, day_range=None,cursor=None,
                review_type=None, purchase_type=None, num_per_page=None):
        self.filter_ = filter_
        self.language = language
        self.day_range = day_range
        self.cursor = cursor
        self.review_type = review_type
        self.purchase_type = purchase_type
        self.num_per_page = num_per_page
        self.appid = appid
        
    def parse_data(self):
        pass
    
    def call_api(self):
        pass
    
    def set_parameters(self, **kwargs):
        pass
    
    def get_appid(self, product):
        pass
    
    def build_request(self):
        pass
        
    
    
        

steam_api = 'https://store.steampowered.com/appreviews/'

