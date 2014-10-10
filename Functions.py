#Functions
#ADDITION
def sum(num1, num2):
    total = num1 + num2
    print total
#SUBTRACT
def sub(num1, num2):
    total = num1 - num2
    return total
#SubSmall
def SubSmall(num1, num2):
    if num1 < num2:
        total = num2 - num1
        return total
    if num2 < num1:
        total = num1 - num2
        return total
sum(590495, 85086)
sub(364734, 76756)
SubSmall(123, 123)