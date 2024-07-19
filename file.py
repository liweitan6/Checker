import os
from PyQt5.QtWidgets import QFileDialog,QMessageBox

# def sys_import_files(directory):
#     python_files = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.py'):
#                 python_files.append(os.path.join(root, file))
#     return python_files

def sys_import_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Python Files", "", "Python Files (*.py);;All Files (*)")
        # if files:
        if files:
            QMessageBox.information(self, '成功', f'{len(files)} files imported successfully')
            return files
        else:
            QMessageBox.warning(self, '错误', '没有选择文件')
            return None
        #     results = check_duplication(files)
        #     self.display_results(results)

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()