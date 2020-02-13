import sys

orig_stdout = sys.stdout
fout = open('out2.txt', 'w+')
sys.stdout = fout


out1 = open("out.txt", "r")

for i in out1:
    print(chr(int(i)), end="")

sys.stdout = orig_stdout
fout.close()