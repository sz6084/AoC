import pathlib

line = pathlib.Path("input.txt").read_text().split()

num=50 #init
op=1
passwd=0
#print(line)
for char in line:
    if char.startswith("L"):
        op=-1
    else:
        op=1
    num+=(op*int(char[1:]))
    while num<0:
        num+=100
    while num>=100:
        num-=100
    if num==0:
        passwd+=1
    #print(num)
print(passwd)
#452 is too low
#955 too low