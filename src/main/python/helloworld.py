"""
This is a simple module to demonstrate a hello world function in Python.
"""

import sys

def helloworld(out):
    """
    Print a hello world message.

    Args:
        out: Output stream to write the message to.
    """
    out.write("Hello world of Python\n")

# Call the function with a file object
helloworld(sys.stdout)
