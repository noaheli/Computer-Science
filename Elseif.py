def printmax(num1, num2):
    if num1 > num2:
        print int(num1)
    elif num2 > num1:
        print int(num2)
def printmaxmin(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print int(num1)
    elif num2 > num1 and num2 > num3:
        print int(num2)
    elif num3 > num1 and num3 > num2:
        print int(num3)
    if num1 < num2 and num1 < num3:
        print int(num1)
    elif num2 < num1 and num2 < num3:
        print int(num2)
    elif num3 < num1 and num3 < num2:
        print int(num3)
def isevenorodd(num):
    if num % 2 == 0:
        print "Even."
    else:
        print "Odd."
def printmaxoflist(num1, num2, num3):
    maxlist = [num1, num2, num3]
    print maxlist
    print "Maximum Value =" and max(maxlist)