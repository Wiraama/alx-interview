#!/usr/bin/python3
""" method that determines if a given data set represents a valid UTF-8 encoding"""

def validUTF8(data):
    for d in data:
        if d > 255:
            return False
    bytes_data = bytes(data)
    try:
        bytes_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
