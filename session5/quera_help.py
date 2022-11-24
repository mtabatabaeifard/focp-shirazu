binary = input("enter binary:")
#  get's binary
if len(binary) == 8:
    # check's that user input is 8bit
    binary_2 = int(binary)
    # calculating unsigned int
    int_val , i , n =0,0,0
    while (binary_2 != 0):
        a = binary_2 % 10
        int_val = int_val + a * pow(2,i)
        binary_2 = binary_2//10
        i += 1
    print (int_val)
    char = (chr(int_val))
    print(char)

else:
    print("invalid input")
