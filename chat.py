
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
        return lines

def convert(user1, user2, lines):
    new_format = []
    person = None
    for line in lines:
        if line == user1:
            person = user1
            continue
        elif line == user2:
            person = user2
            continue
        if person:
            new_format.append(person + ': ' + line)
    return new_format

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    user1 = input('請輸入使用者1姓名: ')
    user2 = input('請輸入使用者2姓名: ')
    lines = convert(user1, user2, lines)
    write_file('output.txt', lines)

main()