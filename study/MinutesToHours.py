#! /usr/bin/env python
import sys

def start(argv):
    try:
        arg = int(argv[1])
        if arg < 0:
            raise ValueError("A value error happened.")
        hour = arg//60
        Minu = arg%60
        print('%d H, %d M'%(hour, Minu))
    except ValueError:
        print("ValueError: Input number cannot be negative")
    except IndexError:    
        print("IndexError: Please input a int")
if __name__ == '__main__':
    start(sys.argv)
 