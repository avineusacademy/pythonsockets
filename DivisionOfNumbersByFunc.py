### This program is to find if given number is divisible

# Function with 2 arguments to find divisible of number
def FindDivisibleNumbers(num, div):
    if ((num % div) == 0):
        print('Given number', str(num), 'Is Divisible by ', str(div))
    else:
        print('Given number', str(num), 'Is not Divisible by ', str(div))

#Get number to find divisibility
num = int(input('Enter number to test divisibility with numbers '))

for index in range(1, 13):
    #FindDivisibleNumbers(9, 1)
    #..
    #FindDivisibleNumbers(9, 10)
    FindDivisibleNumbers(num, index)

