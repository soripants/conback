#!/usr/bin/python
# This python file uses the following encoding: utf-8
import sys
import subprocess
import re
import os.path
import getpass
import glob
from pathlib import Path

class FileOperations:
    ## Get only hidden files or folders
    @staticmethod
    def searchHidden(directory , isFolderBool):
        folders = next(os.walk(directory))[1]
        files = next(os.walk(directory))[2]
        foldersHidden = [""]
        filesHidden = [""]
        if isFolderBool:
            for item in folders:
                 if item.startswith("."):
                    foldersHidden.append(item)
            foldersHidden.remove('')
            return(foldersHidden)
        else:
            for item in files:
                if item.startswith(".") and not os.path.islink(directory + item):
                    filesHidden.append(item)
            filesHidden.remove('')
            return filesHidden

    ## Search the directory and remove large folders from the given variable
    @staticmethod
    def delistLargeFolders(baseDir , pathList):
        output = [""]
        for folder in pathList:
            folderPath = Path(baseDir + folder)
            if not os.path.islink(folderPath):
                folderSize = sum(f.stat().st_size for f in folderPath.glob('**/*') if f.is_file() )
                if folderSize < 10000000:
                    output.append(folder)
        output.remove('')
        return output

    ## Check if file is symlink
    @staticmethod
    def removeSymlinks(baseDir , fileList):
        output = [""]
        for files in fileList:
            filePath = Path(baseDir + files)
            if not os.path.islink(filePath):
                output.append(files)
        output.remove('')
        return output