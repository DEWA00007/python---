# Text Analyzer

text = input("Enter a word or sentence: ")

# Word count
words = text.split()
print("\nNumber of words:", len(words))

# Character count
print("Number of characters:", len(text))

# Reverse
reverse = text[::-1]
print("Reversed:", reverse)

# Palindrome check
if text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")