# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        DialogLogin.setObjectName("DialogLogin")
        DialogLogin.resize(430, 286)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/icon-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogLogin.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DialogLogin)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelGGPOLogo = QtWidgets.QLabel(DialogLogin)
        self.labelGGPOLogo.setText("")
        self.labelGGPOLogo.setPixmap(QtGui.QPixmap(":/assets/logo-vertical.png"))
        self.labelGGPOLogo.setObjectName("labelGGPOLogo")
        self.horizontalLayout_2.addWidget(self.labelGGPOLogo)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setObjectName("formLayout")
        self.labelUsername = QtWidgets.QLabel(DialogLogin)
        self.labelUsername.setObjectName("labelUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUsername)
        self.uiUsernameLine = QtWidgets.QLineEdit(DialogLogin)
        self.uiUsernameLine.setObjectName("uiUsernameLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiUsernameLine)
        self.labelPassword = QtWidgets.QLabel(DialogLogin)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.uiPasswordLine = QtWidgets.QLineEdit(DialogLogin)
        self.uiPasswordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiPasswordLine.setObjectName("uiPasswordLine")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiPasswordLine)
        self.uiSavePasswordChk = QtWidgets.QCheckBox(DialogLogin)
        self.uiSavePasswordChk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.uiSavePasswordChk.setChecked(True)
        self.uiSavePasswordChk.setObjectName("uiSavePasswordChk")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.uiSavePasswordChk)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiRegisterLink = QtWidgets.QCommandLinkButton(DialogLogin)
        self.uiRegisterLink.setObjectName("uiRegisterLink")
        self.horizontalLayout.addWidget(self.uiRegisterLink)
        self.uiLoginBtn = QtWidgets.QCommandLinkButton(DialogLogin)
        self.uiLoginBtn.setObjectName("uiLoginBtn")
        self.horizontalLayout.addWidget(self.uiLoginBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.uiErrorLbl = QtWidgets.QLabel(DialogLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiErrorLbl.sizePolicy().hasHeightForWidth())
        self.uiErrorLbl.setSizePolicy(sizePolicy)
        self.uiErrorLbl.setMouseTracking(False)
        self.uiErrorLbl.setStyleSheet("QLabel { color : red; font-weight: bold}")
        self.uiErrorLbl.setText("")
        self.uiErrorLbl.setTextFormat(QtCore.Qt.PlainText)
        self.uiErrorLbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.uiErrorLbl.setWordWrap(True)
        self.uiErrorLbl.setObjectName("uiErrorLbl")
        self.verticalLayout.addWidget(self.uiErrorLbl)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.uiNewVersionLink = QtWidgets.QCommandLinkButton(DialogLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNewVersionLink.sizePolicy().hasHeightForWidth())
        self.uiNewVersionLink.setSizePolicy(sizePolicy)
        self.uiNewVersionLink.setObjectName("uiNewVersionLink")
        self.horizontalLayout_21.addWidget(self.uiNewVersionLink)
        self.uiVersionLbl = QtWidgets.QLabel(DialogLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVersionLbl.sizePolicy().hasHeightForWidth())
        self.uiVersionLbl.setSizePolicy(sizePolicy)
        self.uiVersionLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uiVersionLbl.setObjectName("uiVersionLbl")
        self.horizontalLayout_21.addWidget(self.uiVersionLbl)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.labelUsername.setBuddy(self.uiUsernameLine)
        self.labelPassword.setBuddy(self.uiPasswordLine)

        self.retranslateUi(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)
        DialogLogin.setTabOrder(self.uiUsernameLine, self.uiPasswordLine)
        DialogLogin.setTabOrder(self.uiPasswordLine, self.uiSavePasswordChk)
        DialogLogin.setTabOrder(self.uiSavePasswordChk, self.uiLoginBtn)
        DialogLogin.setTabOrder(self.uiLoginBtn, self.uiRegisterLink)

    def retranslateUi(self, DialogLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogLogin.setWindowTitle(_translate("DialogLogin", "FightCade"))
        self.labelUsername.setText(_translate("DialogLogin", "Username"))
        self.labelPassword.setText(_translate("DialogLogin", "Password"))
        self.uiSavePasswordChk.setText(_translate("DialogLogin", "Save Password"))
        self.uiRegisterLink.setText(_translate("DialogLogin", "Create Account..."))
        self.uiLoginBtn.setText(_translate("DialogLogin", "Login"))
        self.uiNewVersionLink.setText(_translate("DialogLogin", "Download Update..."))
        self.uiVersionLbl.setText(_translate("DialogLogin", "version"))
# import ggpo_rc
