import sys

def read_input(filename: str) -> list[list[int]]:
    f = open(filename, "r")
    result = list()
    for line in f:
        clean_line = line.replace(" ", "").replace("[", "").replace("]", "").replace("\n","")
        content = [int(number) for number in clean_line.split(',')]
        result.append(content)
    f.close()
    return result

if __name__ == "__main__":
    print(read_input(sys.argv[1]))