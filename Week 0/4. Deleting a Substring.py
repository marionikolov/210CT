def validateInt(prompt):
  while True:
    try:
      inp = int(input(prompt))
      return inp
    except ValueError:
      print("Please insert an integer.")
      continue

def deleteSubstring():
  inpString = input("Input the string that you want to delete from: ")
  startPos = validateInt("What position would you like to start deleting from? ")
  delLength = validateInt("How many letters would you like to delete? ")
  secondStartPos = startPos + delLength
  substring = inpString[0:startPos] + inpString[secondStartPos:]
  return substring

print(deleteSubstring())