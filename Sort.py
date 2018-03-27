import random
import copy
def getArray (size):
    ans =[]
    for i in range(size):
        ans.append(random.randint(1,101))
    return ans
def bubble(array):
    ans=array
    print(array)
    #create a loop to go trough every pair
    cont = True
    while cont:
        cont=False
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
            #check to see if two items are in order
            #if not swap them
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
                cont=True
        #continue until no changes are made
    print (ans)
    return ans