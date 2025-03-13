import customtkinter as ctk
import reading_writing_functions as rwf
import order_functions as of
import stock_functions as sf
import order_functionsV2 as of2
import meniu_functions as mf
import tkinter as tk
import frame_functions as ff

new_order=[]
new_order_items=[]

ordersFile=open("orders_out.csv","r" )
stockFile=open("stock_out.csv", "r")
ingredientsFile=open("ingredients.csv","r")
meniuFile=open("meniu_out.csv","r")

ordersList=[]
stockList=[]
ingredientsList=[]
meniu=[]

headerStock=[]
headerOrders=[]
headerIngredients=[]
headerMeniu=[]
    
headerOrders, ordersList = rwf.readingFile(ordersFile)
headerStock, stockList = rwf.readingFile(stockFile)
headerIngredients, ingredientsList= rwf.readingIngr(ingredientsFile)
headerMeniu, meniu=rwf.read_meniu(meniuFile, ingredientsList)

outOrders=open("orders_out.csv", "w+", newline='')
outStock=open("stock_out.csv", "w+", newline='')
outMeniu=open("meniu_out.csv", "w", newline="")
outIngredients=open("ingredients_out.csv", "w", newline="")


rwf.print_stock(headerStock, stockList)
of.show_orders(ordersList, stockList, ingredientsList)
rwf.print_table(headerMeniu, meniu)



# Configurare inițială
ctk.set_appearance_mode("Light")  # Mod luminos
ctk.set_default_color_theme("blue")  # Temă

# Crearea ferestrei principale
app = ctk.CTk()
app.title("Coffee Shop")

# Setarea ferestrei să fie maximizată (fullscreen-like cu controale)
app.geometry("800x600")  # Default size before maximizing
app.after(100, lambda: app.state("zoomed"))  # Maximize the window after launch

# Funcția pentru a minimiza fereastra
def minimize_app():
    app.iconify()

# Funcția pentru a afișa un anumit cadru


# Crearea cadrelor (paginilor)
frame_home = ctk.CTkFrame(app, width=800, height=600)
frame_view = ctk.CTkFrame(app, width=800, height=600)
frame_view_orders=ctk.CTkFrame(app, width=800, height=600)
frame_add_orders=ctk.CTkFrame(app, width=800, height=600)
frame_view_meniu=ctk.CTkFrame(app, width=800, height=600)
frame_add_product=ctk.CTkFrame(app, width=800, height=600)

for frame in (frame_home, frame_view, frame_view_orders,frame_add_orders, frame_view_meniu, frame_add_product):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    

frame = ctk.CTkFrame(frame_home)
frame.grid(pady=20, padx=20, sticky="nsew") 

frame_home.grid_columnconfigure(0, weight=1)
frame_home.grid_columnconfigure(1, weight=1)
frame_home.grid_columnconfigure(2, weight=1)
frame_home.grid_columnconfigure(3, weight=1)
frame_home.grid_columnconfigure(4, weight=1)

# Pagina principală (Home)
label_home = ctk.CTkLabel(frame_home, text="     https:\\\\", font=("Arial", 63))
label_home.grid(row=0, column=1, pady=10, sticky="ew")
label_home = ctk.CTkLabel(frame_home, text="COFFEE_", font=("Arial", 63))
label_home.grid(row=0, column=2,pady=10, sticky="ew")
label_home = ctk.CTkLabel(frame_home, text="SHOP.ru  ", font=("Arial",63))
label_home.grid(row=0, column=3, pady=10, sticky="ew")

label_home = ctk.CTkLabel(frame_home, text="STOCK", font=("Arial", 24))
label_home.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
button_1 = ctk.CTkButton(frame_home, text="Show Stock", width=300, height=100, command=lambda: ff.show_frame(frame_view))
button_1.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

label_home = ctk.CTkLabel(frame_home, text="ORDERS", font=("Arial", 24))
label_home.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
button_3 = ctk.CTkButton(frame_home, text="Show orders",width=300, height=100, command=lambda: ff.show_and_refresh(frame_view_orders, canvas, frame_scrollable, ordersList, stockList, ingredientsList))
button_3.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
button_4 = ctk.CTkButton(frame_home, text="Add order",width=300, height=100, command=lambda: ff.show_frame(frame_add_orders))
button_4.grid(row=4, column=1, padx=10,  pady=10, sticky="ew")

label_home = ctk.CTkLabel(frame_home, text="MENU", font=("Arial", 24))
label_home.grid(row=3, column=3, padx=10, pady=10, sticky="ew")
button_8 = ctk.CTkButton(frame_home, text="Show menu",width=300, height=100, command=lambda: ff.show_frame(frame_view_meniu))
button_8.grid(row=4, column=3, padx=10, pady=10, sticky="ew")

label_home = ctk.CTkLabel(frame_home, text="TOTALS", font=("Arial", 24))
label_home.grid(row=1, column=3, padx=10, pady=10, sticky="ew")
button_12 = ctk.CTkButton(frame_home, text="View day",width=300, height=100, command=lambda: ff.show_frame(frame_view))
button_12.grid(row=2, column=3, padx=10, pady=10, sticky="ew")
button_13 = ctk.CTkButton(frame_home, text="End day", width=300, height=100,command=lambda: ff.show_frame(frame_view))
button_13.grid(row=2, column=4, padx=10, pady=10, sticky="ew")


# frame view stock
sf.show_stock_frame(frame_view, stockList, headerStock, frame_home)

#frame view orderds

# Crearea unui canvas și a unui scrollbar personalizat
canvas = ctk.CTkCanvas(frame_view_orders, bg="white", width=1600, height=800)
canvas.grid(row=0, column=0, columnspan=8, sticky="nsew")

scrollbar = ctk.CTkScrollbar(frame_view_orders, orientation="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=8, sticky="ns")

# Configurarea canvas-ului pentru a răspunde la scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Crearea unui cadru pe canvas pentru a adăuga widget-uri
frame_scrollable = ctk.CTkFrame(canvas, width=1600, height=800)  # Conținutul care va fi derulabil

# Plasarea acestui cadru pe canvas
canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")

# Funcția pentru scroll folosind mouse-ul
def on_mouse_scroll(event):
    if event.delta:  # Pentru Windows și Linux
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    
# Legarea evenimentelor de scroll
canvas.bind_all("<MouseWheel>", on_mouse_scroll)  # Pentru Windows și MacOS


frame_view_orders.grid_columnconfigure(0, weight=1)
frame_view_orders.grid_columnconfigure(1, weight=1)
frame_view_orders.grid_columnconfigure(2, weight=1)
frame_view_orders.grid_columnconfigure(3, weight=1)
frame_view_orders.grid_columnconfigure(4, weight=1)
frame_view_orders.grid_columnconfigure(5, weight=1)
frame_view_orders.grid_columnconfigure(6, weight=1)
frame_view_orders.grid_columnconfigure(7, weight=1)

label_view = ctk.CTkLabel(frame_scrollable, text="Orders info", font=("Arial", 30))
label_view.grid(row=1, column=0, padx=10, pady=20)

of2.show_orders( ordersList, stockList, ingredientsList, frame_scrollable)

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Legarea evenimentului de configurare a frame-ului
frame_scrollable.bind("<Configure>", on_frame_configure)


button_back_insert = ctk.CTkButton(frame_view_orders, text="Înapoi", width=300, height=100, command=lambda: ff.show_frame(frame_home))
button_back_insert.grid(row=1, column=0, padx=10, pady=20, sticky="ew")

entry_order_id = ctk.CTkEntry(frame_view_orders, width=200, height=40, placeholder_text="Enter order ID")
entry_order_id.grid(row=2, column=2, padx=10, pady=20)

button_5 = ctk.CTkButton(frame_view_orders, text="Complete order", width=300, height=100,command=lambda: of2.on_complete_order(entry_order_id, canvas, frame_scrollable,ordersList, stockList, ingredientsList, headerStock ))
button_5.grid(row=1, column=2, padx=10, pady=20, sticky="ew")

button_7 = ctk.CTkButton(frame_view_orders, text="Delete order",width=300, height=100, command=lambda: of2.on_delete_order(entry_order_delete_id, canvas, frame_scrollable, ordersList, stockList, ingredientsList))
button_7.grid(row=1, column=4, padx=10, pady=20, sticky="ew")

entry_order_delete_id = ctk.CTkEntry(frame_view_orders, width=200, height=40, placeholder_text="Enter order ID")
entry_order_delete_id.grid(row=2, column=4, padx=10, pady=20)


# frame_add_orders 

frame_add_orders.grid_columnconfigure(0, weight=1)
frame_add_orders.grid_columnconfigure(1, weight=1)
frame_add_orders.grid_columnconfigure(2, weight=1)
frame_add_orders.grid_columnconfigure(3, weight=1)
frame_add_orders.grid_columnconfigure(4, weight=1)
frame_add_orders.grid_columnconfigure(5, weight=1)
frame_add_orders.grid_columnconfigure(6, weight=1)
frame_add_orders.grid_columnconfigure(7, weight=1)


button_back_view = ctk.CTkButton(frame_add_orders, text="BACK", command=lambda: ff.show_and_refresh(frame_view_orders, canvas, frame_scrollable, ordersList, stockList, ingredientsList))
button_back_view.grid(row=6, column=1, padx=10, pady=30)

entry_name = ctk.CTkEntry(frame_add_orders, width=200, height=40, placeholder_text="Enter name")
entry_name.grid(row=1, column=1, padx=10, pady=20)

button_latte = ctk.CTkButton(frame_add_orders, text="LATTE",width=300, height=100, command=lambda: new_order_items.append( "latte"))
button_latte.grid(row=2, column=1, padx=10, pady=20, sticky="ew")

button_caramel_latte = ctk.CTkButton(frame_add_orders, text="CARAMEL LATTE",width=300, height=100, command=lambda: new_order_items.append("caramel_latte"))
button_caramel_latte.grid(row=2, column=2, padx=10, pady=20, sticky="ew")

button_americano = ctk.CTkButton(frame_add_orders, text="AMERICANO",width=300, height=100, command=lambda:new_order_items.append("americano"))
button_americano.grid(row=3, column=2, padx=10, pady=20, sticky="ew")

button_capuccino = ctk.CTkButton(frame_add_orders, text="CAPUCCINO",width=300, height=100, command=lambda: new_order_items.append("capuccino"))
button_capuccino.grid(row=3, column=1, padx=10, pady=20, sticky="ew")

button_cookie = ctk.CTkButton(frame_add_orders, text="COOKIE",width=300, height=100, command=lambda: new_order_items.append("cookie"))
button_cookie.grid(row=4, column=2, padx=10, pady=20, sticky="ew")

button_finish_adding_order = ctk.CTkButton(frame_add_orders, text="FINISH",width=300, height=100, command=lambda: of2.on_order_add(entry_name, ordersList, new_order_items))
button_finish_adding_order.grid(row=5, column=2, padx=10, pady=20, sticky="ew")
# Setarea cadrului inițial (Home)
ff.show_frame(frame_home)

# frame view meniu

frame_view_meniu.grid_columnconfigure(0, weight=1)
frame_view_meniu.grid_columnconfigure(1, weight=1)
frame_view_meniu.grid_columnconfigure(2, weight=1)
frame_view_meniu.grid_columnconfigure(3, weight=1)
frame_view_meniu.grid_columnconfigure(4, weight=1)
frame_view_meniu.grid_columnconfigure(5, weight=1)

# Crearea unui canvas și a unui scrollbar personalizat
canvas2 = ctk.CTkCanvas(frame_view_meniu, bg="white", width=1400, height=600)
canvas2.grid(row=0, column=0, columnspan=8, sticky="nsew")

scrollbar2 = ctk.CTkScrollbar(frame_view_meniu, orientation="vertical", command=canvas2.yview)
scrollbar2.grid(row=0, column=8, sticky="ns")

canvas2.configure(yscrollcommand=scrollbar2.set)

# Crearea unui cadru pe canvas pentru a adăuga widget-uri
frame_scrollable2 = tk.Frame(canvas2)
canvas_window = canvas2.create_window((0, 0), window=frame_scrollable2, anchor="nw")

# Funcția pentru scroll folosind mouse-ul
def on_mouse_scroll2(event):
    canvas2.yview_scroll(-1 * (event.delta // 120), "units")

canvas2.bind("<MouseWheel>", on_mouse_scroll2)  # Pentru Windows/MacOS

# Adăugarea conținutului


mf.show_meniu(headerMeniu, meniu, frame_scrollable2)
rows=0

def on_frame_configure2(event):
    canvas2.configure(scrollregion=canvas2.bbox("all"))
    canvas2.itemconfig(canvas_window, width=canvas2.winfo_width())  # Ajustează lățimea frame-ului scrollabil
    canvas2.itemconfig(canvas_window, height=canvas2.winfo_height())  # Ajustează lățimea frame-ului scrollabil

frame_scrollable2.bind("<Configure>", on_frame_configure2)

# Actualizare dimensiuni după adăugarea widget-urilor
canvas2.update_idletasks()
canvas2.configure(scrollregion=canvas2.bbox("all"))
    



button_back_view = ctk.CTkButton(frame_view_meniu, text="Înapoi", command=lambda: ff.show_frame(frame_home))
button_back_view.grid(row=rows+8, column=2, padx=10, pady=30)

button_9 = ctk.CTkButton(frame_view_meniu, text="Change price", width=300, height=100,command=lambda: mf.on_change_price(entry_meniu_id, entry_price, meniu, canvas2, frame_scrollable2,headerMeniu))
button_9.grid(row=rows+6, column=1, padx=10, pady=10, sticky="ew")
entry_meniu_id = ctk.CTkEntry(frame_view_meniu, width=200, height=40, placeholder_text="Enter product number")
entry_meniu_id.grid(row=rows+7, column=1, padx=10, pady=20)
entry_price = ctk.CTkEntry(frame_view_meniu, width=200, height=40, placeholder_text="Enter new price")
entry_price.grid(row=rows+8, column=1, padx=10, pady=20)


button_10 = ctk.CTkButton(frame_view_meniu, text="Add product",width=300, height=100, command=lambda: ff.show_frame(frame_add_product))
button_10.grid(row=rows+6, column=2, padx=10, pady=10, sticky="ew")

button_100 = ctk.CTkButton(frame_view_meniu, text="Add drink",width=300, height=100, command=lambda: ff.show_frame(frame_add_product))
button_100.grid(row=rows+7, column=2, padx=10, pady=10, sticky="ew")

button_11 = ctk.CTkButton(frame_view_meniu, text="Delete product",width=300, height=100, command=lambda: mf.on_delete_product(entry_delete_meniu, meniu, canvas2, frame_scrollable2, headerMeniu))
button_11.grid(row=rows+6, column=3, padx=10, pady=10, sticky="ew")
entry_delete_meniu = ctk.CTkEntry(frame_view_meniu, width=200, height=40, placeholder_text="Enter product number")
entry_delete_meniu.grid(row=rows+7, column=3, padx=10, pady=20)


#frame_add_product

    

    
button_back_view = ctk.CTkButton(frame_add_product, text="Înapoi", command=lambda: ff.show_frame(frame_view_meniu))
button_back_view.grid(row=8, column=2, padx=10, pady=30)

label_add_name = ctk.CTkLabel(frame_add_product, text=" Product name:", font=("Arial", 20))
label_add_name.grid(row=1, column=3, pady=10, sticky="ew")

entry_add_name = ctk.CTkEntry(frame_add_product, width=200, height=40, placeholder_text="Enter product number")
entry_add_name.grid(row=3, column=3, padx=10, pady=20)

label_add_price = ctk.CTkLabel(frame_add_product, text=" Product price (RON):", font=("Arial", 20))
label_add_price.grid(row=1, column=4, pady=10, sticky="ew")

entry_add_price = ctk.CTkEntry(frame_add_product, width=200, height=40, placeholder_text="Enter product number")
entry_add_price.grid(row=3, column=4, padx=10, pady=20)


button_15 = ctk.CTkButton(frame_add_product, text="Add product", command=lambda: mf.on_add_product(entry_add_name, entry_add_price, meniu, outMeniu, stockList))
button_15.grid(row=5, column=4, padx=10, pady=20)


# frame add drink
button_14 = ctk.CTkButton(frame_add_product, text="Add drink", command=lambda: mf.on_add_drink(entry_add_name, entry_add_price, meniu, outMeniu))
button_14.grid(row=5, column=4, padx=10, pady=20)

# Rularea aplicației


app.mainloop()

rwf.writingFiles(outOrders, headerOrders, ordersList)
rwf.writingFiles(outStock, headerStock, stockList)
rwf.writingFiles(outMeniu, headerMeniu, meniu)