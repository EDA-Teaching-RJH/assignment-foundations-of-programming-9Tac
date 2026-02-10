Names=["Michael Burnham", "Christopher Pike", "Kathryn Janeway", "Tom Paris", "Benjamin Sisko"]
Ranks=["Commander", "Captian", "Captain", "Lietenant", "Commander"]
Divisions=["Science", "Command", "Command", "Helm", "Command"]
IDs=["0001","0002","0003", "0004", "0005"]
    
def main():
    
    ## Asking the user for their name and what th require to be done by the system
    First_name = input("What is your first name ")
    last_name = input("What is your last name")
    print("Welcome", First_name + last_name, 
          "\n 1. Check curent memebrs" 
          "\n 2. Add a member" 
          "\n 3. Remove a member " 
          "\n 4. Update the Ranks " 
          "\n 5. Search Crew" 
          "\n 6. Filter by divisions " 
          "\n 7. Calculate payroll" 
          "\n 8. Count officers Ranks ")
    
## User validation 
    
    
    # init_database(Names, Ranks, Division, IDs)
    while True:
        Option = int(input("Pick from the optios above what you would like to do "))
        while Option > 8 or Option < 0:
            Option = int(input("Pick from the optios above what you would like to do "))

## Taking theusers input ad taking it to the right function 
        if Option == 1:
            Display_roster(Names, Ranks, Divisions, IDs)
        elif Option == 2:
            Add_member(Names, Ranks, Divisions, IDs)
        elif Option == 3:
            Remove_member()
        elif Option == 4:
            Update_Ranks(Names, Ranks, IDs)
        elif Option == 5:
            Search_Crew
        elif Option == 6:
            Filter_by_division()
        elif Option == 7:
            Calculate_payroll()
        elif Option == 8:
            Count_officers()
        else:
            print("Shutting down")

            break
        

def Display_roster(Names, Ranks, Divisions, IDs):
    print("Current team members")
    for i in range(len(Names)):
            print(Names[i] + " - " + Ranks[i] + " - " + Divisions[i] + " - " + IDs[i]) 
    


def Add_member(Names, Ranks, Divisions, IDs):
    Add_Name = str(input("What is the new Members name ")).title()
    Add_Rank = str(input("What is their Rank ")).title()
    Add_Division = str(input("what division are they in "))
    Add_IDs = str(input("what is there ID code"))
    Names.append(Add_Name)
    Ranks.append(Add_Rank)
    Divisions.append(Add_Division)
    IDs.append(Add_IDs)
    return Names, Ranks, Divisions, IDs
     



main()