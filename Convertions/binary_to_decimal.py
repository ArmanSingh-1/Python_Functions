#Take binary input
n = (input("Enter the Binary Number: \n"))

#Check if input is a number
if (not(n.isdigit())):
    print("Invalid Entry.")
    exit()

#checks if input is in binary form
for i in n:
    if (i not in "01"):
        print("Invalid Number.")
        exit()

#convertion Function    
def binary_to_decimal(n):
    list1 = []                          #empty list
    decimal = 0                         #decimal number init 
    
    #string convert to list
    for i in n:
        list1.append(int(i))

    list1.reverse()                     #reversing list for easy calculation
    
    #Multiplying with 2^n and adding it
    for i in range(len(list1)):        
        decimal = decimal + ((2**(i))*(list1[i]))
    
    return decimal

print(f"The Decimal representation of binary {n} is {binary_to_decimal(n)}.")