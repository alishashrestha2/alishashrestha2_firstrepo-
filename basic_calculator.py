import os
import datetime
'''The os module is imported to use the system function'''

print("\n\t\t\tWelcome to BASIC CALCULATOR\n")
input("Press any key to continue.........")
os.system('cls' if os.name == 'nt' else 'clear')

'''1.The system function in Python is a part of the os module that allows you to execute shell commands directly from a Python script
A shell command is a command that is executed directly by the operating system (OS) shell, 
such as the command line interface (CLI) or graphical user interface (GUI)

2.This is a conditional expression that determines which command to execute based on the operating system.

3.os.name is a variable that returns a string indicating the operating system.
 For Windows, it returns 'nt', and for Unix-based systems (like Linux and macOS), it returns 'posix'.

4.The expression os.name == 'nt' checks if the operating system is Windows.
If it is, the expression evaluates to True, and the command 'cls' is executed.
If the operating system is not Windows (i.e., it's Unix-based), the expression evaluates to False, and the command 'clear' is executed.

5.cls is a command that clears the screen in Windows.

6.clear is a command that clears the screen in Unix-based systems (like Linux and macOS).'''

result = 0
operator = " "
count = 0
list = []

def display_menu():
    print("\n\t\t\tWelcome to BASIC CALCULATOR\n")
    print("Select the operation you want to perform :")
    print("_________________________")
    print("|1.\t|Addition\t|")
    print("|-------|---------------|")
    print("|2.\t|Subtraction\t|")
    print("|-------|---------------|")
    print("|3.\t|Multiplication\t|")
    print("|-------|---------------|")
    print("|4.\t|Division\t|")
    print("|-------|---------------|")
    print("|5.\t|See history\t|")
    print("|-------|---------------|")
    print("|6.\t|Exit\t\t|")
    print("|_______|_______________|\n")
    
def choice_and_calculation(count, list, choice, num1, num2):
    if choice == "1" :
        operator = "+"
        result = num1 + num2
    elif choice == "2" :
        operator = "-"
        result = num1 - num2
    elif choice == "3" :
        operator = "*"
        result = num1 * num2
    elif choice == "4":
        operator = "/"
        if num2 == 0 :
            result = "Undefined"
        else :
            result = num1 / num2
    print(f"\n{num1} {operator} {num2} = {result}")
    count = count + 1
    time = datetime.datetime.now()
    i = f"{time}\t:\t{num1} {operator} {num2} = {result}\n"
    list.append(i)
    return count

def next_calc():
    next = input("\nDo you want to calculate again ? (Yes/No) : ")
    while next != "Yes" and next != "yes" and next != "No" and next != "no" :
        print("\nPlease enter either yes or no .")
        next = input("\nDo you want to calculate again ? (Yes/No) : ")
    return next

def next_calc_exit():
    print("\n\t\tAre you sure you want to exit?  ")
    exit = input("\t\t\t____________\n\t\t\t|No   |Yes  |\n\t\t\t|_____|_____|    : ")
    while exit != "Yes" and exit != "yes" and exit != "No" and exit != "no" :
        print("\nPlease enter either yes or no .")
        print("\n\t\tAre you sure you want to exit?  ")
        exit = input("\t\t\t____________\n\t\t\t|No   |Yes  |\n\t\t\t|_____|_____|    : ")
    return exit

def history(count, list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------------------------History--------------------------------\n")
    if count >= 1 :
        print("Time\t\t\t\t:\t\tCalculation\n")
        print(*list, sep="\n") #to show each element of a list in new line.
    else :
         print("\nNothing to show here.")

def option_exit():
    print("\n\t\tAre you sure you want to exit?")
    back = input("\t\t\t____________\n\t\t\t|Yes  |No   |\n\t\t\t|_____|_____|    : ")
    while back != "Yes" and back != "yes" and back != "No" and back != "no" :
        print("\nPlease enter either yes or no .")
        print("\n\t\tAre you sure you want to exit?  ")
        back = input("\t\t\t____________\n\t\t\t|No   |Yes  |\n\t\t\t|_____|_____|    : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    return back

while True :
    display_menu()

    choice =input("Enter your choice (1/2/3/4/5/6) : ")
 
    if choice == "1" or choice == "2" or choice == "3" or choice == "4" :
        while True:
            try :
                num1 = float(input("\nEnter your 1st number : "))
                num2 = float(input("Enter your 2nd number : "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.....")
                continue
            
        count = choice_and_calculation(count, list, choice, num1, num2)
       
        next = next_calc()        
        if next == "yes" or next == "Yes" :
            os.system('cls' if os.name == 'nt' else 'clear')
        elif next == "No" or next == "no" :
            exit = next_calc_exit()
            if exit == "Yes" or exit == "yes" :
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif exit == "No" or exit == "no" :
                os.system('cls' if os.name == 'nt' else 'clear')
                continue 

    elif choice == "5" :
        history(count, list)

    elif choice == "6" :
        back = option_exit()
        if back == "Yes" or back == "yes" :
                break
        elif back == "No" or back == "no" :
                continue
        
    else :
        print("Invalid operation.")


