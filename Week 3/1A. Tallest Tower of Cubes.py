"""
Used to find a cube of a given length within the listOfCubes provided. Returns the first cube it finds that fits the criterion or returns None if not appropriate cube is found.
PARAMETERS
    listOfCubes - list of cubes to search in the format (2, 'red') where the integer is the size of the cube and the string its colour
    length - the required length of the cube
"""
def findFirstSmallerCube(listOfCubes, length):
    for item in listOfCubes:
        if item[0] < length:
            return item
    return None
"""
Used to find a cube of the same length but a different colour within the listOfCubes provided. Returns the first cube it finds that fits the criteria or returns None if not appropriate cube is found.
PARAMETERS
    listOfCubes - list of cubes to search in the format (2, 'red') where the integer is the size of the cube and the string its colour
    length - the required length of the cube
    colour - the colour the cube must NOT be
"""
def findCubeDiffColour(listOfCubes, length, colour):
    for item in listOfCubes:
        if item[0] == length and item[1] != colour:
            return item
    return None

"""
Build the tallest tower of cubes possible from a set of input cubes following the given rules:
- the cube size needs to be in descending order starting from the base; no two cubes of the same size can be put on top of each other;
- colours of neighbouring cubes must vary; no two cubes of the same colour can be put on top of each other.
PARAMETERS
    inputCubes - a list of input cubes in the format (2, 'red') where the integer is the size of the cube and the string its colour
    towerOfCubes - the resulting tower the code is building
    discardedCubes - a list of cubes already used in the process, but discarded due to ineligibility
    duplicates - a boolean value showing whether the inputCubes have been checked for duplicates or not; the value is set from the function itself
    isSorted - a boolean value showing whether the inputCubes are sorted by size or not; the value is set from the function itself
To call the function only provide the list of inputCubes in the correct format. E.g.: buildCubeTower([(2, 'red'), (1, 'purple'), (4, 'blue'), (2, "purple")])
"""
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
            buildCubeTower([], towerOfCubes, discardedCubes, False, True) # explicitly call the base case
        else:
            towerOfCubes.append(nextCubeToPut)
            inputCubes.remove(nextCubeToPut)
            print(str(towerOfCubes))
            buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True)

if __name__ == "__main__":
    data = [(2, 'red'), (1, 'purple'), (4, 'blue'), (2, "purple")]
    buildCubeTower(data)