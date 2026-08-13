# Roman Nepali to English dictionary
nepali_dict = {
    "namaste": "Hello",
    "pani": "Water",
    "ghar": "House",
    "kitab": "Book",
    "sathi": "Friend",
    "khana": "Food",
    "school": "School",
    "maya": "Love",
    "surya": "Sun",
    "jun": "Moon"
}

# Let the user look up words
while True:
    word = input("Enter a Roman Nepali word (or type 'exit' to quit): ")

    if word.lower() == "exit":
        print("Goodbye!")
        break

    if word.lower() in nepali_dict:
        print("English translation:", nepali_dict[word.lower()])
    else:
        print("Word not found in the dictionary.")