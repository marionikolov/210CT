# listOfList

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

