before_19 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen',
             'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']

for_tens =['','','Twenty','Thirty','Fourty','Fifty','Sixty','seventy','Eighty','Ninety']

n =int(input(" the digit between 0 to 99:  "))
Output=''
if n==0:
    output='Zero'
elif n<=19:
    output=before_19[n]
elif n<=99:
    output =for_tens[n//10]+" "+before_19[n%10]                 # [n//10] -->  To know how many tens are there in entered number
else:                                                           # before_19[n%10]   --> to get the value of unit place
    output ="Please enter valid number"
print(output)



