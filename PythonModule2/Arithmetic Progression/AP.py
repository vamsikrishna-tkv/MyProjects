# take input here
num_list = input()
num = int(input())

num_list = list(map(int, num_list.split(',')))


# print (num_list)
# start writing your code here

def ap(num_list, key):
    dif1 = num_list[1] - num_list[0]
    dif2 = num_list[2] - num_list[1]

    if dif2 == dif1:
        if (key - num_list[0]) % dif1 == 0:
            return True
        else:
            return False
    else:
        return False


print(ap(num_list, num))
