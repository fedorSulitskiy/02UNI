# 7
import sys
docs = sys.argv[1:]
for i in docs:
    try:
        with open(rf"C:\Users\fsuli\Programming\02UNI\Programming_0066\{i}", 'r') as fp:
            x = len(fp.readlines())
            print(i, 'total lines:', x)
        fp.close()
    except:
        print(i, ' document suffered an error whilst counting lines')