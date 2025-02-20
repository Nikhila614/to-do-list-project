import json
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    def view_contacts(self):
        for c in self.contacts:
            print(f"{c['name']} - {c['phone']}")
    def search_contact(self, query):
        for c in self.contacts:
            if query in (c['name'], c['phone']):
                print(json.dumps(c, indent=2))
    def update_contact(self, name, phone=None, email=None, address=None):
        for c in self.contacts:
            if c['name'] == name:
                if phone: c['phone'] = phone
                if email: c['email'] = email
                if address: c['address'] = address
    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
cb = ContactBook()
while True:
    choice = input("1. Add 2. View 3. Search 4. Update 5. Delete 6. Exit: ")
    if choice == '1':
        cb.add_contact(input("Name: "), input("Phone: "), input("Email: "), input("Address: "))
    elif choice == '2':
        cb.view_contacts()
    elif choice == '3':
        cb.search_contact(input("Search by Name/Phone: "))
    elif choice == '4':
        cb.update_contact(input("Name: "), input("New Phone: ") or None, input("New Email: ") or None, input("New Address: ") or None)
    elif choice == '5':
        cb.delete_contact(input("Name to Delete: "))
    elif choice == '6':
        break
