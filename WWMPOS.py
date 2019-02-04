# -*- coding: utf-8 -*-
"""
Crremove_itemed on Sat Nov  3 15:09:24 2018W
@author: Sameer
"""

from typing import List

from shoppingcart      import ShoppingCartABC,Item
from shopping_cart_list import ShoppingCartList

    
def checkout(cart: ShoppingCartABC[Item]) -> None:
    def print_receipt():
        items=[]
        subtotal:float=0
        tax_rate=0.07
        for i in range(len(cart.cart)):
            items.append(cart.cart[i])
        items=list(set(items))
        
        
        print('\t   Wally World Marketplace')
        print()
        for item in items:
            subtotal+=cart.count(item)*item.price
            print('\t{} ({})..........{}'.format(item.name, cart.count(item) ,cart.count(item)*item.price))
        
        print()
        print(f'\tSubtotal..........{subtotal}')
        print(f'\tTax...............{round(subtotal*tax_rate,2)}')
        print(f'\tTotal.............{subtotal+(subtotal*tax_rate)}')

            
    print(f"Check out complete. Dont forget to take your receipt with you.")
    print_receipt()
    


if __name__ == '__main__':
    
    '''Item with value (IdTag, price, name).'''
    item1 = Item(112312,2,'Mango')
    item2 = Item(223445,10,'Chicken')
    item3 = Item(312343,4,'Water')
    item4 = Item(434504,2.3,'Milk')
    item5 = Item(509734,1.5,'Coca Cola')
    item6 = Item(690823,20,'Rice')
    item7 = Item(723445,4.3,'Egges')
    item8 = Item(823453,4.6,'Banana')
    item9 = Item(923454,6.6,'Shrimp')  
    item10 = Item(103333,.6,'Apple')
    
    '''Database with 10 items. It could changed to any format in future.'''
    items: List[Item] = [item1,item2,item3,item4,item5,item6,item7,item8,item9,item10]
    cart: ShoppingCartABC[Item]
    cart = ShoppingCartList[Item]()
    
    
    '''Point of sale'''
    print()
    print('\tWelcome to Wally World Marketplace\n')
    print('Select the item you want to add to Cart or anything else to checkout')
    for x in range(len(items)):
        print(f'{x+1}.{items[x].name} ${items[x].price} ')
    i = input("-> ")   

    while i.isdigit() and int(i)<=10 and int(i)>0 :
        cart.add_item(items[int(i)-1])
        print(f'{items[int(i)-1].name} added to cart')
        print('Select the item you want to add to Cart or anything else to checkout')
        for x in range(len(items)):
            print(f'\t{x+1}.{items[x].name} ${items[x].price} ')
        i = input("-> ")
#    print(cart)
    checkout(cart)
    
    print()
    print('You are a valued customer. Thank you for shopping with us. ')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    