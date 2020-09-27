# Reading the inputs
n = int(input())
k = int(input())

# Function
def pattern(n,dif=k,final=n):
    if n<=0:
        print(n,end=", ")
    else:
        print(n,end=", ")
        pattern(n-dif)
        if final==n:
            print(n)
        else:
            print(n,end=", ")
    # Write your recursive function here
pattern(n,k)