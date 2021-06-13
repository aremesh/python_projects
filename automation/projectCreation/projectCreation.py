import os
from parser import args


folders = []
files = []

def main():
    os.chdir(args.dir)
    printTextMat("Temporary changed path to:", args)
    createProjectFolder(args)
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
    if items.dir == '.':
        print()
    else:
        text = f"{text} {items.dir}"
        width = len(text)
        print()
        print(("").center(width, "-"))
        print(text)
        print(("").center(width, "-"))
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