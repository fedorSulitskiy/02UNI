# 1
if __name__ == '__main__':
    import sys
    import math
    radius = int(sys.argv[1])
    height = int(sys.argv[2])
    print(2*math.pi*radius*height + 2*math.pi*radius**2)