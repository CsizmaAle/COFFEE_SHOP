import customtkinter as ctk
import stock_functions as stkf
import reading_writing_functions as rwf
import order_functions as of
#import meniu_functions as mf
#import tkinter as tk
import frame_functions as ff
#import interface as i

def show_orders(orderList, stockList, ingredients, frame):
    something=["milk", "coffee", "water", "caramel", "vanilla"]
    list_of_drinks=["latte", "caramel_latte" , "americano", "capuccino"]
    #ordersAndIngredientsList=[]
    row_index=3
    col_index=0
    for line in orderList:
        for i in range(0,6):
            label=ctk.CTkLabel(frame, text="***************************", width=150, anchor="center", font=("Arial", 24))
            label.grid(row=row_index, column=i, padx=1, pady=20)
        row_index+=1
        #order_details["number"]=line[0]
        #order_details["name"]=line[1]
        #print(f"Order number: {line[0]}    Client name: {line[1]}")
        col_index=0
        label=ctk.CTkLabel(frame, text=f"Number: {line[0]}", width=150, anchor="center", font=("Arial", 24))
        label.grid(row=row_index, column=col_index, padx=5, pady=5)
        col_index+=1
        label=ctk.CTkLabel(frame, text=f"Name: {line[1]}", width=150, anchor="center", font=("Arial", 24))
        label.grid(row=row_index, column=col_index, padx=5, pady=5)
        
        order=line[2].split(";")
        contor=1
        for item in order:
            row_index+=1
            col_index=1
            
            label=ctk.CTkLabel(frame, text=f"{str(contor)}. {item}", width=150, anchor="center", font=("Arial", 24))
            label.grid(row=row_index, column=col_index, padx=5, pady=5)
            col_index+=1
            item_quantity=search_in_table(stockList, item)
            if item not in list_of_drinks:    
                if int(item_quantity)>=1:    
                    label=ctk.CTkLabel(frame, text="-in stock", width=150, anchor="center", font=("Arial", 24))
                    label.grid(row=row_index, column=col_index, padx=5, pady=5)
                    #print(f"{contor}. {item} - in stock")
                else:
                    label=ctk.CTkLabel(frame, text="-not in stock", width=150, anchor="center", font=("Arial", 24))
                    label.grid(row=row_index, column=col_index, padx=5, pady=5)
                    #print(f"{contor}. {item} - not in stock")
            else:
                #print(f"{contor}. {item} " )
                for dictionary in ingredients:
                    
                    if dictionary["name"]==item:
                        for ing in something:
                            if dictionary[ing]!="0":
                                row_index+=1
                                col_index=2
                                label=ctk.CTkLabel(frame, text=f" - x{dictionary[ing]} {ing}", width=150, anchor="center", font=("Arial", 24))
                                label.grid(row=row_index, column=col_index, padx=5, pady=5)
                                col_index+=1
                                #print(f" - x{dictionary[ing]} {ing}", end="")
                                item_quantity=search_in_table(stockList,ing)
                                if ing=="milk" or ing=="water":
                                    label=ctk.CTkLabel(frame, text=f" - {int(dictionary[ing])*50}ml", width=150, anchor="center", font=("Arial", 24))
                                    label.grid(row=row_index, column=col_index, padx=5, pady=5)
                                    col_index+=1
                                    if int(dictionary[ing])*50<=int(item_quantity):
                                        label=ctk.CTkLabel(frame, text=" - in stock", width=150, anchor="center", font=("Arial", 24))
                                        label.grid(row=row_index, column=col_index, padx=5, pady=5)
                                        #print(f" - {int(dictionary[ing])*50}ml - in stock")
                                    else:
                                        label=ctk.CTkLabel(frame, text=" - not in stock", width=150, anchor="center", font=("Arial", 24))
                                        label.grid(row=row_index, column=col_index, padx=5, pady=5)
                                        #print(f" - {int(dictionary[ing])*50}ml - not in stock")
                                else:
                                    label=ctk.CTkLabel(frame, text=f" - {int(dictionary[ing])*10}g", width=150, anchor="center", font=("Arial", 24))
                                    label.grid(row=row_index, column=col_index, padx=5, pady=5)
                                    col_index+=1
                                    if int(dictionary[ing])*10<=int(item_quantity):
                                        label=ctk.CTkLabel(frame, text=" - in stock", width=150, anchor="center", font=("Arial", 24))
                                        label.grid(row=row_index, column=col_index, padx=5, pady=5)
                                        #print(f" - {int(dictionary[ing])*10}g - in stock")
                                    else:
                                        label=ctk.CTkLabel(frame, text=" - not in stock", width=150, anchor="center", font=("Arial", 24))
                                        label.grid(row=row_index, column=col_index, padx=5, pady=5)
                                         # print(f" - {int(dictionary[ing])*10}g - not in stock")
                                #print(" ")
            contor+=1
        row_index+=1
            
def search_in_table(List, item):
    for line in List:
        if item in line:
            quantity=line[2]
            return quantity
    else:
        return "0"



def delete_order(line, orderList, stockList, ingredients,index):
    something=["milk", "coffee", "water", "caramel", "vanilla"]
    list_of_drinks=["latte", "caramel_latte" , "americano", "capuccino"]
    order=line[2].split(";")
    for item in order:
        item_quantity=search_in_table(stockList, item)
        if item not in list_of_drinks:    
            if int(item_quantity)>=1:    
                stkf.change_stock(str(int(item_quantity)-1),stockList, item)
        else:
            for dictionary in ingredients: 
                if dictionary["name"]==item:
                    possibleComplet=True
                    for ing in something:
                        if dictionary[ing]!="0" and possibleComplet==True:
                            item_quantity=search_in_table(stockList,ing)
                            if ing=="milk" or ing=="water":
                                if int(dictionary[ing])*50<=int(item_quantity):
                                    stkf.change_stock(str(int(item_quantity)-(int(dictionary[ing])*50)),stockList, ing)
                                else:
                                    possibleComplet=False                                        
                            else:
                                if int(dictionary[ing])*10<=int(item_quantity):
                                     stkf.change_stock(str(int(item_quantity)-(int(dictionary[ing])*10)),stockList,ing)
                                else:
                                    possibleComplet=False
    orderList.pop(index)
    

def completed_order(orderList, stockList, ingredients, nr):
    index=0
    for line in orderList:
        if nr==line[0]:
            delete_order(line, orderList, stockList, ingredients,index)
        else:
            index+=1


def delete_order_fr(ordersList,order_id):
    index=0
    for line in ordersList:
        if order_id==line[0]:
           ordersList.pop(index)
        else:
            index+=1

def create_new_order(order_name, orderList,clientinfo):
    line=orderList[-1]
    if int(line[0])<=998:
        clientNumber=str(int(orderList[-1][0])+1)
    else:
        clientNumber="000"
    clientinfo=[clientNumber, order_name]
    return clientinfo

def add_to_order( item, orders):
    if orders!="":
        orders=orders+';'+item
    else:
        orders=item

def on_complete_order(entry, canvas, frame_content,ordersList, stockList, ingredientsList, headerStock):
    order_id = entry.get()
    if order_id:  # Verifică dacă s-a introdus un text
        completed_order(ordersList, stockList, ingredientsList,order_id)
        entry.delete(0, "end")  # Șterge textul după trimitere
        ff.refresh_canvas(canvas, frame_content,ordersList, stockList, ingredientsList)  # Dă refresh la frame
        of.show_orders(orderList=ordersList, stockList=stockList, ingredients=ingredientsList)
        rwf.print_stock(header=headerStock, List=stockList)

def on_delete_order(entry, canvas, frame_content,ordersList, stockList, ingredientsList):
    order_id = entry.get()
    if order_id:  # Verifică dacă s-a introdus un text
        delete_order_fr(ordersList,order_id)
        entry.delete(0, "end")  # Șterge textul după trimitere
        ff.refresh_canvas(canvas, frame_content,ordersList, stockList, ingredientsList)  # Dă refresh la frame
        of.show_orders(orderList=ordersList, stockList=stockList, ingredients=ingredientsList)

def on_order_add(entry,ordersList, new_order_items):
    order_name= entry.get()
    if order_name:  # Verifică dacă s-a introdus un text
        new_order=[]
        
        new_order=create_new_order(order_name, ordersList,new_order)
        entry.delete(0, "end")  # Șterge textul după trimitere
        
        orders_string=";".join(new_order_items)
        new_order.append(orders_string)
        ordersList.append(new_order)
        
        new_order=[]
        new_order_items=""