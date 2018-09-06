def average(lst):
    sum = 0
    for num in lst:
        sum += int(num)
    average = sum/len(lst)
    print(average)

mylist = [10,10,2,3,5]

average(mylist)