#Create a generator to produce first n prime numbers

def gen_prime(n):
    a=2
    while n:
        for x in range(2,a):
            if a%x==0:
                a+=1
                break
        else:
            yield a
            a+=1
            n-=1

for x in gen_prime(int(input('Enter N Value : '))):
    print(x,end=' ')