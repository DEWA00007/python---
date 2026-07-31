# A contact book Program

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = int(input("Enter phone number: "))

    contacts[name] = phone
    print(f"{name} added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts saved.\n")
    else:
        print("\n--- Contact List ---")
        for name in contacts:
            print(name, ":", contacts[name])
        print()


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print(f"{name}'s phone number is {contacts[name]}\n")
    else:
        print("Contact not found.\n")


def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        phone = int(input("Enter new phone number: "))
        contacts[name] = phone
        print(f"{name}'s number updated!\n")
    else:
        print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        contacts.pop(name)
        print(f"{name} deleted!\n")
    else:
        print("Contact not found.\n")


while True:
    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")