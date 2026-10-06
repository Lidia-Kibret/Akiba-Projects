print("========================================")
print("          STUDENT RESULT")
print("========================================")

student_name = input("Enter Student Name: ")
python_score = float(input("Enter Python Score: "))
english_score = float(input("Enter English Score: "))
mathematics_score = float(input("Enter Mathematics Score: "))

average = (python_score + english_score + mathematics_score) / 3

print("\n========================================")
print("          STUDENT RESULT")
print("========================================")

print(f"Student: {student_name}")
print(f"\nPython:        {python_score:g}")
print(f"English:       {english_score:g}")
print(f"Mathematics:   {mathematics_score:g}")
print("----------------------------------------")
print(f"Average:       {average:.2f}")

print("========================================")