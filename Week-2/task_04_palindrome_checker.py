word = input("Enter a word: ")
word = word.lower()
if word == word[::-1]:
  print("The word is Palindrome. ")
else:
  print("The word is not Palindrome. ")
  