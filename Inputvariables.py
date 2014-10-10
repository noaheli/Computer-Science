#Python
print "<INSERT WELCOME STATEMENT HERE>"
print "WHAT IS YOUR NAME?"
str1 = raw_input()
print " "
print "Hello," +str1
print "PLEASE ENTER 1 INTEGER."
int1 = raw_input()
print "PLEASE INSERT THE SECOND INTEGER"
int2 = raw_input()
print "Add or subtract the 2 numbers?"
answer = raw_input()
if answer == "Add":
    print " "
    print int1
    print int2  
    print int(int1) + int(int2)
if answer == "Subtract":
    print " "
    print int1
    print int2
    print int(int1) - int(int2)