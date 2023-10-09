import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
# To generate random numbers
import random
# To clear the terminal
from os import system
# To get the current date 
from datetime import datetime, date
# To create a delay in execution
from time import sleep
import pprint
from tabulate import tabulate

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
    """
    Generates the current date and converts it to a string and returns it.

    """
    # Get the current date
    current_date = datetime.now().date()
    # Converts the current date into a string
    string_date = current_date.strftime("%x")
    return (string_date)


def turn_to_currency(amount):
    """
    Turns a number into a float with 2 decimal places.
    """
    currency = round(float(amount), 2)
    return currency


def clear():
    """
    clears the screen

    """
    system('clear')


def check_pin(pin):
    """
    Compares the given pin with the pin inthe database
    """
    print("\nPLEASE ENTER YOUR PIN....")
    entered_pin = input(">>")
    sleep(2)
    
    if entered_pin == pin:
        return True

    else:
        print("\nINCORRECT PIN.... ")
        return False


class customer:
    """
    Creates a user class to store user information.
    """
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin

    
def delete_account(username, pin):
    """
    Deletes the user's account and removes the data from database

    """
    print("\nAre you sure you want to delete the account")
    print("press Y or N")
    # Begins a loop to get the answer again in case of incorrect answer 
    answer_loop = True
    while answer_loop:
        answer = input(">>")
        # If the answer is no theen go back to the welcome page and breaks the loop
        if answer.lower() == "n":
            print("\nGOING  BACK TO ACCOUNT....")
            sleep(2)
            account_welcome_page(username, pin)
            answer_loop = False
        # If the answer is yes then checks the pin and proceeds to delete the account
        elif answer.lower() == "y":
            # Calls the function to compare the pin
            given_pin = check_pin(pin)
            # If entered pin is correct then proceeds to delete the account
            if given_pin:
                print("\nDELETING YOUR ACCOUNT.....")
                sleep(1)
                # Deltes the user's individual worksheet and deletes it.
                user_sheet = SHEET.worksheet(username)
                SHEET.del_worksheet(user_sheet)
                # Gets the user's name from the database
                gets_name = PersonalDetails.find(username, in_column=1)
                # The complete row of information of the selected user is taken
                row_values = PersonalDetails.row_values(gets_name.row)
                # The complete row is deleted
                PersonalDetails.delete_rows(gets_name.row)
                print("\nACCOUNT DELETED SUCCESSFULLY")
                sleep(2)
                answer_loop = False
            else:
                # If entered pin is incorrect takes the user to welcome page.
                sleep(1)
                account_welcome_page(username, pin)
                break
        else:
            print("\nInvalid Input..")
            print("\nPRESS Y or N ")

    # After deleting takes the user to welcome page so that they can create a new account.
    welcome()


def withdraw_amount(username, pin):
    """
    Withdraws the amount from the account after validation

    """
    clear()
    print("Please enter the amount you want to withdraw ")
    amount = input(">>")
    withdraw = turn_to_currency(amount)
    # Gets the user's name from the database
    gets_name = PersonalDetails.find(username, in_column=1)
    # Gets the current balance amount in the account
    gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 3).value

    if float(withdraw) > float(gets_balance):
        print("\nINSUFFICIENT BALANCE...")
        sleep(1)
        withdraw_amount(username, pin)
    elif float(withdraw) == 0 or float(withdraw) < 0: 
        print("\nINPUT INVALID....")
        sleep(1)
        withdraw_amount(username, pin)
    else:
        print(f"\nWITHDRAWING {withdraw} EURO FROM ACCOUNT.....")
        user_sheet = SHEET.worksheet(username)
        date = current_date()
        deposit = 0
        new_bal = float(gets_balance)-float(withdraw)
        updation = []
        updation = [date, deposit, withdraw, new_bal]
        # appends the new data to the worksheet generated
        user_sheet.append_row(updation)

        # Get the name from personal details page 
        gets_name = PersonalDetails.find(username, in_column=1)
        # Gets the complete row values
        row_values = PersonalDetails.row_values(gets_name.row)
        # Changes the last value in the array to new balance
        row_values[-1] = new_bal
        # Deletes the present row 
        PersonalDetails.delete_rows(gets_name.row)
        # The new row with updated information is appended
        PersonalDetails.append_row(row_values)
        sleep(2)
        print("\nAMOUNT SUCESSFULLY WITHDRAWN.....")
        sleep(2)
        account_welcome_page(username, pin)


def check_balance(username, pin):
    """
    Checks the current balance amount in the users account
    
    """
    print("\nCHECKING BALANCE.....")
    sleep(2)
    # Gets the user's name from the database
    gets_name = PersonalDetails.find(username, in_column=1)
    # Gets the current balance amount in the account
    gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 3).value
    print(f"\nYOUR CURRENT BALANCE IS {gets_balance} EURO")
    sleep(2)
    # Calls the welcome page so that the user can select anothe function
    account_welcome_page(username, pin)


def know_pin(username):
    """
    Shows the secret PIN to the user

    """
    # Gets the user's name from the database
    gets_name = PersonalDetails.find(username, in_column=1)
    # Gets the PIN
    pin = PersonalDetails.cell(gets_name.row, gets_name.col + 1).value
    print(f"\nYour PIN is {pin}")
    sleep(3)
    # Again calls the welcome page
    account_welcome_page(username, pin)


def deposit_amount(username, pin):
    """
    Deposits the given amount into the account after validation

    """
    clear()
    print("Please enter the amount you want to deposit ")
    amount = input(">>")
    deposit = turn_to_currency(amount)
    print("DEPOSITING THE AMOUNT...")
    sleep(1)
    # Gets the user's name from the database
    gets_name = PersonalDetails.find(username, in_column=1)
    # Gets the current balance amount in the account
    gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 3).value
    # The new balance is the sum of old balance and the present deposit amount
    new_bal = float(gets_balance) + float(deposit)
    # The complete row of information of the selected user is taken
    row_values = PersonalDetails.row_values(gets_name.row)
    # The last two values are edited 
    row_values[-1] = new_bal
    # The present Row is deleted
    PersonalDetails.delete_rows(gets_name.row)
    # The new row with updated information is appended
    PersonalDetails.append_row(row_values)
    # Calls the  worksheet with the new user
    user_sheet = SHEET.worksheet(username)
    date = current_date()
    withdraw = 0
    updation = []
    updation = [date, deposit, withdraw, new_bal]
    # appends the new data to the worksheet generated
    user_sheet.append_row(updation)
    print(f"\n{deposit} Euro has been deposited!!! ")
    sleep(2)
    # Calls the welcome page so that the user can select anothe function
    account_welcome_page(username, pin)


def generate_pin():
    """
    Generates a random number between 1000 and 9999 
    which is used as the PIN and returns it

    """
    pin = random.randint(1000, 9999)
    return pin


def account_welcome_page(username, pin):
    
    # Displays the various function that can be done by the user 
    clear()
    print(f"\n\nHello {username}!!!")
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
            withdraw_amount(username, pin)
            break
        elif selected_option == "4":
            know_pin(username)
            break
        elif selected_option == "5":
            delete_account(username, pin)
            break
        else:
            print("\n INVALID INPUT.PLEASE ENTER A VALID OPTION ")
            break


def generate_new_worksheet(username):
    """
    Create a new worksheet using the username and add the headings:
    Deposit, Withdraw and Balance.
    """
    # Create the worksheet
    new_sheet = SHEET.add_worksheet(title=username, rows=100, cols=4)
    # Add in heading and starting balance
    headings = ['Date', 'Deposit', 'Withdraw', 'Balance']
    date = current_date()
    starting_balance = [date, "0", "0", "0"]
    new_sheet.append_row(headings)
    new_sheet.append_row(starting_balance)


def create_new_account():
    """
    Creates new account by getting username from the user and assigns a 
    PIN to each account.It also validates that the username has required
    length, avoids repetition,is not starting with a number and has no spaces 
    in it.
    
    """
    clear()
    print("PLEASE ENTER YOUR USERNAME ")
    print("(The username should have 4 to 10 characters)")
    username = input("\n>>").capitalize()
    # compares the user given username with the database and avoids repeatition
    if PersonalDetails.find(username, in_column=1) is not None:
        print(f"{username} username is unavailable .Please try a new username")
    # Checks if the username begins with a number
    elif not username[0].isalpha():
        print("Username should not begin with number")
    # Checks if the username has more than the required number of characters
    elif len(username) < 3 and len(username) > 11:
        print("The username should have minimum 4 characters and maximum 10 characters")
    # Checks if the username begins with a space
    elif any(char.isspace() for char in username):
        print(f"{username} is invalid, no white spaces are allowed")
    # Checks if the username has the required number of characters
    elif len(username) > 3 and len(username) < 11:
        print("\nCREATING ACCOUNT.PLEASE WAIT A MINUTE... ")
        sleep(3)
        pin = generate_pin()
        
        balance = "00.00"
        date = current_date()
        # Makes a new customer object of the class customer
        n_cust = customer(username, pin)
        customer_info = [n_cust.username, n_cust.pin, date, balance]
        PersonalDetails.append_row(customer_info)
        generate_new_worksheet(username)
        permission = False
        sleep(1)
        account_welcome_page(username, pin)


def logging_out():
    print("\nLOGGING OUT...")


def admin_delete_acc(username, pin):
    pass


def view_acc_holders(username, pin):
    """
    Give Admin a list of all the users, their PIN last updation date and balance.
    """
    print("\nLOADING DATA.....\n\n")
    sleep(2)
    full_data = PersonalDetails.get_all_values()
    acc_holder_data = full_data[2:]
    print(tabulate(acc_holder_data, headers=['Username', 'PIN', 'Last updated on', 'Balance']))
    admin_login(username, pin)


def admin_login(username, pin):
    """
    Opens a panel for admin to view all users, delete a user and to logout.
    
    """
    print("\nWELCOME ADMIN")
    print("\n1. View all account holders")
    print("\n2. Delete an account")
    print("\n3. Log out")

    selection_loop = True
    while selection_loop:

        admin_choice = input(">>")
        # View all account holders
        if admin_choice == "1":
            selection_loop = False
            view_acc_holders(username, pin)
             
        elif admin_choice == "2":
            print("\nTo delete an account, Please enter the username")
            user_to_delete = input(">>")
            # Get the name in database
            stored_names = PersonalDetails.find(user_to_delete, in_column=1)

            if stored_names:
                admin_delete_acc(username, pin)
                selection_loop = False
            elif user_to_delete == "0":
                logging_out()
                sleep(1)
                welcome()
                break
            else:
                print("\nUser not found")

        elif admin_choice == "0":
            logging_out()
            sleep(2)
            welcome()
            break
        else:
            print("\n Invalid Input.Please try again ")
        

def login_account():
    clear()
    print("Enter your name to login:")
    entered_username = input(">>").capitalize()
    print("Enter your PIN :")
    entered_pin = input(">>")
    stored_names = PersonalDetails.find(entered_username, in_column=1)
    sleep(1)
    # If username is present in database
    if stored_names:
        # Gets the pin corresponding to the username
        stored_pin = PersonalDetails.cell(stored_names.row, stored_names.col + 1).value
        # ADMIN login
        if entered_username == "Admin" and entered_pin == stored_pin:
            print("\nACCOUNT LOADING....")
            sleep(1)
            admin_login(entered_username, entered_pin)
        # checks if the entered pin is same as the one in database
        elif stored_pin == entered_pin:
            print("\nLOADING ACCOUNT....")
            sleep(1)
            account_welcome_page(entered_username, entered_pin)

        else:
            print("\n USERNAME OR PIN INCORRECT")
            sleep(1)
            welcome()
    else:
        print("\n USERNAME OR PIN INCORRECT")
        sleep(1)
        welcome()

       
def welcome():
    """
    Displays the welcome message when the user opens the website

    """
    clear()
    permission = True
    while permission:

        print("\n\nWELCOME TO PEOPLES ONLINE BANKING SERVICES")
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


main()





