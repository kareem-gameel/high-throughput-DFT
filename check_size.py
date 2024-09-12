import argparse

# Function to count the number of structures in the XYZ file
def count_structures(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_structures = sum(1 for line in lines if line.strip().isdigit())
    return num_structures

def main():
    parser = argparse.ArgumentParser(description='Count the number of structures in an XYZ file.')
    parser.add_argument('file_path', type=str, help='Path to the XYZ file')
    args = parser.parse_args()
    
    num_structures = count_structures(args.file_path)
    print(f"Number of structures in {args.file_path}: {num_structures}")

if __name__ == "__main__":
    main()
