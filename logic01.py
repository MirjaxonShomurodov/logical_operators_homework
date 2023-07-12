def main(a,b,c):
    return (a<b and b<c) or (b<a and b>c)
print(main(3,4,5))
    
"""
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
