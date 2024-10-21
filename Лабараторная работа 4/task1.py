# TODO решите задачу

from json import load

def task() -> float:
    with open('input.json') as file:
        sum_ = sum(rec['score'] * rec['weight'] for rec in load(file))
        return round(sum_, 3)



print(task())
