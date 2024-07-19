from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget,\
QTableWidgetItem, QFileDialog ,QMessageBox
from PyQt5.QtCore import Qt
from checker import check_duplication,show_checker_window
from database import sys_show_history
from file import sys_import_files
from export_section import export_code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        widget1 = QWidget()
        widget2 = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.import_button = QPushButton('文件导入')
        self.import_button.clicked.connect(self.import_files)
        
        self.history_button = QPushButton('历史记录')
        self.history_button.clicked.connect(self.show_history)
        
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(['主文件', '核查文件', '相似度'])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        self.mannual_check_button = QPushButton('人工查重')
        self.mannual_check_button.clicked.connect(self.mannual_check)
        
        self.export_button = QPushButton('代码导出')
        self.export_button.clicked.connect(self.export_codes)
        
        layout.addWidget(self.results_table)
        layout.addWidget(self.import_button)
        layout.addWidget(self.mannual_check_button)
        
        self.setWindowTitle('Code Duplication Checker')
        self.setGeometry(100, 100, 800, 600)

    def import_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Python Files", "", "Python Files (*.py);;All Files (*)")
        if files:
            results = check_duplication(files)
            self.display_results(results)
            QMessageBox.information(self, 'Import Success', f'Successfully imported {len(files)} files.')


    def display_results(self, results):
        self.results_table.setRowCount(len(results))
        for row, result in enumerate(results):
            self.results_table.setItem(row, 0, QTableWidgetItem(result['file1']))
            self.results_table.setItem(row, 1, QTableWidgetItem(result['file2']))
            self.results_table.setItem(row, 2, QTableWidgetItem(f"{result['similarity']:.2%}"))
        self.results_table.resizeColumnsToContents()
        
    def show_history(self):
        results = sys_show_history()
        self.display_results(results)
        
    def mannual_check(self):
        show_checker_window()
    def export_codes(self):
        export_directory = QFileDialog.getExistingDirectory(self, "Select Export Directory")
        if export_directory:
            try:
                result_dir = export_code(export_directory)
                QMessageBox.information(self, "Export Successful", f"Files and code exported to:\n{result_dir}")
            except Exception as e:
                QMessageBox.warning(self, "Export Failed", f"An error occurred during export:\n{str(e)}")