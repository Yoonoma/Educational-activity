# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_report.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 560)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(560, 560))
        Dialog.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(540, 350))
        self.tableWidget.setSizeIncrement(QtCore.QSize(540, 350))
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(171)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(73)
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.lbl_1 = QtWidgets.QLabel(Dialog)
        self.lbl_1.setStyleSheet("border: 1px solid;\n"
"background-color: rgb(211, 215, 207);")
        self.lbl_1.setObjectName("lbl_1")
        self.verticalLayout_2.addWidget(self.lbl_1)
        self.Layout_input_path = QtWidgets.QHBoxLayout()
        self.Layout_input_path.setObjectName("Layout_input_path")
        self.le_folder_path = QtWidgets.QLineEdit(Dialog)
        self.le_folder_path.setMinimumSize(QtCore.QSize(0, 35))
        self.le_folder_path.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border: 1px solid;")
        self.le_folder_path.setReadOnly(True)
        self.le_folder_path.setObjectName("le_folder_path")
        self.Layout_input_path.addWidget(self.le_folder_path)
        self.btn_chouse_dir = QtWidgets.QPushButton(Dialog)
        self.btn_chouse_dir.setMinimumSize(QtCore.QSize(70, 0))
        self.btn_chouse_dir.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_chouse_dir.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_chouse_dir.setObjectName("btn_chouse_dir")
        self.Layout_input_path.addWidget(self.btn_chouse_dir)
        self.verticalLayout_2.addLayout(self.Layout_input_path)
        self.lbl_2 = QtWidgets.QLabel(Dialog)
        self.lbl_2.setStyleSheet("border: 1px solid;\n"
"background-color: rgb(211, 215, 207);")
        self.lbl_2.setObjectName("lbl_2")
        self.verticalLayout_2.addWidget(self.lbl_2)
        self.Layout_chouse_format = QtWidgets.QVBoxLayout()
        self.Layout_chouse_format.setObjectName("Layout_chouse_format")
        self.checkBox_word = QtWidgets.QCheckBox(Dialog)
        self.checkBox_word.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border: 1px solid;")
        self.checkBox_word.setObjectName("checkBox_word")
        self.Layout_chouse_format.addWidget(self.checkBox_word)
        self.checkBox_excel = QtWidgets.QCheckBox(Dialog)
        self.checkBox_excel.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border: 1px solid;")
        self.checkBox_excel.setObjectName("checkBox_excel")
        self.Layout_chouse_format.addWidget(self.checkBox_excel)
        self.verticalLayout_2.addLayout(self.Layout_chouse_format)
        self.Layout_dialog = QtWidgets.QHBoxLayout()
        self.Layout_dialog.setObjectName("Layout_dialog")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_dialog.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setMinimumSize(QtCore.QSize(70, 35))
        self.btn_cancel.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.Layout_dialog.addWidget(self.btn_cancel)
        self.btn_report = QtWidgets.QPushButton(Dialog)
        self.btn_report.setMinimumSize(QtCore.QSize(70, 35))
        self.btn_report.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_report.setObjectName("btn_report")
        self.Layout_dialog.addWidget(self.btn_report)
        self.verticalLayout_2.addLayout(self.Layout_dialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Создание отчета"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "B"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "C"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "№\n"
"п/п"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "Наименование показателя"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "Значение показателя"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "1.1"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Dialog", "Общая численность студентов"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Dialog", "1.2"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Dialog", "Удельный вес численности студентов, обучающихся по очной форме обучения в общей численности студентов"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Dialog", "1.3"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Dialog", "Удельный вес численности студентов, обучающихся за счет средств соответствующих бюджетов бюджетной системы РФ в общей численности студентов"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Dialog", "1.4"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Dialog", "Общая численность студентов, обучающихся по профессиям и специальностям, соответствующим  списку 50 наиболее востребованных на рынке труда"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Dialog", "1.4.1"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Dialog", "Удельный вес численности студентов, обучающихся по профессиям и специальностям, соответствующим  списку 50 наиболее востребованных на рынке труда, в общей численности студентов"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Dialog", "1.5"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Dialog", "Средний балл аттестата об основном общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(бюджетники) "))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Dialog", "1.5.1"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Dialog", "Средний балл аттестата об основном общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(платники) "))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Dialog", "1.6"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("Dialog", "Средний балл аттестата об среднем общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(бюджетники) "))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Dialog", "1.6.1"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("Dialog", "Средний балл аттестата об среднем общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(платники) "))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lbl_1.setText(_translate("Dialog", "1. Укажите путь к папке для создания отчета."))
        self.le_folder_path.setPlaceholderText(_translate("Dialog", "Путь к папке"))
        self.btn_chouse_dir.setText(_translate("Dialog", "Выбрать"))
        self.lbl_2.setText(_translate("Dialog", "2. Выберите нужный формат файла для создания отчета."))
        self.checkBox_word.setText(_translate("Dialog", "Word"))
        self.checkBox_excel.setText(_translate("Dialog", "Excel"))
        self.btn_cancel.setText(_translate("Dialog", "Отмена"))
        self.btn_report.setText(_translate("Dialog", "Отчет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
