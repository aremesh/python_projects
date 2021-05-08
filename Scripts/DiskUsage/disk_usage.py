import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True is there is enough space"""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total

    gig_free = du.free / 2**30
    if percent_free < min_absolute or percent_free < min_percent:
        return False
    return True

if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")
    sys.exit(1)

print("A OK")
sys.exit(0)