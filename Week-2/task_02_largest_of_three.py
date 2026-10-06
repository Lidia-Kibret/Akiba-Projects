num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1 == num2 == num3:
  print("All three numbers are equal.")
elif num1 >= num2 and num1 >= num3:
  print(f"The largest number is: {num1}.")
elif num2 >= num1 and num2 >= num3:
  print(f"The largest number is: {num2}.")
else:
  print(f"The largest number is: {num3}.")