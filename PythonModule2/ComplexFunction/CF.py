# input has been taken for you
n = int(input())


# start writing your code from here
# we define function f(n, x)
# this will take in n and x and find n^x+x
def f(n, x):
    a = n ** x
    b = a + x
    return b


# initial search space is from -n to n
l = -n
r = n
# depending on value of f(n,x) we will change our search space
mid = (l + r) / 2

while (abs(l - r) > 10 ** -8) and (f(n, mid) != 0):
    mid = (l + r) / 2
    if f(n, mid) > 0:  # if f(n,x) > 0 means root lies in the left half
        r = mid
    elif f(n, mid) < 0:  # if f(n,x) < 0 means root lies in the right half
        l = mid

print('%0.6f' % round(mid, 6))