

def add_Order(orderList):
    print("Nume:", end="")
    clientName=input()
    print("Order:", end="")
    clientOrder=input()
    if int(orderList[-1][0])<=998:
        clientNumber=str(int(orderList[-1][0])+1)
    else:
        clientNumber="000"
    client=[clientNumber, clientName, clientOrder]
    orderList.append(client)
    return orderList

def show_orders(orderList, stockList, ingredients):
    something=["milk", "coffee", "water", "caramel", "vanilla"]
    list_of_drinks=["latte", "caramel_latte" , "americano", "capuccino"]
    ordersAndIngredientsList=[]
    for line in orderList:
        print(f"Order number: {line[0]}    Client name: {line[1]}")
        order=line[2].split(";")
        contor=1
        for item in order:
            
            if item not in list_of_drinks:
                item_quantity=search_in_table(stockList, item)
                if int(item_quantity)>=1:
                    print(f"{contor}. {item} - in stock")
                else:
                    print(f"{contor}. {item} - not in stock")
            else:
                print(f"{contor}. {item} " )
                for dictionary in ingredients:
                    if dictionary["name"]==item:
                        for ing in something:
                            if dictionary[ing]!="0":
                                print(f" - x{dictionary[ing]} {ing}", end="")
                                item_quantity=search_in_table(stockList,ing)
                                if ing=="milk" or ing=="water":
                                    if int(dictionary[ing])*50<=int(item_quantity):
                                        print(f" - {int(dictionary[ing])*50}ml - in stock")
                                    else:
                                         print(f" - {int(dictionary[ing])*50}ml - not in stock")
                                else:
                                    if int(dictionary[ing])*10<=int(item_quantity):
                                        print(f" - {int(dictionary[ing])*10}g - in stock")
                                    else:
                                         print(f" - {int(dictionary[ing])*10}g - not in stock")
                                #print(" ")
            contor+=1
        print(" ")
            
def search_in_table(List, item):
    for line in List:
        if item in line:
            quantity=line[2]
            return quantity
    else:
        return "0"