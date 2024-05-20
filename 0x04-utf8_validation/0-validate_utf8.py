#!/usr/bin/python3
"""
Module: UTF-8 validation.
"""

def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    for byte in data:
        if skip > 0:
            if byte & 0b11000000 != 0b10000000:
                return False
            skip -= 1
        else:
            if byte < 0x80:
                continue
            elif byte & 0b11100000 == 0b11000000:
                skip = 1
            elif byte & 0b11110000 == 0b11100000:
                skip = 2
            elif byte & 0b11111000 == 0b11110000:
                skip = 3
            else:
                return False
    return skip == 0
