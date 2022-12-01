from classes.restaurant import Restaurant
from classes.product import *

def register_products(products_edd):
    products = {}
    beverages = []
    food = []
    for product in products_edd:
        name = product["name"]
        quantity = product["quantity"]
        price = (product["price"]) + (product["price"])*0,16
        classification = product["type"]
        additional = product["adicional"]
        if classification == "beverages":
            beverages.append(Beverage(name, price, classification, additional))
        else:
            food.append(Food(name,price,classification,additional))
    products["beverages"] = beverages
    products["food"] = food
    return products

def register_restaurants(restaurants_edd):
    restaurants = []
    for restaurant in restaurants_edd:
        name = restaurant["name"]
        products = register_products(restaurant["products"])
        restaurants.append(Restaurant(name,products))
    return restaurants

def search_filter_products(products): 
    option = input("Search by:\n1. Name\n2. Product Type\n3. Price Range\n->")
    if option.isnumeric():
        option = int(option)
        if option == 1:
            search_name_products(products)
        elif option == 2:
            search_type_products(products)
        elif option == 3:
            search_price_products(products)
    print("Please enter a valid value.")
    return search_filter_products()

def search_name_products(products):
    name = input("Please enter the product name: ")
    if name.isalpha():
        name = name.capitalize()
        for product in products:
            if product.name == name:
                product.show()
    else:
        print (f"There are no matches available for {name}")

def search_type_products(products):
    type = input("Please enter the product name: ").lower()
    if type == "beverages":
        print("Beverages")
        print("-----------------------------------------")
        for product in products[type]:
            product.show()
    elif type == "food":
        print("Food")
        print("-----------------------------------------")
        for product in products[type]:
            product.show()
    else:
        print("There are no matches available for that type of product.")

def search_price_products(products):
    num1 = input("Enter the first number for the price range: ")
    while not num1.isnumeric():
        num1 = input("Invalid input. Enter the first number for the price range: ")
    num2 = input("Enter the second number for the price range: ")
    while not num2.isnumeric():
        num2 = input("Invalid input. Enter the second number for the price range: ")
    if num1>num2:
        for product in products:
            if product.price <= num1 and product.price >= num2:
                product.show()
            else:
                print("No products between prices {} and {}.".format(num1,num2))
    elif num1<num2:
        for product in products:
            if product.price >= num1 and product.price <= num2:
                product.show()
            else:
                print("No products between prices {} and {}.".format(num1,num2))
    else:
        for product in products:
            if product.price == num1:
                product.show()
            else:
                print("No products between prices {} and {}.".format(num1,num2))

