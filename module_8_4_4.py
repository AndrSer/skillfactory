list = [1,19,2,3,4,5]
K = 3
mid = len(list)//2
low = 0
high = len(list)-1
position = 0
print(list)

while low <= high:
   if K < list[0]:
       print("\nНет возможности найти позицию элемента")
       position=0
       break
   if K>list[len(list)-1]:
       position = len(list)
       break
   if list[mid] < K < list[mid + 1]:
       position = mid+1
       break
   if list[mid] == K:
       if mid != len(list) - 1:
           i = mid+1
           while list[i] == K:
               i+=1
           position = i
           break
       else:
           position = len(list)
           break
   if K > position[mid]:
       low = mid + 1
   else:
       high = mid - 1
   mid = (low +


          high) // 2
print(position)



