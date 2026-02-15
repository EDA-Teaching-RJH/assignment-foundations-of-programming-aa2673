def main():
    names, ranks, divisions, ids = init_database()
    display_menu(names,ranks,divisions,ids)
    
def display_menu(names,ranks,divisions,ids):
    print("Initialising System... \nInitialisation Complete. \nFleet Manager Online.")
    while True:
        username = input("What is your full name: ").strip().title()
        if username == "":
            print("Please enter a valid name")
        else:
            print("\nWelcome", username)
            break
                
    
    while True:
        print("\n---MENU--- \n1. Add Member \n2. Remove Member \n3. Update Rank \n4. Display Roster \n5. Search Crew \n6. Filter Crew by division \n7. Calculate Payroll \n8. Count Officers \n9. Exit ")
        choice = input("Select an option: ")
        if choice == "1":
            add_member(names,ranks,divisions,ids)
        elif choice == "2":
            remove_member(names,ranks,divisions,ids)
        elif choice == "3":
            update_rank(names,ranks,divisions,ids)
        elif choice == "4":
            display_roster(names,ranks,divisions,ids)
        elif choice == "5":
            search_crew(names,ranks,divisions,ids)
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
    
        systemCheck = 1
        if systemCheck > 0:
            print("\nSystems Operational")
        else:
            print("\nCritical failure")
        if len(names) > 0:
            print("System contains active data")
        else:
            print("System contains no data")
        
        loading = 1
        while loading > 0:
            print("Please wait...")
            break

def init_database():
    names = ["James T. Kirk", "Spock", "Jean-Luc Picard", "Data", "Kathryn Janeway"]
    ranks = ["Captain", "Lieutenant Commander", "Captain", "Lieutenant Commander", "Captain"]
    divisions = ["Command", "Science", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "S179-276", "289-49-16-JLP", "034-756-319-SPD", "927-20-40-52-T"]

    return names, ranks, divisions, ids

def add_member(names,ranks,divisions,ids):
    validRanks = ["Fleet Admiral","Admiral", "Vice Admiral", "Rear Admiral", "Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign", "Cadet"]
    while True:
        escape = input("Press N to return to menu or Y to continue: ").upper()
        if escape == "N":
            break
        elif escape == "Y":
            newMemberName = input("\nNew members' name: ").strip().title()
            newMemberRank = input("New members' rank: ").strip().title()
            newMemberDivision = input("New members' division: ").strip().title()
            newMemberId = input("New members' ID: ").upper()
            if newMemberName != "" and newMemberRank in validRanks and newMemberDivision != "" and newMemberId not in ids:
                names.append(newMemberName)
                ranks.append(newMemberRank)
                divisions.append(newMemberDivision)
                ids.append(newMemberId)
                print("New member added.")
                break
            else:
                print("Invalid please try again.")

def display_roster(names,ranks,divisions,ids):
    print("\nCurrent Crew:")
    print(f"{'Name':<30} {'Rank':<30} {'Division':<30} {'ID':<30}")
    for i in range(len(names)):
        print(f"{names[i]:<30} {ranks[i]:<30} {divisions[i]:<30} {ids[i]:<30}")

def remove_member(names,ranks,divisions,ids):
    while True:
        escape = input("Press N to return to menu or Y to continue: ").upper()
        if escape == "N":
            break
        elif escape == "Y":
            remove = input("Enter the ID of the crew member you'd like to remove: ").upper()
            if remove in ids:
                rmv = ids.index(remove)
                names.pop(rmv)
                ranks.pop(rmv)
                divisions.pop(rmv)
                ids.pop(rmv)
                print("Crew member removed")
                break
            else:
                print("ID not found among existing crewmates")

def update_rank(names,ranks,divisions,ids):
    validRanks = ["Fleet Admiral","Admiral", "Vice Admiral", "Rear Admiral", "Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign", "Cadet"]
    while True:
        escape = input("Press N to return to menu or Y to continue: ").upper()
        if escape == "N":
            break
        elif escape == "Y":
            update = input("Enter the ID of the crew member whose rank you'd like to update: ").upper()
            if update in ids:
                findMember = ids.index(update)
                break
            else:
                print("Invalid ID")
        while True:
            rankUpdate = input("What rank would you like to change " + ranks[findMember] + " " + names[findMember] + " to: ").strip().title()
            if rankUpdate in validRanks:
                ranks[findMember] = rankUpdate
                print("Crew member's rank has been updated.")
                break
            else:
                print("Invalid rank")
            

def search_crew(names,ranks,divisions,ids):
    while True:
        escape = input("Press N to return to menu or Y to continue: ").upper()
        if escape == "N":
            break
        elif escape == "Y":
            searchTerm = input("What would you like to search crew members by Name, Rank, Division or Id: ").strip().title()
            if searchTerm == "Name":
                nameSearch = input("Enter the name you'd like to search for: ").strip().title()
                if nameSearch in names:
                    name = names.index(nameSearch)
                    print("Crew member details\nName: " + names[name] + " \nRank: " + ranks[name] + " \nDivision: " + divisions[name] + " \nID: "+ ids[name]) 
                    break
                else:
                    print("No crew members of this name exist")
            elif searchTerm == "Rank":
                rankSearch = input("Enter the rank you'd like to search for: ").strip().title()
                rankFound = False
                for i in range(len(ranks)):
                    if rankSearch == ranks[i]:
                        rank = i
                        print("\n"+ rankSearch, "Rank Crew member details\nName: " + names[rank] + " \nRank: " + ranks[rank] + " \nDivision: " + divisions[rank] + " \nID: "+ ids[rank]) 
                        rankFound = True
                        
                if not rankFound:
                    print("No crew members of this rank exist")
            elif searchTerm == "Division":
                divSearch = input("Enter the division you'd like to search for: ").strip().title()
                divFound = False
                for d in range(len(divisions)):
                    if divSearch == divisions[d]:
                        div = d
                    
                        print("\n"+ divSearch, "Division Crew member details\nName: " + names[div] + " \nRank: " + ranks[div] + " \nDivision: " + divisions[div] + " \nID: "+ ids[div]) 
                        divFound = True
                if not divFound:
                    print("No crew members of this division exist")
            elif searchTerm == "Id":
                idSearch = input("Enter the ID you'd like to search for: ").upper()
                if idSearch in ids:
                    id = ids.index(idSearch)
                    print("Crew member details\nName: " + names[id] + " \nRank: " + ranks[id] + " \nDivision: " + divisions[id] + " \nID: "+ ids[id]) 
                    break
                else:
                    print("No crew members with this ID exist")
            else:
                print("Please enter a valid search parameter")
main()