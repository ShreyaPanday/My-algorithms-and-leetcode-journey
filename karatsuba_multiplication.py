#Shreya Shivanand Pandey
#Karatsuba Multiplication is a smart multiplication technique that uses the principles of the  divide and conquer strategy.  
# to run this program u need to have an input file with the name "input.txt" in the same directory as this python file.

import sys

def read_input(filename):
    with open(filename, 'r') as file:
        x = int(file.readline().strip())
        y = int(file.readline().strip())
        return x, y


def convert_to_binary(t):
    return bin(t)[2:]


def convert_back_to_decimal(binary_string):
    return int(binary_string, 2)


def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


def recursive_multiplication(x, y, file):
    ns = min(len(x), len(y)) // 2

    if ns == 0:
        return convert_back_to_decimal(x) * convert_back_to_decimal(y)

    xl, xr = x[:len(x) - ns], x[len(x) - ns:]
    yl, yr = y[:len(y) - ns], y[len(y) - ns:]

    c = recursive_multiplication(add_binary(xl, xr), add_binary(yl, yr), file)
    a = recursive_multiplication(xl, yl, file)
    b = recursive_multiplication(xr, yr, file)
    product = (a << (2 * ns)) + ((c - a - b) << ns) + b


    file.write(f"{ns},{convert_back_to_decimal(xl)},{convert_back_to_decimal(xr)},"
               f"{convert_back_to_decimal(yl)},{convert_back_to_decimal(yr)},"
               f"{a},{c},{b}\n")

    return product


def main():
    if len(sys.argv) < 2:
        print("No input file specified.")
        sys.exit(1)
    else:
        x, y = read_input(sys.argv[1])

    x_bin = convert_to_binary(x)
    y_bin = convert_to_binary(y)

    with open("output.txt", "w") as file:
        recursive_multiplication(x_bin, y_bin, file)
        # file.write(f"answer: {result}\n")


if __name__ == "__main__":
    main()
