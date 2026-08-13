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