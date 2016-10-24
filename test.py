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

a = product_recursion([[1,2,3], [4],[5,6]])
print(a)