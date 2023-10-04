import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import random
import os
import sys
from datetime import datetime ,date

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


def current_date():
    return datetime.now()

def check_balance(username, pin):
    """
    Checks the current balance amount in the users account
    
    """
    print("\n CHECKING BALANCE.....")
    # Gets the user's name from the database
    gets_name = PersonalDetails.find(username, in_column=1)
    # Gets the current balance amount in the account
    gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 4).value
    print(f"\nYOUR CURRENT BALANCE IS {gets_balance} Euro")


def deposit_amount(username, pin):
    """
    Deposits the given amount into the account after validation

    """
    print("Please enter the amount you want to deposit ")
    deposit = input(">>")
    # Gets the user's name from the database
    gets_name = PersonalDetails.find(username, in_column=1)
    # Gets the current balance amount in the account
    gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 4).value
    #The new updated amount is the current deposit amount
    new_upd_amt = deposit
    # The new balance is the sum of old balance and the present deposit amount
    new_bal = int(gets_balance) + int(deposit)
    #The complete row of information of the selected user is taken
    row_values = PersonalDetails.row_values(gets_name.row)
    # The last two values are edited 
    row_values[-1] = new_bal
    row_values[-2] = new_upd_amt
    # The present Row is deleted
    PersonalDetails.delete_rows(gets_name.row)
    # The new row with updated information is appended
    PersonalDetails.append_row(row_values)


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


def account_welcome_page(username, pin):
    print(f"Welcome{ username}!!!")
    print("\nSELECT THE SERVICE YOU WANT TO CHOOSE..")
    print("\n 1.Deposit Amount ")
    print("\n 2.Check your Account Balance")
    print("\n 3.Withdraw Amount")
    print("\n 4.Know your PIN")
    print("\n 5.Delete  your Account")
    selected_option = input("\n>>")

    option_loop = True
    while option_loop:
        if selected_option == "1":
            deposit_amount(username, pin)
            break
        elif selected_option == "2":
            check_balance(username, pin)
            break
        elif selected_option == "3":
            withdraw_amount()
            break
        elif selected_option == "4":
            know_pin()
            break
        elif selected_option == "5":
            delete_account()
            break
        else:
            print("\n INVALID INPUT.PLEASE ENTER A VALID OPTION ")
            break

def create_new_account():
    """
    Creates new account by getting username from th2 user and assigns a 
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
        upd_amt = 0
        balance = 0
        date = current_date()
        new_customer = customer(username, pin)
        customer_info = [new_customer.username, new_customer.pin, date, upd_amt, balance]
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

def current_date():
    date = datetime.date.today()
    print(date)
current_date()

