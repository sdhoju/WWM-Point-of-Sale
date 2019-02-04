# Wally World Marketplace Point of Sale 

Wally World Marketplace point of sale project is the stimulation of check out in a market place. 
It is a class Project for Multiparadigm Programming in Python.


## Authors

* **Sameer Dhoju** - *author* - [sdhoju](https://github.com/sdhoju)


## Built With

* [Python 3](https://www.python.org/downloads/) - an interpreted, high-level, general-purpose programming language


## Getting Started

Clone this repository by 
```
git clone https://github.com/sdhoju/WWM-Point-of-Sale.git
```

### Prerequisites

Python 3. Check Python version by running following command.
```
python --version
```

### Running

The runner file is WWMPOS.py. You can start the program by following code or clicking run in IDE.

```
python WWMPOS.py
```

OUTPUT in Spyder IDE is as follows
```
Welcome to Wally World Marketplace
Select the item you want to add to Cart or anything else to checkout
1.Mango $2 
2.Chicken $10 
3.Water $4 
4.Milk $2.3 
5.Coca Cola $1.5 
6.Rice $20 
7.Egges $4.3 
8.Banana $4.6 
9.Shrimp $6.6 
10.Apple $0.6 
-> 1
Mango added to cart
Select the item you want to add to Cart or anything else to checkout
        1.Mango $2 
        2.Chicken $10 
        3.Water $4 
        4.Milk $2.3 
        5.Coca Cola $1.5 
        6.Rice $20 
        7.Egges $4.3 
        8.Banana $4.6 
        9.Shrimp $6.6 
        10.Apple $0.6 
-> 2
Chicken added to cart
Select the item you want to add to Cart or anything else to checkout
        1.Mango $2 
        2.Chicken $10 
        3.Water $4 
        4.Milk $2.3 
        5.Coca Cola $1.5 
        6.Rice $20 
        7.Egges $4.3 
        8.Banana $4.6 
        9.Shrimp $6.6 
        10.Apple $0.6 
-> a
Check out complete. Don’t forget to take your receipt with you.
          		 Wally World Marketplace
        Chicken (1)..........10
        Mango (1)…..........2

        Subtotal................12
        Tax.....................0.84
        Total................12.84
You are a valued customer. Thank you for shopping with us.

```




## Running the tests

Tests are included in testWWMPOS.py. If you are using an IDE you can simply run it. You can also run the test by following command.
```
python testWWMPOS.py
``` 

### Break down into end to end tests

The test contains 3 times. Each item is added to the shopping cart and each step are outputted.
```
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
```
### Test

```
Begin testShoppingCart test.

cart = ShoppingCartList[Item]()

Show me the cart.
ShoppingCartList(cart=[])

Is cart empty?
True
How many items in cart?
0
Is Apple in cart?
False
How many Apple in cart?
0
Is Mango in cart?
False
How many Mango in cart?
0
Is Chicken in cart?
False
How many Chicken in cart?
0

Add Apple in cart

Show me the cart.
ShoppingCartList(cart=[<item.Item object at 0x00000284A5C14B70>])

Is cart empty?
False
How many items in cart?
1
Is Apple in cart?
True
How many Apple in cart?
1
Is Mango in cart?
False
How many Mango in cart?
0
Is Chicken in cart?
False
How many Chicken in cart?
0

Remove Apple from cart

Is cart empty?
True
How many items in cart?
0
Is Apple in cart?
False
How many Apple in cart?
0
Is Mango in cart?
False
How many Mango in cart?
0
Is Chicken in cart?
False
How many Chicken in cart?
0

End ShoppingCartList test.
```

