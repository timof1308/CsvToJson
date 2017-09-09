#!/usr/bin/python
# Author= Timo Fischer

import sys
import getopt
from CsvFile import CsvFile
from JsonFile import JsonFile


def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        sys.stderr.write('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            sys.stdout.write('main.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if outputfile == "":
        outputfile = inputfile

    file = CsvFile(inputfile)
    content = file.parseContent()

    # write dict to json-file
    json_file = JsonFile(outputfile)
    json_file.writeContent(content)


if __name__ == '__main__':
    main(sys.argv[1:])
