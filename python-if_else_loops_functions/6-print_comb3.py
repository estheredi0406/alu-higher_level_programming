#!/usr/bin/python3
for i in range(10):
  for j in range(i + 1, 10):
    if j <= 9:  # Check if second digit is less than or equal to 9
      print("{}{}".format(i, j), end=", ")
  # Print 8 + second digit directly after the loop for i=7
  if i == 7:
    print("89")
print()  # Separate newline for final output
