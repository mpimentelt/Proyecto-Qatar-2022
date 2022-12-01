from tabulate import tabulate

def vip_average_consumption(vip_clients):
    if not len(vip_clients) == 0:
        acum = 0
        for client in vip_clients:
            acum += client.consumption
        print("The average consumption of vip clients was: ", {acum/len(vip_clients)})
    else:
        print("There are no vip clients.")

def partition_match(lista):
    menores = []
    mayores = []
    medio = lista[0]
    for i in range(len(lista)):
        if lista[i].assistance < medio.assistance:
            menores.append(lista[i])
        elif lista[i].assistance > medio.assistance:
            mayores.append(lista[i])
    return menores, medio, mayores

def quick_sort_match(lista):
    if len(lista)<2:
        return lista
    menor,medio,mayor = partition_match(lista)
    print(menor,medio,mayor)
    return quick_sort_match(menor) + [medio] + quick_sort_match(mayor)

def match_assistance(matches):
    matches = quick_sort_match(matches)
    data = []
    column_headers = ["Teams playing", "Stadium ID", "Sold Tickets", "Amount of assistants", "Assistance/Sale"]
    for match in matches: 
        data.append([f"{match.home_team} vs {match.away_team}", match.stadium, match.sold_tickets, match.assistance, match.sold_tickets//match.assistance])
    print(tabulate(data, headers=column_headers))
    print(f"\n")
    print("The match with the most assistance was: ")
    matches[len(matches)-1].show()

def match_sold_tickets(matches):
    aux = 0
    match_most_tickets = 0
    for match in matches:
        if match.sold_tickets > aux:
            aux = match.sold_tickets()
            match_most_tickets = match
    print("The match with the most sold tickets was: ")
    match_most_tickets.show()

def partition_products(lista):
    menores = []
    mayores = []
    medio = lista[0]
    for i in range(len(lista)):
        if lista[i].quantity < medio.quantity:
            menores.append(lista[i])
        elif lista[i].quantity > medio.quantity:
            mayores.append(lista[i])
    return menores, medio, mayores

def quick_sort_products(lista):
    if len(lista)<2:
        return lista
    menor,medio,mayor = partition_products(lista)
    print(menor,medio,mayor)
    return quick_sort_products(menor) + [medio] + quick_sort_products(mayor)

def sold_product(stadiums):
    products = []
    for stadium in stadiums:
        for restaurant in stadium.restaurants:
            for product in restaurant.products:
                products.append(product)
    products = quick_sort_products(products)
    print("Top 3 Products Sold")
    print("1.")
    print("------------------------------------")
    products[len(products)-1].show()
    print("====================================")
    print("2.")
    print("------------------------------------")
    products[len(products)-2].show()
    print("====================================")
    print("3.")
    print("------------------------------------")
    products[len(products)-3].show()
    print("====================================")
    
def partition_clients(lista):
    menores = []
    mayores = []
    medio = lista[0]
    for i in range(len(lista)):
        if len(lista[i].tickets) < len(medio.tickets):
            menores.append(lista[i])
        elif len(lista[i].tickets) > len(medio.tickets):
            mayores.append(lista[i])
    return menores, medio, mayores

def quick_sort_clients(lista):
    if len(lista)<2:
        return lista
    menor,medio,mayor = partition_clients(lista)
    print(menor,medio,mayor)
    return quick_sort_clients(menor) + [medio] + quick_sort_clients(mayor)

def top_clients(general,vip):
    clients = []
    for client in general:
        clients.append(client)
    for client in vip:
        clients.append(client)
    clients = quick_sort_clients(clients)
    print("Top 3 Clients")
    print("1.")
    print("------------------------------------")
    clients[len(clients)-1].show()
    print("====================================")
    print("2.")
    print("------------------------------------")
    clients[len(clients)-2].show()
    print("====================================")
    print("3.")
    print("------------------------------------")
    clients[len(clients)-3].show()
    print("====================================")