print("========================================")
print("              RECEIPT")
print("========================================")

customer = input("Enter Customer Name: ")

product1 = input("Enter Product Name: ")
price1 = float(input("Enter Price: "))
quantity1 = int(input("Enter Quantity: "))

product2 = input("Enter Second Product Name: ")
price2 = float(input("Enter Second Product Price: "))
quantity2 = int(input("Enter Second Product Quantity: "))

total1 = price1 * quantity1
total2 = price2 * quantity2
total = total1 + total2

print("\n========================================")
print("              RECEIPT")
print("========================================")

print(f"Customer: {customer}")

print("\nProduct\t\tPrice\t\tQty")
print("----------------------------------------")
print(f"{product1}\t\t{price1:g} ETB\t\t{quantity1}")
print(f"{product2}\t\t{price2:g} ETB\t\t{quantity2}")

print("----------------------------------------")
print(f"Total: {total:g} ETB")

print("\nThank you for shopping!")
print("========================================")