## Program to print multiplication table 

## iterate from 1 to 10
for index in range(1, 11):
    print("********************************")
    print("Multiplication Table for ", index)
    print("********************************")
    # iterates from 1 to 12
    for base in range(1, 13):
        # 1 * 1 = 1... 1 * 12 = 12
        # 2 * 1 = 2 ... 2 * 12 = 24
        print(index, '*' ,base, "=", index * base)
