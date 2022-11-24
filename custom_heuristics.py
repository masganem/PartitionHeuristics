import sys
from statistics import mean
from greedy import greedy
from read_input import read_input

def custom_heuristics(instance: list[int]) -> int:
    (diff, [A, B]) = greedy(instance)
    A = sorted(A)
    B = sorted(B)
    # print(diff)
    swap_diffs = [abs(diff)]
    for a, b in zip(A, B):
        # print(a, b, abs((a - b)*2 - diff))
        swap_diffs.append(abs((a - b)*2 - diff))
    return min(swap_diffs)

def custom_heuristics_performance(instances: list[list[int]]) -> int:
    results = list()
    for instance in instances:
        results.append(custom_heuristics(instance))
    return mean(results)

if __name__ == "__main__":
    instances = read_input(sys.argv[1])
    print(custom_heuristics_performance(instances))