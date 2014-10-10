def makeList(num, num1, num2):
    list1 = [num, num1, num2]
    return list1
def getFirst(list2):
    return list2[0]
def getLast(list3):
    return list3[len(list3) - 1]
def swapList(list4):
    list4[0], list4[len(list4) - 1] = list4[len(list4) - 1], list4[0]
    return list4