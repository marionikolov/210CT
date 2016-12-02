"""
Checks whether the input list is sorted in ascending order or not. Returns True if it is and False if not.
"""
def isSorted(lst):
    for i in range(len(lst)-2):
        if lst[i] > lst[i+1]:
            return False
    return True
"""
Returns True or False according to whether the input list (lst) contains a number in the range x and y. Returns as soon as it finds a number in that range, even if there is more than one.
PARAMETERS
    lst - list of numbers
    x - beginning of range; needs to be less than y
    y - end of range; needs to be more than x
"""
def binarySearchWithinRange(lst, x, y):
    if isSorted(lst) != True:
        lst.sort()
    firstLoc = 0
    lastLoc = len(lst) - 1
    while lastLoc >= firstLoc:
        testLoc = firstLoc + (lastLoc - firstLoc)//2
        if lst[testLoc] >= x and lst[testLoc] <= y:
            return True
        elif lst[testLoc] < x:
            firstLoc = testLoc + 1
        else:
            lastLoc = testLoc - 1
    return False

if __name__ == '__main__':
    a = [2,3,4,7,9,13]
    result = binarySearchWithinRange(a, 10, 14)
    print(result)