import customtkinter as ctk
#import order_functions as of
#import stock_functions as sf
import order_functionsV2 as of2
#import meniu_functions as mf
#import tkinter as tk
#import interface as i

def show_frame(frame):
    frame.tkraise()  # Aduce cadrul în față
    print(f"Switching to frame: {frame}")

def show_and_refresh(frame, canvas, canvas_frame, ordersList, stockList, ingredientsList):
    show_frame(frame) 
    refresh_canvas(canvas, canvas_frame, ordersList, stockList, ingredientsList)
    
def refresh_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()  # Remove existing widgets
    

def refresh_canvas(canvas, frame_scrollable,ordersList, stockList, ingredientsList):
    # Șterge conținutul actual al canvas-ului
    for widget in frame_scrollable.winfo_children():
        widget.destroy()

    # Poți repopula canvas-ul cu date noi aici (dacă e nevoie)
    label_view = ctk.CTkLabel(frame_scrollable, text="Orders info", font=("Arial", 30))
    label_view.grid(row=1, column=0, padx=10, pady=20)
    
    of2.show_orders(
    orderList=ordersList, 
    stockList=stockList, 
    ingredients=ingredientsList, 
    frame=frame_scrollable
)

    # Actualizează zona scrollabilă
    frame_scrollable.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    
def refresh_menu_frame(frame_scrollable, canvas):
    # Șterge conținutul actual al canvas-ului
    for widget in frame_scrollable.winfo_children():
        widget.destroy()
     # Actualizează zona scrollabilă
    frame_scrollable.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))