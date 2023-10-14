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
        * [Log out](<#Logout>)        
    
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













