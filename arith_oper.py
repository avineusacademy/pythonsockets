#Sample code for airthmetic operations

## Addition 2 numbers
f1 = input('Enter first number ')
f2 = input('Enter second number ')

sum = int(f1) + int(f2)
sub = int(f1) - int(f2)
mul = int(f1) * int(f2)
div = int(f1) / int(f2)
fdiv = int(f1) // int(f2)
mod = int(f1) % int(f2)
apowb = int(f1) ** int(f2)

print ('Sum of ', f1 ,' + ', f2 , ' = ',  sum )
print ('Subtraction of ', f1 ,' - ', f2 , ' = ',  sub)
print ('Multiplication of ', f1 ,' * ', f2 , ' = ',  mul )
print ('Division of ', f1 ,' / ', f2 , ' = ',  div )
print ('Floor Division of ', f1 ,' // ', f2 , ' = ',  fdiv )
print ('Mod Division of ', f1 ,' // ', f2 , ' = ',  mod )
print ('Powerof of ', f1 ,' ** ', f2 , ' = ',  apowb)
