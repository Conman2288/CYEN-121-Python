# Step 1: Move n-1 discs to source to spare
# Step 2: Move 1 disc from source to destination
# Step 3: Move n - 1 discs from spare to destination

def hanoi(n, source, destination, spare):
    if (n == 1):
        print("{} -> {}".format(source, destination))
    else:
        hanoi(n-1, source, spare, destination)
        hanoi(1, source, destination, spare)
        hanoi(n-1, spare, destination, source)
        
hanoi(3, "A", "C", "B")
