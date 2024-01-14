#!/usr/bin/python

import os
import logging
import argparse


def fgrep():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_string", type=str, help="String to search for")
    parser.add_argument("--path", type=str, help="String to search for", default=os.getcwd())
    parser.add_argument("-V", "--verbose", action="store_true" , help="Verbosity")
    args = parser.parse_args()

    for path, dirs, files in os.walk(args.path):
        for file in files:
            c_file = os.path.join(path,file)        # Current File
            with open(c_file, "r") as f:
                try:
                    file_data = f.read()
                except:
                    if args.verbose:
                        logging.error(f"[ Some kind of encoding error on file: {c_file} ]")
                    continue
                if args.search_string in file_data:
                    print(c_file)
            
if __name__ == '__main__':
    fgrep()
