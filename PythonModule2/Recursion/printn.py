# Read the input
n = int(input())

def print_num(n):
    if n==0:
        print (0)
    else:
        print(-n)
        print_num(n-1)
        print(n)

print_num(n)