n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        ## 3) fixing the indefinate loop by adding and increase value of 1 to loading for each loop
        loading= loading + 1
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        ##2) validation symbol incorrect
        if opt == "1":  
            print("Current Crew List:")

## 4) fixing the range od the for loop as it shoul equal the amount of values in the list
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ").title()
            new_rank = input("Rank: ").title()
            new_div = input("Division: ").title()
# 5) Insurning that it follows the same structure of naming convention in the list names 
            
           
            n.append(new_name)
# 6) making sure that the new updated names have been added to the list 
            r.append(new_rank)
            d.append(new_div)
            print("\n Crew member added.")
            
        elif opt == "3":
## 7) insuring that the naming is in the right format
            rem = input("Name to remove: ").title()
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or "Commander": 
                    count = count + 1
            print("High ranking officers: " + count) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")
##1) incomplete function as it was not closeed
run_system_monolith()
