 # Spam messages:::

spam_keywords = ["buy now", "click this", "free money", "win prize", "subscribe now"]

comment = input("Enter a comment: ").lower()

is_spam = False

for keyword in spam_keywords:
    if keyword in comment:
        is_spam = True
        break

if is_spam:
    print("Spam comment detected!")
else:
    print("This comment is not spam.")


# Write a Python function to remove a given word from a list and strip it at the same time

def remove_word(words, word):
    new_list = []

    for item in words:
        item = item.strip()

        if item != word:
            new_list.append(item)

    return new_list


# Creating a list
words = [" apple ", "banana", " orange ", "apple", " mango "]

# Asking the user which word to remove
word = input("Enter the word to remove: ")

# Calling the function
result = remove_word(words, word)

# Displaying the updated list
print("Updated list:", result)