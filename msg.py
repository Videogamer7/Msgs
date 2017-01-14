
datafile = open("Msgs.txt", 'w')
datafile.write("hello everyone 123")
datafile.close

datafile = open("Msgs.txt", 'r')
print(datafile.readline())
datafile.close
