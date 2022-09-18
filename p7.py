list=[]
numbers = int (input('Enter number of element : '))
for i in range(1,numbers + 1):
    x=int (input('enter number : '))
    list.append(x)
print(list)
max = list[0]
for i in list:
    if i>max:
        max =i
print('the maximum number is : ',max)