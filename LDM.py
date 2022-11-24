import sys
from statistics import mean
from read_input import read_input

def LDM(instance: list[int]) -> int:
    while len(instance) > 1:
        largest = max(instance)
        instance.remove(largest)
        second_largest = max(instance)
        instance.remove(second_largest)
        difference = largest - second_largest
        instance.append(difference)
    return instance[0]

def LDM_performance(instances: list[list[int]]) -> int:
    results = list()
    for instance in instances:
        results.append(abs(LDM(instance)))
    return mean(results)

if __name__ == "__main__":
    instances = read_input(sys.argv[1])
    print(LDM_performance(instances))