from controller import *
import csv
import os

header = ['Operation', 'Equation', 'Result']
with open('History.csv', 'w', newline ='') as csvfile:
    content = csv.writer(csvfile, delimiter = ',')
    content.writerow(header)


def main():
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()
    os.remove('History.csv')

if __name__ == '__main__':
    main()