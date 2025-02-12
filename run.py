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
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Python Project')
habits = SHEET.worksheet('habits')
completion_data = SHEET.worksheet('percentage of completion')

def get_habit_data():
    """
    Get habit data for the user.
    """
    while True:
        print("Please Enter an option below")
        print("1. Enter a new habit")
        print("2. View all habits")
        print("3. Delete a habit")
        print("4. View completion percentages")
        print("5. Exit\n")
        data_str = input("Enter your choice here: ")
        
        if data_str == "1":
            enter_new_habit()
        elif data_str == "2":
            view_all_habits()
        elif data_str == "3":
            delete_habit()
        elif data_str == "4":
            view_completion_percentages()
        elif data_str == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def enter_new_habit():
    new_habit = input("Enter the name of your new habit: ")
    habits.append_row([new_habit])
    print(f"Habit '{new_habit}' added successfully!")

def view_all_habits():
    all_habits = habits.get_all_values()
    if all_habits:
        print("Your habits:")
        for habit in all_habits:
            print(habit[0])
    else:
        print("You have no habits recorded.")


def delete_habit():
    habit_name = input("Enter the name of the habit to delete: ")
    all_habits = habits.get_all_values()
    habit_found = False
    for i, habit in enumerate(all_habits):
        if habit[0] == habit_name:
            habits.delete_rows(i + 1)  
            print(f"Habit '{habit_name}' deleted successfully!")
            habit_found = True
            break
    if not habit_found:
        print(f"Habit '{habit_name}' not found.")

    def view_completion_percentages():
    completion_records = completion_data.get_all_values()
    if completion_records:
        print("Completion percentages:")
        for record in completion_records:
            habit_name = record[0]
            completion_percentage = record[1]
            print(f"{habit_name}: {completion_percentage}%")
    else:
        print("No completion data available.")

get_habit_data()