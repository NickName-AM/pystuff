#!/usr/bin/python3

import os
import sys
import argparse

f"""
Usage:
python3 {sys.argv[0]} --help 
"""


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str,
                        help="File to search")
    parser.add_argument("--folder", type=str,
                        help="Folder to search")
    parser.add_argument("--path", type=str,
                        help="Path from where the search will start")
    args = parser.parse_args()

    search_file = args.file
    search_folder = args.folder
    search_path = '.'
    if args.path and os.path.isdir(args.path):
        search_path = args.path

    for path, dirs, files in os.walk(search_path):
        if search_file in files:
            print(f'{os.path.join(path, search_file)}')
        elif search_folder in dirs:
            print(f'{os.path.join(path, search_folder)}')


if __name__ == '__main__':
    main()
