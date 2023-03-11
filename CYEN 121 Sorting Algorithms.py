from random import randint

# Generate List of Random Integers
def get_list():
    numbers = []
    while(len(numbers) < 20):
        numbers.append(randint(1,99))
    return(numbers)

# Sequential Search
def seq_search():
    
    minIndex = 0

    for index in range(1, len(numbers)):
        if (numbers[index] < numbers[minIndex]):
            minIndex = index
    return minIndex

                   
                   
                   
# Binary Search
def bin_search(num, numbers):
    found = False
    first = 0
    last = len(numbers) - 1
    index = -1

    while(found != True and first <= last):
        mid = (first + last) // 2
        if (num == numbers[mid]):
            found = True
            index = mid
        elif(num > numbers[mid]):
            first = mid + 1
        else:
            last = mid - 1
    return index


# Bubble Sort
def bubble_sort(numbers):
    n = len(numbers)
    for i in range (1, n):
        for j in range (1, n - i + 1):
            if (numbers[j] < numbers[j-1]):
                temp = numbers[j]
                numbers[j] = numbers[j - 1]
                numbers[j - 1] = temp


#Insertion Sort
def insertion_sort(numbers):
    i = 1
    n = len(numbers)
    while (i < n):
        if (numbers[i - 1] > numbers[i]):
            temp = numbers[i]
            j = i - 1
            while (j >= 0 and numbers[j] > temp):
                numbers[j + 1] = numbers[j]
                j -= 1
            number[j + 1] = temp
        i += 1    

##############MAIN###############
nums = get_list()
print(nums)
num = int(input("Enter an integer: "))
bubble_sort(nums)
print(nums)
print("The index of {} is {}".format(num, bin_search(num, nums)))



