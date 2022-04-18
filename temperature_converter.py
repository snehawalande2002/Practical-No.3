class Temperature:

    def fu(self,f):
       celsius =  (f-32)* 0.5556
       return celsius


fu =int(input("enter the value to convert Fahrenheit to celsius"))

obj = Temperature()
celsius = obj.fu(f)

print("The temprature in celsius is :  ",celsius)


