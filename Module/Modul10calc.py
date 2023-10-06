# Test Funktionen

PI = 3.1489580475029384780729

def addition(x,y):
    return x+y


def faculty(x):
    """
    test text
    :param x:
    :return: factorial of any integer
    """
    if x < 0:
        return None
    elif x == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, x + 1):
            factorial *= i
        return factorial


if __name__ == "__main__":  # pass as placeholder
    print("Hier Testablauflogik")

