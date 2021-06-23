import os
from parser import args


structure = {
            0: {'folder': '.', 'files': ['README.md','main.py', '.gitignore', '.env']},
            1: {'folder': 'test', 'files': ['unittest.py']},
            2: {'folder': 'docs', 'files': ['idea.md']},
        }


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


def makeStructure():
    os.chdir(f"{args.dir}/{args.name}")
    for s_id, s_info in structure.items():
        if s_info['folder'] != '.':
            os.makedirs(s_info['folder'])
            for file_name in s_info['folder'] and s_info['files']:
                os.chdir(s_info['folder'])
                open(file_name, 'w').close()
                os.chdir('..')
        else:
            for file_name in s_info['files']:
                if file_name == "README.md":
                    os.system(f"echo '# {args.name}' > README.md")
                else:
                    open(file_name, 'w').close()

# Create git functions #
def initGit():
    os.system('git init .')


def initRepo(*flags):
    if flags:
        # print("Private Repo created")
        os.system(f'gh repo create {args.name} -y -d "" --private')
    else:
        # print("Public Repo created")
        os.system('gh repo create')

def pushRepo():
    os.system('git add .')
    os.system('git commit -m "initialized project"')
    os.system('git push -q -u origin main')