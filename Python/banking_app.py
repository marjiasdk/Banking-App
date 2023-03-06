# import tkinter and mysql.connector
from tkinter import *
import mysql.connector

# connect to the database
bank_details = mysql.connector.connect(
    host="localhost",
    user="root",
    password="isuckcockX1#",
    database="banking"
)

# create a class to check login details
class CheckLogin:
    def __init__(self): # constructor
        # get the values from the entry boxes
        self.name = name_entry.get()
        self.card_number = card_number_entry.get()
        self.password = password_entry.get()

        cursor = bank_details.cursor()
        query = "SELECT balance FROM users WHERE name =%s AND card_number=%s AND password=%s"
        cursor.execute(query, (self.name, self.card_number, self.password))

        # fetch the result
        result = cursor.fetchone()

        if result is None:
            error_label.config(text="Invalid name or card number or password")
        else:
            balance_label.config(text="Your Balance is: €" + str(result[0]))

# create GUI
window = Tk()
window.title("Banking App")
window.geometry("500x500")

# name label and entry  
name_label = Label(window, text="Name: ")
name_label.grid(row=0, column=0)
name_entry = Entry(window)
name_entry.grid(row=0, column=1)

# card number label and entry
card_number_label = Label(window, text="Card Number: ")
card_number_label.grid(row=1, column=0)
card_number_entry = Entry(window)
card_number_entry.grid(row=1, column=1)

# password label and entry
password_label = Label(window, text="Password: ")
password_label.grid(row=2, column=0)
password_entry = Entry(window, show="*")
password_entry.grid(row=2, column=1)

button = Button(window, text="Login", command=CheckLogin) # command=check_login: calls the check_login() function when the button is clicked
button.grid(row=3, column=1)

balance_label = Label(window)
balance_label.grid(row=5, column=1)

error_label = Label(window, foreground="red")
error_label.grid(row=4, column=1)

window.mainloop()
