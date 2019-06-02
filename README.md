# EasyAsync - Python3

# Requirements & Install

    Python3

    To install library for system use, run the following:

        pip install .

# Usage

    

# Examples
```python
from EasyAsync import EasyAsync

def test(item):
    print(item)

if __name__=="__main__":
    easy = EasyAsync()
    
    x = range(0, 150)
    easy.easy_work(test, x)
```