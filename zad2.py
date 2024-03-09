import sys
sys.stdout.write("a = ")
a = int(sys.stdin.readline())
sys.stdout.write("b = ")
b = int(sys.stdin.readline())
sys.stdout.write("c = ")
c = int(sys.stdin.readline())

print("a^b + c = {}".format(a ** b + c))
