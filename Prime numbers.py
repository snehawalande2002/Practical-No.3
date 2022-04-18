
# Print prime numbers up to n

n = int(input("Enter the number:  "))
print("The prime numbers are: ")
for i in range(2,n+1):
    j=2
    for j in range(2,i):
        if(i%j==0):
            j=i
            break

    if(j!= i):
        print(i,end=" ")

