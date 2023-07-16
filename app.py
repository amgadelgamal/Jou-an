import tkinter as tk
from tkinter import messagebox
from FoodChatBot import FoodChatBot


class User:
    def __init__(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def login(self):
        # code to authenticate the user, for example by checking against a database of valid users
        # return true if the login is successful, false otherwise
        return True


class FoodChatGUI:
    def __init__(self):
        self.chat_bot = FoodChatBot()

        self.root = tk.Tk()
        self.root.geometry("300x300")
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
        user = User(username)
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

        self.calorie_label = tk.Label(self.root, text="How many calories should the meal have? (enter a range): ")
        self.calorie_label.pack()

        self.lower_calorie_label = tk.Label(self.root, text="Lower bound: ")
        self.lower_calorie_label.pack()

        self.lower_calorie_entry = tk.Entry(self.root)
        self.lower_calorie_entry.pack()

        self.upper_calorie_label = tk.Label(self.root, text="Upper bound: ")
        self.upper_calorie_label.pack()

        self.upper_calorie_entry = tk.Entry(self.root)
        self.upper_calorie_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.get_food_options)
        self.submit_button.pack()

#    def get_food_options(self):
#        dietary_restriction = self.dietary_entry.get()
#        lower_calorie_bound = self.lower_calorie_entry.get()
#        upper_calorie_bound = self.upper_calorie_entry.get()
#        food_options = self.chat_bot.get_food_options(dietary_restriction, lower_calorie_bound, upper_calorie_bound)

#        self.dietary_label.destroy()
#        self.dietary_entry.destroy()
#        self.calorie_label.destroy()
#        self.lower_calorie_label.destroy()
#        self.lower_calorie_entry.destroy()
#        self.upper_calorie_label.destroy()
#        self.upper_calorie_entry.destroy()
#        self.submit_button.destroy()

#        self.food_options_label = tk.Label(self.root, text="Here are some food options for you:")
#        self.food_options_label.pack()

#        self.food_options_listbox = tk.Listbox(self.root)
#        for option in food_options:
#            self.food_options_listbox.insert(tk.END, option)
#        self.food_options_listbox.pack()

#        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout)
#        self.logout_button.pack()

#    def logout(self):
#        self.food_options_label.destroy()
#        self.food_options_listbox.destroy()
#        self.logout_button.destroy()
#        self.__init__()


