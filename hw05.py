"""
Name: Violet McAuliffe
Peers: N/A
References: Class Slides
"""

def get_letter():
    """ 
        1: Create a while loop
        2: Check the length of input is 1
        3: Create conditions for the letters we don't want
        4: return the correct input
    """
    while True:
        char = input("Give a single uppercase letter: ") #gather input
        if len(char) != 1: #checking length
            print("Error: it needs to be a single character.")
            continue
        if char != "A" and char != "B" and char != "C":
            #making sure it is one of the three inputs we want
            print("Error: You provided the wrong character.")
            continue
        else:
            #storing the output in the function
            return char
         #moving the output into the global variable
def get_digit():
    """
    1: Creat while True: loop
    2: take input
    3: use is.digit to check if the input is a digit
    4: use if, and, and to ensure the digit is 1,2, or 3
    """
    #creating loop
    while True:
        dig = input("Give a single number character: ") #getting input
        if dig.isdigit() == False: #ensuring input is a digit, if not we restart loop
            print("Error: your input should be only digits.") 
            continue
        if int(dig) not in range(1,4): #ensuring the integer value of the digit is in rang[1,3], inclusively
            print("Error: a single digit needs to be in [1,3].")
            continue
        else: #storing the correct digit as a global variable
            return dig

def check_pattern(char, dig, st_list):
    """ 
    1: Create a for-loop that follows the items in st_list
    1.5: Create a nested loop that follows each charachter in the item
    2: create the conditions of each character
        -find the index of first time char appears
        -search after that index for the first time dig appears
    3: ensure that the format of the print out is correct
    """
    print("Strings with the pattern:\n")
    for elem in st_list: #considering each element
        for let in range(len(elem)): #considering the character in each element
            if elem[let] != char:
                continue
            if elem[let] == char:
                for nex in range(let + 1, len(elem)):
                    #considerent the next element
                    if elem[nex] != dig:
                        continue
                    if elem[nex] == dig:
                        print(elem, end = " ")
                        continue
            break #breaking the other loop             
        
def main ():
       
    """ 1: create a while loop
        2: call the functions
        3: get the y/n input
        4: break the loop if it is anything except y
    """

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    
    
    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    
    while True: #making loop
        st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33", 
        "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
        "1B1B", "333B", "1@CC", "3@@C", "333C"]
        char = get_letter() #storing called function (returned value) within variable
        dig = get_digit() 
        check_pattern(char, dig, st_list)
        yn = input("\nTry Again? (y/n): ") #getting input
        if yn != "y": #creating the condition
            break


    # -------------------------------------------------
    # No need to modify anything Below this line
    
    print("The End")
    
# Do not modify these two lines
if __name__ == "__main__":
    main()