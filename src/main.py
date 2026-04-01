from read_file import read_file
from soln import highest_val_subseq
import sys

def main():
    if len(sys.argv) < 2:
        print("ERROR...Must include file name of data set in data/")
        return -1
        
    file_name = sys.argv[1]
    a, b, dict = read_file(file_name)
    

    value, subseq = highest_val_subseq(a, b, dict)
    
    print("Solution: ")
    print(value)
    print(subseq)
    
if __name__ == "__main__":
    main()