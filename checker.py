import difflib
from file import read_file_content
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget\
, QTableWidgetItem, QFileDialog ,QMessageBox, QApplication
import sys

class checkerWindow(QWidget):
    def __init__(self):
        super().__init__()
        
    
    
def calculate_similarity(code1, code2):
    diff = difflib.SequenceMatcher(None, code1, code2)
    return diff.ratio()

def check_duplication(files):
    results = []
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            code1 = read_file_content(files[i])
            code2 = read_file_content(files[j])
            similarity = calculate_similarity(code1, code2)
            results.append({
                'file1': files[i],
                'file2': files[j],
                'similarity': similarity
            })
    return sorted(results, key=lambda x: x['similarity'], reverse=True)

def mannual_check(file1, file2):
    code1 = read_file_content(file1)
    code2 = read_file_content(file2)
    similarity = calculate_similarity(code1, code2)
    return similarity


def show_checker_window():
    app = QApplication(sys.argv)
    ex = checkerWindow()
    sys.exit(app.exec_())

