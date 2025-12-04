## PART ONE ##
import pathlib

base_path = pathlib.Path(__file__).parent.resolve()
lines = (base_path / "input.txt").read_text().split("\n")

num=50 #init
op=-1
passwd=0

## PART TWO ##

for line in lines:
    extractedNum=int(line[1:]) # goofy ver
    if line[0]=='L':    
        num-=extractedNum%100
        passwd+=extractedNum//100
    else:
        num+=extractedNum%100
        passwd+=extractedNum//100
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
print("numZeroes:",passwd)
#6863 too high