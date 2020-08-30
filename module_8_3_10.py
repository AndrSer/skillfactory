list = [19,2,31,35,30,11,121,27]

for i in range(1, len(list)):
    b = list[i]
    j = i-1
    while (j >= 0) and (b < list[j]):
        list[j+1] = list[j]
        j-=1
    list[j+1] = b
print(list)

i=1
while i <= len(list)-1:
    b = list[i]
    j = i - 1
    while (j >= 0) and (b < list[j]):
        list[j + 1] = list[j]
        j -= 1
    list[j + 1] = b
    i=i+1
print(list)



