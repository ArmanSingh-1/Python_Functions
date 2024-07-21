#Take the input
n = int(input("Enter the Number: "))

#Check if input is a number
if (not(n.isdigit())):
    print("Invalid Entry.")
    exit()

#Convertion Function
def decimal_to_binary(n):
    #Formulating the binary number
    list1 = []
    while (n >=1):
        i = n % 2
        n = n // 2
        list1.append(i)
    list1.reverse()
    
    #Combining the binary number
    binary = ""
    for i in list1:
        binary += str(i)

    return binary

print(decimal_to_binary(n))