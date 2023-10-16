import gspread
from google.oauth2.service_account import Credentials
# To generate random numbers
import random
# To clear the terminal
import os
# To get the current date
from datetime import datetime, date
# To create a delay in execution
from time import sleep
# To display as a table
from tabulate import tabulate
# ascii art file
import heading_art

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
    os.system('clear')


def check_pin(pin):
    """
    Compares the given pin with the pin inthe database
    """
    print("\n\nPLEASE ENTER YOUR PIN....")
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
    clear()
    print(heading_art.logo)
    print("\n\nAre you sure you want to delete the account")
    print("press Y or N")
    # Begins a loop to get the answer again in case of incorrect answer
    answer_loop = True
    while answer_loop:
        answer = input(">>")
        # If the answer is no theen go back to the welcome
        # page and breaks the loop
        if answer.lower() == "n":
            print("\nGOING  BACK TO ACCOUNT....")
            sleep(2)
            account_welcome_page(username, pin)
            answer_loop = False
        # If the answer is yes then checks the pin and
        # proceeds to delete the account
        elif answer.lower() == "y":
            # Calls the function to compare the pin
            given_pin = check_pin(pin)
            # If entered pin is correct then proceeds to delete the account
            if given_pin:
                print("\nDELETING YOUR ACCOUNT.....")
                sleep(1)
                # Finds the user's individual worksheet and deletes it.
                user_sheet = SHEET.worksheet(username)
                SHEET.del_worksheet(user_sheet)
                # Gets the user's name from the database
                gets_name = PersonalDetails.find(username, in_column=1)
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

    # After deleting takes the user to welcome page so
    # that they can create a new account.
    welcome()


def withdraw_amount(username, pin):
    """
    Withdraws the amount from the account after validation

    """
    clear()
    print(heading_art.logo)
    print("\n\nPlease enter the amount you want to withdraw ")
    print("Press 'e' to exit")
    amount = input("€")
    # Checks if the value is 'e' and exits the function
    if amount == "e":
        logging_out()
        account_welcome_page(username, pin)
    else:
        if not amount.isalpha():
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
                print(f"\nWITHDRAWING €{withdraw} FROM ACCOUNT.....")
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
                print(f"\nYOUR CURRENT ACCOUNT BALANCE IS :€{new_bal}")
                sleep(5)
                account_welcome_page(username, pin)
        else: 
            print("\nPlease Enter a valid Input..")
            sleep(2)
            withdraw_amount(username, pin)


def check_balance(username, pin):
    """
    Checks the current balance amount in the users account

    """
    clear()
    print(heading_art.logo)
    print("\nCHECKING BALANCE.....")
    sleep(2)
    # Gets the user's name from the database
    gets_name = PersonalDetails.find(username, in_column=1)
    # Gets the current balance amount in the account
    gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 3).value
    print(f"\nYOUR CURRENT BALANCE IS €{gets_balance}")
    sleep(5)
    # Calls the welcome page so that the user can select anothe function
    account_welcome_page(username, pin)


def change_pin(username):
    """
    Changes the PIN number to a new PIN or user selected PIN

    """
    clear()
    print(heading_art.logo)
    print("\n\nSelect any one option:")
    print("\n\n1.Enter a PIN of your choice")
    print("\n2.Get a new PIN ")
    users_choice = input(">>")
    if users_choice == "1":
        print("\n\nPlease enter a four-digit PIN number")
        users_pin = input(">>")
        # Searches for the username in database
        get_name = PersonalDetails.find(username, in_column=1)
        # Gets the complete row of the username
        get_row = PersonalDetails.row_values(get_name.row)
        # Changes the pin to the new user selected number
        get_row[1] = users_pin
        # The present Row is deleted
        PersonalDetails.delete_rows(get_name.row)
        # The new row with updated information is appended
        PersonalDetails.append_row(get_row)
        # Calls the  worksheet with the new user
        user_sheet = SHEET.worksheet(username)
        # Generates the current date
        date = current_date()
        # Creates an empty array
        pin_change = []
        # Date and pin change information is entered
        pin_change = [date, "-", "-", "-", "PIN changed"]
        # appends the new data to the worksheet generated
        user_sheet.append_row(pin_change)
        print("\nYour PIN number has been changed.")
        sleep(3)
        # Calls the welcome page so that the user can select anothe function
        account_welcome_page(username, users_pin)

    elif users_choice == "2":
        print("\nGenerating a new PIN for your account.")
        # generates new pin
        new_pin = generate_pin()
        print(f"\nYOUR NEW PIN NUMBER IS {new_pin}")
        # Searches for the username in database
        get_name = PersonalDetails.find(username, in_column=1)
        # Gets the complete row of the username
        get_row = PersonalDetails.row_values(get_name.row)
        # Changes the pin to the new user selected number
        get_row[1] = new_pin
        # The present Row is deleted
        PersonalDetails.delete_rows(get_name.row)
        # The new row with updated information is appended
        PersonalDetails.append_row(get_row)
        # The username corresponding worksheet is taken
        user_sheet = SHEET.worksheet(username)
        # Generates the current date
        date = current_date()
        # Creates an empty array
        pin_change = []
        # Date and pin change information is entered
        pin_change = [date, "-", "-", "-", "PIN changed"]
        # Appends the new data to the worksheet generated
        user_sheet.append_row(pin_change)
        print("\nYour PIN number has been changed.")
        sleep(3)
        # Calls the welcome page so that the user can select anothe function
        account_welcome_page(username, new_pin)
    else:
        change_pin(username)


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


def recent_transaction(username, pin):
    """
    Shows the recent ten transaction of the user
    """
    clear()
    print(heading_art.logo)
    print("\nLOADING DATA....\n\n")
    sleep(3)
    # Calls the  worksheet with the new user
    user_sheet = SHEET.worksheet(username)
    # Gets all the information in the sheet
    full_data_arr = user_sheet.get_all_values()
    # Slices the required data
    acc_holder_data = full_data_arr[-10:]
    # Prints the data as a table
    print(tabulate(acc_holder_data, headers=['Date', 'Deposit', 'Withdraw', 'Balance', 'PIN status']))
    sleep(3)
    while True:
        answer = input("\n\n                          Enter 0 to go back :")
        if answer == "0":
            clear()
            account_welcome_page(username, pin)
            break
        

def deposit_amount(username, pin):
    """
    Deposits the given amount into the account after validation

    """
    clear()
    print(heading_art.logo)
    # Answer loop
    while True:
        print("\n\nPlease enter the amount you want to deposit ")
        amount = input(">>")
        try:
            deposit = turn_to_currency(amount)
            if deposit < 0:
                print("\nNegative values not accepted")
                sleep(2)
                deposit_amount(username, pin)
                break
            elif deposit == 0:
                print("\nZero value not accepted")
                sleep(2)
                deposit_amount(username, pin)
                break
            else:
                print("\nDEPOSITING THE AMOUNT...")
                sleep(1)
                # Gets the user's name from the database
                gets_name = PersonalDetails.find(username, in_column=1)
                # Gets the current balance amount in the account
                gets_balance = PersonalDetails.cell(gets_name.row, gets_name.col + 3).value
                # The new balance is the sum of old balance and the present
                # deposit amount
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
                print(f"\n€{deposit} has been deposited!!! ")
                sleep(2)
                # Calls the welcome page so that the user can select another function
                account_welcome_page(username, pin)
                
        # tells the user entered value is not valid
        except ValueError:
            print(f"\nEntered amount value {amount} is not valid")
            sleep(4)
            deposit_amount(username, pin)
            break


def generate_pin():
    """
    Generates a random number between 1000 and 9999

    """
    pin = random.randint(1000, 9999)
    return pin


def account_welcome_page(username, pin):
    # Displays the various function that can be done by the user
    clear()
    print(heading_art.logo)
    print(f"\n\nHello {username}!!!")
    print("\nSELECT THE SERVICE YOU WANT TO CHOOSE..")
    print("\n 1.Deposit Amount ")
    print("\n 2.Check your Account Balance")
    print("\n 3.Withdraw Amount")
    print("\n 4.Know your PIN")
    print("\n 5.Change your PIN")
    print("\n 6.Your recent Transactions")
    print("\n 7.Delete  your Account")
    print("\n                                       Enter 0 to log out...")
    selected_option = input("\n>>")

    option_loop = True
    while option_loop:
        if selected_option == "0":
            logging_out()
            break
        elif selected_option == "1":
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
            change_pin(username)
            break
        elif selected_option == "6":
            recent_transaction(username, pin)
            break
        elif selected_option == "7":
            delete_account(username, pin)
            break
        else:
            print("\n INVALID INPUT.PLEASE ENTER A VALID OPTION ")
            sleep(2)
            account_welcome_page(username, pin)
            break


def generate_new_worksheet(username):
    """
    Create a new worksheet using the username and add the headings:
    Deposit, Withdraw and Balance.
    """
    # Create the worksheet
    new_sheet = SHEET.add_worksheet(title=username, rows=100, cols=4)
    # Add in heading and starting balance
    headings = ['Date', 'Deposit (Euro)', 'Withdraw (Euro)', 'Balance (Euro)', 'PIN status']
    date = current_date()
    starting_balance = [date, "0", "0", "0", "PIN generated"]
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
    print(heading_art.logo)
    print("\n\nPLEASE SELECT YOUR USERNAME ")
    print("(The username should have 4 to 10 characters)")
    username = input("\n>>").capitalize()
    # compares the user given username with the database and avoids repeatition
    if PersonalDetails.find(username, in_column=1) is not None:
        print(f"{username} username is unavailable .Please try a new username")
        sleep(2)
        create_new_account()
    # Checks if the username begins with a number
    elif not username[0].isalpha():
        print("Username should not begin with number or space")
        sleep(2)
        create_new_account()
    # Checks if the username has more than the required number of characters
    elif len(username) < 4 or len(username) > 11:
        print("The username should have minimum 4 characters and maximum 10 characters")
        sleep(2)
        create_new_account()
    # Checks if the username begins with a space
    elif any(char.isspace() for char in username):
        print(f"{username} is invalid, no white spaces are allowed")
        sleep(2)
        create_new_account()
    # Checks if the username has the required number of characters
    elif len(username) > 4 and len(username) < 11:
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
        print(f"\n{username} IS YOUR USERNAME")
        print(f"\nYOUR PIN IS:{pin}")
        sleep(5)
        login_account()


def logging_out():
    clear()
    print(heading_art.logo)
    print("\nLOGGING OUT...")
    sleep(3)
    welcome()


def admin_delete_acc(user_to_delete, pin):
    # Finds the username in the database
    get_name = PersonalDetails.find(user_to_delete, in_column=1)
    print("\n\nAre you sure the account should be deleted")
    print("\nPress Y or N")
    decision = input(">>").lower()
    if decision == "n":
        print("\nRETURNING BACK....")
        sleep(2)
        admin_login("Admin", 9053)
    elif decision == "y":
        # The complete row is deleted
        PersonalDetails.delete_rows(get_name.row)
        # Finds the user's individual worksheet and deletes it.
        user_sheet = SHEET.worksheet(user_to_delete)
        SHEET.del_worksheet(user_sheet)
        print("\nACCOUNT DELETED SUCCESSFULLY")
        sleep(3)
        admin_login("Admin", 9053)
    else:
        print("\nINPUT INVALID. PLEASE TRY AGAIN")
        sleep(1)
        admin_login("Admin", 9053)


def view_acc_holders(username, pin):
    """
    Give Admin a list of all the users, their PIN last
    updation date and balance.
    """
    clear()
    print(heading_art.logo)
    print("\nLOADING DATA.....\n\n")
    sleep(2)
    full_data = PersonalDetails.get_all_values()
    acc_holder_data = full_data[2:]
    print(tabulate(acc_holder_data, headers=['Username', 'PIN', 'Last updated on', 'Balance']))
    print("\n                                Press '0' to go back")
    next_step = input("\n")
    answer_loop = True
    while answer_loop:
        if next_step == "0":
            admin_login(username, pin)
            answer_loop = False
        else:
            print("Press'0' to go back")


def admin_login(username, pin):
    """
    Opens a panel for admin to view all users, delete a user and to logout.
    """
    clear()
    print(heading_art.logo)
    print("\n\nWELCOME ADMIN")
    print("\n1. View all account holders")
    print("\n2. Delete an account")
    print("\n3. Check account of a user")
    print("\n4. Log out")

    selection_loop = True
    while selection_loop:

        admin_choice = input(">>")
        # View all account holders
        if admin_choice == "1":
            selection_loop = False
            view_acc_holders(username, pin)
        # Delete an account
        elif admin_choice == "2":
            print("\nTo delete an account, Please enter the username")
            user_to_delete = input(">>").capitalize()
            # Get the name in database
            stored_names = PersonalDetails.find(user_to_delete, in_column=1)

            if stored_names:
                admin_delete_acc(user_to_delete, pin)
                selection_loop = False
            elif user_to_delete == "0":
                sleep(1)
                admin_login(username, pin)
                break
            else:
                print("\nUser not found")
                break
        # View the account of user
        elif admin_choice == "3":
            clear()
            print("\nEnter the username for the account you want to see.")
            account_un = input(">>").capitalize()
            # Searches the username in Database
            get_name = PersonalDetails.find(account_un, in_column=1)
            if get_name:
                clear()
                print(heading_art.logo)
                print("\nLOADING DATA.....\n\n")
                sleep(2)
                # Finds the user's individual worksheet.
                full_data = SHEET.worksheet(account_un)
                full_data_arr = full_data.get_all_values()
                acc_holder_data = full_data_arr[1:]
                print(tabulate(acc_holder_data, headers=['Date', 'Deposit', 'Withdraw', 'Balance', 'PIN satus']))
                answer_loop = True
                while answer_loop:
                    answer = input("\n\nType '0' to go back\n")
                    if answer == "0":
                        admin_login(username, pin)
                        answer_loop = False
                    else:
                        input("\n\nType '0' to go back\n")

            else:
                print("\nUser not found")
                break

        elif admin_choice == "4":
            logging_out()
            sleep(2)
            welcome()
            break
        elif admin_choice == "0":
            admin_login(username, pin)
            sleep(2)
            welcome()
            break
        else:
            print("\n Invalid Input.Please try again ")
            sleep(2)
            admin_login(username, pin)


def login_account():
    clear()
    print(heading_art.logo)
    print("\n\nEnter your username to login:")
    entered_username = input(">>").capitalize()
    print("\nEnter your PIN :")
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
            print("\nUSERNAME OR PIN INCORRECT")
            sleep(1)
            welcome()
    else:
        print("\nUSERNAME OR PIN INCORRECT")
        sleep(1)
        welcome()


def welcome():
    """
    Displays the welcome message when the user opens the website

    """
    clear()
    print(heading_art.logo)
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
            sleep(2)
            welcome()


def main():
    welcome()


main()

