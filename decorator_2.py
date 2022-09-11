"""
Define a function which calculates HCF of two numbers. 
Define and apply a decorator to check whether two given numbers are co-prime or not.
"""

#METHOD : 1
def deco_fun(fun):
    def prime_hcf(first,second):
        hcf=fun(first,second)
        print('HCF of {} and {} is {}.'.format(first,second,hcf))
        if hcf ==1:
            print('These Are co-prime Numbers Also')
        else:
            print('These Are Not co-prime Numbers')
    return prime_hcf

@deco_fun
def hcf_fun(first,second):
    small=second if first>second else first

    while small>0:
        if first%small==0 and second%small==0:
            return small
        small-=1

hcf_fun(int(input('Enter First Number : ')),int(input('Enter Second Number : ')))

"""
#METHOD : 2

def decor_fun(fun):
    def hcf_coprime(var1,var2):
        hcf_value=fun(var1,var2)
        print('HCF of %d and %d is %d.'%(var1,var2,hcf_value))
        if hcf_value==1:
            print('co-prime')
        else:
            print('not co-prime')
    return hcf_coprime


def hcf(var1,var2):
    small=var2 if var1>var2 else var1

    while small>0:
        if var1%small==0 and var2%small==0:
            return small
        small-=1

hcf=decor_fun(hcf)
hcf(10,5)
"""