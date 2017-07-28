def change_needed():
    total = float(input("Please enter the total amount due: $ "))
    change = float(input("Please enter the amount given: $ "))
    
    change = change - total
    change_p = change
    
    quarters = change // .25
    change -= (quarters * .25)
    
    dimes = change // .10
    change -= (dimes * .10)
    
    nickels = change // .05 
    change -= (nickels * .05)
    
    pennies = round(change / .01, 2)
    
    print("You need $%.2f in change: \n" % (change_p))
    print("Quarters: %s" % (quarters))
    print("Dimes: %s" % (dimes))
    print("Nickels: %s" % (nickels))
    print("Pennies: %s" % (pennies))
    print()
    
    restart()
    
def restart():
    print("What would you like to do:")
    print("    1. Calculate more change")
    print("    2. Quit")
    choice = int(input('Enter: '))
    
    if choice == 1:
        change_needed()
    elif choice == 2:
        pass
    else:
        print("I'm sorry. Please choose again.")
        restart()
change_needed()
