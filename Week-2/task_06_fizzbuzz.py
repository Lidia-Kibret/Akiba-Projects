s = int(input("Enter the starting number:"))
e = int(input("Enter the ending number: "))

for i in range(s, e + 1):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)