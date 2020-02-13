import sys

orig_stdout = sys.stdout
fout = open('out.txt', 'w+')
sys.stdout = fout

with open("ThisisBroken.png", "rb") as image:
  f = image.read()
  b = bytearray(f)
  for i in range(len(b)):
      print(b[i])
  print (b[0])


sys.stdout = orig_stdout
fout.close()