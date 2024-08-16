# A list of functions that can be used for calcutions!

def digit_check(min,max,requestedNum):
    '''
    Re-Usable function to make sure a users input is a digit.
    Need to pass a minimum, maximum, and what the number you are requesting represents.
    '''
    choice = 'WRONG'
    acceptablerange = range(min,max)
    within_range = False

    #two conditions to check
    while choice.isdigit() == False or within_range == False:
        choice = input(f"Please enter a {requestedNum} ({min}-{max}): ")
        #digit check
        if choice.isdigit() == False:
            print('what you entered as not a digit.')

        if choice.isdigit() == True:
            if int(choice) in acceptablerange:
                within_range = True
            else:
                print('out of range.')
                within_range = False

    return int(choice)

def continue_choice():
    choice = 'Wrong'
    while choice.lower() not in ['y','n']:
        choice = input('New Calculator? (Y,N): ')

        if choice.lower() not in ['y','n']:
            print('sorry, invalid choice!')

    if choice.lower() == 'y':
        return True
    else:
        return False

def validate_existance(d):
    choice = 'wrong'

    while choice not in d.keys():
        choice = digit_check(1,len(d)+1,'Calculator')

        if choice not in d.keys():
            print('Your choice does not exist')
        else:
            break
    
    return choice

def Mountain_Bike_Tire_Pressure():
    '''
    Takes in a rider's weight and outputs the pressure they need in PSI.
    '''
    rider_weight = digit_check(0,1000,'Weight in lbs')
    x = rider_weight/7

    Front = x-1
    Rear = x+2

    print(f'Front Tire: {Front} PSI')
    print(f'Rear Tire: {Rear} PSI')


# main logic loop
CalculatorList = {1:Mountain_Bike_Tire_Pressure}
New_Calculator = True

while New_Calculator:
    
    print('Here is the list of calculators: \n')
    for k in CalculatorList.keys():
        print(str(k) + ':' + CalculatorList[k].__name__)
    print('\n')

    
    calcNum = validate_existance(CalculatorList)

    CalculatorList[calcNum]()

    New_Calculator = continue_choice()

    if New_Calculator:
        print('\n'*10)