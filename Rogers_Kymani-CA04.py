#Rogers_Kymani Nov2024 CA-04.py

for i in range(1, 177): #auto generate student id numbers
    validCode = False
    while not validCode:  #code will loop until validCode is True, meaning a valid input has been entered
        code = input('Enter code mark for student '+ str(i) +': ')
        if code.isdigit(): #checking input is an integer
            code = int(code)
            if code in range(0,101): #checking code is in range
                validCode = True #loop ends as input has been validated
            else:
                print('Marks for code may only be integers between 1 and 100')
        else:
                print('Marks for code may only be integers between 1 and 100')
    print()
    validTest = False 
    while not validTest:  #code will loop until validTest is true which means a valid input has been entered
        test = input('Enter test mark for student ' + str(i) +': '); #getting input
        if test.isdigit():  #checking input is a digit
            test = int(test)
            if test in range(0,101):  # checking input is between 1 and 100
                validTest = True
            else:
                print('Marks for test may only be integers between 1 and 100')
        else:
            print('Marks for test may only be integers between 1 and 100')

    print()
    
    validLate = False
    while not validLate: #looping code untila valid input is entered and validLate is set to true
        late = input('Enter days late for student ' + str(i) + ': ') #getting input
        
        if late.isdigit():
            late = int(late) #checking input is a integer
            if 0 <= late <= 2: #checking the assignment was submitted within the 48 hour threshold 
                validLate = True
                raw = (code + test) / 2 #calculaitons for students overall mark
                overall = raw - (late * 5)
                print()
                print('Student ' + str(i) + ' scored',code,'in their code;',test,'in their test;',raw,'is their raw mark; Their submission was',late,'days late;') 
                print('Overall, student ' + str(i) + ' scored',overall)  #output
                print('------------')
            elif late > 2:
                print('Student submitted the assignment more than 2 days late so their assignment is not accpeted and scores 0')#the case where student doesn't submit assignment within the 48 hour threshold
                validLate = True
                print('------------')
            else:
                print('Days late should be 0 or a positive integer.')
        else:
            print('Invalid input. Please enter a number greater than or equal to 0.')
            
        
