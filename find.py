import os
import sys

def usage():
    print(f'Usage: {sys.argv[0]} <filename>')
    exit(0)

def main():
    actual_file = sys.argv[1]
    search_file = sys.argv[1].lower()

    for path, dirs, files in os.walk('.'):
        if search_file in [file.lower() for file in files]:
            print(f'{os.path.join(path, search_file)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        usage()