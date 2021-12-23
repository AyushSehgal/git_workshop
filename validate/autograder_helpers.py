import os


def enc(word):
    line = word.split()
    final = 0
    for l in line:
        for w in l:
            final += ord(w)
    return hex(final ^ 0b0110110110110)


def find_files(names, path):
    for root, dirs, f in os.walk(path):
        for n in names:
            if n not in f:
                return False
    return True


def check_line(filename, line, expected):
    if enc(line) not in expected:
        print("INCORRECT: Check your answer in " + filename)
        return 1
    return 0

# def check_files(filename, expected, length):
