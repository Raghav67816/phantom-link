from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame
from interface.contact_card import Ui_ContactCard

class ContactWidget(QFrame):

    info_clicked = Signal(str)

    def __init__(self, name: str, on_info: callable = None):
        super().__init__()

        self.ui = Ui_ContactCard()
        self.ui.setupUi(self)

        self.name = name

        self.ui.contactName.setText(name)
        self.ui.contactImage.setMaximumSize(40, 40)
        
        if on_info is None:
            self.ui.infoBtn.clicked.connect(self.on_info_clicked)
        else:
            self.ui.infoBtn.clicked.connect(on_info)

    def on_info_clicked(self):
        self.info_clicked.emit(self.name)
