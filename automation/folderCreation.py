import os
import sys


def createFolder(name, path):
    if path != ".":
        os.chdir(path)
    os.mkdir(foldername)
    print(f"Folder {name} created successfully")


if __name__ == '__main__':
    cwd = os.getcwd()
    foldername = sys.argv[1]
    if len(sys.argv) == 3:
        path = sys.argv[2]
    else:
        path = "."
    createFolder(foldername, path)
