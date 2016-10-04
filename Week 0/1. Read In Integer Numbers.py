def validate(prompt):
  while True:
    try:
      inp = int(input(prompt))
      return inp
    except ValueError:
      print("Please insert an integer.")
      continue

a = validate("Enter an integer value for a: ")
b = validate("Enter an integer value for b: ")
c = validate("Enter an integer value for c: ")
d = validate("Enter an integer value for d: ")

ab = a/b
cd = c/d

if ab > cd:
  print(str(ab))
elif ab < cd:
  print(str(cd))
else:
  print("Both fractions equate to " + str(cd))