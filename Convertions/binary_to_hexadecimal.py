#Take Binary Input
n = (input("Enter the Binary Number: \n"))

#Check if it is a number
if (not(n.isdigit())):
    print("Invalid Entry.")
    exit()

#checks if it is in binary form
for i in n:
    if (i not in "01"):
        print("Invalid Number.")
        exit()

#Binary to Hexa value of all 16 code
dict1 =  {
    "0000" : "0",
    "0001" : "1",
    "0010" : "2",
    "0011" : "3",
    "0100" : "4",
    "0101" : "5",
    "0110" : "6",
    "0111" : "7",
    "1000" : "8",
    "1001" : "9",
    "1010" : "A",
    "1011" : "B",
    "1100" : "C",
    "1101" : "D",
    "1110" : "E",
    "1111" : "F",
}

def binary_to_hexa(n):
    #String to list convertion
    list1 = []
    for i in n:
        list1.append(i)
    
    #Making sure that the Format of Hexa is in Multiple of 4 
    if (len(list1) % 4) == 0:
        pass
    elif (len(list1) % 4) == 1:
        list1 = ['0','0','0'] + list1
    elif (len(list1) % 4) == 2:
        list1 = ['0','0'] + list1
    elif (len(list1) % 4) == 3:
        list1 = ['0'] + list1

    #Making Pairs of four to match the dictionary key
    list2 = []
    string = ""
    count = 0
    for i in list1:
        if count >= 4:
            list2.append(string)
            string = ""
            count = 0
        string += i
        count += 1
    list2.append(string)
    
    #Final Hexadecimal number
    hex = ""
    for i in list2:
        hex += (dict1[i])

    return hex

print(f"The Hexadecimal representation of binary {n} is {binary_to_hexa(n)}.")