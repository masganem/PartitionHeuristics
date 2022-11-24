import sys
from LDM import LDM_performance
from custom_heuristics import custom_heuristics_performance
from greedy import greedy_performance

from read_input import read_input

if __name__ == "__main__":
    print("LDM:", LDM_performance(read_input(sys.argv[1])))
    print("Custom:", custom_heuristics_performance(read_input(sys.argv[1])))
    print("Greedy:", greedy_performance(read_input(sys.argv[1])))