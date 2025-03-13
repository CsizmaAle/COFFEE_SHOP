import customtkinter as ctk
#import reading_writing_functions as rwf
#import order_functions as of
#import tkinter as tk
import frame_functions as ff
#import interface as i
#import stock_functions as sf


"""_summary_
it calculates the total quantity of a drink 
"""
def quantity_calculate(drink, ingredientsList):
    totalQuantity=0
    something=["milk", "coffee", "water", "caramel", "vanilla"]
    for dictionary in ingredientsList:
        if dictionary["name"]==drink:
            for ing in something:
                if ing=="water" or ing=="milk":
                    totalQuantity+=int(dictionary[ing])*50
                else:
                    totalQuantity+=int(dictionary[ing])*10
    return totalQuantity


    """_summary_
    deletes a product from the meniu just by recieveng the index of the product and the meniu list
    """
def delete_meniu_product(product_id,meniu):
    index=0
    for line in meniu:
        if line[0]==product_id:
            meniu.pop(index)
            break
        else:
            index+=1
    return meniu


    """_summary_
    changes a price of a product from the meniu just by recieveng the index of the product, the new price and the meniu list
    :parameters: string product_id: the id of the product; list meniu: the list where we will save the change; string product_price: the new price of the product
    :return: meniu: the modified list
    """

def change_price(product_id, meniu, product_price):
    for line in meniu:
        if line[0]==product_id:
            line[3]=product_price
            return meniu

def addProductIngredients(line, ingredientsList):
    dict={
            "name":line[0],
            "milk":line[1],
            "coffee":line[2],
            "water":line[3],
            "caramel":line[4],
            "vanilla": line[5] 
        }
    ingredientsList.append(dict)
    return ingredientsList

def add_meniu_product(name, price, meniu):
    list[0]=str(int(meniu[-1][0])+1)
    list[1]=name
    list[2]=price
    meniu.append(list)
    return meniu

def show_meniu(header, meniu, frame):
    label_meniu = ctk.CTkLabel(frame, text="Meniu info", font=("Arial", 30))
    label_meniu.grid(row=1, column=1, padx=10, pady=20)
    
    for col_index, cell in enumerate(header):
        label = ctk.CTkLabel(frame, text=cell, width=150, anchor="center", font=("Arial", 24))
        label.grid(row=2, column=col_index, padx=5, pady=5)
        
    for row_index, row in enumerate(meniu):
        for col_index, cell in enumerate(row):
            label = ctk.CTkLabel(frame, text=cell, width=150, anchor="center", font=("Arial", 24))
            label.grid(row=row_index+3, column=col_index, padx=5, pady=5)

def on_delete_product(entry, meniu, canvas, frame_content, headerMeniu):
    product_id= entry.get()
    if product_id:  # Verifică dacă s-a introdus un text
        meniu=delete_meniu_product(product_id,meniu)
        entry.delete(0, "end")  # Șterge textul după trimitere
        ff.refresh_menu_frame(frame_content, canvas)
        show_meniu(headerMeniu, meniu, frame_content)
        #rwf.print_table(headerMeniu,meniu)
        
def on_change_price(entry_meniu_id, entry_price, meniu, canvas, frame, headerMeniu):
    product_id=entry_meniu_id.get()
    product_price=entry_price.get()
    if product_id and product_price:  # Verifică dacă s-a introdus un text
        meniu=change_price(product_id,meniu, product_price)
        entry_price.delete(0, "end")  # Șterge textul după trimitere
        entry_meniu_id.delete(0, "end")  # Șterge textul după trimitere
        ff.refresh_menu_frame(frame, canvas) 
        show_meniu(headerMeniu, meniu, frame)
        #rwf.print_table(headerMeniu,meniu)

def on_add_product(entry_add_name, entry_add_price, meniu, outMeniu, stockList):
    pass

    """
    def on_add_product(entry_name, entry_price, entry_weight, frame, headerMeniu,meniuList ):
    name=entry_name.get()
    price=entry_price.get()
    weight=entry_weight.get()
    if name and weight and price:
        meniuList=add_meniu_product(name, price,meniuList)
        meniuList[-1][2]..... trb facut debugg ca nu mai stiu ce si cum arata menuList si quantity stuff
    """


def on_add_drink(entry_add_name, entry_add_price, meniu, outMeniu, stockList):
    pass