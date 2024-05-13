import argparse
import json


def load_file(filename):
    data = {}
    file_extension = filename.split('.')[-1]
    if file_extension == 'json':
        data = load_json(filename)
    else:
        print("Error: Wrong file format!")
    return data


def load_json(filename):
    with open(filename, 'r') as file:
        try:
            data = json.load(file)
            print("Json loaded!")
            return data
        except json.JSONDecodeError:
            print("Error: Invalid JSON syntax!")
            return {}

def main():
    parser = argparse.ArgumentParser(description="Data Processor")
    parser.add_argument("input_files", nargs=2, help="Input files + formats")
    args = parser.parse_args()
    
    input_files = args.input_files

    filename, file_format = input_files[0].split('.')
    data = load_file(filename + '.' + file_format)

if __name__ == "__main__":
    main()
