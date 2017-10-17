"""The following code will cause various Python Exceptions to occur"""

def name_error():
    """This function will raise a NameError."""
    no_function()


def type_error():
    """This function will raise a TypeError."""
    "hello world" + 7


def attribute_error():
    """This function will raise a AttributeError."""
    new_numbers = [1, 2, 3]
    print(new_numbers.upper())


def big_boom():
    """This function calls on big_bodda_boom function."""
    big_bodda_boom()


def big_bodda_boom():
    """This function calls on big_big_bodda_boom function."""
    big_big_bodda_boom()


def big_big_bodda_boom():
    """This function will raise 4 level NameError"""
    print(oh_no())


def syntax_error):
    """This function will raise a SyntaxError."""
    print("hello")
