#searching binary search in python
my_list =[1,2,4,5,4]
my_target =4
def myclass(arr,traget):
 start=0
 end=len(arr)-1 
 while (start<=end):
        mid=start+(end-start)//2
        if(traget < arr[mid]):
            end=mid-1 
        
        elif (traget > arr[mid]):
                start=mid+1
        else:
          return mid
        
        return -1 


ans = myclass(my_list,my_target)
print(ans)
