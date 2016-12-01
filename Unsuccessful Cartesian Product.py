# Diana, please ignore this file. Cheers!

def product_recursion(*listOfLists):
    if len(listOfLists) == 0:
        return ()
    else:
        for singleList in listOfLists[0]:
            newListofLists = []
            for i in range (1, len(listOfLists)):
                newListofLists.append(listOfLists[i])
            for product in product_recursion(*newListofLists):
                return tuple(singleList) + product

# a = product_recursion([[1,2,3], [4],[5,6]])
# print(a)

def cartesianProductRecursive(listOfLists):
    print(listOfLists)
    if len(listOfLists) == 0:
        return []
    else:
        products = []
        for i in range(0, len(listOfLists[1])):
            prod = [listOfLists[0][0]]
            for lst in listOfLists[1:]:
                print(str(lst[i]))
                prod.append(lst[i])
            products.append(prod)
        print(str(prod))
        if type(listOfLists[0]) != int:
            print(str([prod]) + "+ cartesianProductRecursive(" + str(listOfLists[1][1:]) + ") + "  + str(listOfLists[1:]))
            return [prod] + cartesianProductRecursive(listOfLists[1][1:] + listOfLists[1:])

result = cartesianProductRecursive([[1,2,3], [4,5,6], [7,8,9]])
print(result)


CARTESIAN-PRODUCT(set1, set2, ..., setN) // the input parameters are lists of numbers
    outputSet <- NIL
    for i <- set1[1] ... set1[length(set1)]
        for j <- set2[1] ... set2[length(set2)]
            ...
            for n <- setN[1] ... setN[length(setN)]
                outputSet.add((i, j, ..., n))
    return outputSet

    make it recursive!

CARTESIAN-PRODUCT(listOfLists) // pass in a list containing lists of all sets
    if listOfLists is empty
        return () // empty tuple
    else
        for singleList in listsOfLists[1]
            newListofLists <- NIL
            for i <- listOfLists[2] ... listOfLists[length(listsOfLists)]
                newListofLists.add(listOfLists[i])
            for product in CARTESIAN-PRODUCT(newListofLists)
                return tuple(singleList) + product

