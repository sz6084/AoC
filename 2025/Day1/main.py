## PART ONE ##
import pathlib

base_path = pathlib.Path(__file__).parent.resolve()
lines = (base_path / "input.txt").read_text().split("\n")

num=50 #init
op=-1
passwd=0
# for line in lines:
#     if line[0]=='L':
#         num-=int(line[1:])
#     else:
#         num+=int(line[1:])
#     while num<0:
#         num+=100
#     while num>=100:
#         num-=100
#     if num==0:
#         passwd+=1
# print(passwd)

## PART TWO ##

for line in lines:
    extractedNum=int(line[1:])
    if line[0]=='L':
        num-=extractedNum
    else:
        num+=extractedNum
    while num<0:
        if num+extractedNum!=0:
            passwd+=1
        num+=100
    while num>=100:
        if num!=100:
            passwd+=1
        num-=100
    if num==0:
        passwd+=1
    #print("num:",num)
    #print("numZeroes:",passwd)
print(passwd)
#6863 too high