def main(a,b):
    return (a%2==0 and b%2==1) or (a%2==1 and b%2==0)
print(main(7,12))
"""
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """