import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Enter project name")
parser.add_argument("dir", help="Enter project directory.")
# Optional arguments
parser.add_argument('-r','--repo', type=bool, const=True, nargs='?',
                    help='Set online repository default is public')
parser.add_argument('-p','--privaterepo', type=bool, const=True, nargs='?', 
                    help="Set the online repository to private")

args = parser.parse_args()