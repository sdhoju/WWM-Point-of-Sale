# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:59:09 2018

@author: Sameer Dhoju
"""


from typing import Generic, TypeVar

ItemType = TypeVar('ItemType')

class Item(Generic[ItemType]):
    def __init__(self,IdTag:int, price:float , name:str)->None:
        self.IdTag=IdTag
        self.price=price
        self.name=name
        
    def get_name(self)->str:
        return self.name
    
    def get_price(self)->float:
        return self.price
    
    def set_name(self,name)->None:
        self.name =name
    
    def set_price(self,price)->None:
        self.price=price

