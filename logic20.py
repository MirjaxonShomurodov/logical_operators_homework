# def main(n):
 
# """
#     A number consisting of one and zero is given (the number starts at once). 
#     If the number of ones is greater than zero, true, otherwise False is returned.
    
#     Args:
#         n(int): parameter n
#     Returns:
#         bool: answer
#     """
def main(n):
    n1=n%10
    n//=10

    n2=n%10
    n//=10

    n3=n%10
    n//=10

    n4=n%10
    n//=10
    n5=n
    son=n1+n2+n3+n4+n5
    son1=5-son
    return son>son1
n=11110
print(main(n))