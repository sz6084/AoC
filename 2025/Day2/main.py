## PART ONE ##
import pathlib, math

base_path = pathlib.Path(__file__).parent.resolve()
lines = (base_path / "exinput.txt").read_text().split(",")
sum=0
for line in lines:
    if line[0]==0:
        sum+=line
    id=line.split("-")
    i=int(id[0])
    for i in range(int(id[0]),int(id[-1])+1):
        halfLen = len(str(i))/2 # int division! - only for part 1
        base = 10**(halfLen)
        #if len(str(i))==2*halfLen: # check if length even - only for part 1
        if int(i/base)==int(i%base) and base>9:
            print(i)
            sum+=i
        # else:
        #     print("valid id:",i) # debug; too long
    # while i>int(id[0]) and i<=int(id[-1]):
    #     base = 10**(len(str(i))/2)
    #     if int(i/base)==int(i%base):
    #         sum+=i
    #     i+=1

print("sum:",sum)
# 26368490878 too high
# 26368490864 too high