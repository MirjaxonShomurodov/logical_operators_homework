def main(a):
    x=a//10000 
    y=a//1000%10
    b=a//100%10 
    d=a//10%10
    m=a%10
    return (x<y and x<b and b<d and d<m)
print(main(98765))
"""
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """