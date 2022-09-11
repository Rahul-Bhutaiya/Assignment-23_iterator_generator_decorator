#Create a generator to produce first n even natural numbers

def generator_even(n):
    start=1
    while start<=n:
        yield start*2
        start+=1

for x in generator_even(int(input('Enter N Value : '))):
    print(x,end=' ')