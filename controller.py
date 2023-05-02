from PyQt5.QtWidgets import *
from gui import *
from formulas import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)

        self.add_button.clicked.connect(lambda: self.add_submit())
        self.sub_button.clicked.connect(lambda: self.sub_submit())
        self.mult_button.clicked.connect(lambda: self.mult_submit())
        self.div_button.clicked.connect(lambda: self.div_submit())
        self.perc_button.clicked.connect(lambda: self.perc_submit())


    def add_submit(self):
        values = self.add_input.text()
        self.add_output_label.setText(f'Sum of ({values}) = {add(values):.2f}')

    def sub_submit(self):
        num1 = self.sub_input1.text()
        num2 = self.sub_input2.text()
        self.sub_output_label.setText(f'{num1} - {num2} = {subtract(num1,num2):.2f}')

    def mult_submit(self):
        values = self.mult_input.text()
        self.mult_output_label.setText(f'Product of ({values}) = {multiply(values):.2f}')

    def div_submit(self):
        num1 = self.div_input1.text()
        num2 = self.div_input2.text()
        self.div_output_label.setText(f'{num1} / {num2} = {divide(num1,num2):.2f}')

    
    def perc_submit(self):
        num1 = self.perc_input1.text()
        num2 = self.perc_input2.text()
        self.perc_output_label.setText(f'{num2}% of {num1}: {percentage(num1,num2):.2f}')

    
        