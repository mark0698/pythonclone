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
    while True:
        print("Please Enter an option below")
        print("1. Enter a new habit")
        print("2. View all habits")
        print("3. Add a habit")
        print("4. Delete a habit")
        print("5. Exit\n")
        data_str = input("Enter your choice here: ")
        
        if data_str == "1":
            enter_new_habit()
        elif data_str == "2":
            view_all_habits()
        elif data_str == "3":
            add_habit()
        elif data_str == "4":
            delete_habit()
        elif data_str == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def enter_new_habit():
    new_habit = input("Enter the name of your new habit: ")
    SHEET.append_row([new_habit])
    print(f"Habit '{new_habit}' added successfully!")

    get_habit_data()