"""
A program to play poker 24 game. The objective is to find a way to manipulate
four integers from the poker deck so that the end result is 24.
For example, for the card with the numbers 4, 7, 8, 8, a possible solution is
(7-(8/8))*4 = 24. Only basic operations +, -, *, and / are allowed. Additional
operations, such as square root and factorial are not permitted in this program.

The 4 input numbers are given by the user, and must to randomly selected from 52-card
poker deck.



"""
    
input4 = input("Which four cards did you get, separate by comma?")

# List the possible operation combinations to get 24.
'''def get24(a,b,c,d):
    """(int,int,int,int) -> expr

    Return the equation to calculate 24 based on the 4 values, a, b, c, and d
    provided by the user.

    Precondition: 1 <= a,b,c,d <= 13

    >>>get24(1,2,3,4)
    1*2*3*4
    """

    
    count = 0
    result = a*b*c*d
    return result'''

# Save the input numbers for calculation
def assign_input(input4):

    """(str) -> list

    Assign the input values into a, b, c, and d for further calculation.
    Convert J, Q, K to 11, 12, 13, respectively.
    
    >>>assign_input('1,2,K,4')
    [1,2,13,4]
    """
    '''nums = []
    for item in input4:
        for i range(4):
            if str.isalnum(item):
                nums[i] = item'''

    for item in input4:
        if item.isalpha():
            if item == 'J':
                item = 11
            elif item == 'Q':
                item = 12
            elif item == 'K':
                item = 13
        elif item in range(0,11)    
    '''a = int(input4[0])
    b = int(input4[2])
    c = int(input4[4])
    d = int(input4[6])
    nums = [a,b,c,d]'''
    return input4
    
