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
        #if i%2==0:
        base = 10**(len(str(i))/2)
        if int(i/base)==int(i%base):
            sum+=i
    # while i>int(id[0]) and i<=int(id[-1]):
    #     base = 10**(len(str(i))/2)
    #     if int(i/base)==int(i%base):
    #         sum+=i
    #     i+=1

print("sum:",sum)
# 26368490878 too high