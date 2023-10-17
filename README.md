# PEOPLES BANK
Peoples Bank is a python based online banking application which allows the user to create an account, login to the account, deposit money, withdraw money, check their account balance, change their PIN number and delete their account if needed.
This application also allows the admins to login, view all the users having account, view te account details of any particular person and to delete any particular account.

* [Live site](https://peoples-bank-2e284f64d1c0.herokuapp.com/)

* ![Responsive Mockup]()

## Contents
* [**Project**](#project)
    * [User Stories](#user-stories)
        * [First Time User](#first-time-user)
        * [Return User](#return-user)
    * [Site Owner Goals](#site-owner-goals)
* [**User Experience**](<#user-experience-ux>)
    * [Site Structure](<#site-structure>)
    * [Data Model](<#data-model>)

* [**Features**](#features)
    * [Existing Features](<#existing-features>)
        * [Login](<#login>)
        * [Create Account](<#create-account>)
        * [Account Welcome Page](<#account-home>)
        * [Deposit Amount](<#Deposit-Amount>)
        * [Check your Account Balance](<#Check-your- Account-Balance>)
        
        * [Withdraw Amount](<#Withdraw-Amount>)
        * [Know your PIN](<#Know -your-PIN>)
        * [Change your PIN](<#Change-your-pin>)
        * [Logout](<#Logout>)
        * [Delete Account](<#delete-account>)
        * [Admin Welcome Page](<#admin-welcome-page>)
        * [Admin: View all users](<#admin-view-all-users>)
        * [Admin: Delete a User](<#admin-delete-a-user>)
        * [Check account of a user](<#Check-acc-of-a-user>)
        * [Admin Log out](<#Logout>)        
    
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Libraries](<#libraries>)
    * [Resources](<#resources>)
* [**Testing**](<#testing>)
    * [Bugs](<#bugs>)
        * [Solved Bugs](<#solved-bugs>)
        * [Unsolved Bugs](<#unsolved-bugs>)
    * [Validator Testing](<#validator-testing>)
    * [Peer Testing](<#peer-testing>)
* [**Deployment**](<#deployment>)
    * [Heroku Deployment](<#heroku-deployment>)
    * [To Fork the Project](<#to-fork-the-project>)
    * [To Clone the Project](<#to-clone-the-project>)
* [**Credits**](<#credits>)
    * [Content](<#content>)
    * [Technical](<#technical>)
* [**Acknowledgements**](<#acknowledgements>)

## Project
### User Stories
#### First Time User
A first time user can :
- Create an account
- Deposit some amount
- Know their PIN 
- Log out.

#### Return Users
A return user can :
- Login to Account
- Check their Balance
- Change their PIN
- Withdraw amount
- See their recent transactions
- Close their account

#### Site owner goals
As the site owner you may want:
- To access the Admin's page 
- See the login details of all the users
- See the account details of each user
- Delete any account

[Back to top](<#contents>)

### User Experience (UX)

#### Site Structure
The site displays a welcome page at the beginning which displays two options:
- Login
- Create a new account

After logging in the user is taken to the account home page where the following panel is displayed:

- Deposit Amount 
- Check your Account Balance
- Withdraw Amount
- Know your PIN
- Change your PIN
- Delete  your Account

If an admin enters the website the following panel is displayed:

- View all account holders
- Delete an account
- Check account of a user
- Log out

#### Data Model
Google sheets were used to store and access user data.There are two types of google sheets:
 
 - for all users details
 - for each user

 The sheet with all users details contains:

 - Name
 - PIN
 - Last updation date
 - Balance

 The sheet for individual user contains:

 - Date
 - Deposit
 - Withdraw
 - Balance
 - PIN status

 [Back to top](<#contents>)

 #### Design

* Logo

The bank's logo is displayed on each page and ascii atr generator was used for this.

![Logo]()

* Tables

The tabulate module was used to display information in tables.The following are displayed in tables:
    
  - Admin views all users
  - Admin view any users full account
  - User views recent transactions

  ### FEATURES
  #### Existing Features
On entering into the website the bank's logo is displayed and the user is given two options.

1. Login
2. Create a new account

insert image

#### Create a new account

If the user is a first time user, he has to create an account by selecting a username.The username is unique for each user and appropriate error message is displayed on entering :

- already existing username
- if it begins with a number
- if it contains space
- characters less than 4 and more than 10

After validating the username, the PIN is automatically generated and a worksheet entiteled to username is generated populated with:

- Date 
- Deposit
- Withdraw
- Balance
- PIN status.
The username and PIN is displayed on the screen.


#### Login

All the users have to login to their account, to attain the services.

To login, the username and PIN is asked and both are cross checked.

If they are found correct, the user is taken to the home page of their account.

#### 1. Account Home Page

The home page contains the following options:
    
            0: Log out

            1:Deposit Amount

            2:Check your Balance

            3:Withdraw amount

            4:Know your PIN

            5:Change your PIN

            6:Your recent transactions

            7:Delete your account

insert image

#### Deposit Amount
---

The user can deposit amount into their account here. They will be asked the amount they want to deposit and a confirmation message will be displayed after depositing the amount sucessfully. Then the user returns to home page automatically.

An appropriate error message will be displayed, if the user enters:

- Negative numbers
- Number Zero
- Any value other than numbers

If the user enters float values of more than two decimal numbers, it will be rounded to two digits before entering the database.

insert image

#### Check your Balance
---

The user can check their account balance here. The current balance will be displayed and then they will be taken back to the home page.

insert image

#### Withdraw Amount
---
The user can withdraw thier funds from their account as per need.They will be prompted about the amount the want to withdraw. The input is validated and a appropriate error message is displayed if:

- The value is non-numeric
- Negative value
- Zero value
- Greater than their account balance

insert image

#### Know your PIN
---
If the user wants to know their PIN ,they can check it here,as it is needed to delete their account.

insert image

#### Change Your PIN
---
If the user finds it difficult to remember his PIN,he can change his PIN here.

He will be given two options here:

1. Enter a PIN of your choice
2. Get a new PIN

The user can either select a PIN of his choice or can generate a new PIN number as per his comfort.
A confirmation message will be displayed after the PIN has been changed and the user will be taken back to the home page.

The new PIN will be updated in the Worksheet with the details of clients and in the PIN status column in user's individual worksheet will be updated with 'PIN changed'.

insert image

#### Your recent Transactions
---
The user can check their recent transactions here.
The last ten transactions with the particular date will be displayed in table format.

insert image

#### Delete your account
---
The user can delete his account, but as it cannot be reversed the user has to confirm it by typing 'y' followed by PIN. 

If he types 'n', he will be taken back to the home page, else a message will be displayed saying their account has been sucessfully deleted.

insert image

#### Log out
---

The user can log out from the home page by clicking '0'. To keep them safe, a 'Logging out' message will be displayed and they will be taken to the Login page.

#### Admin: Home page
---
This website also provides access to admin.The admin can view all account holders username, PIN, last updation date and Current Balance. This is accessible from the login page by entering 'admin' as username and '9053' as PIN.once the admin logs in a menu is displayed with the fillowing content:

* View all account holders
* Delete an account
* Check account of a user
* Log out

insert image

#### Admin :View all account holders
---
The Admin can view  a list of all account holders in a tabulated form with username, PIN, last updated date and Balance

insert image

#### Admin :Delete an account
---
The admin can delete any user's account.To delete the account ,admin has to enter the username and he will be prompted again 'Are you sure the account should be deleted?'.If 'y' is enterd the account will be deleted otherwise it will go back to the home page.

insert image

#### Admin :Check account of a user
---
The admin can check any user's account by entering their username.After entering the username the entire account transaction will be displayed in tabuar form. It includes each transaction with respective date and changes in PIN.

insert image

#### Admin :Log out
---
The admin can safely Log out by selecting the respective option in the menu.

[Back to top](<#contents>)

## Technologies Used
---
#### Languages used
- Python is used for the full funtionality of the website.

#### Libraries used
---

- [gspread](https://docs.gspread.org/en/v3.7.0/api.html) to link up the Google Sheet.
- [credentials](https://pypi.org/project/credentials/) to link the Google Sheet.
- [random](https://docs.python.org/3/library/random.html) to generate a 4 digit random PIN.
- [os](https://www.geeksforgeeks.org/clear-screen-python/) to clear the terminal.
- [datetime](https://docs.python.org/3/library/datetime.html) to get current date
- [time](https://www.programiz.com/python-programming/time/sleep) for the sleep function.
- [Tabulate](https://pypi.org/project/tabulate/) to put data in a table
- [TAAG](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) for the logo.

#### Resources
---

- [Github](<https://github.com/>) to store the code.
- [Heroku](<https://heroku.com/>)
- [Codeanywhere](<https://app.codeanywhere.com/) to write the code.
- [Am I Responsive?](<https://ui.dev/amiresponsive>) for the display image across devices.
- [Stack Overflow](<https://stackoverflow.com/>) for general troubleshooting.
- [W3 Schools](<https://www.w3schools.com/>) for general troubleshooting.
- [MDN Web Docs](<https://developer.mozilla.org/en-US/>) for general troubleshooting.
- [Google Sheets](<https://www.google.co.uk/sheets/about/>) for the spreadsheet used to store the customer data.

[Back to top](<#contents>)

## Testing
---
### Bugs
#### Solved bugs

- A user could enter empty spaces as username, I needed enter one more validation to correct it.
- In withdraw amount() the user could enter a non numeric value, later I added an isalpha() as condition to clear it.
- Repetition of username was possible which lead to multiple sheet with same username.It was removed but adding a condition that makes sure that same username is not present in the database.
- In withdraw amount() negative value and zero was possible to be entered.Later it was removed by adding two if conditions.
- Deposit amount() could also take negative numbers and zero value, It was removed by passing if conditions.
- Deposit amount() had an answer loop wchich did not display the question but only the input area.It was correted by altering the loop.
- Initially account welcome page() had no way to exit and go back to login page. A condition with '0 to log out' was added to correct it.
- The recent transaction() was displaying the first 10 transactions initialy. Added [-10:] to slice the last 10 values.
- Exiting from recent transaction was not possible which was corrected by adding a condition with 'Enter 0 to exit' condition.
- Float values could not be entered in deposit amount() and withdraw amount().It was corrected by adding turn to currency() which converts the amount to float value with two decimal digits.

#### Unsolved bugs
- No known Bugs


[Back to top](<#contents>)

### Validator Testing
![PEP8](code pep8)

- No errors were found by PEP8 validator
- There were only notifications regarding lines too long.As these won't affect the terminal view I decided to leave it to make the code easier to understand.

[Python Validator](https://extendsclass.com/python-tester.html)

- No errors found in python validator.

### Peer Testing

Apart from myself, this program was tested by the following users for bugs and usability
- Rahul Mulakkal
- Ramsankar Adampurath

All of them passed all the tested without any bugs.The following tests were carried out:

| Function                    | Test                                           | Result |
|-----------------------------|------------------------------------------------|--------|
|welcome | Enter incorrect value| Error message displayed and asks again to enter value|
|   | Enter value '1' | The user is asked to enter  their username|
|   | Enter value '2' | The user is asked to select a username |
|   |   |   |
| Login :  Enter Username | Enter invalid username or PIN | Error message displayed and asks again to enter username and PIN |
|   | Enter invalid username and PIN | Error message displayed and asks again to enter username and PIN |
|   | Enter incorrect username and correct PIN | Error message displayed and asks again to enter username and PIN |
|   | Enter correct username and incorrect PIN | Error message displayed and asks again to enter username and PIN |
|   | Enter correct username and PIN | Loading account... is displayed and the user is taken to account's home page |
|   |   |   |
| Account Home page |Entered an invalid input (alphabets,symbols,space,nos. other than the one in menu) | Error message displayed and asks again to enter option |
|   | Enter '1'| The user is taken to Deposit amount page |
|   | Enter '2'| The user is taken to Check your account balance page |
|   | Enter '3'| The user is taken to Check your Withdraw amount page |
|   | Enter '4'| The user is taken to Check your Know your PIN page |
|   | Enter '5'| The user is taken to Check your Change your PIN page |
|   | Enter '6'| The user is taken to Check your Your recent Transactions page |
|   | Enter '7'| The user is taken to Check your Delete your account page |
|   | Enter '0'| The user is taken to Check your Logging out page |
|   |   |   |
| Create Account | Enter a username below 4 characters| Error message displayed and user can try again|
|    |Enter a username over 10 characters            | Error message displayed and user can try again  |
|    |Enter username containing whitespace           | Error message displayed and user can try again |
|    | Enter a username beginning with a non letter  |  Error message displayed and user can try again |
|    | Enter '0'                                     | The user is asked for the username to login and the login function is run. |
|    | A valid username is entered                    | The users username and PIN is displayed, then they are taken to the login screen. |






























