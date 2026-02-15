def main():
    names, ranks, divisions, ids = init_database()
    
    
def init_database():
    names = ["James T. Kirk", "Spock", "Jean-Luc Picard", "Data", "Kathryn Janeway"]
    ranks = ["Captain", "Lt. Commander", "Captain", "Lt. Commander", "Captain"]
    divisions = ["Command", "Science", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "S179-276", "289-49-16-JLP", "034-756-319-SPD", "927-20-40-52-T"]

    return names, ranks, divisions, ids



main()