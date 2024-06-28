import sqlite3
import tkinter as ck
import customtkinter as tk
from tkinter import messagebox

class IceCreame:
    def __init__(self):
        self.root=tk.CTk()
        # self.root._set_appearance_mode("Light")
        self.root.title("Ice Cream Parlor")
        self.root.geometry("500x600")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        label=tk.CTkLabel(self.root, text="Ice Cream Parlor", font=("Ariel",18))
        label.pack()
        # Connect to database
        self.conn = sqlite3.connect("IceCream.db")
        self.cursor = self.conn.cursor()

        #Creating Tabs View
        self.tabview = tk.CTkTabview(self.root, width=900, height=700)
        self.tabview.pack(padx=20,pady=20)
        self.cursor.execute("SELECT * FROM Varieties WHERE season = 'Summer'")
        summer_varieties = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM Varieties WHERE season = 'Rainy'")
        rainy_varieties = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM Varieties WHERE season = 'Winter'")
        winter_varieties = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM Allergy")
        allergies = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM Cart")
        yummies = self.cursor.fetchall()
        # print(yummies)
        #Creating Tabs 
        self.shop_tab = self.tabview.add("Shop")
        self.allergen_tab = self.tabview.add("Allergen")
        self.cart_tab = self.tabview.add("Cart")

        #shopping tab 
        tk.CTkLabel(self.shop_tab, text="Summer Collection!").pack()

        for i, (variety_id, variety_name,season ,allergens) in enumerate(summer_varieties, start=1):
            frame = tk.CTkFrame(self.shop_tab)
            frame.pack(pady=10)

            label = tk.CTkLabel(frame, text=f"{i}. {variety_name},\n{allergens}", font=("Ariel", 12))
            label.pack(side="left", padx=10)

            button = tk.CTkButton(frame, text="Add to cart", command=lambda variety_id=variety_id: self.select_variety(variety_id))
            button.pack(side="right", padx=10)

        tk.CTkLabel(self.shop_tab, text="Monsoon Collection!").pack()

        for i, (variety_id, variety_name,season ,allergens) in enumerate(rainy_varieties, start=1):
            frame = tk.CTkFrame(self.shop_tab)
            frame.pack(pady=10)

            label = tk.CTkLabel(frame, text=f"{i}. {variety_name},\n{allergens}", font=("Ariel", 12))
            label.pack(side="left", padx=10)

            button = tk.CTkButton(frame, text="Add to cart", command=lambda variety_id=variety_id: self.select_variety(variety_id))
            button.pack(side="right", padx=10)

        tk.CTkLabel(self.shop_tab, text="Winter Collection!").pack()

        for i, (variety_id, variety_name,season ,allergens) in enumerate(winter_varieties, start=1):
            frame = tk.CTkFrame(self.shop_tab)
            frame.pack(pady=10)

            label = tk.CTkLabel(frame, text=f"{i}. {variety_name},\n{allergens}", font=("Ariel", 12))
            label.pack(side="left", padx=10)

            button = tk.CTkButton(frame, text="Add to cart", command=lambda variety_id=variety_id: self.select_variety(variety_id))
            button.pack(side="right", padx=10)

        #Allergens tab 
        tk.CTkLabel(self.allergen_tab, text="Our Daily Allergens").pack()

        for i, (id, name, description) in enumerate(allergies, start=1):
            frame = tk.CTkFrame(self.allergen_tab)
            frame.pack(pady=10)

            label = tk.CTkLabel(frame, text=f"{i}. {name},\n{description}", font=("Ariel", 12),wraplength=400)
            label.pack(fill="x", padx=10)
        #Add Allergen 
        tk.CTkLabel(self.allergen_tab, text="\nWould you like to add an allergen").pack()

        label = tk.CTkLabel(self.allergen_tab, text="name: ", font=("Ariel", 12))
        label.place(x=55, y=300)

        name_textbox = tk.CTkTextbox(self.allergen_tab, height=3, width=100, font=("Ariel", 12))
        name_textbox.place(x=120, y=300)

        label = tk.CTkLabel(self.allergen_tab, text="description: ", font=("Ariel", 12))
        label.place(x=55, y=350)

        desc_textbox = tk.CTkTextbox(self.allergen_tab, height=3, width=300, font=("Ariel", 12))
        desc_textbox.place(x=120, y=350)

        def save_allergy():
            name = name_textbox.get("1.0", "end-1c")
            description = desc_textbox.get("1.0", "end-1c")
            self.cursor.execute("INSERT INTO Allergy(name,description)VALUES (?,?)",(name,description))
            self.conn.commit()
            print(f"Saving allergy: {name} - {description}")

        button = tk.CTkButton(self.allergen_tab, text="Save Allergy", command=save_allergy)
        button.place(x=145, y=400)

        self.root.mainloop()
    #Adding values to the cart 
    def select_variety(self, variety_id):
        self.cursor.execute("SELECT * FROM Varieties WHERE id=?", (variety_id,))
        variety_row = self.cursor.fetchone()
        if variety_row:
            variety_id, variety_name, season, allergens = variety_row
            # print(f"Variety Name: {variety_name}, Season: {season}, Allergens: {allergens}")
            self.cursor.execute("SELECT * FROM Cart WHERE iceid=?", (variety_id,))
            cart_row = self.cursor.fetchone()
            if cart_row:
                self.cursor.execute("UPDATE Cart SET quantity = quantity + 1 WHERE iceid=?", (variety_id,))
            else:
                self.cursor.execute("INSERT INTO Cart (iceid, name, quantity) VALUES (?,?,1)",
                            (variety_id, variety_name))
            self.conn.commit()
            self.update_cart_tab()
    #Removing values from the cart 
    def remove_from_cart(self, cart_id):
        self.cursor.execute("SELECT * FROM Cart WHERE cartid=?", (cart_id,))
        cart_row = self.cursor.fetchone()
        if cart_row:
            if cart_row[3] > 1:
                self.cursor.execute("UPDATE Cart SET quantity = quantity - 1 WHERE cartid=?", (cart_id,))
            else:
                self.cursor.execute("DELETE FROM Cart WHERE cartid=?", (cart_id,))
            self.conn.commit()
            self.update_cart_tab()
    #update the cart on add click or remove 
    def update_cart_tab(self):
        for widget in self.cart_tab.winfo_children():
            widget.destroy() 

        tk.CTkLabel(self.cart_tab, text="Your Delicious Selections!").pack()

        self.cursor.execute("SELECT * FROM Cart")
        yummies = self.cursor.fetchall()
        for i, (cart_id, iceid, variety_name, quantity,) in enumerate(yummies, start=1):
            frame = tk.CTkFrame(self.cart_tab)
            frame.pack(pady=10,padx=5)

            label = tk.CTkLabel(frame, text=f"{i}. {variety_name},{quantity}", font=("Ariel", 12))
            label.pack(side="left", padx=10)

            button = tk.CTkButton(frame, text="Remove from cart", command=lambda cart_id=cart_id: self.remove_from_cart(cart_id))
            button.pack(side="right", padx=10)   

        if yummies:
            order_button = tk.CTkButton(self.cart_tab, text="Order")
            order_button.pack(pady=20)
    #confirmation if u wanna close the app 
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do You Really Want To Quit"):
            self.root.destroy()

if __name__ == "__main__":
    app = IceCreame()