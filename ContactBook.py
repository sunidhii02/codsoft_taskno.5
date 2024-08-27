class Contact:
    def __init__(self, name, phone, email=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, phone, email=None, address=None):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact { name } added successfully.")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
    def search_contact(self, term):
        results = [contact for contact in self.contacts if term.lower() in contact.name.lower() or term.lower() in contact.phone.lower()]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(contact)
    def update_contact(self, name, new_name, new_phone=None, new_email=None, new_address=None):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                contact.name = new_name
                contact.phone = new_phone if new_phone else contact.phone
                contact.email = new_email if new_email else contact.email
                contact.address = new_address if new_address else contact.address
                print(f"Contact { name } updated successfully.")
                return
        print(f"Contact { name } not found.")
    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact { name } deleted successfully.")
                return
        print(f"Contact { name } not found.")
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name (optional): ")
            new_phone = input("Enter new phone number (optional): ")
            new_email = input("Enter new email (optional): ")
            new_address = input("Enter new address (optional): ")
            contact_book.update_contact(name, new_name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book.Thank You, Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
