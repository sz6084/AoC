import pathlib

base_path = pathlib.Path(__file__).parent.resolve()
line = (base_path / "input.txt").read_text().split("\n")

num=50 #init
op=1
passwd=0
for char in line:
    if char.startswith("L"):
        op=-1
    else:
        op=1
    extractedNum=int(char[1:])
    num+=(op*extractedNum)
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
#452 is too low
#955 too low