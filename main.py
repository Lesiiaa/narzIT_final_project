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

def save_file(filename, data):
    file_extension = filename.split('.')[-1]
    if file_extension == 'json':
        save_json(filename, data)
    else:
        print("Error: Wrong file format!")


def load_json(filename):
    with open(filename, 'r') as file:
        try:
            data = json.load(file)
            print("Json loaded!")
            return data
        except json.JSONDecodeError:
            print("Error: Invalid JSON syntax!")
            return {}


def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Json saved!")


def main():
    parser = argparse.ArgumentParser(description="Data Processor")
    parser.add_argument("input_files", nargs=2, help="Input files + formats")
    args = parser.parse_args()
    
    input_files = args.input_files

    filename, file_format = input_files[0].split('.')
    data = load_file(filename + '.' + file_format)

    output_file = input_files[1]
    save_file(output_file, data)

if __name__ == "__main__":
    main()
