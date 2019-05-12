


#This the code for solving a linear equation.
'''
give the coefficient of x which is a and the constant b
from the equation ax+b=0
'''
def linear ():
    a=eval(input('Enter the coefficient of x:  '))
    b=eval(input('Enter the value of the constant:  '))
    
    if a == 0:
        if b !=0:
            return 'Undefined, no solution'
        
        else:
            return 'All real numbers,infinitely many solutions'
        
    elif a > 0 or a < 0:
        x=-b/a
        
        f= open("linear.txt","a+")
        f.write("The solution for "+ str(a)+ "x"+ "+"+ str(b)+ "=0, is x= " + str(x) + "\n") 
        f.close()
        return x
    
    else:
        return 'Invalid'
    
    

def linear_history():
    f=open("linear.txt","r")
    hasNext = True
    while (hasNext):
        contents=f.readline()
        print (contents)
        #there is no other line to be read
        if not contents:
            hasNext = False 
        
        
        



#This is the code for solving quadratic equations.
'''
This function solves quadratic equations a*x**2+b*x+c=0
and thus it requires the user to give the coefficient of x**2 which is a
,the coefficient of x which is b and the constant c.
the output expected is x_1 and x_2 if the output exists, or no solution if the output does not exist.
The ouput does not exist when the delta is less than 0.
'''

def quadratic ():
    import math
    v= open("quadratic.txt","a+")
    a=eval(input('Enter the coefficient of x^2:  '))
    b=eval(input('Enter the coefficient of x:  '))
    c=eval(input('Enter the value of the constant:  '))

    if a == 0:
        if b == 0:
            if c == 0:
                return 'Undetermined, the solution is all real numbers'
            elif c != 0:
                return 'No solution'
        elif b != 0:
            x= -c/b
            v.write("The solution for "+ str(a)+ "x^2"+ "+"+ str(b)+ "x +"+str(c)+ "=0, x= " + str(x) + "\n")
            return x
    else:
        delta = b**2 - 4*a*c

        # check if the     
        if delta >= 0:
            x_1=(-b + math.sqrt(delta)) / 2*a
            x_2=(-b - math.sqrt(delta)) / 2*a
            x_values=[x_1 , x_2]

            
            
            v.write("The solution for "+ str(a)+ "x^2"+ "+"+ str(b)+ "x +"+str(c)+ "=0, x_1= " + str(x_1) + "x_2= " +str(x_2) + "\n")
            v.close()

            #Storing the values of x in a list
            return x_values[0], x_values[1]

        else:
           return ('No solution')

def quadratic_history():
    v=open("quadratic.txt","r")
    hasNext = True
    while (hasNext):
        contents=v.readline()
        print (contents)
        #there is no other line to be read
        if not contents:
            hasNext = False 
        
    
    
        
    
#This is the code to graphically represent the 2D equations.
'''
This function graphs the equation of the form a*x+b*y+c=0,
it requires the user to give a,b and the constant c.
I'm using randomization to get a value of x which will help me
to solve and get the value of y, and thus get a point.
using two points I can draw the line.
However, randomization of x has a certain range to prevent the line being tiny.
'''

def graph(a,b,c):
    import turtle
    import random
    x_1=random.randint(100,201)
    y_1=(-c-x_1*b)/a
    x_2=random.randint(-201,-100)
    y_2=(-c-x_2*b)/a
    p = turtle.Turtle()
    for i in range(4):
        p.forward(500)
        p.up()
        p.backward(500)
        p.left(90)
        p.down()
    for i in range (3):
        p.backward(500)
        p.down()
        p.right(180)
        p.forward(500)
        p.up()
    
    p.up()
    point_1={"x":x_1, "y": y_1}
    point_2={"x":x_2, "y": y_2}
    p.goto(x_1,y_1)
    p.down()
    p.goto(x_2,y_2)
    p.hideturtle()


