from solution import PL_Resolution


class ConfigureConstants:
    def __init__(self):
        self.input_dir = 'input.txt'
        self.output_dir = 'output.txt'

class GlobalStorage:
    def __init__(self):
        self.clauses = []


# -A
# 4
# -A OR B
# B OR -C
# A OR -B OR C
# -B


# A
# 4
# -A OR B
# -C OR B
# A OR C OR -B
# -B

if __name__ == '__main__':
    print({'A;-B;C'}.issubset({'A', '-A;B', 'A;-B;C', '-B', 'B;-C'}))
    cc = ConfigureConstants()
    gs = GlobalStorage()
    with open(cc.input_dir) as file:
        for index, line in enumerate(file): 
            if index == 0:
                alpha = line.rstrip()
            elif index == 1:
                num = int(line.rstrip())
            else:
                temporary = ';'.join(line.rstrip().split(' OR '))
                gs.clauses.append(temporary)
            
    # print(gs.clauses)
    logs = []
    terminal_state = PL_Resolution(gs.clauses, alpha, logs)
    print(logs)
    with open(cc.output_dir, 'w') as file:
        for i in range(0, len(logs) - 1, 2):
            leng = logs[i] 
            moves = logs[i + 1]
            file.write(str(leng) + '\n')
            for j in range(leng):
                if moves[j] == '':
                    file.write('{}\n')
                    continue
                # print(' OR '.join(moves[j].split(';')))
                file.write(' OR '.join(moves[j].split(';')) + '\n')
        if terminal_state:
            file.write('YES')
        else: 
            file.write('NO')


# read the input
# change the unary (not) into a prefix
