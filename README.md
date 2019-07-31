# EasyAsync - Python3

# Requirements & Install

    Python3

    To install library for system use, run the following:

        pip3 install .

# Usage

    

# Examples
```python
from EasyAsync import EasyAsync

def printNum(arg):
    '''
    :param arg:
    :return None:
    '''
    print(arg)

def add(args):
    '''
    :param args:
    :return sum of args:
    '''
    return args[0]+args[1]

if __name__ == "__main__":
    # create a EasyAsync object
    easy = EasyAsync(workers=16)

    # [0, 1, 2..., 149]
    args = range(0, 150)
    # example 0: use to print numbers
    for rets in easy.easy_work(printNum, args):
        # process something between printing
        pass

    # [(0, 150), (0, 151) ... (149, 299)] list of arguments for function
    args = [(x, y) for x in range(0, 150) for y in range(150, 300)]

    # example 1: use as generator and process small chunks at a time
    for rets in easy.easy_work(add, args):
        for r in rets:
            print(r)

    # example 2: get all returns into single list, then process all data at the same time
    rets = [r for rets in easy.easy_work(add, args) for r in rets]
    for r in rets:
        print(r)
```