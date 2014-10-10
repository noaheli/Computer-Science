#McSwag = []
#swag = 1
#while (swag <= 300):
#    if swag % 2 != 0:
#        McSwag.append(swag)
#    swag = swag + 1
#print McSwag
#
#List1 = ['fdsf', 'sdf', 'sdf', 'sfdg', 'sfgsd', 'sdfgsdfgfrhg', 'fgh', 'fgh', 'wer'] 
#x = 0
#while (x < len(List1) - 1):
#    print List1[x]
#    x = x + 1
#  
x = 2  
import random
rand = random.randint(0,50)
swag = 1
while (swag == 1):
    print "Guess a number m8."
    asd = int(raw_input())
    if asd > rand:
        print "Too High!"
    if asd < rand:
        print "Too Low!"
    if asd == rand:
        print "yay"
        swag = 2