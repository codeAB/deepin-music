#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2012 Deepin, Inc.
#               2011 ~ 2012 Hou Shaohui
# 
# Author:     Hou Shaohui <houshao55@gmail.com>
# Maintainer: Hou Shaohui <houshao55@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
from utils import load_db
from xdg_support import get_config_file

class WebcastsDatabase(object):
    
    def __init__(self):
        self.raw_db_file = os.path.join((os.path.dirname(os.path.realpath(__file__))), "data", "webcasts.db")
        self.collect_db_file = get_config_file("collect_webcasts.db")
        self.custom_db_file = get_config_file("custom_webcasts.db")
    
    def load(self):
        try:
            self.raw_db_objs = load_db(self.raw_db_file)
        except:    
            self.raw_db_objs = None
            
        try:    
            self.collect_db_objs = load_db(self.collect_db_file)
        except:    
            self.collect_db_objs =None
            
        try:    
            self.custom_db_objs = load_db(self.custom_db_file)
        except:    
            self.custom_db_objs = None
            
    def get_keys_from_categroy(self, categroy):        
        if not self.raw_db_objs:
            return []
        else:
            return self.raw_db_objs.get(categroy, {}).keys()
        
    def get_items(self, categroy, key):    
        if not self.raw_db_objs:
            return []
        else:
            return self.raw_db_objs.get(categroy, {}).get(key, [])
        
    def get_custom_items(self):    
        if not self.custom_db_objs:
            return []
        return self.custom_db_objs
    
    def get_collect_items(self):
        if not self.collect_db_objs:
            return []
        else:
            return self.collect_db_objs
        
    def is_collect(self, uri):    
        if not self.collect_db_objs:
            return False
        for item  in self.collect_db_objs:
            if uri == item.get("uri", ""):
                return True
            return False
        
    def save(self):    
        pass
        
WebcastsDB = WebcastsDatabase()        
