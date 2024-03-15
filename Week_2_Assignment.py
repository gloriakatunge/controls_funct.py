my_list =[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#print(my_list)
#Output = [10, 20, 30, 40]

my_list.insert(1,15)
#print(my_list)
 #Output=[10, 15, 20, 30, 40]
my_list.extend([50,60,70])
#print(my_list)
#output =[10, 15, 20, 30, 40, 50, 60, 70]

my_list.pop(-1)
#print(my_list)
#output = [10, 15, 20, 30, 40, 50, 60]

my_list.sort()
#The list is already sorted in ascending order

#finding the index of item 30 in my_list
index_of_30 =my_list.index(30)
print(index_of_30)
#output = 3


