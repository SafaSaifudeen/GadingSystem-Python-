# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1903068
# Date: 17/4/2022


#Declaring VARIABLES
Total = 0
credit_range=[0,20,40,60,80,100,120] 

Progress=[]
Trailer=[]
Retriever=[]
Exclude=[]

outcomes=0

PASS=[]
DEFER=[]
FAIL=[]


print("Staff Version with Histogram")

while True : 
    try: #EXCEPTION HANDLING FOR VALUE ERROR
        Pass_credits=int(input("\nEnter your total Pass credits  : ")) #USER INPUTS AND ERROR MESSAGES FOR OUT OF RANGE
        if Pass_credits not in credit_range:
            print("Out of range.")
            continue

        Defer_credits=int(input("Enter your total Defer credits : "))
        if Defer_credits not in credit_range:
            print("Out of range.")
            continue
        Fail_credits=int(input("Enter your total Fail credits  : "))
        if Fail_credits not in credit_range:
            print("Out of range.")
            continue
        Total=Pass_credits+Defer_credits+Fail_credits #CALCULATION OF TOTAL CREDITS

        if Total != 120: #ERROR MESSAGE FOR INCORRECT TOTAL OF CREDITS
            print("Total incorrect.")
            continue
        elif Pass_credits == 120: #CONDITION TO PROGRESS
            print("Progress")
            Progress.append("*")
        elif Pass_credits == 100: #CONDITION TO TRAILER
            print("Progress (module Trailer)")
            Trailer.append("*")
        elif Pass_credits <= 80 and Fail_credits <= 60: #CONDITION TO RETRIEVER
            print("Module Retriever")
            Retriever.append("*")
        elif Fail_credits >=80 : #CONDITION TO EXCLUDED
            print("Exclude")
            Exclude.append("*")
        if Total == 120: #SORTING AND APPENDING ALL THE INPUTS IN LISTS
            PASS.append(Pass_credits)
            DEFER.append(Defer_credits)
            FAIL.append(Fail_credits)

        choice = str(input(
            "\nwould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results :")) #IF STAFF CHOOSES "q" PRINTS BOTH THE HISTOGRAMS . ELSE IF CHOOSES "y" THE LOOP WILL CONTINUE
        if choice.lower() == "q":
            print(63*"-")
            print("Horizontal Histogram") # PRINT COMMANDS TO HORIZONTAL HISTOGRAM
            print("Progress ", len(Progress), "  : ", len(Progress) * "*")
            print("Trailer ", len(Trailer), "   : ", len(Trailer) * "*")
            print("Retriever ", len(Retriever), " : ", len(Retriever) * "*")
            print("Excluded ", len(Exclude), "  : ", len(Exclude) * "*")
            outcomes= len(Progress) + len(Trailer) + len(Retriever) + len(Exclude) #CALCULATING THE TOTAL OUTCOMES
            print("")
            print(63*"-")
            print("Vertical Histogram") #PRINT COMMANDS TO VERTICAL HISTOGRAM

            print(f"Progress {len(Progress)} | Trailer {len(Trailer)} | Retriever {len(Retriever)} | Excluded {len(Exclude)}") # PRINT COMMANDS TO THE ALL FOUR LEVELS
            for i in range(max(len(Progress), len(Trailer), len(Retriever), len(Exclude))): #FOR LOOP TO FIND AND PRINT THE MAX LEVEL WHICH GOT MANY PROGRESSIONS
                print(
                    f'     {"*" if i < len(Progress) else " "}           {"*" if i < len(Trailer) else " "}            {"*" if i < len(Retriever) else " "}            {"*" if i < len(Exclude) else " "}') #F-STRINGS TO PRINT WHITESPACES IF NO PROGRESSIONS AND AND PRINT STARS WHEN THERE ARE PROGRESSIONS
          
            
            print(63*"-")
            print("All the inputs and their Progressions respectively:\n")
            for j in range(len(PASS)): #FOR LOOP TO PRINT THE SPECIFIC VALUES FROM THE LIST'S INDEX IN ORDER 
                if PASS[j] == 120:
                    print("Progress - ", PASS[j], ",", DEFER[j], ",", FAIL[j])
                elif PASS[j] == 100:
                    print("Progress (module Trailer) - ", PASS[j], ",", DEFER[j], ",", FAIL[j])
                elif PASS[j]<= 80 and Fail[j] <= 60:
                    print("Module Retriever - ", PASS[j], ",", DEFER[j], ",", FAIL[j])
                elif FAIL[j] >=80:
                    print("Exclude - ", PASS[j], ",", DEFER[j], ",", FAIL[j])
            print("")
            print(outcomes,"outcomes in total.") #DISPLAYING THE TOTAL OUTCOMES
            print(63*"-")
            break
        elif choice.lower() != "y": #ERROR MESSAGE FOR INVALID CHOICE
            print("Invalid choice!")
            break

        
    except ValueError: #EXCEPTION FOR VALUE ERROR
        print("Integer required")
        
