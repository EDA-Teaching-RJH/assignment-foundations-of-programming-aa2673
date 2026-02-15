def main():
    names, ranks, divisions, ids = init_database()
    display_menu()
    
def display_menu():
            print("Initialising System... \nInitialisation Complete. \nFleet Manager Online.")
            while True:
                username = input("What is your full name: ").strip().title()
                if username == "":
                    print("Please enter a valid name")
                else:
                    print("\nWelcome", username)
                    print("\n---MENU--- \n1. Add Member \n2. Remove Member \n3. Update Rank \n4. Display Roster \n5. Search Crew \n6. Filter Crew by division \n7. Calculate Payroll \n8. Count Officers \n9. Exit ")
                    break
                
    
            while True:
                choice = input("\nSelect an option: ")
                if choice == "1":
                    add_member()
                elif choice == "2":
                    remove_member()
                elif choice == "3":
                    update_rank()
                elif choice == "4":
                    display_roster()
                elif choice == "5":
                    search_crew()
                elif choice == "6":
                    filter_division()
                elif choice == "7":
                    calculate_payroll()
                elif choice == "8":
                    count_officers()
                elif choice == "9":
                    print("Shutting Down...")
                    break
                else:
                    print("Invalid choice")
def init_database():
    names = ["James T. Kirk", "Spock", "Jean-Luc Picard", "Data", "Kathryn Janeway"]
    ranks = ["Captain", "Lt. Commander", "Captain", "Lt. Commander", "Captain"]
    divisions = ["Command", "Science", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "S179-276", "289-49-16-JLP", "034-756-319-SPD", "927-20-40-52-T"]

    return names, ranks, divisions, ids



main()