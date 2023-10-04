import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import random
import os
import sys
from datetime import date

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('PeoplesBank')

PersonalDetails = SHEET.worksheet("PersonalDetails")


def generate_pin():
    """
    Generates a random number between 1000 and 9999 
    which is used as the PIN and returns it

    """
    pin = random.randint(1000, 9999)
    return pin


class customer:
    """
    Creates a class called customer which has username 
    and pin as information.
    """
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin


def deposit_amount(username, pin):
    """
    Deposits the given amount into the account after validation

    """
    gets_name =  PersonalDetails.find(username, in_column=1)
    print(gets_name)   


def account_welcome_page(username, pin):
    print(f"Welcome{ username}!!!")
    print("\nSELECT THE SERVICE YOU WANT TO CHOOSE..")
    print("\n 1. Deposit Amount ")
    print("\n 2.Check your Account Balance")
    print("\n 3. Withdraw Amount")
    print("\n 4.Know your PIN")
    print("\n 5.Delete  your Account")
    selected_option = input("\n>>")

    option_loop = True
    while option_loop:
        if selected_option == 1:
            deposit_amount(username, pin)
            break
        elif selected_option == 2:
            check_balance()
            break
        elif selected_option == 3:
            withdraw_amount()
            break
        elif selected_option == 4:
            know_pin()
            break
        elif selected_option == 5:
            delete_account()
            break
        else:
            print("\n INVALID INPUT.PLEASE ENTER A VALID OPTION ")


def create_new_account():
    """
    Creates new account by getting username from the user and assigns a 
    PIN to each account.It also validates that the username has required
    length, avoids repetition,is not starting with a number and has no spaces 
    in it.
    
    """
    print("Please enter your username")
    print("The username should have 4 to 10 characters")
    username = input("\n>>")

    if PersonalDetails.find(username, in_column=1) is not None:
        print(f"{username} username is unavailable .Please try a new username")
    elif not username[0].isalpha():
        print("Username should not begin with number")
    elif len(username) < 3 and len(username) > 11:
        print("The username should have minimum 4 characters and maximum 10 characters")
    elif any(char.isspace() for char in username):
        print(f"{username} is invalid, no white spaces are allowed")
    elif len(username) > 3 and len(username) < 11:
        print("Creating Account.Please wait a second... ")
        pin = generate_pin()

        new_customer = customer(username, pin)
        customer_info = [new_customer.username, new_customer.pin]
        PersonalDetails.append_row(customer_info)
        print("\n NEW ACCOUNT SUCCESSFULLY CREATED....")
        print(f"Your username is :{username}")
        print(f"Your PIN is :{pin}")
        permission = False
        account_welcome_page(username, pin)
        

def login_account():
   # print("Enter your name to login :")
    #entered_username = input(">>")
    #print("Enter your PIN :")
    #entered_pin = input(">>")
    #stored_names = PersonalDetails.find(entered_username, in_column=1)

    #if stored_names:
     #   PersonalDetails.cell(stored_names.row, stored_names.col + 1).value
    pass

        
def welcome():
    """
    Displays the welcome message when the user opens the website

    """
    permission = True
    while permission:

        print("Welcome to Peoples Online Banking Services")
        print("\nWhat would you like to do..?")
        print("\n 1.Login")
        print("\n 2.Create a new account")
        option_selected = input("\n>>")

        if option_selected == "1":
            login_account()
        elif option_selected == "2":
            create_new_account()
        else:
            print("Invalid Input.Please select 1 or 2 .")


def main():
    welcome()

#main()


username = "sivadas"
pin = 1234

def deposit_amount(username, pin):
    """
    Deposits the given amount into the account after validation

    """
    print("Please enter the amount you want to deposit ")
    deposit = input(">>")
    
    gets_name = PersonalDetails.find(username, in_column=1)
    print(f"The name is {gets_name}")
    gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 4).value
    bal_cell = PersonalDetails.cell(gets_name.row, gets_name.col + 4)
    print(gets_balance)
    last_upd_amt = PersonalDetails.cell(gets_name.row, gets_name.col + 3).value
    print(last_upd_amt)
    new_upd_amt = deposit
    new_bal = gets_balance + deposit
    
    PersonalDetails.values_clear("E4:E4")


deposit_amount(username, pin) 


def turn_to_currency(deposit):
    """
    Turns a number into a float with 2 decimal places.
    """
    currency = round(float(deposit), 2)
    return currency
