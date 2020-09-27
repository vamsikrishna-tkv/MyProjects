input_str = input()
input_list = input_str.split(',')

a = int(input_list[0])
b = int(input_list[1])
c = int(input_list[2])


# write code here

def F(n, x=a, y=b, z=c):
    if n > y:
        return n - z
    else:
        return F(x + F(x + F(x + F(x + n))))


def large_sum(a, b, c):
    total = 0
    for i in range(b + 1):
        total += F(i)
    return total


# store the result in the following variable
result = large_sum(a, b, c)

# print result -- do not change the following code
print(result)