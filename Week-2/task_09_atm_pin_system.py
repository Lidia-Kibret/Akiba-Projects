
correct_pin = 1234
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = int(input("Enter your PIN: "))
    attempts += 1

    if pin == correct_pin:
        print("Correct PIN!")
        print("Access granted.")
        break
    else:
        remaining = max_attempts - attempts
        print("Incorrect PIN.")

        if remaining > 0:
            print("Attempts remaining:", remaining)
        else:
            print("Account locked!")
