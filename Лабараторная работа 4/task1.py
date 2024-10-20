# TODO решите задачу

from json import load

def task() -> float:
    with open('input.json') as file:
        return round(sum(rec['score'] * rec['weight'] for rec in load(file)), 3)



print(task())
