# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 700)
        MainWindow.setMinimumSize(QSize(480, 700))
        MainWindow.setMaximumSize(QSize(480, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.contacts_page = QWidget()
        self.contacts_page.setObjectName(u"contacts_page")
        self.verticalLayout_2 = QVBoxLayout(self.contacts_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.searchBtn = QLineEdit(self.contacts_page)
        self.searchBtn.setObjectName(u"searchBtn")

        self.verticalLayout_2.addWidget(self.searchBtn)

        self.contactsContainer = QFrame(self.contacts_page)
        self.contactsContainer.setObjectName(u"contactsContainer")
        self.contactsContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.contactsContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.contactsLayout = QVBoxLayout(self.contactsContainer)
        self.contactsLayout.setObjectName(u"contactsLayout")

        self.verticalLayout_2.addWidget(self.contactsContainer)

        self.addContactBtn = QPushButton(self.contacts_page)
        self.addContactBtn.setObjectName(u"addContactBtn")

        self.verticalLayout_2.addWidget(self.addContactBtn)

        self.pages.addWidget(self.contacts_page)
        self.contact_info_page = QWidget()
        self.contact_info_page.setObjectName(u"contact_info_page")
        self.verticalLayout_4 = QVBoxLayout(self.contact_info_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.avataar = QLabel(self.contact_info_page)
        self.avataar.setObjectName(u"avataar")

        self.verticalLayout_4.addWidget(self.avataar)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.nameLabel_2 = QLabel(self.contact_info_page)
        self.nameLabel_2.setObjectName(u"nameLabel_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.nameLabel_2)

        self.nameLineEdit = QLineEdit(self.contact_info_page)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.contactNumberLabel = QLabel(self.contact_info_page)
        self.contactNumberLabel.setObjectName(u"contactNumberLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.contactNumberLabel)

        self.number_box = QLineEdit(self.contact_info_page)
        self.number_box.setObjectName(u"number_box")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.number_box)

        self.commentLabel = QLabel(self.contact_info_page)
        self.commentLabel.setObjectName(u"commentLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.commentLabel)

        self.comment_box = QLineEdit(self.contact_info_page)
        self.comment_box.setObjectName(u"comment_box")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comment_box)


        self.verticalLayout_4.addLayout(self.formLayout_2)

        self.btnBox = QFrame(self.contact_info_page)
        self.btnBox.setObjectName(u"btnBox")
        self.btnBox.setMaximumSize(QSize(16777215, 60))
        self.btnBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.btnBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.callBtn = QPushButton(self.btnBox)
        self.callBtn.setObjectName(u"callBtn")

        self.horizontalLayout_3.addWidget(self.callBtn)

        self.deleteBtn = QPushButton(self.btnBox)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.horizontalLayout_3.addWidget(self.deleteBtn)


        self.verticalLayout_4.addWidget(self.btnBox)

        self.pages.addWidget(self.contact_info_page)
        self.add_contact_page = QWidget()
        self.add_contact_page.setObjectName(u"add_contact_page")
        self.verticalLayout_3 = QVBoxLayout(self.add_contact_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.add_contact_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_3.addWidget(self.label_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.add_contact_page)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameInput = QLineEdit(self.add_contact_page)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameInput)

        self.contactNoLabel = QLabel(self.add_contact_page)
        self.contactNoLabel.setObjectName(u"contactNoLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.contactNoLabel)

        self.contactInput = QLineEdit(self.add_contact_page)
        self.contactInput.setObjectName(u"contactInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.contactInput)

        self.commentsLabel = QLabel(self.add_contact_page)
        self.commentsLabel.setObjectName(u"commentsLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.commentsLabel)

        self.commentInput = QLineEdit(self.add_contact_page)
        self.commentInput.setObjectName(u"commentInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.commentInput)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.btnContainer_2 = QFrame(self.add_contact_page)
        self.btnContainer_2.setObjectName(u"btnContainer_2")
        self.btnContainer_2.setMinimumSize(QSize(0, 50))
        self.btnContainer_2.setMaximumSize(QSize(16777215, 50))
        self.btnContainer_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnContainer_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.btnContainer_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveBtn = QPushButton(self.btnContainer_2)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_2.addWidget(self.saveBtn)

        self.discardBtn = QPushButton(self.btnContainer_2)
        self.discardBtn.setObjectName(u"discardBtn")

        self.horizontalLayout_2.addWidget(self.discardBtn)


        self.verticalLayout_3.addWidget(self.btnContainer_2)

        self.pages.addWidget(self.add_contact_page)

        self.verticalLayout.addWidget(self.pages)

        self.btnContainer = QFrame(self.centralwidget)
        self.btnContainer.setObjectName(u"btnContainer")
        self.btnContainer.setMinimumSize(QSize(0, 40))
        self.btnContainer.setMaximumSize(QSize(16777215, 40))
        self.btnContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.btnContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.contactsBtn = QToolButton(self.btnContainer)
        self.contactsBtn.setObjectName(u"contactsBtn")
        self.contactsBtn.setMinimumSize(QSize(40, 40))
        self.contactsBtn.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/icons/contacts.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contactsBtn.setIcon(icon)
        self.contactsBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.contactsBtn)

        self.dialPadBtn = QToolButton(self.btnContainer)
        self.dialPadBtn.setObjectName(u"dialPadBtn")
        self.dialPadBtn.setMinimumSize(QSize(40, 40))
        self.dialPadBtn.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/phone.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dialPadBtn.setIcon(icon1)
        self.dialPadBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.dialPadBtn)

        self.settingsBtn = QToolButton(self.btnContainer)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(40, 40))
        self.settingsBtn.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon2)
        self.settingsBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.settingsBtn)


        self.verticalLayout.addWidget(self.btnContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Page name", None))
        self.addContactBtn.setText(QCoreApplication.translate("MainWindow", u"Add Contact", None))
        self.avataar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/user.png\"/></p></body></html>", None))
        self.nameLabel_2.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.contactNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Contact Number: ", None))
        self.commentLabel.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.callBtn.setText(QCoreApplication.translate("MainWindow", u"Call", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/user.png\"/></p></body></html>", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.contactNoLabel.setText(QCoreApplication.translate("MainWindow", u"Contact No: ", None))
        self.commentsLabel.setText(QCoreApplication.translate("MainWindow", u"Comments: ", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.discardBtn.setText(QCoreApplication.translate("MainWindow", u"Discard", None))
        self.contactsBtn.setText("")
        self.dialPadBtn.setText("")
        self.settingsBtn.setText("")
    # retranslateUi

