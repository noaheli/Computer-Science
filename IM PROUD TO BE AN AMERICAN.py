total = 0
print "How many numbers will you be entering?"
userInput = int(raw_input())
for dingus in range(userInput):
    print "Please enter a number:"
    num1 = int(raw_input())
    total = total + num1
print total
dums = []
print "How many numbers will you be entering?"
userInput = int(raw_input())
for x in range(userInput):
    print "Please enter a number:"
    num1 = int(raw_input())
    dums.append(num1)
print sum(dums)
total = 1
print "What number do you want to take the factorial of?"
userInput = int(raw_input())
for dongis in range(userInput):
    total = total * (dongis + 1)
print total
factors = []
print "What number do you want to factor m9?"
userInput = int(raw_input())
for dongus in range(userInput):
        if (userInput % (dongus + 1)) == 0:
            factors.append((dongus + 1))
print factors