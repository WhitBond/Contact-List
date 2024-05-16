class DSAContact:
    def __init__(self, name, phone_number, email, group):
        self.name = name # Store the name of the contact
        self.phone_number = phone_number # Store the phone number of the contact
        self.email = email # Store the email address of the contact
        self.group = group # Store the group of the contact (e.g., Friends, Family)

    def __str__(self):# Define the string representation of the contact with its name, phone number, email, and group
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}, Group: {self.group}"

class ContactList:
    def __init__(self, size=15):  # Default size set to 15
        self.size = size # Store the size of the contact list
        self.count = 0 # Initialize the count of contacts to zero
        self.contacts = [None] * size  # Initialize hash table with None values
        

    def get_index(self, phone_number):  # Generate an index in the contact list based on the phone number
        return int(phone_number) % self.size

    def hash2(self, phone_number):
        # Secondary hash function for double hashing
        # Example: hash2(phone_number) = prime - (phone_number % prime)
        prime = 31
        return prime - (int(phone_number) % prime)

    def resize(self, new_size):  # Resize the contact list to accommodate more contacts
        old_contacts = self.contacts
        self.size = new_size
        self.contacts = [None] * new_size
        self.count = 0

        for contact in old_contacts:
            if contact:
                self.add_contact(contact)

    def check_duplicate(self, phone_number): #Cheking if the number already exsit
        index = self.get_index(phone_number)
        contact = self.contacts[index]
        if contact and contact.phone_number == phone_number:
            return True
        index2 = self.hash2(phone_number)
        step = 1
        while step < self.size:
            new_index = (index + step * index2) % self.size
            contact = self.contacts[new_index]
            if contact and contact.phone_number == phone_number:
                return True
            step += 1
        return False

    def add_contact(self, contact):# Add a contact to the contact list
        if not contact.phone_number.isdigit():#check if the phone number have any non-numberic character
            print("Phone number should contain only numeric characters.")
            return
        if self.check_duplicate(contact.phone_number):
            print("Contact with this phone number already exists.")
            return

        if self.count / self.size > 0.7: # Check if the load factor exceeds 0.7
            new_size = self.size * 2 # Double the size of the contact list
            self.resize(new_size) # Resize the contact list

        index = self.get_index(contact.phone_number)  # Get the index for the contact

        if not self.contacts[index]: # If the index is empty
            self.contacts[index] = contact# Add the contact to the list
            self.count += 1 # Increment the count of contacts
            print(f"Contact added successfully: {contact.name}")
        else: # If collision occurs
            index2 = self.hash2(contact.phone_number)  # Get the secondary hash index
            step = 1
            while True:# Resolve collision by double hashing
                new_index = (index + step * index2) % self.size
                if not self.contacts[new_index]:
                    self.contacts[new_index] = contact
                    self.count += 1
                    print(f"Contact added successfully: {contact.name}")
                    return
                step += 1

    def remove_contact(self, phone_number):  # Remove a contact from the contact list based on the phone number
        if not phone_number.isdigit():
            print("Phone number should contain only numeric characters.")
            return

        index = self.get_index(phone_number)
        contact = self.contacts[index]
        if contact and contact.phone_number == phone_number:
            self.contacts[index] = None #remove the contact from the list
            self.count -= 1
            print(f"Contact with phone number {phone_number} removed successfully.")
            return
        elif contact and contact.phone_number != phone_number:# If collision occurs
            index2 = self.hash2(phone_number) # Resolve collision by double hashing
            step = 1
            while step < self.size:
                new_index = (index + step * index2) % self.size
                if self.contacts[new_index] and self.contacts[new_index].phone_number == phone_number:
                    self.contacts[new_index] = None 
                    self.count -= 1
                    print(f"Contact with phone number {phone_number} removed successfully.")
                    return
                step += 1
        print(f"No contact found with phone number {phone_number}.")

    def update_contact(self, phone_number, updated_contact):  # Update the contact with the given phone number with the information provided in updated_contact
        if not phone_number.isdigit():
            print("Phone number should contain only numeric characters.")
            return

        index = self.get_index(phone_number)
        contact = self.contacts[index]

        if contact and contact.phone_number == phone_number: # If the contact is found, update its information
            contact.name = updated_contact.name #update new name
            contact.email = updated_contact.email #update new email
            contact.group = updated_contact.group #update new group contact
            return
            print(f"Contact with phone number {phone_number} updated successfully.")
        elif contact and contact.phone_number != phone_number:  # If collision occurs, search for the contact using double hashing
            index2 = self.hash2(phone_number)
            step = 1
            while step < self.size:
                new_index = (index + step * index2) % self.size #new index after use double hashing
                contact = self.contacts[new_index]
                if contact and contact.phone_number == phone_number:
                    contact.name = updated_contact.name
                    contact.email = updated_contact.email
                    contact.group = updated_contact.group
                    print(f"Contact with phone number {phone_number} updated successfully.")
                    return
                step += 1
        print(f"No contact found with phone number {phone_number}.")
    
    
    def print_all_contacts(self):#to print out the list of contact
        print("All Contacts:")
        for contact in self.contacts:
            if contact:
                print(contact)

    def search_contacts(self, search_term):# Search for contacts containing the given search term (case-insensitive) in their name or phone number
        matching_contacts = []
        for contact in self.contacts:
            if contact and (search_term.lower() in contact.name.lower() or search_term in contact.phone_number):
                matching_contacts.append(contact)
        if matching_contacts:
            print("Matching Contacts:")
            for contact in matching_contacts:
                print(contact)
        else:
            print("No matching contacts found.")

    def extract_contact_names(self):   # Extract the names of all contacts in the contact list
        contact_names = []
        for contact in self.contacts:
            if contact:
                contact_names.append(contact.name)
        return contact_names

    def merge_sort(self, arr):# Perform merge sort on the given list arr
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def sort_contacts_by_name(self): # Sort contacts in the contact list by their names and print them
        contact_names = self.extract_contact_names()
        self.merge_sort(contact_names)

        print("Sorted Contacts by Name:")
        for name in contact_names:
            for contact in self.contacts:
                if contact and contact.name == name:
                    print(contact)
                    

    def filter_contacts_by_group(self, group): # Filter contacts in the contact list by the given group and print them
        filtered_contacts = []
        for contact in self.contacts:
            if contact and contact.group == group:
                filtered_contacts.append(contact)

        if filtered_contacts:
            print(f"Contacts in the '{group}' group:")
            for contact in filtered_contacts:
                print(contact)
        else:
            print(f"No contacts found in the '{group}' group.")
contact_list = ContactList() # Create an instance of the ContactList class
def read_contacts_from_file(file_name):
    contact_list = ContactList()
    with open(file_name, 'r') as file: # Open the file for reading
        for line in file: # Iterate over each line in the file
            data = line.strip().split(',') # Split the line by comma to extract contact information
            phone_number, name, email, group = data # Unpack the contact information
            contact = DSAContact(name, phone_number, email, group)  # Create a DSAContact object
            contact_list.add_contact(contact) # Add the contact to the contact list
    return contact_list  # Return the populated contact list


