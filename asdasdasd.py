anExampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in anExampleList:
    print item
    print ""
for item in range(11, 20, 1):
    print item
    print ""
for item in range(99, 0, -2):
    print item
    print ""
ExampleList2 = []
for item in range(0, 5, 1):
    print "Enter a number"
    userinput = raw_input()
    ExampleList2.append(userinput)
print ""
for item in ExampleList2:
    print item