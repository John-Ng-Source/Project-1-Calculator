from gui import *
import numpy


def add(values):
    number_list = values.strip().split(',')
    new_list = [float(x) for x in number_list]
    return sum(new_list)

def subtract(num1, num2):
    answer = float(num1) - float(num2)
    return answer

def multiply(values):
    numbers_list = values.strip().split(',')
    new_list = [float(x) for x in numbers_list]
    return numpy.prod(new_list)

def divide(num1, num2):
    return float(num1) / float(num2)

def percentage(num1, num2):
    percent = float(num2) / 100.00
    return float(num1) * percent 


    


    
    