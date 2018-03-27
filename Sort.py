import random
def getArray (size):
    ans =[]
    for i in range(size):
        ans.append(random.randint(1,101))
    return ans