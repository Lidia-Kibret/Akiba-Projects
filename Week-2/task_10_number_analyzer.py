
total_sum = 0
even_count = 0
odd_count = 0
largest = None
smallest = None

for i in range(10):
    num = int(input("Enter a number: "))

    total_sum += num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

average = total_sum / 10

print("\n--- Number Analysis ---")
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total_sum)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
