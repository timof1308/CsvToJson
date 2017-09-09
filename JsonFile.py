#!/usr/bin/python
# Author= Timo Fischer

import os
import re
import json
from File import File


class JsonFile(File):
    """
    JSON File Class
    """

    def __init__(self, file):
        """
        JsonFile class constructor
        :param file:
        """
        super().__init__(file)
        self.file_name = self.file.rsplit('.', 1)[0]
        self.absolute_path = "%s\\%s.json" % (self.path, self.file_name)
        # check if file exists
        self.checkFile()

    def checkFileType(self):
        """
        check if file is csv
        :return:
        """
        reg = re.compile(r"(.?)*\.(json)")
        if reg.match(self.file):
            return True
        else:
            return False

    def checkFile(self):
        """
        Create json file if file does not exist
        :return:
        """
        if not os.path.isfile(self.absolute_path):
            open(self.absolute_path, 'w')
            print('Created new file: %s' % self.absolute_path)

    def writeContent(self, content):
        """
        Write content to json file
        :param content: dict
        :return:
        """
        with open(self.absolute_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(content, indent=2, sort_keys=True))

        print('Successfully wrote output json file')
