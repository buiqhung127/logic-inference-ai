from utils import *
from solution import PL_Resolution
class ConfigureConstants:
    def __init__(self):
        self.input_dir = 'input.txt'
        self.output_dir = 'output.txt'

class GlobalStorage:
    def __init__(self):
        self.clauses = []


if __name__ == '__main__':
    # a = {'aa', 'bbba'}
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
    print(PL_Resolution(gs.clauses, alpha))

# read the input
# change the unary (not) into a prefix