#######################################################################
# author: Connor Heard
# date: 12 / 2 / 2022
# desc: Program 1: How Many Prime Numbers?
########################################################################

# A function to prompt the user for a number and return that value to
# the calling statement.
def get_number():
    x = int(input("What limit are you interested in? "))
    return x

# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
def is_num_prime(x):
    if (x == 2):
        return True
    else:        
        for nums_before_prime in range (2, x):        
            if (x % nums_before_prime == 0):
                return False
        return True

################### MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.
prime_list = []
z = get_number()
if (z > 1):
    for i in range (2, z):
        if (is_num_prime(i)):
            prime_list.append(i)
    print("There are {} prime numbers less than {}".format(len(prime_list),z))
    print(prime_list)
else:
    print("There are 0 prime numbers less than {}".format(z))
    print(prime_list)


         
     
 
