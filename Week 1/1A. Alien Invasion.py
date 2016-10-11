aliens = 1
aliensArray = []
eggs = 0
eggsDaily = 3
hatchingPeriod = 5
period = 30
currentDay = 1

while currentDay < period:
    aliensArray.append(aliens)
    print(aliensArray)
    if currentDay >= hatchingPeriod - 1: # We assume that the first day counts as part of the incubation period.
        aliens += aliensArray[currentDay-hatchingPeriod+1] * eggsDaily
        print(aliens)
    currentDay += 1

print("Final number of aliens after " + str(period) + " days: " + str(aliens))