import sys

n = 6
src = 1
dest = 3
print(n)
print(src)
print(dest)

def move_disk(src, dest):
    print("Moving top disk from peg ", src, " to peg ", dest, ".")


def towers(n, src, dest):
    if n == '1':
        move_disk(src, dest)
    else:
        tmp = 6 - int(src) - int(dest)
        towers(n - 1, src, tmp)

        move_disk(src, dest)
        towers(n - 1, tmp, dest)

towers(n, src, dest)
