list=[]
num=int(input('how many numbers:'))
for n in range (num):
    numbers=int(input('enter the number'))
    list.append(numbers)
    print("sum of the numers in list is:",sum(list))
