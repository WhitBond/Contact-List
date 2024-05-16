from Contact import ContactList
from Contact import DSAContact
from Contact import read_contacts_from_file
def display_menu():
    print("\nContact List Management System")
    print("1. View contacts list")
    print("2. Add new contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. Search contacts")
    print("6. Sort contact list")
    print("7. Display contacts belonging to a particular group")
    print("8. Exit")

def main():
    contact_list = ContactList()

    # Load contacts from file if needed
    contact_list = read_contacts_from_file("contact_list.txt")

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            contact_list.print_all_contacts()
        elif choice == "2":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            group = input("Enter group (F/W/FR): ")
            contact = DSAContact(name, phone_number, email, group)
            contact_list.add_contact(contact)
        elif choice == "3":
            phone_number = input("Enter phone number of contact to delete: ")
            contact_list.remove_contact(phone_number)
        elif choice == "4":
            phone_number = input("Enter phone number of contact to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            group = input("Enter new group (F/W/FR): ")
            updated_contact = DSAContact(name, phone_number, email, group)
            contact_list.update_contact(phone_number, updated_contact)
        elif choice == "5":
            search_term = input("Enter search term (name or phone number): ")
            contact_list.search_contacts(search_term)
        elif choice == "6":
            contact_list.sort_contacts_by_name()
        elif choice == "7":
            group = input("Enter group to display contacts: ")
            contact_list.filter_contacts_by_group(group)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()

