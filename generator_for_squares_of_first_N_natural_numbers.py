#Create a generator to produce squares of first N natural numbers

def generator_square(n):
    first=1
    while first<=n:
        yield first**2
        first+=1

n_val=int(input('Enter N Value : '))
gene_obj=generator_square(n_val)

while n_val:
    print(next(gene_obj),end=' ')
    n_val-=1