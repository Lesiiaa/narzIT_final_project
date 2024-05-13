import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert files')
    parser.add_argument('input_file', help='Input file path + extension')
    parser.add_argument('output_file', help='Output file path + extension')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    print(f'Input file: {args.input_file}')
    print(f'Output file: {args.output_file}')