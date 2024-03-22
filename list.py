#Create an empty list called my_list.
my_list=[]
#Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"The list with appended values:\n {my_list}")
#Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print(f"The list with the value 15 inserted at the second position:\n {my_list}")
#Extend my_list with another list: [50, 60, 70].
new_list=[50,60,70]
my_list.extend(new_list)
print(f"The list extended with another list:\n {my_list}")
#Remove the last element from my_list.
my_list.pop(-1)
print(f"The list with the last element removed:\n {my_list}")
#Sort my_list in ascending order.
my_list.sort()
print(f"The list sorted in ascending order:\n {my_list}")
#Find and print the index of the value 30 in my_list.
print("the index of the value 30 in my_list:\n",my_list.index(30))


