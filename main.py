from soldier_manager import add_soldier,remove_soldier,get_all_soldiers
from duty_manager import add_duty_to_soldier,update_duty_status,get_soldier_duties
import time
import os

def show_menu() -> None:
    print(f"1. add soldier enter 1\n"
          f"2. delete soldier from the system enter 2\n"
          f"3. show list of all soldiers enter 3\n"
          f"4. add duty for soldier enter 4\n"
          f"5. update duty's status enter 5\n"
          f"6. show soldier's dutys enter 6\n"
          f"7. enter exit or 7 for close the system ")

def get_user_choice() -> str:
    user_input = input("please enter your choice: ")
    return user_input


def handle_add_soldier() -> None:
    new_id = int(input("please enter the new soldier's id: "))
    new_name = input("please enter the soldier's name: ")
    try:
        add_soldier(new_id,new_name)
        print("Soldier added successfully✅")
    except ValueError as error:
        print(f"error: {error}❌")

def handle_remove_soldier() -> None:
    soldier_id = int(input("please enter soldier's id for remove: "))
    try:
        remove_soldier(soldier_id)
        print("Soldier successfully removed✅")
    except KeyError as error:
        print(f"oops error❌: {error}")

def handle_view_soldiers() -> None:
    list_soldiers = get_all_soldiers()
    for soldier in list_soldiers:
        print(soldier)


def handle_add_duty() -> None:
    soldier_id = int(input("please enter soldier's id: "))
    duty_name = input("please enter the name of duty: ")
    day = input("please enter the day of duty: ")
    try:
        add_duty_to_soldier(soldier_id,duty_name,day)
        print("The duty added successfully✅ ")
    except KeyError as Key_error:
        print(f"oops error❌: {Key_error}")
    except ValueError as Val_error:
        print(f"oops error❌: {Val_error}")


def handle_update_duty_status() -> None:
    soldier_id = int(input("please enter soldier's id: "))
    duty_name = input("please enter the name of duty: ")
    new_status = input("please enter the new status for the duty: ")
    try:
        update_duty_status(soldier_id,duty_name,new_status)
        print("The operation was successful.✅")
    except KeyError as Key_error:
        print(f"oops error❌: {Key_error}")
    except ValueError as Val_error:
        print(f"oops error❌: {Val_error}")


def handle_view_soldier_duties() -> None:
    soldier_id = int(input("please enter soldier's id: "))
    try:
        print(get_soldier_duties(soldier_id))
    except KeyError as Key_error:
        print(f"oops error❌: {Key_error}")

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main() -> None:
    while True:
        show_menu()
        user_choice = get_user_choice()
        if user_choice == "1":
            handle_add_soldier()
        elif user_choice == "2":
            handle_remove_soldier()
        elif user_choice == "3":
            handle_view_soldiers()
        elif user_choice == "4":
            handle_add_duty()
        elif user_choice == "5":
            handle_update_duty_status()
        elif user_choice == "6":
            handle_view_soldier_duties()
        elif user_choice == "7" or user_choice == "exit":
            print("good bye")
            break
        else:
            print("Please select an existing option.")

        if user_choice != "3" and user_choice != "6":
            time.sleep(3)
            clear_terminal()
main()