##########################################################################
# author: Connor Heard  
# date: 12 / 7 / 2022   
# desc: Program 2: Significant Digits   
#########################################################################
from random import randint, seed
SHOWLIST = True 	# a boolean to determine whether to show the list
MIN = 0			# the smallest random number that can be created.
MAX = 1000		# the largest random number that can be created.

# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.
def get_info():
    size_list = int(input("How big a list do you want to create? "))
    seed_number = int(input("What seed should be used for its creation? "))
    
    return size_list, seed_number

# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.
def print_list(list_name, data):
    print(list_name + "\t", end =" ")
    for number in data:
        print(str(number) + "\t", end=" ")
    print("")    

# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.
def list_of_random_integers(list_size, seed_number):
    random_numbers = []
    seed(seed_number)
    while (len(random_numbers) < list_size):
        random_numbers.append(randint(MIN, MAX))

    return random_numbers

# A function that recieves a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statemet.
def MSD(random_list):
    string = ""
    for num in random_list:
        string += (str(num) + " ")    
    MSD_list = []
    word_list = string.split()
    for i in range(0, len(word_list)+1):
        if (len(MSD_list) >= 10):
            break
        count = 0
        for number in word_list:
            if (int(number[0]) == i):
                count += 1
        MSD_list.append(count)

    return MSD_list

# Similar to the function above, a function that recieves a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.
def LSD(random_list):
    string = ""
    for num in random_list:
        string += (str(num) + " ")    
    LSD_list = []
    word_list = string.split()
    for i in range(0, len(word_list)+1):
        if (len(LSD_list) >= 10):
            break
        count = 0
        for number in word_list:
            if (int(number[len(number)-1]) == i):
                count += 1
        LSD_list.append(count)

    return LSD_list

###################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.
list_size, seed_number = get_info()

#   create the list of random numbers
random_list = list_of_random_integers(list_size, seed_number)

#   If SHOWLIST is selected, print out the list of numbers
if (SHOWLIST):
    print("Original List:")
    print(random_list)

#   print the head of the table which just shows the numbers 0-9
print("---------------------------------------------------------------------------------------")
for i in range (0, 10):
    print("\t " + str(i),end=" ")
print("")
print("---------------------------------------------------------------------------------------")


#   Calculate the MSD and LSD, and print out their statistics.
msd_list = MSD(random_list)
lsd_list = LSD(random_list)
print_list("MSD", msd_list)
print_list("LSD", lsd_list)
 

