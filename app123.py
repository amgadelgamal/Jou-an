import tkinter as tk
from tkinter import messagebox
import pandas as pd


class User:
    def init(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def login(self):
        # code to authenticate the user, for example by checking against a database of valid users
        # return true if the login is successful, false otherwise
        return True
    
class FoodChatBot:
    def __init__(self):
        pass

    def get_food_options(self, dietary_restriction):
        # replace this with code to get food options from a database or API
        data = {"name": ["Poulet Rouge", "McDonald's", "KFC", "Copper Branch", 'Shawarmaz', "Boustan", "Pizza Pizza", "Subway", "St-hubert"],
                "vegan": [False, False, False, True, False, False, False, False, False],
                "vegetarian": [False, False, False, True, False, False, True, False, False],
                "gluten_free": [False, False, False, True, False, False, True, False, False],
                "halal": [True, False, False, True, True, True, False, False, True],
                "location": [" is located at 1623 Saint-Catherine St W, Montreal", " is located at 3330 Boulevard Cote Vertu Ouest, Saint-Laurent", " is located at 1595 Boulevard Cote Vertu Ouest, Saint-Laurent", " is located at 2310 Rue Wilfrid-Reid, Saint-Laurent"," is located at 159 Bd du Curé-Labelle, Laval", " is located at 3500 Boulevard Cote Vertu Ouest O, Saint-Laurent", " is located at 5510 Henri Bourassa Blvd W, Montreal", " is located at 3131 Boulevard Cote Vertu Ouest, Saint-Laurent", " is located at 1300 Blvd. Marcel-Laurin, Montréal"]}
        df = pd.DataFrame(data)
        
        if dietary_restriction == "vegan":
            df_filtered = df[df["vegan"]==True]
        elif dietary_restriction == "vegetarian":
            df_filtered = df[df["vegetarian"]==True]
        elif dietary_restriction == "gluten_free":
            df_filtered = df[df["gluten_free"]==True]
        elif dietary_restriction == "halal":
            df_filtered = df[df["halal"]==True]
        
        # convert the "name" column to a list
        name_list = df_filtered["name"].tolist()
        location_list = df_filtered["location"].tolist()
        # convert the list to a tuple
        restaurants = tuple(zip(name_list,location_list))
        return restaurants
    
    


class FoodChatGUI:
    def __init__(self):
        self.chat_bot = FoodChatBot()

        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.root.title("Jou3an Food Chatbot")

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        self.root.mainloop()


    def login(self):
        username = self.username_entry.get()
        user = User()
        if user.login():
            messagebox.showinfo("Welcome", f"Welcome, {username}!")
            self.start_chat()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def start_chat(self):
        self.username_label.destroy()
        self.username_entry.destroy()
        self.login_button.destroy()

        self.dietary_label = tk.Label(self.root, text="Do you have any dietary restrictions?: ")
        self.dietary_label.pack()

        self.dietary_entry = tk.Entry(self.root)
        self.dietary_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.get_food_options)
        self.submit_button.pack()

    def get_food_options(self):
        # Fix for issue 1: Make sure the `x` variable is an integer
        x = 1
        try:
            x = int(x)
        except ValueError:
            print("Error: x must be an integer.")
            return

        # Fix for issue 2: Check if `x` is greater than 0
        if x <= 0:
            print("Error: x must be greater than 0.")
            return

        # Rest of your code goes here

        dietary_restriction = self.dietary_entry.get()
        food_options = self.chat_bot.get_food_options(dietary_restriction)

        self.dietary_label.destroy()
        self.dietary_entry.destroy()
        self.submit_button.destroy()

        self.food_options_label = tk.Label(self.root, text="Here are some food options for you:")
        self.food_options_label.pack()

        self.food_options_listbox = tk.Listbox(self.root)
        
        for option in food_options:
            self.food_options_listbox.insert(tk.END, option)
            
        self.food_options_listbox.pack()

        self.select_button = tk.Button(self.root, text="Select", command=self.select_food)
        self.select_button.pack()
        
        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        self.logout_button.pack()
        
    def select_food(self):
        selected_food = self.food_options_listbox.get(self.food_options_listbox.curselection())
        messagebox.showinfo("Selected food", f"{selected_food}")
        self.chat_bot.order_food(selected_food)
    
f = FoodChatGUI()

    


