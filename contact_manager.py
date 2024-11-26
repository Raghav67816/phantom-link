from json import dump, load

class ContactsManager():
    def __init__(self):
        super().__init__()

        self.contacts_data = None

        self.file_path = './config/contacts.json'
        with open(self.file_path, 'r') as contacts_file:
            self.contacts_data = load(contacts_file)
            print(self.contacts_data)
            contacts_file.close()

    def get_contacts(self):
        return self.contacts_data
    
    def get_contact_info(self, name):
        return self.contacts_data[name]
    
    def add_new(self, name: str, number: int, comment: str):
        contact = {
            "name": name,
            "number": number,
            "comment": comment
        }
        self.contacts_data[name] = contact
        with open(self.file_path, 'w') as contacts:
            dump(self.contacts_data, contacts, indent=4)
            contacts.close()
        self.contacts_data = self.get_contacts()

    def remove_contact(self, name: str):
        self.contacts_data.pop(name)
        with open(self.file_path, 'w') as contacts:
            dump(self.contacts_data, contacts, indent=4)
            contacts.close()
        
