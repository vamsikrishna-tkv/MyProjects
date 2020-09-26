#take input here
import ast
inp_list=ast.literal_eval(input())
key=int(input())

#start writing your code from here
def search(data,key):
    l=0
    r=len(data)-1
    while(l<=r):
        mid1=l + (r-l)//3
        mid2=r - (r-l)//3
        if(data[mid1]==key):
            return mid1
        elif data[mid2]==key:
            return mid2
        elif key>data[l] and key<data[mid1]:
            r=mid1-1
        elif key>data[mid2] and key<data[r]:
            l=mid2+1
        else:
            l=mid1+1
            r=mid2-1
    return -1
print(search(inp_list,key))
