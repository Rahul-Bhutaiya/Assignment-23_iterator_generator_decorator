#Create a generator to produce first n terms of Fibonacci series

def gen_fib(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

for x in gen_fib(int(input('Enter N Value : '))):
    print(x,end=' ')