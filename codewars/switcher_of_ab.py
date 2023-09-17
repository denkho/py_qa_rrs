def switcheroo(s):
    new_line = []
    for letter in s:
        if letter == 'a':
            new_line.append('b')
        elif letter == 'b':
            new_line.append('a')
        else:
            new_line.append(letter)
    return ''.join(new_line)
    # return string.translate(string.maketrans('ab','ba'))


if __name__ == '__main__':
    print(switcheroo('aabccbbabab'))
    print(switcheroo('abc'))
    print(switcheroo('ccc'))
        