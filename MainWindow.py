# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QFileDialog,  QMessageBox

from Ui_MainWindow import Ui_MainWindow


import webbrowser, os

from dedupMacro import *

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
        self.table_summary.setRowCount(3)
        self.table_summary.setColumnCount(2)
        self.table_summary.horizontalHeader().setVisible(True)
        self.table_summary.horizontalHeader().setVisible(True)
        
        
        self.table_summary_2.setRowCount(5)
        self.table_summary_2.setColumnCount(4)
        self.table_summary_2.horizontalHeader().setVisible(True)
        self.table_summary_2.horizontalHeader().setVisible(True)
        
        #hide the results widget
        self.results_tab = self.tabWidget.widget(1)
        self.results_iterate_tab = self.tabWidget.widget(2)
        
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(1)
    
    
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Runs the depulication and displays results
        """
        self.run_uniquify()
            
    
    def run_uniquify(self):
        if(self.listWidget.count() == 0):
            msg = QMessageBox()
            msg.setText('No file has been selected for dedup')
            msg.setInformativeText('Use the browse button to browse for the correct reference file')
            msg.setWindowTitle('Setup issue')
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            return
        
        fileList = self.get_file_list()
                
        if(self.rb_method_iteration.isChecked()):
            #TO DO: Implement multiple file capability for the iteration (iteration needs fixing first!)
            results = iterate_dedup(str(fileList[0]), self.user_preferences())
            self.display_iterate_results(results,  self.listWidget.item(0).text())
        else:
            results = run_dedup(fileList)
            self.display_title_results(results)
    
    def get_file_list(self):
        fileList = []
        for i in range(self.listWidget.count()):
            fileList.append(str(self.listWidget.item(i).text()))
        return fileList
        
    
    def user_preferences(self):
        """Creates a function container dependent on user preferences returns a DedupFuncContainer"""
        fc = DedupFuncContainer()
        
        if(self.rb_author_surname.isChecked()):
            fc.authorFunc = truncate_surname
        elif(self.rb_author_initial.isChecked()):
            fc.authorFunc = truncate_first_initial
        else:
            fc.authorFunc = None
            
        return fc
    
    def display_title_results(self,  results):
        self.show_record_count(results)
        self.show_file_paths(self.listWidget.item(0).text())
        
        self.tabWidget.addTab(self.results_tab,  'Results - title dedup')
        self.tabWidget.setCurrentWidget(self.results_tab)
        
    def show_record_count(self,  results):
        self.table_summary.item(0, 0).setText(str(results.count_found()))
        self.table_summary.item(1, 0).setText(str(results.count_unique()))
        self.table_summary.item(2, 0).setText(str(results.count_title_duplicates()))
        
        
    def show_file_paths(self,  fname):
        self.table_summary.item(0, 1).setText(fname)
        self.table_summary.item(1, 1).setText(fname[:-4] + '_edit.txt')
        self.table_summary.item(2, 1).setText(fname[:-4] + '_dups.txt')
        self.table_summary.horizontalHeader().setStretchLastSection(True)
        
    def display_iterate_results(self,  results,  fname):
        for iteration in range(0, len(results)-1):
            self.table_summary_2.item(iteration,  0).setText(str(len(results[iteration].duplicates)))
            self.table_summary_2.item(iteration,  1).setText(str(len(results[iteration].edit)))
            self.table_summary_2.item(iteration,  2).setText(fname[:-4] + '_Iteration' + str(iteration) + '.txt')
            self.table_summary_2.item(iteration,  3).setText(fname[:-4] + '_Duplicates' + str(iteration) + '.txt')
            
        self.table_summary_2.horizontalHeader().setStretchLastSection(True)
        self.table_summary_2.item(0,  2).setText(fname)
        self.table_summary_2.item(0,  3).setText('')
        
        self.tabWidget.addTab(self.results_iterate_tab,  'Results - iterative dedup')
        self.tabWidget.setCurrentWidget(self.results_iterate_tab)
    
    def on_table_summary_2_cellDoubleClicked(self, row, column):
        if(column > 1):
            try:            
                os.system("start " + str(self.table_summary_2.item(row,  column).text()))
                #webbrowser.open(str(self.table_summary.item(row,  1).text()))
            except IOError as e:
                msg = 'File does not exist with specified path and name'
                QMessageBox.warning(self, 'Error', msg, QMessageBox.Close)
        
    
    @pyqtSignature("int, int")
    def on_table_summary_cellDoubleClicked(self, row, column):
        """
        Open reference file via double click
        """
        
        try:            
            os.system("start " + str(self.table_summary.item(row,  1).text()))
            #webbrowser.open(str(self.table_summary.item(row,  1).text()))
        except IOError as e:
            msg = 'File does not exist with specified path and name'
            QMessageBox.warning(self, 'Error', msg, QMessageBox.Close)
    
    @pyqtSignature("")
    def on_add_file_button_clicked(self):
        """
        Opens file brower and adds tselected file o QListWidget
        """
        fname = QFileDialog.getOpenFileName(\
            None,
            self.trUtf8("Please select a reference file to deduplicate"),
            self.trUtf8("C:"),
            self.trUtf8("*.txt"),
            None)
        
        if(fname != ''):
            self.listWidget.addItem(fname)
    
      
        
    
    @pyqtSignature("")
    def on_actionExit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
    
    @pyqtSignature("")
    def on_actionRun_Uniquify_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.run_uniquify()
