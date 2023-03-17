# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 650)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jira_project_label = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jira_project_label.sizePolicy().hasHeightForWidth())
        self.jira_project_label.setSizePolicy(sizePolicy)
        self.jira_project_label.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.jira_project_label.setFont(font)
        self.jira_project_label.setStyleSheet("color: rgb(30, 167, 224);")
        self.jira_project_label.setObjectName("jira_project_label")
        self.horizontalLayout.addWidget(self.jira_project_label)
        self.jira_proj_comboBox = QtGui.QComboBox(Dialog)
        self.jira_proj_comboBox.setObjectName("jira_proj_comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jira_proj_comboBox.addItem(icon, "")
        self.horizontalLayout.addWidget(self.jira_proj_comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.open_bug_radioButton = QtGui.QRadioButton(Dialog)
        self.open_bug_radioButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.open_bug_radioButton.setFont(font)
        self.open_bug_radioButton.setStyleSheet("QRadioButton:enabled  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.open_bug_radioButton.setObjectName("open_bug_radioButton")
        self.gridLayout_2.addWidget(self.open_bug_radioButton, 3, 0, 1, 1)
        self.feat_rqst_radioButton = QtGui.QRadioButton(Dialog)
        self.feat_rqst_radioButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.feat_rqst_radioButton.setFont(font)
        self.feat_rqst_radioButton.setStyleSheet("QRadioButton:enabled  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.feat_rqst_radioButton.setObjectName("feat_rqst_radioButton")
        self.gridLayout_2.addWidget(self.feat_rqst_radioButton, 3, 1, 1, 1)
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 2, 0, 1, 2)
        self.form_widget = QtGui.QWidget(Dialog)
        self.form_widget.setEnabled(True)
        self.form_widget.setObjectName("form_widget")
        self.gridLayout_3 = QtGui.QGridLayout(self.form_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.title_lineEdit = QtGui.QLineEdit(self.form_widget)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.gridLayout_3.addWidget(self.title_lineEdit, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.form_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.log_lineEdit = QtGui.QLineEdit(self.form_widget)
        self.log_lineEdit.setEnabled(True)
        self.log_lineEdit.setReadOnly(True)
        self.log_lineEdit.setObjectName("log_lineEdit")
        self.gridLayout_3.addWidget(self.log_lineEdit, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.form_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.results_pixmap = QtGui.QLabel(self.form_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_pixmap.sizePolicy().hasHeightForWidth())
        self.results_pixmap.setSizePolicy(sizePolicy)
        self.results_pixmap.setMinimumSize(QtCore.QSize(190, 190))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.results_pixmap.setFont(font)
        self.results_pixmap.setStyleSheet("QLabel {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #000000;\n"
"    border: 1px solid #000000;\n"
"}")
        self.results_pixmap.setFrameShape(QtGui.QFrame.NoFrame)
        self.results_pixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.results_pixmap.setObjectName("results_pixmap")
        self.gridLayout_3.addWidget(self.results_pixmap, 6, 1, 2, 2)
        self.log_pushButton = QtGui.QPushButton(self.form_widget)
        self.log_pushButton.setEnabled(True)
        self.log_pushButton.setObjectName("log_pushButton")
        self.gridLayout_3.addWidget(self.log_pushButton, 4, 2, 1, 1)
        self.submitPushButton = QtGui.QPushButton(self.form_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.submitPushButton.setFont(font)
        self.submitPushButton.setStyleSheet("QPushButton:enabled  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.submitPushButton.setObjectName("submitPushButton")
        self.gridLayout_3.addWidget(self.submitPushButton, 9, 0, 1, 3)
        self.screen_capture_btn = QtGui.QPushButton(self.form_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen_capture_btn.sizePolicy().hasHeightForWidth())
        self.screen_capture_btn.setSizePolicy(sizePolicy)
        self.screen_capture_btn.setObjectName("screen_capture_btn")
        self.gridLayout_3.addWidget(self.screen_capture_btn, 6, 0, 1, 1)
        self.clear_capture_btn = QtGui.QPushButton(self.form_widget)
        self.clear_capture_btn.setObjectName("clear_capture_btn")
        self.gridLayout_3.addWidget(self.clear_capture_btn, 7, 0, 1, 1)
        self.descrpt_plainTextEdit = QtGui.QPlainTextEdit(self.form_widget)
        self.descrpt_plainTextEdit.setObjectName("descrpt_plainTextEdit")
        self.gridLayout_3.addWidget(self.descrpt_plainTextEdit, 2, 1, 1, 2)
        self.line_2 = QtGui.QFrame(self.form_widget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 5, 0, 1, 3)
        self.label_5 = QtGui.QLabel(self.form_widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.form_widget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 8, 0, 1, 3)
        self.label_3 = QtGui.QLabel(self.form_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.priority_comboBox = QtGui.QComboBox(self.form_widget)
        self.priority_comboBox.setObjectName("priority_comboBox")
        self.priority_comboBox.addItem(icon, "")
        self.gridLayout_3.addWidget(self.priority_comboBox, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.form_widget, 5, 0, 1, 2)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.jira_proj_comboBox, self.open_bug_radioButton)
        Dialog.setTabOrder(self.open_bug_radioButton, self.feat_rqst_radioButton)
        Dialog.setTabOrder(self.feat_rqst_radioButton, self.title_lineEdit)
        Dialog.setTabOrder(self.title_lineEdit, self.priority_comboBox)
        Dialog.setTabOrder(self.priority_comboBox, self.descrpt_plainTextEdit)
        Dialog.setTabOrder(self.descrpt_plainTextEdit, self.log_lineEdit)
        Dialog.setTabOrder(self.log_lineEdit, self.log_pushButton)
        Dialog.setTabOrder(self.log_pushButton, self.screen_capture_btn)
        Dialog.setTabOrder(self.screen_capture_btn, self.clear_capture_btn)
        Dialog.setTabOrder(self.clear_capture_btn, self.submitPushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.jira_project_label.setText(QtGui.QApplication.translate("Dialog", "Jira Project:", None, QtGui.QApplication.UnicodeUTF8))
        self.jira_proj_comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Select Jira Project", None, QtGui.QApplication.UnicodeUTF8))
        self.open_bug_radioButton.setText(QtGui.QApplication.translate("Dialog", "Submit Bug Report", None, QtGui.QApplication.UnicodeUTF8))
        self.feat_rqst_radioButton.setText(QtGui.QApplication.translate("Dialog", "Submit Feature Request", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.log_lineEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "(optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.results_pixmap.setText(QtGui.QApplication.translate("Dialog", "(Optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.log_pushButton.setText(QtGui.QApplication.translate("Dialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.submitPushButton.setText(QtGui.QApplication.translate("Dialog", "Submit Jira Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.screen_capture_btn.setText(QtGui.QApplication.translate("Dialog", "Capture Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_capture_btn.setText(QtGui.QApplication.translate("Dialog", "Clear Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Log File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Priority:", None, QtGui.QApplication.UnicodeUTF8))
        self.priority_comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Select Priority", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc