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
        Option = int(input("Pick from the options above what you would like to do "))
        while Option > 8 or Option < 0:
            Option = int(input("Pick from the options above what you would like to do "))

## Taking theusers input ad taking it to the right function 
        if Option == 1:
            Display_roster(Names, Ranks, Divisions, IDs)
        elif Option == 2:
            Add_member(Names, Ranks, Divisions, IDs)
        elif Option == 3:
            Remove_member(Names, Ranks, Divisions, IDs)
        elif Option == 4:
            Update_Ranks(Names, Ranks, IDs)
        elif Option == 5:
            Search_Crew(Names, Ranks, Divisions, IDs)
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
            print(Names[i] + " - " , Ranks[i] , " - " , Divisions[i] , " - " , IDs[i]) 
    


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
     

def Remove_member(Names, Ranks, Divisions, IDs):
    Member_removed = input("Name to remove: ").title()   
    idex = Names.index(Member_removed)
    Names.pop(idex)
    Ranks.pop(idex)
    Divisions.pop(idex)
    print("Removed,", Member_removed)
    return Names, Ranks, Divisions, IDs

def Update_Ranks(Names, Ranks, IDs):
    try:
        # for i in len(IDs):
        #     idex = int(IDs[i])
        #     if 0 <= idex < len(Names):
        #         print(f"Updating rank for {Names[idex]} (Current: {Ranks[idex]})")
        #         new_rank = input("Enter new rank: ").title()
        #         Ranks[idex] = new_rank
        #         print(f"Rank updated to {new_rank}")
                # idex= int(IDs[int+1])
        index = str(input("enter the ID of the officer for a rank change "))
        for i in range(len(IDs)):
            if IDs[i] == index:
                print(f"Updating rank for {Names[i]} (Current:{Ranks[i]})")
                New_ranks = input("Enter the new rank: ").title()
                Ranks[i] = New_ranks
                print(f"Rank has been updated for {Names[i]} (Rank has been updated to {New_ranks})")
        else:
            print("Invalid ID. No such crew member.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
    return Names, Ranks, IDs

def Search_Crew(Names, Ranks, Divisions, IDs):
    print("What are you searching for \n 1) The Names of the crew members \n 2) The Ranks and the amount of people with that rank \n 3) The divisions in the crew  4)IDs in the crew")
    options = int(input("Which would you like to carry out in this protocal"))
    if options == 1:
        print("Names of the crew members ")
        N0 = 1
        for i in range(len(Names)):
            print(N0, "Crew member: " ,Names[i])
            N0 = N0 + 1
    elif options == 2:
        print("The ranks of the crew ")
        select = int(input(" 1) Finding the ranks \n 2. Finding the amount of people with those ranks"))
        if select == 1:
            print("THe Ranks of the in the crew  \n Captian \n Commander \n Lieutenant Commander \n Lieutenant \n ")
            rank_selection = input("which rank")
            for i in range(len(Ranks)):
                if rank_selection == Ranks[i]:
                    print(Names[i], "-", Ranks[i] )
                else:
                    break  
        elif options == 2: 
            try:
                
                for rank in range(len(Ranks)):
                    count = 0
                    if Ranks[rank] == rank_selection: 
                        count = count + 1

                        print("The rank of ", rank_selection, "has ", count, "members")    
            except:
                print("Rank is not shown ")
        else:
            print("Not an option")



main()         