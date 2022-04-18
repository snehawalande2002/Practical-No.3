
list2 = [20,90,10,5,100]
print(list2)
list2.sort()
print(list2)

print("The second largest number is: ",list2[-2])


print("***************************************************************************")
# Method 2

print("             Method 2              ")
list = [4,5,2,8]
print(list)
list1 = set(list)
list1.remove(max(list1))

print(max(list1))


#Method 3
print("***************************************************************************")

print("             Method 3              ")

list3 = [ ]

number = int(input("Enter the number of element: "))
for i in range(1, number+1):
    elements = int(input("Enter the elements: "))
    list3.append(elements)
list3.sort();
print("The second largest number is:  ",list3[-2])
