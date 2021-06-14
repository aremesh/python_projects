

def printTextMat(items):
    print()
    if items.dir == '.' and os.path.exists(args.name):
        print("Project created in the current directory")
    else:
        text = f"Temporary path change: {items.dir}"
        print(text)
    print()


def createProjectFolder(items):
    os.makedirs(items.name)


def makeFolders(folders=[]):
    os.chdir(f"{args.dir}/{args.name}")
    for folder in folders:
        os.makedirs(folder)


def makeFiles(files):
    os.chdir(f"{args.dir}/{args.name}")
    for file in files.items:
        os.makedirs(file)
        print(file)
    print("Created Files")


# Create git functions #
def initGit():
    pass # os.system('git init .')


def initRepo(*flags):
    if flags:
        print("Private Repo created")
        # os.system('gh repo create --private')
    else:
        print("Public Repo created")
        # os.system('gh repo create')
