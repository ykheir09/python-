"""
Yusuf Kheir
ICS 140-03
3/14/17
This program checks you're eligible for senate and US representative.
"""

def main():
    try:
        print("This program checks if you're eligible for Senate and House:")
    
    
        age = eval(input("Please enter your age:"))
        citizenYear = eval(input("please enter numbers of year your have been a Citizen:"))

        if age <= 0:
            print("\nPlease correct person's age:")

        elif citizenYear<0:
            print("\nPlease correct years of citizenship:")

        elif citizenYear > age:
            print("\nThe number of citizenship years is greater than age.\n please try again:")
        
        # elif check if age is greater or equel 30 and if citizenship years is greater or equel 9
        # if its true the user is eligible for senator and US representative
        elif age >= 30 and citizenYear >=9:
            print("\nYou're eligible to ran for both US Senate and US Representative:")
        elif age >=27 and citizenYear >=7:
            print("\nYou're eligible to run only for US Representative:")
        #else check all cases and if age is less than 25 or citizenyears is less then 7 user not eligible     
        else:
            print("\nYou're not eilgible:")
    # excep checks for Errors and helps your to enter correct information.    
    except NameError:
        print("please enter correct numbers:")
    except SyntaxError:
        print("\nplease enter correct information:")
    except: 
        print("\nUnknow Error:")
main()              

        
    
