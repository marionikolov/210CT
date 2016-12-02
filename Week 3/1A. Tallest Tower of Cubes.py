def findFirstSmallerCube(listOfCubes, length):
    for item in listOfCubes:
        if item[0] < length:
            return item

def findCubeDiffColour(listOfCubes, length, colour):
    for item in listOfCubes:
        if item[0] == length and item[1] != colour:
            return item
    return None

# cube format: (7, "blue")
def buildCubeTower(inputCubes, towerOfCubes = [], discardedCubes = [], duplicates = True, isSorted = False):
    if len(inputCubes) == 0: # base case
        print(str(towerOfCubes))
        print("Exited")
        return ()

    if duplicates:
        inputCubes = list(set(inputCubes)) # remove duplicates by casting to a set (no duplicates by definition) and then cast to a list again for further use
        duplicates = False

    if not isSorted:
        inputCubes.sort(key = lambda x: x[0], reverse = True) # sort the input cubes by size in descending order
        isSorted = True

    if len(towerOfCubes) == 0: # if this is the first run, place the first cube from the sorted input data on the tower
        towerOfCubes.append(inputCubes[0])
        del inputCubes[0]
        print(str(towerOfCubes))
        buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True)
    else:
        if len(towerOfCubes) >= 2: # check whether the current cube is correctly placed
            ultCube = towerOfCubes[-1] # ultimate / topmost cube
            penultCube = towerOfCubes[-2] # penultimate / topmost-but-one cube
            if ultCube[1] == penultCube[1]: # the last two cubes are of the same colour
                currentCubeSameSizeDiffColour = findCubeDiffColour(inputCubes, towerOfCubes[-1][0], towerOfCubes[-1][1])
                lowerCubeSameSizeDiffColour = findCubeDiffColour(inputCubes, towerOfCubes[-2][0], towerOfCubes[-2][1])
                if currentCubeSameSizeDiffColour is not None: # if there is a cube of the same size but of different colour to substitute the topmost coinciding one
                    discardedCubes.append(towerOfCubes[-1]) # put current topmost cube in discarded
                    del towerOfCubes[-1] # remove current topmost from tower
                    towerOfCubes.append(currentCubeSameSizeDiffColour)
                    inputCubes.remove(currentCubeSameSizeDiffColour)
                    print(str(towerOfCubes))
                    buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True)
                elif lowerCubeSameSizeDiffColour is not None: # if there is a bigger cube of same size but diff colour to substitute the lower conflicting cube
                    currentCubeSize = towerOfCubes[-1][0] # get the size of the current topmost cube
                    inputCubes.append(towerOfCubes[-1]) # return the current topmost cube to the inputCubes list
                    del towerOfCubes[-1]
                    for cube in discardedCubes: # return all cubes of the same size as the now returned topmost cube to the inputCubes list
                        if cube[0] == currentCubeSize:
                            inputCubes.append(cube)
                    discardedCubes.append(towerOfCubes[-1]) # discard the lower conflicting cube
                    del towerOfCubes[-1]
                    towerOfCubes.append(lowerCubeSameSizeDiffColour)
                    inputCubes.remove(lowerCubeSameSizeDiffColour) # it used to remove currentCubeSameSizeDiffColour ??
                    print(str(towerOfCubes))
                    buildCubeTower(inputCubes, towerOfCubes, discardedCubes, True, False) # check the last two parameters
        currentCubeSize = towerOfCubes[-1][0]
        nextCubeToPut = findFirstSmallerCube(inputCubes, currentCubeSize)
        if nextCubeToPut is None:
            buildCubeTower([], towerOfCubes, discardedCubes, False, True)
        else:
            towerOfCubes.append(nextCubeToPut)
            inputCubes.remove(nextCubeToPut)
            print(str(towerOfCubes))
            buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True)

if __name__ == "__main__":
    data = [(2, 'red'), (1, 'purple'), (4, 'blue'), (2, "purple")]
    buildCubeTower(data)