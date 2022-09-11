#Create an endless iterator using generator method to produce terms of Fibonacci series

def endless_fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

gen_obj=endless_fib()

while True:
    inp=input('Now,Do You Want To Generate Fibonacci Number..?[y/n] : ')
    if inp=='y':
        print(next(gen_obj))
    else:
        break
