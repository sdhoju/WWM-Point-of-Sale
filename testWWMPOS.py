# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:57:35 2018

@author: Sameer
"""


from typing import List

from shoppingcart      import ShoppingCartABC,Item
from shopping_cart_list import ShoppingCartList

def testShoppingCart(cart: ShoppingCartABC[Item], items: List[Item]) -> None:
    def print_cart_test(items)->None:
        print()
        print(f"Show me the cart.\n{cart}\n")
        print(f"Is cart empty? \n{cart.is_empty()}")
        print(f"How many items in cart? \n{cart.cardinality()}")

        for item in items:
            print(f"Is {item.name} in cart? \n{cart.has(item)}" )
            print(f"How many {item.name} in cart? \n{cart.count(item)}")

#     
        print()
    
    print_cart_test(items)    
    
    for i in items:
        '''Add item'''
        cart.add_item(i)
        print(f"Add {i.name} in cart")
        print_cart_test(items)
  

    for i in items:
        '''Add item'''
        cart.add_item(i)
        print(f"Add {i.name} in cart")
        print_cart_test(items)
        
        
    for i in items:
        '''Remove item 2 times'''
        cart.remove_item(i)
        cart.remove_item(i)
        print(f"Remove {i.name} from cart")
        print_cart_test(items)


# Function run_all_tests executes testCookieJar on the various
# implementations of CookieJar.

def run_all_tests() -> None:
    print("\nBegin Shopping Cart test.\n")
    item0 = Item(687123,'2.6','Apple')
    item1 = Item(787879,'2','Mango')
    item2 = Item(887123,'10','Chicken')

    
    test_items: List[Item.name] = [item0,item1,item2]
    cart: ShoppingCartABC[Item]

    print("Begin testShoppingCart test.\n")
    cart = ShoppingCartList[Item]()
    
    print("cart = ShoppingCartList[Item]()")
    testShoppingCart(cart, test_items)
    print("End ShoppingCartList test.\n")
    
if __name__ == '__main__':
    run_all_tests()