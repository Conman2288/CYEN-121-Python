from random import randint, seed

def roll():
    return randint(1, 6)

dice_sums = [0] * 11

#print("Die1\tDie2\tSum")
for die1 in range(1, 7):
    for die2 in range(1, 7):
        dice_sum = die1 + die2
        dice_sums[dice_sum -2] += 1

      #  print("{}\t{}\t{}".format(die1, die2, dice_sum))

print("\nSum\tFreq\tProb")
for i in range(len(dice_sums)):
    print("{}\t{}\t{}".format(i + 2, dice_sums[i], dice_sums[i] / sum(dice_sums)))

# Experiments
dice_sums = [0] * 11
num_rolls = int(input("How many rolls?"))
rand_seed = int(input("Enter the seed: "))

seed(rand_seed)
#print("Die1\tDie2\tSum")
for i in range(0, num_rolls):
    die1 = roll()
    die2 = roll()
    dice_sum = die1 + die2
    dice_sums[dice_sum - 2] += 1

  #  print("{}\t{}\t{}".format(die1, die2, dice_sum))

print("\nSum\tFreq\tProb")
for i in range(len(dice_sums)):
    print("{}\t{}\t{}".format(i + 2, dice_sums[i], dice_sums[i] / sum(dice_sums)))
