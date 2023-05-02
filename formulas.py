from gui import *
import numpy
import csv

def add(values):
    number_list = values.strip().split(',')
    new_list = [float(x) for x in number_list]

    with open('History.csv', 'a', newline ='') as csvfile:
        equation = '+'.join(number_list)
        entry = ['Addition', f'{equation}', f'{sum(new_list)}']
        content = csv.writer(csvfile, delimiter = ',')
        content.writerow(entry)
    
    return sum(new_list)

def subtract(num1, num2):
    answer = float(num1) - float(num2)
    with open('History.csv', 'a', newline ='') as csvfile:
        entry = ['Subtraction', num1 + ' - ' + num2, f'{answer}']
        content = csv.writer(csvfile, delimiter = ',')
        content.writerow(entry)
    return answer

def multiply(values):
    number_list = values.strip().split(',')
    new_list = [float(x) for x in number_list]
    with open('History.csv', 'a', newline ='') as csvfile:
        equation = '*'.join(number_list)
        entry = ['Multiplication', f'{equation}', f'{numpy.prod(new_list)}']
        content = csv.writer(csvfile, delimiter = ',')
        content.writerow(entry)


    return numpy.prod(new_list)

def divide(num1, num2):
    answer = float(num1) / float(num2)
    with open('History.csv', 'a', newline ='') as csvfile:
        entry = ['Division', num1 + '/' + num2, f'{answer}']
        content = csv.writer(csvfile, delimiter = ',')
        content.writerow(entry)
    return answer

def percentage(num1, num2):
    percent = float(num2) / 100.00
    with open('History.csv', 'a', newline ='') as csvfile:
        entry = ['Percentage', num2 + '%' +' of ' + num1, f'{percent}%']
        content = csv.writer(csvfile, delimiter = ',')
        content.writerow(entry)

    return float(num1) * percent 


    


    
    