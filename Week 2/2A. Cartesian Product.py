def cartesianProductRecursive(listOfLists):
    result = [] # initiate a list which will hold the resulting sets
    for i in listOfLists[0]:
        for j in listOfLists[1]:
            if type(i) == list: # if we pass in a list, append results to it
                x = i.copy()
            else: # this means it is the code's first run; initiate a list to hold the products
                x = [i]
            x.append(j)
            result.append(x)
    if len(listOfLists[2:]) > 0: # if there are more sets to combine with the resultant set
        return cartesianProductRecursive([result] + listOfLists[2:])
    else:
        return result

if __name__ == '__main__':
    testList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    testProduct = cartesianProductRecursive(testList)
    print(str(testProduct))