n = (input("Enter the Binary Number: "))

def binary_to_decimal(n):
    list1 = []
    decimal = 0
    for i in n:
        list1.append(int(i))
    list1.reverse()
    for i in range(len(list1)):        
        decimal = decimal + ((2**(i))*(list1[i]))
    return decimal

print(binary_to_decimal(n))