# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python Projects\DedupInterface\MainWindow.ui'
#
# Created: Thu Nov 14 18:36:36 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(764, 392)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 761, 371))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(670, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lbl_file = QtGui.QLabel(self.tab)
        self.lbl_file.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.lbl_file.setObjectName(_fromUtf8("lbl_file"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.txt_file = QtGui.QLineEdit(self.tab)
        self.txt_file.setGeometry(QtCore.QRect(90, 10, 571, 20))
        self.txt_file.setObjectName(_fromUtf8("txt_file"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 40, 241, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.rb_method_iteration = QtGui.QRadioButton(self.groupBox_2)
        self.rb_method_iteration.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.rb_method_iteration.setChecked(True)
        self.rb_method_iteration.setObjectName(_fromUtf8("rb_method_iteration"))
        self.rb_method_title = QtGui.QRadioButton(self.groupBox_2)
        self.rb_method_title.setGeometry(QtCore.QRect(10, 40, 161, 17))
        self.rb_method_title.setObjectName(_fromUtf8("rb_method_title"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(260, 40, 221, 101))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.rb_author_surname = QtGui.QRadioButton(self.groupBox_3)
        self.rb_author_surname.setGeometry(QtCore.QRect(10, 20, 161, 17))
        self.rb_author_surname.setChecked(True)
        self.rb_author_surname.setObjectName(_fromUtf8("rb_author_surname"))
        self.rb_author_initial = QtGui.QRadioButton(self.groupBox_3)
        self.rb_author_initial.setGeometry(QtCore.QRect(10, 40, 201, 17))
        self.rb_author_initial.setObjectName(_fromUtf8("rb_author_initial"))
        self.rb_author_full = QtGui.QRadioButton(self.groupBox_3)
        self.rb_author_full.setGeometry(QtCore.QRect(10, 60, 191, 17))
        self.rb_author_full.setObjectName(_fromUtf8("rb_author_full"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 681, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.table_summary = QtGui.QTableWidget(self.groupBox)
        self.table_summary.setGeometry(QtCore.QRect(10, 20, 611, 141))
        self.table_summary.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.table_summary.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_summary.setAlternatingRowColors(True)
        self.table_summary.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.table_summary.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_summary.setShowGrid(True)
        self.table_summary.setColumnCount(2)
        self.table_summary.setObjectName(_fromUtf8("table_summary"))
        self.table_summary.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary.setItem(2, 1, item)
        self.table_summary.verticalHeader().setDefaultSectionSize(28)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 691, 231))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.table_summary_2 = QtGui.QTableWidget(self.groupBox_4)
        self.table_summary_2.setGeometry(QtCore.QRect(10, 20, 611, 201))
        self.table_summary_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.table_summary_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_summary_2.setAlternatingRowColors(True)
        self.table_summary_2.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.table_summary_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_summary_2.setShowGrid(True)
        self.table_summary_2.setColumnCount(4)
        self.table_summary_2.setObjectName(_fromUtf8("table_summary_2"))
        self.table_summary_2.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(3, 3, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(4, 3, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(5, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_summary_2.setItem(5, 3, item)
        self.table_summary_2.verticalHeader().setDefaultSectionSize(28)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Uniquify - Reference Deduplicator", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_file.setText(QtGui.QApplication.translate("MainWindow", "Reference file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Uniquify Method", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_method_iteration.setText(QtGui.QApplication.translate("MainWindow", "Iteration", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_method_title.setText(QtGui.QApplication.translate("MainWindow", "Titles only (no punctuation)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Author Name Options", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_author_surname.setText(QtGui.QApplication.translate("MainWindow", "Truncate to surname", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_author_initial.setText(QtGui.QApplication.translate("MainWindow", "Truncate to surname and first initial", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_author_full.setText(QtGui.QApplication.translate("MainWindow", "Full name without punctuation", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Deduplication Summary", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Original Records", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.verticalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Unique Titles", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.verticalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Duplicate Titles", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Total", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.table_summary.isSortingEnabled()
        self.table_summary.setSortingEnabled(False)
        item = self.table_summary.item(0, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.item(0, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.item(1, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.item(1, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.item(2, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary.item(2, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        self.table_summary.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Results - Title Dedup", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Deduplication Summary", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Original", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.verticalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Iteration 1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.verticalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Iteration 2", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.verticalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Iteration 3", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.verticalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Iteration 4", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.verticalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Iteration 5", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Removed", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Remaining", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Edited file", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Duplicates file", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.table_summary_2.isSortingEnabled()
        self.table_summary_2.setSortingEnabled(False)
        item = self.table_summary_2.item(0, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(0, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(0, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(0, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(1, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(1, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(1, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(1, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(2, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(2, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(2, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(2, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(3, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(3, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(3, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(3, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(4, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(4, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(4, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(4, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(5, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(5, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(5, 2)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_summary_2.item(5, 3)
        item.setText(QtGui.QApplication.translate("MainWindow", "\"\"", None, QtGui.QApplication.UnicodeUTF8))
        self.table_summary_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Results Iterative Dedup", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

