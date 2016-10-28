def findCubeDiffColour(listOfCubes, length, colour):
    for item in listOfCubes:
        if item[0] == length:
            return item
        else if item[1] != colour:
            return item

# cube format: (7, "blue")
def CubeTower(inputCubes, towerOfCubes = [], discardedCubes = [], duplicates = True, isSorted = False):
        if len(inputCubes) == 0:
            print(str(towerOfCubes))
            return () # is this required?
        # remove duplicates
        # sort

        # check whether the current cube is correctly placed
        ultCube = inputCubes[-1]
        penultCube = inputCube[-2]
        if ultCube[1] == penultCube[1]: # the last two cubes are of the same colour
            currentCubeSameSizeDiffColour = findCubeDiffColour(inputCubes, towerOfCubes[-1][0], towerOfCubes[-1][1])
            if currentCubeSameSizeDiffColour is not None:
                discardedCubes.append(towerOfCubes[-1]) # put current topmost cube in discarded
                del towerOfCubes[-1] # remove current topmost from tower
                towerOfCubes.append(currentCubeSameSizeDiffColour)
                inputCubes.remove(currentCubeSameSizeDiffColour) # remove currentCubeSameSizeDiffColour from inputCubes
                CubeTower(inputCubes, towerOfCubes, discardedCubes, True, False)

            lowerCubeSameSizeDiffColour = #
            elif lowerCubeSameSizeDiffColour is not None: # there is a bigger cube of same size but diff colour

            else:
                pass


        # put next cube of smaller size
