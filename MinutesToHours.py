#! /usr/bin/env python
import sys

def start(argv):
    pass
    # print(argv)
    arg = int(argv[1])
    if arg < 0:
        pass
    hour = arg//60
    Minu = arg%60
    print('%d H, %d M'%(hour, Minu))
    
if __name__ == '__main__':
    start(sys.argv)
    
  