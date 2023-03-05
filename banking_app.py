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

# create a function to check the login details and display the balance or error message
def check_login():
    name = name_entry.get()
    card_number = card_number_entry.get()
    password = password_entry.get()

    # execute a SELECT query to check if the card number and password match the data in the database
    cursor = bank_details.cursor()

    # SELECT: used to select data from a database
    # FROM: specifies the table from which to select data
    # WHERE: specifies which record(s) to select
    # %s: a placeholder for the values to be inserted
    query = "SELECT balance FROM users WHERE name =%s AND card_number=%s AND password=%s"
    cursor.execute(query, (name, card_number, password)) # execute() executes the query and inserts the values in the placeholders

    # fetchone() returns the first row of the result
    # result is a tuple containing the balance: (balance)
    result = cursor.fetchone()

    if result is None:
        error_label.config(text="Invalid name or card number or password") # config() configures the widget
    else:
        balance_label.config(text="Your Balance is: €" + str(result[0])) # result[0] returns the balance from the tuple

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

button = Button(window, text="Login", command=check_login) # command=check_login: calls the check_login() function when the button is clicked
button.grid(row=3, column=1)

balance_label = Label(window)
balance_label.grid(row=5, column=1)

error_label = Label(window, foreground="red")
error_label.grid(row=4, column=1)

window.mainloop()
