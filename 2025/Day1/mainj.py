import pathlib

base_path = pathlib.Path(__file__).parent.resolve()
lines = (base_path / "exinput.txt").read_text().split("\n")

num = 50
score = 0
for i in range(0, len(lines)):
    if lines[i][0] == "L":
        num = num - int(lines[i][1:])
        if num < 0:
            num = 100 + num
    else:
        num = num + int(lines[i][1:])
        if num > 99:
            num = num - 100
    if num == 0:
        score += 1
print(score)