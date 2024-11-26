# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contact_card.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QToolButton, QWidget)
import resources

class Ui_ContactCard(object):
    def setupUi(self, ContactCard):
        if not ContactCard.objectName():
            ContactCard.setObjectName(u"ContactCard")
        ContactCard.resize(509, 75)
        self.horizontalLayout = QHBoxLayout(ContactCard)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.contactImage = QLabel(ContactCard)
        self.contactImage.setObjectName(u"contactImage")
        self.contactImage.setMinimumSize(QSize(50, 0))
        self.contactImage.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.contactImage)

        self.contactName = QLabel(ContactCard)
        self.contactName.setObjectName(u"contactName")

        self.horizontalLayout.addWidget(self.contactName)

        self.infoBtn = QToolButton(ContactCard)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/icons/right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.infoBtn)


        self.retranslateUi(ContactCard)

        QMetaObject.connectSlotsByName(ContactCard)
    # setupUi

    def retranslateUi(self, ContactCard):
        ContactCard.setWindowTitle(QCoreApplication.translate("ContactCard", u"Form", None))
        self.contactImage.setText(QCoreApplication.translate("ContactCard", u"<html><head/><body><p><img src=\":/icons/icons/user.png\"/></p></body></html>", None))
        self.contactName.setText(QCoreApplication.translate("ContactCard", u"Name", None))
        self.infoBtn.setText("")
    # retranslateUi

