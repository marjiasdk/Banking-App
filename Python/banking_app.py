# import tkinter and mysql.connector
from tkinter import *
import mysql.connector

# connect to the database
bank_details = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banking"
)

# create a class to check login details
class CheckLogin:
    # self parameter is a reference to the current instance of the class
    def __init__(self): # constructor
        # get the values from the entry boxes
        self.name = name_entry.get()
        self.card_number = card_number_entry.get()
        self.password = password_entry.get()

        # cursor object is used to execute queries
        # cursor() method creates a cursor object
        cur = bank_details.cursor()
        query = "SELECT balance FROM users WHERE name =%s AND card_number=%s AND password=%s"
        cur.execute(query, (self.name, self.card_number, self.password))

        # fetchone() method returns the first row of the result
        balance = cur.fetchone()

        if balance is None:
            error_label.config(text="Invalid name or card number or password")
        else:
            balance_label.config(text="Your Balance is: €" + str(balance[0]))

# create GUI
window = Tk()
window.title("Banking App")
window.geometry("450x450")

# name label and entry  
name_label = Label(text="Name: ")
name_label.place(x=100, y=90)
name_entry = Entry()
name_entry.place(x=150, y=90)

# card number label and entry
card_number_label = Label(text="Card Number: ")
card_number_label.place(x=60, y=120)
card_number_entry = Entry()
card_number_entry.place(x=150, y=120)

# password label and entry
password_label = Label(text="Password: ")
password_label.place(x=80, y=150)
password_entry = Entry(show="*")
password_entry.place(x=150, y=150)

button = Button(text="Login", command=CheckLogin) # command=check_login: calls the check_login() function when the button is clicked
button.place(x=190, y=200)

balance_label = Label()
balance_label.place(x=135, y=250)

error_label = Label(foreground="red")
error_label.place(x=100, y=250)

window.mainloop()
