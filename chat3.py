
lines = []
with open ('[LINE]黃宇搞2.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] # 第一格清單裡的前五個字
    name = s[0][5:]
    print(name)
    print(time)