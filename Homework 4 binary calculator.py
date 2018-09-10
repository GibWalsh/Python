"""
Gibson Lee Walsh
4/10/2018
I wrote this program with a purpose of making a binary calculator
that is capable of adding and subtracting binary numbers
"""
#----------------------------------------------------------------------------
import sys
def binaryToDec (S):
    """Convert Binary numbers to decimal
    
    
    Params: (S) String multiple of 8
    Return: int decimal of (S)
    """
    index=0
    S=S[::-1]
    total=0
    for i in (S):
        if i == '0':
            index+=1
        else:
            total=total+2**(index)
            index+=1                        
    return total


def decToBinary (I):
    """convert a decimal number to binary 
    The algorithm:
        1. divide the number by 2 using integer division, retaining both the
            quotient and the remainder
        2. the remainder becomes the last character of the binary string,
            wether 1 or 0
        3. The quotient is then divided by 2 again, using integer division
            and regaining both the quotient and the remainder.
        4. This new remainder is pre-fixed tp tje frpmt end of the binary string.
        5. Steps 3 and 4 are repeated until the quotient and remainder 
            come out as zero.
        6. Once the string is completed, sufficient zeros are pre-fixed to
            the front end to round out a multiple of 8 bits in length 
    
    Params: I (int): decimal numgber
    Return: (stirng) binary number of (I)
    """
    
    result=''
    while I != 0:
        num=I%2
        result=result+str(num)
        I=I//2
    result=result[::-1]
    return (result)

def checkBin (x):
    """
    Check if the input(x) is a binary number
    Params: x (str)
    Returns: Bool either True or False
    """
    for i in x:
        if i in '10':
            return True
        else:
            return False            
#menu with function calls                                    
def binCalMenu():
    """ A function that displays a menu to the user with the capability of 
        adding and subtracting binary numbers
        Params: None
        Returns: menu with five different input options
    """
    choice=input('What do you want to do?' '\n'
    '1. Enter the first number''\n'
    '2. Enter the second number''\n'
    '3. Add the two numbers''\n'
    '4. Subtract the second number from the first''\n'
    '5. Exit the program''\n')

    if choice == '1':
        oneChoice = input('What is the first number?')
        if checkBin(oneChoice) == True:
            print('The first number is')
            print(oneChoice)
            choice=input('What do you want to do?' '\n'
            '1. Enter the first number''\n'
            '2. Enter the second number''\n'
            '3. Add the two numbers''\n'
            '4. Subtract the second number from the first''\n'
            '5. Exit the program''\n')
        else:
            print('Please enter a binary number')
            return (binCalMenu())                                        
    if choice == '2':
        twoChoice = input('What is the second number?')
        if checkBin(twoChoice) == True:
            print('The first number is')
            print(oneChoice)
            print('The second number is')
            print(twoChoice)
            choice=input('What do you want to do?' '\n'
            '1. Enter the first number''\n'
            '2. Enter the second number''\n'
            '3. Add the two numbers''\n'
            '4. Subtract the second number from the first''\n'
            '5. Exit the program''\n')
        else:
            print('Please enter a binary number')
            return(binCalMenu())
    if choice == '3':
        try:
            decOne=binaryToDec(oneChoice)
            decTwo=binaryToDec(twoChoice)
            oneTwoSum=(decOne+decTwo)
            print('The Sum of the numbers is')
            print(decToBinary(oneTwoSum))
            choice=input('What do you want to do?' '\n'
            '1. Enter the first number''\n'
            '2. Enter the second number''\n'
            '3. Add the two numbers''\n'
            '4. Subtract the second number from the first''\n'
            '5. Exit the program''\n')
        except:
            print('Please enter two numbers first')
            return binCalMenu()
    if choice == '4':
        try:            
            if twoChoice>oneChoice:
                print('Sorry, this program cannot convert negative numbers, please try again')
                choice=input('What do you want to do?' '\n'
                '1. Enter the first number''\n'
                '2. Enter the second number''\n'
                '3. Add the two numbers''\n'
                '4. Subtract the second number from the first''\n'
                '5. Exit the program''\n')            
            else:
                decOne=binaryToDec(oneChoice)
                decTwo=binaryToDec(twoChoice)
                oneTwoDiff=(decOne-decTwo)
                oneTwoBin=(decToBinary(oneTwoDiff))
                print('The difference of the two numbers is')
                print(oneTwoBin)
                choice=input('What do you want to do?' '\n'
                '1. Enter the first number''\n'
                '2. Enter the second number''\n'
                '3. Add the two numbers''\n'
                '4. Subtract the second number from the first''\n'
                '5. Exit the program''\n')
        except:
            print('Please enter two numbers first')
            return(binCalMenu())
    if choice == '5':
        print('Bye')
        sys.exit()
    else:
        print('Please enter an option either 1,2,3,4,5')
        return binCalMenu() 

          
            
                    
(binCalMenu())        

    
    




