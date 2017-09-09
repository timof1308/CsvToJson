#!/usr/bin/python
# Author= Timo Fischer

import re
import sys
import os


class File:
    """
    File Class
    """

    def __init__(self, file):
        """
        File class constructor
        :param file:
        """
        self.file = file
        self.path = '.\storage'
        self.absolute_path = "%s\\%s" % (self.path, self.file)

    def checkFile(self):
        """
        check if file exists
        :return:
        """
        if self.file in os.listdir(self.path):
            return True
        else:
            sys.stderr.write('File does not exist')
            sys.exit()

    def checkFileType(self):
        """
        check if file is csv
        :return:
        """
        reg = re.compile(r"(.?)*\.(csv)")
        if reg.match(self.file):
            return True
        else:
            return False

    def getContent(self):
        """
        get file content
        :return:
        """
        with open(self.absolute_path) as f:
            return f.read()
