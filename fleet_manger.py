def main():
    ## Asking the user for their name and what th require to be done by the system
    First_name = input("What is your first name ")
    last_name = input("What is your last name")
    print("Welcome", First_name+last_name, 
          "1. Check curent memebrs" \
          "2. Add a member" \
          "3. Remove a member " \
          "4. Update the Ranks " \
          "5. Search Crew" \
          "6. Filter by divisions " \
          "7. Calculate payroll" \
          "8. Count officers Ranks ")
    
## User validation 
    Option = int(input("Pick from the optios above what you would like to do "))
    while Option > 8 and Option < 0:
        Option = int(input("Pick from the optios above what you would like to do "))
    
    init_databse()

## Taking theusers input ad taking it to the right function 
    if Option == 1:
       Display_roster()
    elif Option == 2:
        Add_member()
    elif Option == 3:
        Remove_member()
    elif Option == 4:
        Update_Ranks()
    elif Option == 5:
        Search_Crew
    elif Option == 6:
        Filter_by_division()
    elif Option == 7:
        Calculate_payroll()
    elif Option == 8:
        Count_officers()
    elif Option == 9:
        print("Shutting down")
        break
    else:
         print("Invalid")

def Display_roster():
    print("Current team members")
    for i in range(len(Names)):
                print(Names[i] + " - " + Ranks[i] + " - " + Divisions[i] + " - " + IDs[i]) 
    

def init_databse():
    Names=["Michael Burnham", "Christopher Pike", "Kathryn Janeway", "Tom Paris", "Benjamin Sisko"]
    Ranks=["Commander", "Captian", "Captain", "Lietenant", "Commander"]
    Divisions=["Science", "Command", "Command", "Helm", "Command"]
    IDs=["DS0001","DS0002","VOY001", "VOY002", "DS9003"]
    return Names
    return Ranks
    return Divisions
    return IDs  


main()