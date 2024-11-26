# Import dependencies
from app import Ui_MainWindow
from PySide6.QtCore import Qt
from contact_manager import ContactsManager
from interface.contact_widget import ContactWidget
from PySide6.QtWidgets import QMainWindow, QApplication

# main window class
class PhoneApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.contact_manager = ContactsManager()

        self.clear_list()
        self.load_contacts()

        self.setMaximumSize(480, 700)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.pages.setCurrentIndex(0)
        self.ui.label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ui.contactsLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.ui.addContactBtn.clicked.connect(self.on_add_contact)
        self.ui.saveBtn.clicked.connect(self.on_save_contact)
        self.ui.discardBtn.clicked.connect(self.on_discard_contact)
        self.ui.pages.currentChanged.connect(self.on_page_change)
        self.ui.contactsBtn.clicked.connect(self.on_contact_list_btn_clicked)

        # set stylesheet
        with open('style.css', 'r') as styles:
            style = styles.read()
            self.setStyleSheet(style)
            styles.close()

        self.ui.searchBtn.setPlaceholderText("Search contacts...")
        self.ui.label.setText("Contact List")
        self.ui.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    def clear_list(self):
        widgets = self.findChildren(ContactWidget)
        for widget in widgets:
            widget.deleteLater()

    def load_contacts(self):
        contacts = self.contact_manager.get_contacts()
        for contact in contacts:
            contact_widget = ContactWidget(contact)
            contact_widget.info_clicked.connect(self.show_contact_info)
            self.ui.contactsLayout.addWidget(contact_widget)
            print(f'{contact} added')


    def on_add_contact(self):
        self.ui.label.setText("New Contact")
        self.ui.pages.setCurrentIndex(2)

    def on_save_contact(self):
        name = self.ui.nameInput.text()
        contact_no = self.ui.contactInput.text()
        comment = self.ui.commentInput.text()

        if name != "" and contact_no != "":
            self.contact_manager.add_new(
                name, contact_no, comment
            )
            self.clear_list()
            self.load_contacts()
            self.ui.pages.setCurrentIndex(0)

        else:
            print("Please provide all required fields.")

    def on_discard_contact(self):
        self.contact_manager.remove_contact(self.ui.nameInput.text())
        self.clear_list()
        self.load_contacts()
        self.ui.pages.setCurrentIndex(0)
        self.ui.label.setText("Contacts")

    def on_page_change(self, index):
        if index == 0:
            self.clear_list()
            self.load_contacts()

    def show_contact_info(self, name: str):
        contact_info = self.contact_manager.get_contact_info(name)
        self.ui.pages.setCurrentIndex(2)
        self.ui.nameInput.setText(contact_info['name'])
        self.ui.contactInput.setText(contact_info['number'])
        self.ui.commentInput.setText(contact_info['comment'])
        self.ui.label.setText("Contact Info")

    def on_contact_list_btn_clicked(self):
        self.ui.pages.setCurrentIndex(0)
        self.ui.label.setText('Contacts')

    def on_dialpad_btn_clicked(self):
        pass

    def on_settings_btn_clicked(self):
        pass


# run app
if __name__ == '__main__':
    app = QApplication()
    window = PhoneApp()
    window.show()
    app.exec()
