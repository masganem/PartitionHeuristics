import random
import sys

def generate_test_cases(length):
    a = list()
    for i in range(0, length):
        a.append(random.randint(1, 10000))
    return a

if __name__ == "__main__":
    length = int(sys.argv[1])
    amount = int(sys.argv[2])
    output_filename = sys.argv[3]
    output_file = open(output_filename, "x")
    for i in range(0, amount):
        output_file.write(str(generate_test_cases(length)) + '\n')
    
