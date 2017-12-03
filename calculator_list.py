# Created on Sun Dec 03
# Author: 10358601 Izabela Tyrna

#This program is a calculator that handels lists. 
#For functions that take 2 lists as arugments the list needs to be the same length.

import math

a = [1,2,3,4]
b = [1,2,3,5]
c = [1,2,0,-5]
d = [1,2,3,5,6]

class Calculator(object):

    def add(self, x, y): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)] or [i for i in y if not isinstance(i, number_types)] or (len(x) != len(y)):
            print 'The list element is not int, long, float, complex type or lists do not have the same length'
        else:
            return map(lambda x,y:x+y, x,y)
            
    def subtract(self, x, y): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)] or [i for i in y if not isinstance(i, number_types)] or (len(x) != len(y)):
            print 'The list element is not int, long, float, complex type or lists do not have the same length'
        else:
            return map(lambda x,y:x-y, x,y)
            
    def multiply(self, x, y): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)] or [i for i in y if not isinstance(i, number_types)] or (len(x) != len(y)):
            print 'The list element is not int, long, float, complex type or lists do not have the same length'
        else:
            return map(lambda x,y:x*y, x,y)
            
    def divide(self, x, y): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)] or [i for i in y if not isinstance(i, number_types)] or [i for i in x if i == 0] or [i for i in y if i == 0] or (len(x) != len(y)):
            print 'The list element is not int, long, float, complex type or trying divide by zero or lists do not have the same length'
        else:
            return map(lambda x,y:x/float(y), x,y)
            
    def square(self, x): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)]:
            print 'The list element is not int, long, float, complex type'
        else:
            return map(lambda x:x*x, x)
            
    def cube(self, x): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)]:
            print 'The list element is not int, long, float, complex type'
        else:
            return map(lambda x:x*x*x, x)
            
    def squareroot(self, x): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)] or [i for i in x if i < 0]:
            print 'The list element is not int, long, float, complex type or trying to call fucntion for a negative number'
        else:
            return map(lambda x:math.sqrt(x), x)
            
    def power(self, x,y): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)] or [i for i in y if not isinstance(i, number_types)] or (len(x) != len(y)):
            print 'The list element is not int, long, float, complex type or lists do not have the same length'
        else:
            return map(lambda x,y:math.pow(x,y), x,y)
            
    def factorial(self, x): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)]:
            print 'The list element is not int, long, float, complex type'
        else:
            return map(lambda x:math.factorial(x), x)
            
    def sin(self, x): 
        number_types = (int, long, float, complex)
        if [i for i in x if not isinstance(i, number_types)]:
            print 'The list element is not int, long, float, complex type'
        else:
            return map(lambda x:math.sin(x), x)
        
if __name__ == '__main__':    
    
    call_object  = Calculator()
    v1 = call_object .add(a,b)
    print v1
    v2 = call_object .add(a,d)
    v3 = call_object .subtract(a,b)
    print v3
    v4 = call_object .multiply(a,b)
    print v4
    v5 = call_object .divide(a,b)
    print v5
    v6 = call_object .divide(a,c)
    v7 = call_object .square(b)
    print v7
    v8 = call_object .cube(b)
    print v8
    v9 = call_object .squareroot(b)
    print v9
    v10 = call_object .squareroot(c)
    v11 = call_object .power(a,b)
    print v11
    v12 = call_object .factorial(a)
    print v12
    v13 = call_object .sin(a)
    print v13

    
    


