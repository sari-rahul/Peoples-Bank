import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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


def main():
    print("\n\n    WELCOME TO PEOPLES BANK      ")
    print("----------------------------------")
    
    print("\n\nWHICH OF THE FOLLOWING SERVICES DO YOU WANT TO ACCESS ??\n\n")
    print("1.Open New Account\n"
          "2.Deposit Amount\n"
          "3.Withdraw Amount\n"
          "4.Balance Enquiry\n"
          "5.Show Customer Details\n"
          "6.Close an Account")

          
main()