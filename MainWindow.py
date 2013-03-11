# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QFileDialog,  QMessageBox

from Ui_MainWindow import Ui_MainWindow


import webbrowser

from dedupMacro import run_dedup

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.table_summary.setRowCount(4)
        self.table_summary.setColumnCount(2)
        self.table_summary.horizontalHeader().setVisible(True)
        self.table_summary.horizontalHeader().setVisible(True)
        
        #hide the results widget
        self.results_tab = self.tabWidget.widget(1)
        self.tabWidget.removeTab(1)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        fname = QFileDialog.getOpenFileName(\
            None,
            self.trUtf8("Please select a reference file to deduplicate"),
            self.trUtf8("C:"),
            self.trUtf8("*.txt"),
            None)
            
            
        self.txt_file.setText(fname)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Runs the depulication and displays results
        """
        results = run_dedup(str(self.txt_file.text()))
        self.display_results(results)

    def display_results(self,  results):
        self.show_record_count(results)
        self.show_file_paths(self.txt_file.text())
        
        self.tabWidget.addTab(self.results_tab,  'Results')
        self.tabWidget.setCurrentIndex(1)
        
    def show_record_count(self,  results):
        self.table_summary.item(0, 0).setText(str(results.count_found()))
        self.table_summary.item(1, 0).setText(str(results.count_unique()))
        self.table_summary.item(2, 0).setText(str(results.count_title_duplicates()))
        self.table_summary.item(3, 0).setText(str(results.count_likely_duplicates()))
        
        
    def show_file_paths(self,  fname):
        self.table_summary.item(0, 1).setText(fname)
        self.table_summary.item(1, 1).setText(fname[:-4] + '_edit.txt')
        self.table_summary.item(2, 1).setText(fname[:-4] + '_dups.txt')
        self.table_summary.item(3, 1).setText(fname[:-4] + '_likely_dups.txt')
        self.table_summary.horizontalHeader().setStretchLastSection(True)
    
    @pyqtSignature("int, int")
    def on_table_summary_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        """
        
        # TODO: not implemented yet
        try:
            webbrowser.open(str(self.table_summary.item(row,  1).text()))
        except IOError as e:
            msg = 'File does not exist with specified path and name'
            QMessageBox.warning(self, 'Error', msg, QMessageBox.Close)

   
            
