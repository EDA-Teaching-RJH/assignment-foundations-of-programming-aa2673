def main():
    names, ranks, divisions, ids = init_database()
    display_menu(names,ranks,divisions,ids)
    
def display_menu(names,ranks,divisions,ids):
    print("Initialising System... \nInitialisation Complete. \nFleet Manager Online.")
    while True:
        username = input("What is your full name: ").strip().title()
        if username == "":
            print("Invalid Name")
        else:
            print("\nWelcome", username)
            break
                
    
    while True:
        print("\nCurrently logged in:", username)
        print("\n---MENU--- \n1. Add Member \n2. Remove Member \n3. Update Rank \n4. Display Roster \n5. Search Crew \n6. Filter Crew by division \n7. Calculate Payroll \n8. Count Officers \n9. Exit ")
        choice = input("Select an option: ")
        if choice == "1":
            add_member(names,ranks,divisions,ids)
        elif choice == "2":
            remove_member(names,ranks,divisions,ids)
        elif choice == "3":
            update_rank(names,ranks,ids)
        elif choice == "4":
            display_roster(names,ranks,divisions,ids)
        elif choice == "5":
            search_crew(names,ranks,divisions,ids)
        elif choice == "6":
            filter_division(names,divisions)
        elif choice == "7":
            calculate_payroll(ranks)
        elif choice == "8":
            count_officers(ranks)
        elif choice == "9":
            print("Shutting Down...")
            break
        else:
            print("Invalid choice")
    
        systemCheck = 1
        if systemCheck > 0:
            print("\nSystems Operational")
        else:
            print("\nCritical failure")
        if len(names) > 0:
            print("System contains active data")
        else:
            print("System contains no data")
        
        

def init_database():
    names = ["Kirk", "Spock", "Picard", "Data", "Janeway"]
    ranks = ["Captain", "Lieutenant Commander", "Captain", "Lieutenant Commander", "Captain"]
    divisions = ["Command", "Science", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "S179-276", "289-49-16-JLP", "034-756-319-SPD", "927-20-40-52-T"]

    return names, ranks, divisions, ids

def add_member(names,ranks,divisions,ids):
    while True:
        validRanks = ["Fleet Admiral","Admiral", "Vice Admiral", "Rear Admiral", "Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign", "Cadet"]
        newMemberName = input("\nNew members' name: ").strip().title()
        newMemberRank = input("New members' rank: ").strip().title()
        newMemberDivision = input("New members' division: ").strip().title()
        newMemberId = input("New members' ID: ").upper().strip()
        if newMemberName != "" and newMemberRank in validRanks and newMemberDivision != "" and newMemberId not in ids:
            names.append(newMemberName)
            ranks.append(newMemberRank)
            divisions.append(newMemberDivision)
            ids.append(newMemberId)
            print("New member added.")
            input("\nPress Enter to return to menu...")
            return
            
        else:
            print("Invalid.")
            yn = continue_or_menu()
            if yn == False:
                return

def display_roster(names,ranks,divisions,ids):
    print("\nCurrent Crew:")
    print(f"{'Name':<30} {'Rank':<30} {'Division':<30} {'ID':<30}")
    for i in range(len(names)):
        print(f"{names[i]:<30} {ranks[i]:<30} {divisions[i]:<30} {ids[i]:<30}")
    input("\nPress Enter to return to menu...")
    return

def remove_member(names,ranks,divisions,ids):
    while True:
        remove = input("Enter the ID of the crew member you'd like to remove: ").upper().strip()
        if remove in ids:
            rmv = ids.index(remove)
            names.pop(rmv)
            ranks.pop(rmv)
            divisions.pop(rmv)
            ids.pop(rmv)
            print("Crew member removed")
            input("\nPress Enter to return to menu...")
            return
        else:
            print("ID not found among existing crewmates")
            yn = continue_or_menu()
            if yn == False:
                return

def update_rank(names,ranks,ids):
    validRanks = ["Fleet Admiral","Admiral", "Vice Admiral", "Rear Admiral", "Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign", "Cadet"]
    while True:
        
        update = input("Enter the ID of the crew member whose rank you'd like to update: ").upper().strip()
        if update in ids:
            findMember = ids.index(update)
            
            rankUpdate = input("What rank would you like to change " + ranks[findMember] + " " + names[findMember] + " to: ").strip().title()
            if rankUpdate in validRanks:
                ranks[findMember] = rankUpdate
                print("Crew member's rank has been updated.")
                input("\nPress Enter to return to menu...")
                return

        
            else:
                print("Invalid rank")
                yn = continue_or_menu()
                if yn == False:
                    return
            
        
        else:
            print("Invalid ID")
            yn = continue_or_menu()
            if yn == False:
                return
            
           
            

def search_crew(names,ranks,divisions,ids):
    while True:
        searchTerm = input("What would you like to search crew members by Name, Rank, Division or Id: ").strip().title()
        if searchTerm == "Name":
            nameSearch = input("Enter the name you'd like to search for: ").strip().title()
            if nameSearch in names:
                name = names.index(nameSearch)
                print("Crew member", nameSearch, "details\nName: " + names[name] + " \nRank: " + ranks[name] + " \nDivision: " + divisions[name] + " \nID: "+ ids[name]) 
                input("\nPress Enter to return to menu...")
                return
            else:
                print("No crew members of this name exist")
                yn = continue_or_menu()
                if yn == False:
                    return
        elif searchTerm == "Rank":
            rankSearch = input("Enter the rank you'd like to search for: ").strip().title()
            rankFound = False
            for i in range(len(ranks)):
                if rankSearch == ranks[i]:
                    rank = i
                    print("\n"+ rankSearch, "Rank Crew member details")
                    print("\nName: " + names[rank] + " \nRank: " + ranks[rank] + " \nDivision: " + divisions[rank] + " \nID: "+ ids[rank]) 
                    rankFound = True
            if rankFound:
                input("\nPress Enter to return to menu...")
                return
                    
            if not rankFound:
                print("No crew members of this rank exist")
                yn = continue_or_menu()
                if yn == False:
                    return
        elif searchTerm == "Division":
            divSearch = input("Enter the division you'd like to search for: ").strip().title()
            divFound = False
            for d in range(len(divisions)):
                if divSearch == divisions[d]:
                    div = d
                    print("\n"+ divSearch, "Division Crew member details")
                    print("\nName: " + names[div] + " \nRank: " + ranks[div] + " \nDivision: " + divisions[div] + " \nID: "+ ids[div]) 
                    divFound = True
            if divFound:
                input("\nPress Enter to return to menu...")
                return
            if not divFound:
                print("No crew members of this division exist")
                yn = continue_or_menu()
                if yn == False:
                    return
        elif searchTerm == "Id":
            idSearch = input("Enter the ID you'd like to search for: ").upper().strip()
            if idSearch in ids:
                id = ids.index(idSearch)
                print("Crew member of ID", idSearch, "details\nName: " + names[id] + " \nRank: " + ranks[id] + " \nDivision: " + divisions[id] + " \nID: "+ ids[id]) 
                input("\nPress Enter to return to menu...")
                return
            else:
                print("No crew members with this ID exist")
                yn = continue_or_menu()
                if yn == False:
                    return
        else:
            print("Invalid search parameter")
            yn = continue_or_menu()
            if yn == False:
                return
        


def filter_division(names,divisions):
    while True:
        filter = input("What division would you like to filter the crew members by: ").strip().title()
        matched = False
        for i in range(len(divisions)):
            if filter == divisions[i]:
                print(filter, "Division crew member: " + names[i])
                matched = True
        if matched:
            input("\nPress Enter to return to menu...")
            return
                
                    
        if not matched:
            print("That division does not exist.")
            yn = continue_or_menu()
            if yn == False:
                return
            

def calculate_payroll(ranks):
    validRanks = ["Fleet Admiral","Admiral", "Vice Admiral", "Rear Admiral", "Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign", "Cadet"]
    rankSalary = []
    for i in range(len(validRanks)):
        rankSalary.append(1000 - (100 * i))
    
    crewCost = 0
    for rank in ranks:
        index = validRanks.index(rank)
        crewCost += rankSalary[index]
            
    print("Crew's total salary is", crewCost)
    input("\nPress Enter to return to menu...")
    return

def count_officers(ranks):
    count = 0
    for i in range(len(ranks)):
        if ranks[i] == "Commander" or ranks[i] == "Captain":
            count += 1
    print("There are", count, "officers currently on the crew.")
    input("\nPress Enter to return to menu...")
    return

def continue_or_menu():
    while True:
        yn = input("Press Y to re-enter data or Press X to return to the menu: ").strip().upper()
        if yn == "Y":
            return True
        elif yn == "X":
            return False
        else:
            print("Invalid choice.")

main()