# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1903068
# Date: 17/4/2022


Progress=[]
Trailer=[]
Retriever=[]
Exclude=[]

Outcomes=0
Total=0


credits_range=[0,20,40,60,80,100,120]





 #multiple outcomes and histogram for staff
print("Staffversion with Histogram")
                
while True:
    try:
        Pass_credits=int(input("Enter your Pass credits: "))
        if Pass_credits not in credits_range:
            print("Out of range")
            continue
        Defer_credits=int (input("Enter your Defer credits:"))
        if Defer_credits not in credits_range:
            print("Out of range")
            continue

        Fail_credits=int (input("Enter your total Fail credits:"))
        if Fail_credits not in credits_range:
            print("Out of range")
            continue
        
        Total=Pass_credits+Defer_credits+Fail_credits
        if Total!=120:
            print("Total incorrect")
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

           
        elif no_of_credits_at_fail >=80 :#CONDITION TO EXCLUDED
            print("Exclude")
            Exclude.append("*")

           
        choice = str(input("Would you like to enter another set of data? \nEnter'y' for yes or 'q' to quit:"))   
        if choice =="q":
            print(63*"_")
            print("Horizontal Histogram")
            print("Progress ",len(Progress),"  : ",len(Progress)*"*")
            print("Trailer ",len(Trailer),"   : ",len(Trailer)*"*")
            print("Retriever ",len(Retriever)," : ",len(Retriever)*"*")
            print("Excluded ",len(Exclude),"  : ",len(Exclude)*"*")
            outcomes=len(Progress)+len(Trailer)+len(Retriever)+len(Exclude) #CALCULATING THE TOTAL OUTCOMES
            print("")
            print(63*"-")
            print("Vertical Histogram") #PRINT COMMANDS TO VERTICAL HISTOGRAM


            print(f"Progress {len(Progress)} | Trailer {len(Trailer)} | Retriever {len(Retriever)} | Excluded {len(Exclude)}") # PRINT COMMANDS TO THE ALL FOUR LEVELS
            for i in range(max(len(Progress), len(Trailer), len(Retriever), len(Exclude))): #FOR LOOP TO FIND AND PRINT THE MAX LEVEL WHICH GOT MANY PROGRESSIONS
                print(

                   f'     {"*" if i < len(Progress) else " "}           {"*" if i < len(Trailer) else " "}            {"*" if i < len(Retriever) else " "}            {"*" if i < len(Exclude) else " "}') #F-STRINGS TO PRINT WHITESPACES IF NO PROGRESSIONS AND AND PRINT STARS WHEN THERE ARE PROGRESSIONS (REFERNCE: https://youtu.be/OICqSuUvSUc,https://stackoverflow.com/questions/50809008/how-to-make-a-simple-vertical-histogram-using-only-python-no-matplotlib)  
            print(outcomes,"outcomes in total.") #DISPLAYING THE TOTAL OUTCOMES
            print(63*"-")
            
            break 

            
      

       

    except ValueError:
            print("Integer Requires")












                         
