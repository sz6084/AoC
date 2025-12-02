## PART ONE ##
import pathlib

lines = pathlib.Path("input.txt").read_text().split("\n")

num=50 #init
op=-1
passwd=0
for line in lines:
    if line[0]=='L':
        num-=int(line[1:])
    else:
        num+=int(line[1:])
    while num<0:
        num+=100
    while num>=100:
        num-=100
    if num==0:
        passwd+=1
print(passwd)

## PART TWO ##