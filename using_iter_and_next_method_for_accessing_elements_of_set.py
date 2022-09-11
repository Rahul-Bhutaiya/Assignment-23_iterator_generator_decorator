#Use iter and next method to access all the elements of a given set using while loop

set_var=set([eval(x) for x in input('Enter Set Elements Separated By Comma : ').split(',')])

it_obj=iter(set_var)#iterator object

length_of_set=len(set_var)
while length_of_set:
    print(next(it_obj))
    length_of_set-=1