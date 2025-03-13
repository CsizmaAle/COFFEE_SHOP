import customtkinter as ctk
import reading_writing_functions as rwf
#import order_functions as of
#import order_functionsV2 as of2
#import meniu_functions as mf
#import tkinter as tk
import frame_functions as ff
#import interface as i


def add_Stock(stockList, item):
    for line in stockList:
        if line[1]==item:
            print(f"{line[1]} old quantity: {line[2]}")
            print("New quantity:", end="") 
            new_quantity=input()
            line[2]=new_quantity
            print(f"Quantyty {line[1]} old quantity: {line[2]}")

def change_stock(new_quantity, stockList, item):
    for line in stockList:
        if line[1]==item:
            line[2]=new_quantity
            
def changeStock(entry_id, entry_q, stockList):
    for line in stockList:
        if line[0]==entry_id:
            line[2]=entry_q

def on_change_stock(stockList, entry_id, entry_q, frame_view, headerStock, frame_home):
    entry_stock_id = entry_id.get()
    entry_quantity=entry_q.get()
    rows=0
    if entry_id and entry_q:  # Verifică dacă s-a introdus un text
        changeStock(entry_stock_id, entry_quantity, stockList)
        entry_id.delete(0, "end")  # Șterge textul după trimitere
        entry_q.delete(0, "end")
        ff.refresh_frame(frame_view)
        #rwf.print_stock(header=headerStock, List=stockList)
        show_stock_frame(frame_view, stockList, headerStock, frame_home)


def show_stock_frame(frame_view, stockList, headerStock, frame_home):
    label_view = ctk.CTkLabel(frame_view, text="Stock info", font=("Arial", 30))
    label_view.grid(row=1, column=1, padx=10, pady=20)

    for col_index, cell in enumerate(headerStock):
            label = ctk.CTkLabel(frame_view, text=cell, width=150, anchor="center", font=("Arial", 24))
            label.grid(row=2, column=col_index, padx=5, pady=5)
            
    for row_index, row in enumerate(stockList):
        for col_index, cell in enumerate(row):
            label = ctk.CTkLabel(frame_view, text=cell, width=150, anchor="center", font=("Arial", 24))
            label.grid(row=row_index+3, column=col_index, padx=5, pady=5)  
            rows=row_index
            
    button_back_view = ctk.CTkButton(frame_view, text="Înapoi", width=200, height=50, command=lambda: ff.show_frame(frame_home))
    button_back_view.grid(row=rows+5, column=2, padx=10, pady=30)
    button_2 = ctk.CTkButton(frame_view, text="Modify Stock", width=200, height=50,command=lambda: on_change_stock(stockList, entry_stock_no_id,entry_stock_quantity, frame_view, headerStock, frame_home))
    button_2.grid(row=rows+5, column=0, padx=10, pady=10, sticky="ew")

    entry_stock_no_id = ctk.CTkEntry(frame_view, width=200, height=40, placeholder_text="Enter stock ID")
    entry_stock_no_id.grid(row=rows+6, column=0, padx=10, pady=20)

    entry_stock_quantity=ctk.CTkEntry(frame_view, width=200, height=40, placeholder_text="Enter new quantity")
    entry_stock_quantity.grid(row=rows+7, column=0, padx=10, pady=20)