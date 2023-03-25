# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1903068
# Date: 12/4/2022


#Declaring variables
Pass_credits=0
Fail_credits=0
Defer_credits=0

Progress=0
Trailer=0
Retriever=0
Exclude=0

Outcomes=0



credits_range=[0,20,40,60,80,100,120]

print("Student prgression outcome(one time)")
while True:
    try:
        Pass_credits=int(input("Enter your total Pass credits: "))
        if Pass_credits not in credits_range:
            continue

        Fail_credits=int (input("Enter your total Fail credits:"))
        if Fail_credits not in credits_range:
            continue
        Defer_credits=int (input("Enter your total Defer credits:"))
        if Defer_credits not in credits_range:
            continue
        Total=Pass_credits+Fail_credits+Defer_credits
        if Total!=120:
            print("Total incorrect")
            continue
        elif Pass_credits == 120: #CONDITION TO PROGRESS
            print("Progress")
           
            break
            
        elif Pass_credits == 100: #CONDITION TO TRAILER
            print("Progress (module Trailer)")
            Trailer=Trailer+1
            break
            
        elif Pass_credits <= 80 and Fail_credits <= 60: #CONDITION TO RETRIEVER
            print("Module Retriever")
            Retriver=Retriver
            break
            
        elif Fail_credits >=80 : #CONDITION TO EXCLUDED
            print("Exclude")
            break

    except ValueError:
            print("Integer Requires")

 #multiple outcomes and histogram for staff
print("Staffversion with Histogram")
                
while True:
    try:
        Pass_credits=int(input("Enter your Pass credits: "))
        if Pass_credits not in credits_range:
            print("Out of range")
            continue

        Fail_credits=int (input("Enter your total Fail credits:"))
        if Fail_credits not in credits_range:
            print("Out of range")
            continue
        Defer_credits=int (input("Enter your Defer credits:"))
        if Defer_credits not in credits_range:
            print("Out of range")
            continue
        Total=Pass_credits+Fail_credits+Defer_credits
        if Total!=120:
            print("Total incorrect")
            continue
        elif Pass_credits == 120: #CONDITION TO PROGRESS
            Progress=Progress+1
            Outcomes=Outcomes+1
            print("Progress")
            
            
        elif Pass_credits == 100: #CONDITION TO TRAILER
            Trailer=Trailer+1
            Outcomes=Outcomes+1
            print("Progress (module Trailer)")
            
            
        elif Pass_credits <= 80 and Fail_credits <= 60: #CONDITION TO RETRIEVER
            Retriever=Retriever+1
            Outcomes=Outcomes+1
            print("Module Retriever")
            
            
        elif Fail_credits >=80 : #CONDITION TO EXCLUDED
            Exclude=Exclude+1
            Outcomes=Outcomes+1
            print("Exclude")
   


        choice=input("Would you like to enter another set of data? \nEnter 'y' for or 'q' to quit and view results:  ")
        choice=choice.lower()
        if choice == 'y':
            continue
        if choice =='q':
            break
        

    except ValueError:
            print("Integer Requires")


print(" _ "*63)
print ("Horizontal Histogram")
print("Progress",Progress,"",   ":",Progress*"*")
print("Trailer",Trailer,"","",     ":",Trailer*"*")
print("Retriever",Retriever, ":",Retriever*"*")
print("Excluded",Exclude, '',   ":",Exclude*"*")
print("\n\n",Outcomes,"Outcomes in total")
print(" _ "*63)
            
                         
