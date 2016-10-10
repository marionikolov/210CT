def validateInput(prompt, valType): # valType: 1 = day, 2 = month, 3 = year
  while True:
    try:
      inp = int(input(prompt))
      if valType == 1:
        if inp < 1 or inp > 31:
          raise ValueError("The value for day of month can only be between 1 and 31.")
      elif valType == 2:
        if inp < 1 or inp > 12:
          raise ValueError("The value for month can only be between 1 and 12.")
      return inp
    except ValueError:
      print("Please insert an integer.")
      continue

def isYearLeap(year):
  if year%4 == 0 or year%400 == 0:
    return True
  else:
    return False

def isDateReal(day, month, year):
  #longMonths = [1,3,5,7,8,10,12]
  shortMonths = [4,6,9,11] # excluding February, because it is special
  if month in shortMonths:
    if day == 31:
      raise ValueError("There cannot be 31 days in month " + month + ".")
  elif month == 2:
    if day == 29:
      continue

def DateCalculations():
  # input
  # calidate it is a real day
  # calculate current number of day
  # calculate how many days left
  # return

      # validate feb 30, 31, etc

# Determine whether leap year or not
#if userYear%4 == 0 or userYear%400 == 0:
    #leapyear = True