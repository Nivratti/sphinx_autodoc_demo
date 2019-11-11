import json

# Google style with types in docstrings:

def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True
    

def main():
    func()


if __name__ == "__main__":
    main()