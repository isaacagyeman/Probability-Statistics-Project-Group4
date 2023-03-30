import numpy as np

def mean():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    print(np.mean(data))
    input("press any key to exit")

def median():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    print(np.median(data))
    input("press any key to exit")

def variance():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    print(np.var(data))
    input("press any key to exit")

def std():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    print(np.std(data))
    input("press any key to exit")

def range_calc():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    print(max(data)-min(data))
    input("press any key to exit")

def mode():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    print(max(set(data), key = data.count))
    input("press any key to exit")

def quartile_deviation():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    #the first quartile
    firstmid = len(data) / 2
    Q1 = np.median(data[:int(firstmid)])
    #the second quartile
    Q3 = int(np.median(data[int(firstmid) :]))
    IQR = Q3-Q1
    deviation = IQR / 3
    print(deviation)
    input("press any key to exit")
    
def coefficient_of_var():
    data = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    standard_dev = np.std(data)
    mean_ = np.mean(data)
    coefficient_of_var = standard_dev / mean_
    print(coefficient_of_var)
    input("press any key to exit")
    
    
def mean_dev():
    data = []
    elements = int(input("Enter the total number of elements:  "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    print("items:= ",data)
    res = []
    mean_val = np.mean(data)
    for ele in data:
        res.append(abs(ele - mean_val))
    print("subtracting mean from elements = ",res)
    print("mean_deviation = ",  sum(res))
    input("press any key to exit")


def w_mean():
    data = []
    weight = []
    elements = int(input("Enter the total number of elements: "))
    for i in range(0,elements):
        elements = int(input())
        
        data.append(elements)
    witems = int(input("Enter the total number of weights: "))
    for i in range(0, witems):
        witems = int(input())

        weight.append(witems)
    print("items:= ",data)
    print("weight:= ", weight)
    res1 = np.average(data, weights=weight)
    print("weighted mean is ", res1)
    input("press any key to exit")
    


print("Select one of the operations to work on \n1.Mean\n2.Median\n3.Variance\n4.Standard_deviation\n5.Range\n6.Mode\n7.Quartile_deviation\n8.Weighted mean\n9.Coefficient of variance\n10.Mean deviation\n")
try:
    userchoice = int(input())
    if(userchoice == 1):
        print(mean())
    elif(userchoice == 2):
        print(median())
    elif(userchoice == 3):
        print(variance())
    elif(userchoice == 4):
        print(std())
    elif(userchoice == 5):
        print(rangecalc())
    elif(userchoice == 6):
        print(mode())
    elif(userchoice == 7):
        print(quartile_deviation())
    elif(userchoice == 9):
        print(coefficient_of_var())
    elif(userchoice == 10):
        print(mean_dev())
    elif(userchoice == 8):
        print(w_mean())
except(ValueError, TypeError):
    print("Invalid input!!! numbers only")
    input()


