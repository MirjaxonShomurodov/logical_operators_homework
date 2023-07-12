def main(a,b):
    return (a%2==1 and b%2==0) or (b%2==1 and a%2==0)
print(main(7,3))
"""
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """