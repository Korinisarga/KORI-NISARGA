"""" search in the array return the index if item found otherwise if the item not found return -1 """
def linear1(num,target):
      

        if len(num)==0:
            return-1
        #run for loop
        i=0
        while i<len(num):
            i+i
        #check for the element at every index if it is = target
        element=num[i]
        if element==target:
         return i
number={14,6,2,3}
target_=2
print(linear1(number,target_))     
