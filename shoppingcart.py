# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:59:09 2018

@author: Sameer Dhoju
"""

from typing import Generic
from abc    import ABC, abstractmethod

from item import ItemType,Item
#abstract base class ShoppingCartABC 
class ShoppingCartABC(ABC,Generic[ItemType]):

    # Mutator method add_item(item) adds item to the shopping cart.   
    @abstractmethod
    def add_item(self, item: Item) -> None:
        pass
  
    # Mutator method eat(item) removes item from the item jar
    # It is called Eat in the Dale and Walker book.
    #
    # PRE:  has(item) 
    # POST: Cart(self') == Cart(self) DIFF {| item |} 

    @abstractmethod
    def remove_item(self, item: Item) -> None:
        pass
        
    # Accessor method is_empty() returns True iff the item jar
    # is empty. It is called IsEmpty in the Dale and Walker book.
    #
    # PRE:   True
    # POST:  (Result == (Cart(self) == {| |})) &&
    #        (Cart(self') == Cart(self))
    @abstractmethod
    def is_empty(Item) -> bool:
        pass

    # Accessor method has(item) returns True iff item occurs
    # in the cart . 
    
    # PRE:   True
    # POST:  (Result == (item IN Cart(self)))
    #        && (Cart(self') == Cart(self))
    @abstractmethod
    def has(self, item: Item) -> bool:
        pass

    
    
    
    
    
    
    
    
    