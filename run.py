import gspread
from google.oauth2.service_account import Credentials 
from datetime import datetime 
from colorama import init, Fore, Style

# Initialize colorama
init()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
] 

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Python Project')
habits = SHEET.worksheet('habits')
completion_data = SHEET.worksheet('percentage of completion')  
start_dates = SHEET.worksheet('start dates')

def get_habit_data():
    while True:
        print(f"{Fore.GREEN}Please Enter an option below{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Add a new habit{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Add a successful day to a habit{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Add an unsuccessful day to a habit{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. View all habits{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Delete a habit{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}6. View completion percentage for a habit{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}7. View habit progress (start date and success percentage){Style.RESET_ALL}")
        print(f"{Fore.YELLOW}8. Exit{Style.RESET_ALL}\n")
        data_str = input("Enter your choice here: ")
        
        if data_str == "1":
            enter_new_habit()
        elif data_str == "2":
            add_successful_day()
        elif data_str == "3":
            add_unsuccessful_day()
        elif data_str == "4":
            view_all_habits()
        elif data_str == "5":
            delete_habit()
        elif data_str == "6":
            view_completion_percentages()
        elif data_str == "7":
            view_habit_progress()
        elif data_str == "8":
            print(f"{Fore.GREEN}Exiting the program.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")


def enter_new_habit():
    new_habit = input("Enter the name of your new habit: ")
    new_habit_lower = new_habit.lower()
    
    all_habits = habits.get_all_values()
    existing_habits = [habit[0].lower() for habit in all_habits]
    
    if new_habit_lower in existing_habits:
        print(f"{Fore.RED}Habit '{new_habit}' already exists.{Style.RESET_ALL}")
        return
    
    start_date_str = input("Enter the start date for your habit (DD/MM/YYYY): ")
    
    try:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y")  
    except ValueError:
        print(f"{Fore.RED}Invalid date format. Please use DD/MM/YYYY.{Style.RESET_ALL}")
        return  
    
    habits.append_row([new_habit_lower])
    print(f"{Fore.GREEN}Habit '{new_habit}' added successfully!{Style.RESET_ALL}")
    
    start_dates.append_row([new_habit_lower, start_date.strftime('%d/%m/%Y')]) 
    print(f"{Fore.GREEN}Start date '{start_date.strftime('%d/%m/%Y')}' for habit '{new_habit}' recorded successfully!{Style.RESET_ALL}")


def view_all_habits():
    all_habits = habits.get_all_values()
    if all_habits:
        print(f"{Fore.BLUE}Your habits:{Style.RESET_ALL}")
        for habit in all_habits:
            print(f"{Fore.CYAN}{habit[0]}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}You have no habits recorded.{Style.RESET_ALL}")

def delete_habit():
    habit_name = input("Enter the name of the habit to delete: ")
    all_habits = habits.get_all_values()
    habit_found = False
    
    for i, habit in enumerate(all_habits):
        if habit[0].lower() == habit_name.lower():  
            habits.delete_rows(i + 1)  
            print(f"{Fore.GREEN}Habit '{habit[0]}' deleted successfully!{Style.RESET_ALL}")
            habit_found = True
            break
    
    if not habit_found:
        print(f"{Fore.RED}Habit '{habit_name}' not found.{Style.RESET_ALL}")

def view_completion_percentages():
    habit_name = input("Enter the name of the habit you want the completion percentage for: ")
    completion_records = completion_data.get_all_values()
    
    habit_found = False
    for record in completion_records:
        if record[0].lower() == habit_name.lower():  
            completion_percentage = record[1]
            print(f"{Fore.MAGENTA}Completion percentage for '{record[0]}': {completion_percentage}%{Style.RESET_ALL}")
            habit_found = True
            break
    
    if not habit_found:
        print(f"{Fore.RED}No completion data found for habit '{habit_name}'.{Style.RESET_ALL}")

def view_habit_progress():
    habit_name = input("Enter the name of the habit you want to check progress for: ")
    habit_name_lower = habit_name.lower()  
    start_dates_records = start_dates.get_all_values()
    habit_found = False

    for record in start_dates_records:
        if record[0].lower() == habit_name_lower:  
            start_date_str = record[1] 
            habit_found = True
            break

    if not habit_found:
        print(f"{Fore.RED}No start date found for habit '{habit_name}'.{Style.RESET_ALL}")
        return


    completion_records = completion_data.get_all_values()
    success_percentage = None

    for record in completion_records:
        if record[0].lower() == habit_name_lower:  
            success_percentage = record[1]  
            break

    if not success_percentage:
        print(f"{Fore.RED}No completion data found for habit '{habit_name}'.{Style.RESET_ALL}")
        return


    try:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y") 
        current_date = datetime.now()  
        days_since_start = (current_date - start_date).days 
    except ValueError:
        print(f"{Fore.RED}Invalid date format for habit '{habit_name}'. Expected format: DD/MM/YYYY.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}Habit: {habit_name}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Start Date: {start_date.strftime('%d/%m/%Y')}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Days since start: {days_since_start} days{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Success Percentage: {success_percentage}%{Style.RESET_ALL}\n")

def add_successful_day():
    habit_name = input("Enter the habit for which you want to add a successful day: ")
    completion_records = completion_data.get_all_values()
    
    for i, record in enumerate(completion_records):
        if record[0].lower() == habit_name.lower(): 
            successful_days = int(record[2])  
            unsuccessful_days = int(record[3])  
            successful_days += 1  
            
            completion_data.update_cell(i + 1, 3, successful_days)  
            print(f"{Fore.GREEN}Added a successful day for '{habit_name}'. Total successful days: {successful_days}{Style.RESET_ALL}")
            return

    print(f"{Fore.RED}Habit '{habit_name}' not found in completion data.{Style.RESET_ALL}")

def add_unsuccessful_day():
    habit_name = input("Enter the habit for which you want to add an unsuccessful day: ")
    completion_records = completion_data.get_all_values()
    
    for i, record in enumerate(completion_records):
        if record[0].lower() == habit_name.lower(): 
            successful_days = int(record[2])  
            unsuccessful_days = int(record[3])  
            unsuccessful_days += 1  
            
            completion_data.update_cell(i + 1, 4, unsuccessful_days) 
            print(f"{Fore.GREEN}Added an unsuccessful day for '{habit_name}'. Total unsuccessful days: {unsuccessful_days}{Style.RESET_ALL}")
            return

    print(f"{Fore.RED}Habit '{habit_name}' not found in completion data.{Style.RESET_ALL}")

get_habit_data()