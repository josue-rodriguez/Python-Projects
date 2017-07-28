
def coinNums(weight, cointype):
    coin_weights = {'Cent': 126, 'Nickel': 199, 'Dime': 113, 'Quarter': 226}
    wrapperFits = {'Cent': 50, 'Nickel': 40, 'Dime': 50, 'Quarter': 40}

    coin_count = weight // coin_weights[cointype] #counts how many coins. always rounds down to the nearest number. (can't have parts of a coin)
    
    if coin_count <= wrapperFits[cointype]:                                      # Conditionals for how many wrappers would be needed.
        wrapper_count = 1
    elif cointype == 'Cent' or cointype == 'Dime':
        wrapper_count = coin_count / 50
        if coin_count % 50 == 0:
            wrapper_count = coin_count // 50
        else:
            wrapper_count = coin_count // 50
            wrapper_count += 1
    else:
        wrapper_count = coin_count / 40
        if coin_count % 40 == 0:
            wrapper_count = coin_count // 40
        else:
            wrapper_count = coin_count // 40
            wrapper_count += 1
            
    return (coin_count, wrapper_count)       # Returning the total amount of coins and wrapper
    
def coinEstimator():
    print("Welcome to the coin counting machine, you broke bitch.")
    print('Please enter the type of coin you wish to count: ')
    print('1. Cent')
    print('2. Nickel')
    print('3. Dime')
    print('4. Quarter')
    
    answer = int(input('Enter: \n'))
    
    if answer == 1:
        weight = float(input('Please enter the weight of your pennies in grams:\n '))
        (count, wrappers) = coinNums(weight, 'Cent')
        print('You have {0} cents and you need {1} wrapper(s).'.format(count, wrappers))
        
    elif answer == 2:
        weight = float(input('Please enter the weight of your nickels in grams:\n '))
        (count, wrappers) = coinNums(weight, 'Nickel')
        print('You have {0} nickels and you need {1} wrapper(s).'.format(count, wrappers))
        
    elif answer == 3:
        weight = float(input('Please enter the weight of your dimes in grams:\n '))
        (count, wrappers) = coinNums(weight, 'Dime')
        print('You have {0} dimes and you need {1} wrappers.'.format(count, wrappers))
        
    elif answer == 4:
        weight = float(input('Please enter the weight of your quarters in grams:\n '))
        (count, wrappers) = coinNums(weight, 'Quarter')
        print('You have {0} quarters and you need {1} wrappers.'.format(count, wrappers))
        
    else: 
        print("I'm sorry, the number you chose is not an option. Please try again.")
        print("What would you like to do: ")
        print('1. Try again')
        print('2. Quit')
        options = int(input('Enter: '))
        if options == 1:
            coinEstimator()
        else:
            pass
    print()
    print()
    print("What would you like to do now?")
    print('1. Try again')
    print('2. Quit')
    options = int(input('Enter: '))
    if options == 1:
        coinEstimator()
    else:
        pass

coinEstimator()
