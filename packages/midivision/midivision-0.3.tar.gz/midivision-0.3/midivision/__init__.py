
def division(a, b, type_="str"):
    """Return the division between two numbers

    Args:
        a : Numerator
        b : Denominator
        type_ (, optional): Type of result, possible values are "complex","str","int" and "float". Defaults to float.

    Returns:
        a/b: Result of division in expected type
    """
    allowed = ["complex", "str", "int", "float"]
    if type_ not in allowed:
        raise AttributeError(
            '"{}" is not a valid format, only valid {}'.format(type_, allowed))
    return eval(type_+"({})".format(a/b))


def isdivisible(a, b):
    """
    Args:
        a : Number to divide
        b : Number to divide for

    Returns:
        True if a is divisible by b, else False
    """
    try:
        residual = a % b
        divisible = float(residual) == 0
        return divisible
    except:
        raise TypeError("a and b not are not compatible type")


print(isdivisible(5, 5))
