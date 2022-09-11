#Create a generator to produce first n odd natural numbers

def generator_odd(n):
    start=1
    while start<=n:
        yield start*2-1
        start+=1

n_val=int(input('Enter N Value : '))
gen_fun=generator_odd(n_val)#here generator object will be returned by the generator_odd function and stored in gen_fun

#method 1 to access values from generator object...
"""
while n_val:
    print(next(gen_fun),end=' ')
    n_val-=1
"""

#method 2 to access values from generator object...
"""
for x in generator_odd(int(input('Enter N Value : '))):
    print(x,end=' ')
"""

#method 3 to access values from generator object...
for x in gen_fun:
    print(x,end=' ')