#!/usr/bin/python
# Author= Timo Fischer

import sys
from File import File
from JsonFile import JsonFile


class CsvFile(File):
    """
    CSV File Class
    """

    def __init__(self, file):
        """
        CsvFile class constructor
        :param file:
        """
        super().__init__(file)
        # check if file exists and has correct format
        if self.checkFile():
            if not self.checkFileType():
                sys.stderr.write('File has to be in csv format!')
                sys.exit()

    def parseContent(self):
        """
        parse csv content
        get file content and create dict
        :return:
        """
        lines = self.getContent()
        lines = lines.split('\n')
        column_header = lines[0]
        column_header = column_header.split(';')
        array = []
        for index, line in enumerate(lines):
            if index == 0:
                continue
            columns = line.split(';')
            tmp = {}
            for i, value in enumerate(columns):
                tmp[column_header[i]] = value

            array.append(tmp)

        return array