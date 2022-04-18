hours = input("Enter the hours: ")
rate = input("Enter the rate:  ")

h = float(hours)
r = float(rate)

if h <= 40:
    print(h*r)
else:
    print(40*r+(h-40)*1.5*r)