# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ] 

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Python Project')

def get_habit_data():
    """
    Get habit data for the user.
    """
    print("Please Enter an option below")
    print("1. Enter a new habit")
    print("2. View all habits")
    print("4. Add a habit")
    print("5. Delete a habit")
    print("6. Exit\n")
    data_str = input("Enter your Choice here: ")
    print(f"The data provided is {data_str}")


get_habit_data()
