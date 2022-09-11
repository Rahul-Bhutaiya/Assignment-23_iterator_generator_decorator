"""
Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter of triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides.
"""

def decor_fun(fun):
    def validity_perimeter(val1,val2,val3):
        if (val1+val2>val3) and (val1+val3>val2) and (val2+val3>val1):
            print('It\'s Valid Triangle')
            print('Perimeter of Triangle :',fun(val1,val2,val3))
        else:
            print('It\'s Not Valid Triangle')
    return validity_perimeter

@decor_fun
def perimeter(val1,val2,val3):
    return val1+val2+val3

perimeter(int(input('Enter First Length : ')),int(input('Enter Second Length : ')),int(input('Enter Third Length : ')))