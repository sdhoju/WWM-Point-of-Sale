# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:59:09 2018

@author: Sameer Dhoju
"""

from typing      import List, Generic, TypeVar
from dataclasses import dataclass, field  # 3.7

from shoppingcart import ShoppingCartABC,ItemType,Item

@dataclass
class ShoppingCartList(ShoppingCartABC,Generic[ItemType]):
    cart: List[Item] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        '''Add  "item" into this shopping cart'''
        self.cart.append(item)
    
    
    def remove_item(self, item: Item) -> None:
        '''Remove "item" from this shopping cart'''
        if item in self.cart:
            self.cart.remove(item)
        else:
            print(f"Error: No item of type {item} in cart")

    def is_empty(self) -> bool:
        '''Is this cart  empty?'''
        return len(self.cart) == 0

    def has(self, item: Item) -> bool:
        '''Is "item" in this cart?'''
        return item in self.cart

    def count(self, item: Item) -> int:
        '''How many instances of "item" in cart?'''

        return len([i for i in self.cart if i == item])

    def cardinality(self) -> int:
        '''How many items in cart?'''
        return len(self.cart)