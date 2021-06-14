import os
import sys
from parser import args
from utils import (initGit, initRepo, printTextMat,
                  createProjectFolder, makeFolders, makeFiles)

folders = ['test', 'docs']
files = [
        ('main.py', 'utils.py'),
        ('test',['test.py']),
        ('docs',['README.md'])
        ]

def main():
    os.chdir(args.dir)
    if not os.path.exists(args.name):
        createProjectFolder(args)
        printTextMat(args)
    else:
        print("Project folder already exists")
        sys.exit(0)
    makeFolders(folders)
    makeFiles(files)
    initGit()
    if args.repo:
        if args.privaterepo:
            initRepo(args.privaterepo)
        else:
            initRepo()
    else:
        print("No online repository created")


if __name__=="__main__":
    main()
    print()