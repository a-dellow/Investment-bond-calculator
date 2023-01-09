import math

"""PSEUDOCODE

print menu for user to choose calculator
get user input for choice
convert input to lower case

while input does not equal 'bond' or 'investment'
    print error message
    print menu for user to choose calculator
    get user input for choice

if user input is 'investment'
    get float user input for amount being deposited.
    get float user input for interest rate percentage value
    get int user input for how many years of investment
    initialise 'interest' string variable

    while interest does not equal 'simple' or 'compound'
        get user input for simple/compound interest. Stored in 'interest'

    if user input is 'simple'
        calculate amount
        print amount

    elif user input is 'compound'
        calculate amount
        print amount

elif user input is 'bond'
    get int user input for house value
    get float user input for interest rate percentage value
    get int user input for number of months repayment
    
    calculate amount
    print amount

"""





#This prints the menu and takes the user's choice into a variable
menu_choice = input("""
----------------------------------------------------------------------------------
Choose either 'investment' or 'bond' from the menu below to proceed:

investment  -  to calculate the amount of interest you'll earn on your investment
bond        -  to calculate the amount you'll have to pay on a home loan
----------------------------------------------------------------------------------

""")

#Converting the user input to lower case so that the user's input is not case sensitive
menu_choice = menu_choice.lower()

#Validating the user's input
while menu_choice != 'bond' and menu_choice != 'investment':

    #Re-printing menu with an error message if the user inputs incorrectly
    menu_choice = input("""PLEASE TRY AGAIN - use 'investment' or 'bond'
----------------------------------------------------------------------------------
Choose either 'investment' or 'bond' from the menu below to proceed:

investment  -  to calculate the amount of interest you'll earn on your investment
bond        -  to calculate the amount you'll have to pay on a home loan
----------------------------------------------------------------------------------

""")
    menu_choice = menu_choice.lower()





if menu_choice == 'investment':

    #User inputs the details of their investment
    deposit = float(input("Please input how much you are investing: "))
    interest_rate = (float(input("Please input the annual interest rate i.e. 8% = '8': ")))/100    
    years = int(input("Please input the number of years you are investing for: "))

    #Initialising an empty variable so that the while loop is entered
    interest = 'empty'

    #User input for interest type
    while interest != 'simple' and interest != 'compound':
        interest = input("Please choose an interest type, 'simple' or 'compound': ")
        interest = interest.lower()
    
    if interest == 'simple':

        #Calculating the simple interest
        amount = deposit * (1 + (interest_rate * years))

        print(f"""\nWhen your investment is complete, you will have ${round(amount,2)}.
You will have earned ${round(amount-deposit,2)} in interest.\n""")

    elif interest == 'compound':

        #Calculating compound interest
        amount = deposit * math.pow((1 + interest_rate),years)

        print(f"""\nWhen your investment is complete, you will have ${round(amount,2)}.
You will have earned ${round(amount-deposit,2)} in interest.\n""")





elif menu_choice == 'bond':

    house_value = int(input("Please enter the value of your house: "))
    interest_rate = (float(input("Please input the annual interest rate i.e. 8% = '8': ")))/100
    months = int(input("Please enter how many months you will repay your bond over: "))

    #Calculating bond monthly repayment
    amount = house_value * (interest_rate/12)/(1 - ((1 + interest_rate/12)**(-months)))

    print(f"\nYour monthly repayment will be ${round(amount,2)}, paying a total of ${round(amount*months,2)}.\n")