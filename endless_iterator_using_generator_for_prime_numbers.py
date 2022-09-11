#Create an endless iterator using generator method to produce Prime numbers

def endless_prime():
    a=2
    while True:
        for x in range(2,a):
            if a%x==0:
                a+=1
                break
        else:
            yield a
            a+=1

gen_obj=endless_prime()

while True:
    inp=input('Now, Do You Want To Get Prime Number..?[y/n] : ')
    if inp=='y':
        print(next(gen_obj))
    else:
        break