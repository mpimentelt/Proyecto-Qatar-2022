def is_perfecto(number):
    acum = 0
    for x in range(1,number):
        if number%x == 0:
            acum += x
    if acum == number:
        return True
    else: 
        return False

def get_discount(subtotal, id):
    if is_perfecto(id):
        return subtotal*0.15

def validate_client(id, vip_clients):
    for client in vip_clients:
        if client.id == id:
            return True
        continue
    else:
        return False

def get_client(id,vip_clients):
    for client in vip_clients:
        if client.id == id:
            return client

def select_ticket(client):
    for ticket in client.tickets:
        ticket.show()
        print("=====================================================")
    ticket_id = input("Please enter the ticket id: ")
    for ticket in client.tickets:
        if ticket_id == ticket.id and ticket.type == "VIP":
            return ticket
        else:
            select_ticket(client)

def select_restaurant(ticket,stadiums):
    for stadium in stadiums:
        if ticket.stadium == stadium.id:
            for restaurant in stadium.restaurants:
                print(restaurant.name)
    restaurant_name = input("Please enter the name of the restaurant in which you would like to buy: ")
    for stadium in stadiums:
        if ticket.stadium == stadium.id:
            for restaurant in stadium.restaurants:
                if restaurant.name == restaurant_name:
                    return restaurant
    else:
        select_restaurant(ticket,stadiums)

def show_catalog(restaurant):
    for type,product in restaurant.products.items():
        print(type)
        product.show

def print_tentative_invoice(client,purchase):
    subtotal = 0
    for amount, product in purchase:
        print(f"{product.name} ------ {product.price}")
        subtotal += product.price*amount
    discount = get_discount(subtotal,client.id)
    total = subtotal-discount
    print(f'''Subtotal: {subtotal} $
Discount: {discount} $
Total: {total} $''')

def print_invoice(client, purchase):
    print("******** INVOICE ********")
    print("Successful Payment")
    subtotal = 0
    for amount, product in purchase:
        print(f"{product.name} ------ {product.price}")
        subtotal += product.price*amount
    discount = get_discount(subtotal,client.id)
    total = subtotal-discount
    print(f'''Subtotal: {subtotal} $
Discount: {discount} $
Total: {total} $''')
    return total

def check_amount(amount, product):
    if amount<=product.quantity:
        return True

def update_inventory(purchase, restaurant, stadiums):
    for stadium in stadiums:
        if restaurant in stadium.restaurants:
            for product in restaurant.products:
                for quantity,item in purchase.items():
                    if item.name == product.name:
                        product.quantity -= quantity
    return stadiums

def update_consumption(client, total, vip_clients):
    for vipclient in vip_clients:
        if client == vipclient:
            client.consumption += total
    return vip_clients


def buy_product(stadiums, vip_clients):
    id = input("Please enter your id. ")
    if validate_client(id, vip_clients):
        client = get_client(id,vip_clients)
        ticket = select_ticket(client)
        restaurant = select_restaurant(ticket,stadiums)
        show_catalog(restaurant)
        purchase = {}
        while True:
            product_name = input("Please enter the name of the product you would like to buy: ").capitalize()
            amount = input("Please enter the amount of the product you would like to buy: ")
            while not amount.isnumeric():
                amount = input("Please enter the amount of the product you would like to buy: ")
            amount = int(amount)
            for product in restaurant.products:
                if product_name == product.name:
                    if check_amount(amount,product):
                        purchase[amount] = product
                    else:
                        print("There is not enough {} available on the inventory. Please try again.".format(product_name))
                        continue
            if input("Would you like to add another product? N-no or Other-Yes: ").upper() == "N":
                break
            else:
                continue
        print_tentative_invoice(client,purchase)
        total = print_invoice(client, purchase)
        stadiums = update_inventory(purchase, restaurant, stadiums)
        vip_clients = update_consumption(client, total, vip_clients)
    return(stadiums,vip_clients)