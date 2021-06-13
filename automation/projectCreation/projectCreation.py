import os
import sys
from parser import args


folders = []
files = []

def main():
    os.chdir(args.dir)
    if not os.path.exists(args.name):
        createProjectFolder(args)
        printTextMat(args)
    else:
        print("Project folder already exists")
        sys.exit(0)
    makeFolder()
    makeFiles()
    initGit()
    if args.repo:
        if args.privaterepo:
            initRepo(args.privaterepo)
        else:
            initRepo()
    else:
        print("No online repository created")


def printTextMat(text, items):
    print()
    if items.dir == '.' and os.path.exists(args.name):
        print("Project created in the current directory")
    else:
        text = f"Temporary path change: {items.dir}"
        print(text)
    print()


def createProjectFolder(items):
    os.makedirs(items.name)


def makeFolder():
    print("Created folders")


def makeFiles():
    print("Created folders")


def initGit():
    print("Git initialized")


def initRepo(*flags):
    if flags:
        # print(flags) # True
        print("Private Repo created")
        # gh repo create --private
    else:
        print("Public Repo created")
        # gh repo create


if __name__=="__main__":
    main()
    print()