def split_and_join(line):
    l = []
    l = line.split(" ")
    result = ""
    for i in range(len(l)):
        if i != len(l) - 1:
            result += l[i] + '-'
        else:
            result += l[i]
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)