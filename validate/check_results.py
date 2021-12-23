from autograder_helpers import find_files, enc, check_line

encodings = {
    'stage.txt': ['0xf2d'],
    'first.txt': ['0xfa7'],
    'last.txt': ['0xc76'],
    'log.txt': ['0xf3f', '0xf4a'],
    'log_format.txt0': ['0xf1e'],
    'log_format.txt1': ['0x519', '0x87c'],
    'remote.txt': ['0x9c5'],
    'branch.txt': ['0x507'],
    'branch_create.txt0': ['0x5fb'],
    'branch_create.txt1': ['0x472'],
    'push.txt0': ['0xf3a'],
    'push.txt1': ['0xfd8']
}


def main():
    stop = 0
    """Check if all files are included"""
    files = ['stage.txt', 'first.txt', 'last.txt', 'log.txt', 'log_format.txt',
             'remote.txt', 'branch.txt', 'branch_create.txt', 'push.txt']
    found = find_files(files, "../src")
    if (not found):
        print("INCORRECT: You are missing some files, check the deliverables.")
        stop += 1
        return

    """Check stage.txt"""
    with open("../src/stage.txt") as f:
        line = f.readline()
        stop += check_line('stage.txt', line, encodings['stage.txt'])

    """Check first.txt"""
    with open("../src/first.txt") as f:
        line = f.readline()
        stop += check_line('first.txt', line, encodings['first.txt'])

    """Check last.txt"""
    with open("../src/last.txt") as f:
        line = f.readline()
        stop += check_line('last.txt', line, encodings['last.txt'])

    """Check log.txt"""
    with open("../src/log.txt") as f:
        line = f.readline()
        stop += check_line('log.txt', line, encodings['log.txt'])

    """Check log_format.txt"""
    with open("../src/log_format.txt") as f:
        lines = f.readlines()
        if len(lines) != 2:
            print(
                "INCORRECT: You should have only two lines in log_format.txt (delete empty newlines or check your answer)")
        for i in range(len(lines)):
            stop += check_line('log_format.txt',
                               lines[i], encodings['log_format.txt' + str(i)])

    """Check remote.txt"""
    with open("../src/remote.txt") as f:
        line = f.readline()
        stop += check_line('remote.txt', line, encodings['remote.txt'])

    """Check branch.txt"""
    with open("../src/branch.txt") as f:
        line = f.readline()
        stop += check_line('branch.txt', line, encodings['branch.txt'])

    """Check branch_create.txt"""
    with open("../src/branch_create.txt") as f:
        lines = f.readlines()
        if len(lines) != 2:
            print(
                "INCORRECT: You should have only two lines in branch_create.txt (delete empty newlines or check your answer)")
        for i in range(len(lines)):
            stop += check_line('branch_create.txt', lines[i],
                               encodings['branch_create.txt' + str(i)])

    """Check push.txt"""
    with open("../src/push.txt") as f:
        lines = f.readlines()
        if len(lines) != 2:
            print(
                "INCORRECT: You should have only two lines in push.txt (delete empty newlines or check your answer)")
        for i in range(len(lines)):
            stop += check_line('push.txt', lines[i],
                               encodings['push.txt' + str(i)])

    if (stop == 0):
        print("SUCCESS: Congratulations all your answers are correct.")


main()
