import sys
from statistics import mean
from read_input import read_input

def greedy(instance: list[int]) -> tuple[int, tuple[list[int]]]:
    instance = sorted(instance)
    A = list()
    sumA = 0
    B = list()
    sumB = 0
    while len(instance):
        largest = instance.pop()
        if (sumA <= sumB):
            A.append(largest)
            sumA += largest
        else:
            B.append(largest)
            sumB += largest
    return sumA - sumB, (A, B)

def greedy_performance(instances: list[list[int]]) -> int:
    results = list()
    for instance in instances:
        results.append(abs(greedy(instance)[0]))
    return mean(results)

if __name__ == "__main__":
    instances = read_input(sys.argv[1])
    print(greedy_performance(instances))
