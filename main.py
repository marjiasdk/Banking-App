# import tkinter and mysql.connector
from tkinter import *
import mysql.connector

# connect to the database
bank_details = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banking"
)

# create a function to check the login details and display the balance or error message
def check_login():
    card_number = card_number_entry.get() # get() returns the value entered in the Entry widget
    password = password_entry.get()

    # execute a SELECT query to check if the card number and password match the data in the database
    cursor = bank_details.cursor()

    # SELECT: used to select data from a database
    # FROM: specifies the table from which to select data
    # WHERE: specifies which record(s) to select
    # %s: a placeholder for the values to be inserted
    query = "SELECT balance FROM users WHERE card_number=%s AND password=%s"
    cursor.execute(query, (card_number, password)) # execute() executes the query and inserts the values in the placeholders

    # fetchone() returns the first row of the result
    result = cursor.fetchone()

    if result is None:
        error_label.config(text="Invalid card number or password")
    else:
        balance_label.config(text="Your Balance is: $" + str(result[0]))

# create GUI
window = Tk()
window.title("Banking App")
window.geometry("500x500")

card_number_label = Label(window, text="Card Number: ")
card_number_label.grid(row=0, column=0)
card_number_entry = Entry(window)
card_number_entry.grid(row=0, column=1)

password_label = Label(window, text="Password: ")
password_label.grid(row=1, column=0)
password_entry = Entry(window, show="*")
password_entry.grid(row=1, column=1)

button = Button(window, text="Login", command=check_login) # command=check_login: calls the check_login() function when the button is clicked
button.grid(row=2, column=1)

balance_label = Label(window, text="")
balance_label.grid(row=5, column=1)

error_label = Label(window, text="", fg="red")
error_label.grid(row=4, column=0)

window.mainloop()
