import argparse
import datetime
import os
import platform
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time",    action="store_true", help="Get current time")
parser.add_argument("-d", "--date",    action="store_true", help="Get today date") 
parser.add_argument("-u", "--uname",   action="store_true", help="Get current user username")
parser.add_argument("-v", "--version", action="store_true", help="Get current version python interpreter")
parser.add_argument("-T", "--tree",    action="store_true", help="Get tree of files in current directory")
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()

if args.time:
    print datetime.datetime.now().time().strftime("%H:%M:%S")
if args.date:
    print datetime.date.today()
if args.uname:
    print os.getlogin()
if args.version:
    print "Python version " + platform.python_version()
if args.tree:
    print os.listdir('.')

