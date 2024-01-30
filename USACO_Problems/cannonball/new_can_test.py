import random
import math

stri = ""
for i in range(10**3):
    stri += (str(int(random.randint(1, 10**3)))) + " "

open("USACO_Problems/cannonball/outputfile.txt", 'w').write(str(len(stri))+"\n")
open("USACO_Problems/cannonball/outputfile.txt", 'w').write(stri)