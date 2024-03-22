
#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list
myList=[]
x=int(input("Enter x:\n"))
y=int(input("Enter y:\n"))
z=int(input("Enter z:\n"))

print(myList)
sum=x+y+z
print(f"The sum of the list elements is: {sum}")


#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
myTupleBooks=("Everything,Everything", "Rich Dad,Poor Dad", "Secret Sevens","The faults in the stars", "S Notes")

for i in myTupleBooks:
    print(f"{i} \n")



#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console

person_info={}

person_info['name']=input("Enter your name:\n")
person_info['age']=int(input("Enter your age:\n"))
person_info['favourite_color']=input("Enter your favourite color:\n")

print(person_info)

#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

x=int(input("Enter x:\n"))
y=int(input("Enter y:\n"))
z=int(input("Enter z:\n"))
set1={x,y,z}

a=int(input("Enter a:\n"))
b=int(input("Enter b:\n"))
c=int(input("Enter c:\n"))
set2={a,b,c}

common_set=set1.intersection(set2)

print("Set1: ",set1)
print("Set2: ",set2)
print("Common elements: ",common_set)

#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
wordList=["Appa","Momo", "Aang","Kora", "Katara", "Sukko", "Zukoh", "Uncle Iroh", "Cabbage"]

comprehension_list= [x for x in wordList if len(x)%2==1]
print(f"A list of words that have an odd number of characters: {comprehension_list}")