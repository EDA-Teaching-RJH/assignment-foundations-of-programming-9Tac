Names = ["Michael Burnham", "Christopher Pike", "Kathryn Janeway", "Tom Paris", "Benjamin Sisko"]
Ranks = ["Commander", "Captian", "Captain", "Lietenant", "Commander"]
Divisions = ["Science", "Command", "Command", "Helm", "Command"]
IDs = ["0001","0002","0003", "0004", "0005"]
   

def main():
    ## Asking the user for their name and what th require to be done by the system
    First_name = input("What is your first name ")
    last_name = input("What is your last name")
    
## User validation 
    
    
    # init_database(Names, Ranks, Division, IDs)
    while True:
        print("Welcome", First_name + last_name, 
          "\n 1. Check curent memebrs" 
          "\n 2. Add a member" 
          "\n 3. Remove a member " 
          "\n 4. Update the Ranks " 
          "\n 5. Search Crew" 
          "\n 6. Filter by divisions " 
          "\n 7. Calculate payroll" 
          "\n 8. Count officers Ranks ")
    
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
            Filter_by_division(Names, Divisions)
        elif Option == 7:
            Calculate_payroll(Ranks)
        elif Option == 8:
            Count_officers(Ranks)
        else:
            print("Shutting down")

            break
        
    
def Display_roster(Names, Ranks, Divisions, IDs):
    print("Current team members")
    for i in range(len(Names)):
            print(Names[i] + " - " , Ranks[i] , " - " , Divisions[i] , " - " , IDs[i]) 
    


def Add_member(Names, Ranks, Divisions, IDs):
    #TNG_Ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Esign"]
    Add_Name = input("What is the new Members name ").title()
    Add_Rank = input("What is their Rank ").title()
    Add_Division = input("what division are they in ").title()
    Add_IDs = input("what is there ID code")
    Names.append(Add_Name)
    Divisions.append(Add_Division)
    # for i in range(len(TNG_Ranks)):
    #     count = 0
    #     if TNG_Ranks[i] != Add_Rank:
    #         count = count + 1
    #     Add_Rank = input("Rank is invaild re-enter \nWhat is their Rank ").title()
    # print("User Rank is valid")
        
        
    Ranks.append(Add_Rank)

    for i in range(len(IDs)):
        if IDs[i] != Add_IDs:
            print("Valid ID ") 
        else: 
            Add_IDs = input("ID not valid what is there ID code")
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
            print("Changed")
    except ValueError:
        print("Change Rank")
    return Names, Ranks, IDs

def Search_Crew(Names, Ranks, Divisions, IDs):
    print("What are you searching for \n 1) The Names of the crew members \n 2) The Ranks and the amount of people with that rank \n 3) The divisions in the crew \n 4) Finding the user with ID code ")
    options = int(input("Which would you like to carry out in this protocal "))
    if options == 1:
        print("Names of the crew members ")
        N0 = 1
        for i in range(len(Names)):
            print(N0, "Crew member: " ,Names[i])
            N0 = N0 + 1
    elif options == 2:
        print("The ranks of the crew ")
        select = int(input(" 1) Finding the ranks \n 2. Finding the amount of people with those ranks "))
        if select == 1:
            print("THe Ranks of the in the crew  \n Captian \n Commander \n Lieutenant Commander \n Lieutenant \n ")
            rank_selection = input("which rank: ").title()
            for i in range(len(Ranks)):
                if rank_selection == Ranks[i]:
                    print(Names[i], "-", Ranks[i] )
                else:
                    print("No users found in the Rank")
        

        elif options == 2: 
            try:
                rrank_selection = input("which rank: ").title()
                for rank in range(len(Ranks)):
                    count = 0
                    if Ranks[rank] == rrank_selection: 
                        count = count + 1

                print("The rank of ", rrank_selection, "has ", count, "members")    
            except:
                print("Rank is not shown ")

        else:
            print("Not a select option")
        
    elif options == 3:
        Division = input("Which division").title()
        N0  = 0
        for i in range(len(Divisions)):
            if Divisions[i] == Division:
                N0 = N0 + 1
        print(N0, "members in ", Division)


    elif options == 4:
        id = input("Enter ID code")
        for i in range(len(IDs)):
            
            if id == IDs[i]:
                print(id,"the id belongs to:", Names[i])
            else: 
                print("No user has ID:", id)
    else:
        print("Not an option")

def Filter_by_division(Names, Divisions):

    Division_selection = input("Which division: ").title()
    for div in range(len(Divisions)):
        if Division_selection == Divisions[div]:
            print(Names[div], "-", Divisions[div] )
        else:
            print("enter")
            break
            

def Calculate_payroll(Ranks):
    try:
        cost = 0
        for i in len(Ranks):
            
            if Ranks[i] == "Captain":
                p_Captain = 1000
                print("A Captain makes £", p_Captain)
                cost= cost + p_Captain

            elif Ranks[i] == "Commander":
                p_Commander = 800
                print("A Commander makes £", p_Commander)
                cost = cost + p_Commander
            
            elif Ranks[i] == "Lieutenant Commander":
                p_Commander_Lieutenant = 600
                print("A Lieutenant Commander makes £500", p_Commander_Lieutenant)
                cost = cost + p_Commander_Lieutenant

            elif Ranks[i] == "Lieutenant":
                p_lieutenant = 400
                print("A lieutenant makes £", p_lieutenant)
                cost = cost + p_lieutenant
            elif Ranks[i] == "Esign":
                p_Ensign = 200
                print("An Esign makes £",p_Ensign)
                cost = cost + p_Ensign

    except:
        print("insuffcient fund")

def Count_officers(Ranks):
     
    count_Captain = 0
    count_Commander = 0
    count_Lieutenant = 0
    count_Lieutenant_Commander = 0
    count_Esign = 0
     
    for i in range(len(Ranks)):
            
        if Ranks[i] == "Captain":
            count_Captain = count_Captain + 1

        elif Ranks[i] == "Commander":
            count_Commander = count_Commander + 1
            
        elif Ranks[i] == "Lieutenant Commander":
            count_Lieutenant_Commander = count_Lieutenant_Commander + 1

        elif Ranks[i] == "Lieutenant":
            count_Lieutenant = count_Lieutenant + 1
        elif Ranks[i] == "Esign":
            count_Esign = count_Esign + 1

        else:
            break 
        print("The amount of Captains:", count_Captain, "\nThe amount of Commanders:", count_Commander, "\nThe amount of Lieutenant Commanders:", count_Lieutenant_Commander, "\nThe amount of lieutenants:", count_Lieutenant, "\nThe amount of Esigns:",count_Esign )


main()