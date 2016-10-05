def validate(prompt):
  while True:
    try:
      inp = float(input(prompt))
      return inp
    except ValueError:
      print("Please insert a floating point number.")
      continue
def function(x):
  if x < -2:
    return (x**2 + 4*x + 4)
  elif x == 0:
    return 0
  elif x > -2:
    return (x**2 + 5*x)

x = validate("Enter the value of x: ")
fx = function(x)
print(fx)