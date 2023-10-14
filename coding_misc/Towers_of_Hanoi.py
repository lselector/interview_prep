
"""
# recursive implementation of "towsers of hanoi" problem
# 
# 
"""

counter = 0

# --------------------------------------------------------------
def hanoi(n, source, helper, target):
    global counter

    if n <= 0:
        return
    counter += 1
    print(counter)

    # move tower of size n - 1 from source to helper:
    hanoi(n - 1, source, target, helper)

    # move disk from source peg to target peg
    if source:
        target.append(source.pop())

    # move tower of size n-1 from helper to target
    hanoi(n - 1, helper, source, target)

# --------------------------------------------------------------
def print_state(label, source,helper,target):
    print(label,": ", source, helper, target)

# --------------------------------------------------------------
# main execution starts here
# --------------------------------------------------------------
print()
source = [4,3,2,1]
target = []
helper = []
print_state("Initial state",source, helper, target)
hanoi(len(source),source,helper,target)
print_state("Final state",source, helper, target)
print()


