import sys

arguments = len(sys.argv) - 1
print("the script is called with %i arguments" % (arguments))
position = 1
while (arguments >= position):
    print("parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1
fullCmdArguments = sys.argv
# - further arguments
argumentList = fullCmdArguments[1:]

print(argumentList)
for arg in sys.argv:
    print('Argument:', arg)