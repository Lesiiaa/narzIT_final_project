import argparse
import json
import yaml
import xmltodict


def load_file(filename):
    data = {}
    file_extension = filename.split('.')[-1]
    if file_extension == 'json':
        data = load_json(filename)
    elif file_extension == 'yml':
        data = load_yaml(filename)
    elif file_extension == 'xml':
        data = load_xml(filename)
    else:
        print("Error: Wrong file format!")
    return data

def save_file(filename, data):
    file_extension = filename.split('.')[-1]
    if file_extension == 'json':
        save_json(filename, data)
    elif file_extension == 'yml':
        save_yaml(filename, data)
    elif file_extension == 'xml':
        save_xml(filename, data)
    else:
        print("Error: Wrong file format!")


def load_json(filename):
    with open(filename, 'r') as file:
        try:
            data = json.load(file)
            print("Json loaded!")
            return data
        except json.JSONDecodeError:
            print("Error: Invalid Json syntax!")

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Json saved!")


def load_yaml(filename):
    with open(filename, 'r') as file:
        try:
            data = yaml.safe_load(file)
            print("Yaml loaded!")
            return data
        except yaml.YAMLError:
            print("Error: Invalid Yaml syntax!")

def save_yaml(filename, data):
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print("Yaml saved!")


def load_xml(filename):
    with open(filename, 'r') as file:
        try:
            data = xmltodict.parse(file.read())
            print("Xml loaded!")
            return data
        except xmltodict.ExpatError:
            print("Error: Invalid Xml syntax!")
            return None
        
def save_xml(filename, data):
    if data is not None:
        with open(filename, 'w') as file:
            file.write(xmltodict.unparse(data, pretty=True))
        print("Xml saved!")
    else:
        print("Error: No XML data to save!")

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
