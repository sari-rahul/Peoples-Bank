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






















