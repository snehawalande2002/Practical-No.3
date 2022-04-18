
# Pattern 1

i = 1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1


# Pattern 2
print()
i = 3
row =0
while row< i:
    space = i-row-1
    while space>0:
        print(end=" ")
        space =space-1
    star = row+1
    while star>0:
        print("* ",end=" ")
        star =star-1
    row=row+1
    print()


# pattern 3

n =3
for i in range(n):
    print(' '*(n-i+1)+(str(i+1)+' ')*(i+1))         #  {' '*(n-i+1)} -->  How many times space do you want
                                                    #   {(str(i+1)+' '}  --> Follwed by which symbol
                                                    #    {(i+1)}      --> How many times i want















