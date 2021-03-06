# take input here
import ast

valley_list = ast.literal_eval(input())
key = int(input())
'''
#we will use a similar approach as used in rotated list question
# we notice, if we divide the list at middle, one half is in descending order,
#we can use same approach as binary search there
#other half will have same trend as original valley list
#hence we can loop until there is just one element left

#start writing your code here
def valleysearch(valley_list, key):
    l=0
    r=len(valley_list)-1
    while(l<=r):

        mid=(r+l)//2

        if valley_list[mid]==key:
            return mid

        elif valley_list[mid]<=valley_list[l]:
            #left half is sorted in descending order
            if key<=valley_list[l] and key>valley_list[mid]: #key is in left half
                r=mid-1
            else:
                l=mid+1

        else:
            #this means right half is sorted in ascending order
            if key<valley_list[mid]:
                r=mid-1
            else:
                l=mid+1
    return -1
print(valleysearch(valley_list, key))
'''


def valleysearch(valley_list, key):
    for i in range(len(valley_list)):
        if (valley_list[i] == key):
            return i
    return -1


print(valleysearch(valley_list, key))