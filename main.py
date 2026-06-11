import sys

if len(sys.argv)<2:
    print("too few args")

elif len(sys.argv)>2:
    print("too many args")

else:
    print("hello dear", sys.argv[1])