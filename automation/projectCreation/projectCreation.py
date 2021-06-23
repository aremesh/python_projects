import os
import sys
from parser import args
from utils import (initGit, initRepo, printTextMat,
                  createProjectFolder, makeStructure, pushRepo)

folders = ['test', 'docs']
files = ['main.py', 'utils.py']


def main():
    os.chdir(args.dir)
    if not os.path.exists(args.name):
        createProjectFolder(args)
        printTextMat(args)
    else:
        print("Project folder already exists")
        sys.exit(0)
    makeStructure()
    initGit()
    if args.repo:
        if args.privaterepo:
            initRepo(args.privaterepo)
        else:
            initRepo()
        pushRepo()
    else:
        print("No online repository created")
    print()  # empty line
    print("Project set successfully")



if __name__=="__main__":
    main()