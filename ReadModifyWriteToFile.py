## This program is to read from file. Modify the content and write to another ilf

## Initialize Rstr
Rstr = ''
## Open file to read
Rfile = open('ReadPythonfile.txt', 'r')

## Open another file to write
Wfile = open('ModPythonfile.txt', 'w')


## Read from Rfile and store in string
for rline in Rfile:
    Rstr =  Rstr + rline +  " APPEND "

print ('Content read from file and Modified ', Rstr)

##Write Modified content to another file
Wfile.write(Rstr)

##Close the files
Rfile.close()
Wfile.close()

## Open file to read
Rfile1 = open('ReadPythonfile.txt', 'r')

## Open another file to write
Wfile1 = open('ModPythonfile.txt', 'r')


print("****** Printing content in ReadPythonfile.txt *********\n")
##Print content  in Read file
print(Rfile1.read())

print("****** Printing content in ModPythonfile.txt *********\n")
##Print content writen in Modified file
print(Wfile1.read())


##Close the files
Rfile1.close()
Wfile1.close()
