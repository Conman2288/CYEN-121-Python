#######################################################
# Name: Connor Heard
# Date: 2 / 1 / 23
# Description: Program 06 - Exam Prep Simulation Game
#######################################################
from random import *
DEBUG = True   # Activate intermediate output

# this function generates randomly created lists based on the number of questions in the bank, questions asked, and questions studied
def generate_random_lists(bank_size, questions_studied, actual_num_asked):
    # generates a random list of questions numbers that were studied
    random_questions_studied = sample(range(1, bank_size), k = int(questions_studied))
    # generates a random list of questions numbers that were asked on the test
    random_questions_asked = sample(range(1, bank_size), k = int(actual_num_asked))

    # returns both randomly generated lists
    return random_questions_studied, random_questions_asked

# this functions creates a single instance of a simulation with the randmoly generated lists
def generate_simulation(questions_asked, questions_studied, num_to_pass, sim_number):
    global sim_scores
    global total_passed
    questions_passed = []
    
    # Iterates through the entire list of questions asked and sees if they exist in the list of questions studied, appends to questions_passed.
    for question_num in questions_asked:
        if (question_num in questions_studied):
            questions_passed.append(question_num)

    # adds to the global simulation score list to be printed later
    sim_scores.append(len(questions_passed))

    # if the length of questions_passed list is greater than or equal to number of questions need to pass, then global counter total_passed is incremented by 1 (test was passed)
    if (len(questions_passed) >= num_to_pass):
        total_passed += 1

    # if DEBUG is turned on, then the following lists and information will printed for every time a simulation is created
    if (DEBUG):
        print("Simulation No. " + str(sim_number))
        print("Questions your were asked: " + str(questions_asked))
        print("Questions you studied: " + str(questions_studied)) 
        print("Questions you passed: " + str(questions_passed))
        print("Which means you scored " + str(len(questions_passed)) + "/" + str(len(questions_asked)))
        print("-" * 60)





################## Main ########################
sim_scores = []
total_passed = 0

# All these variables gather information from the user to be used as arguments to generate simulations.
print("=" * 60)
bank_size = int(input("What is the size of the question bank? "))
questions_studied = int(input("How many of those questions have you studied? "))
actual_question_num = int(input("How many questions does the test have? "))
num_to_pass = int(input("How many questions must you answer correctly to pass the text? "))
print("=" * 60)
num_simulations = int(input("How many simulations do you want to run? "))
print("=" * 60)

# For the num_simulations inputted by the user, a unique set of lists will be created and a simulation will be generated.
for i in range(1, num_simulations + 1):
    questions_studied_list, questions_asked_list = generate_random_lists(bank_size, questions_studied, actual_question_num)
    generate_simulation(questions_asked_list, questions_studied_list, num_to_pass, i)

# if the DEBUG is turned on, the list of simulation total scores will be printed to monitor
if (DEBUG):
    print("Simulation scores were:")
    print(sim_scores)
print("=" * 60)

# Calculates the average percent of tests passed based on the total number of simulations
print("You passed the test " + str(total_passed / num_simulations * 100) + "% of the time")

