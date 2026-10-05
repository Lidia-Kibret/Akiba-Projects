print("========================================")
print("           EMPLOYEE PAYSLIP")
print("========================================")

employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
transport_allowance = float(input("Enter Transport Allowance: "))
food_allowance = float(input("Enter Food Allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print("\n========================================")
print("           EMPLOYEE PAYSLIP")
print("========================================")

print(f"Employee: {employee_name}")
print(f"\nBasic Salary:          {basic_salary:,.2f} ETB")
print(f"Transport Allowance:   {transport_allowance:,.2f} ETB")
print(f"Food Allowance:        {food_allowance:,.2f} ETB")
print("----------------------------------------")
print(f"Gross Salary:          {gross_salary:,.2f} ETB")
print("========================================")