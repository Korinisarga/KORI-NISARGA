#removing the duplicate and adding to the new list
def remove(duplicate):
 new_list=[]
 for num  in duplicate:
   if num not in new_list:
     new_list.append(num)
 return new_list

duplicate=[]
duplicate=input("enter the number :")  
print(remove(duplicate))"""
"""for i in range(1,20):
    i=i*i
    print(i)
