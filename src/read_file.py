def read_file(filename):
    filename = '../data/' + filename
    with open(filename, "r") as file:
        content = file.read().split()
    
    k = int(content[0])
    alphabet_dict = {}
    for i in range(1, 2 * k, 2):
        char, val = content[i], content[i+1]
        alphabet_dict[char] = int(val)
    # print(alphabet_dict)
    a, b = content[-2], content[-1]
    return (a, b, alphabet_dict)

if __name__ == "__main__":
    fn = input("Enter a file name: ")
    a, b, alphabet_dict = read_file(fn)
    print(f"Contents of {fn}:\n")
    print("a: ", a)
    print("b: ", b)
    print("dictionary: ", alphabet_dict)
