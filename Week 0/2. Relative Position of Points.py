a = (3,4)
b = (0,5)
c = (6,9)
p = (-2,4)

if p[0] < a[0] and p[0] < b[0] and p[0] < c[0]:
  print("The triangle is located right of the point p.")
elif p[0] > a[0] and p[0] > b[0] and p[0] > c[0]:
  print("The triangle is located left of the point p.")
elif p[1] < a[1] and p[1] < b[1] and p[1] < c[1]:
  print("The triangle is located above of the point p.")
elif p[1] > a[1] and p[1] > b[1] and p[1] > c[1]:
  print("The triangle is located below of the point p.")
else:
  print("The point and the triangle overlap on one of the axes.")