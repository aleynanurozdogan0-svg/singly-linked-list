def create(n):
    lst=[]
    for i in range(n):
        no=int(input("enter the number"))
        lst.append(no)
    return lst

def display(a):
    print("the data in the array are: ")
    print(a)

def access(a,i):
    if 0<=i and i<len(a):
        print("the element at position ",i," is ",a[i])
    else:
        print("the index is more than the size of array")

def insert(a,i,x):
    if i<0:
        print("location is below the range")
        return a
    elif i>len(a):
        print("location is out of the range")
        return a
    else:
        a.insert(i,x)
        return a

def delit(a,i):
    if i<0:
        print("location is below the range")
        return a
    elif i>=len(a):
        print("location is out of the range")
        return a
    else:
        del a[i]
        return a



#main program
n=int(input("enter how many numbers in an array"))
arr=create(n)
display(arr)

print("\n ----data at location----")
i = int(input("element at which position element to get"))
access(arr,i)

print("\n ----insert at a location----")
j=int(input("specify the location to insert"))
y=int(input(" specify the data "))
arr=insert(arr,j,y)
display(arr)

print("\n ----delete at position----")
j=int(input("specify the location to delete"))
arr=delit(arr,j)
display(arr)








    




















