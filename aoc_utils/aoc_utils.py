import urllib.request
import os
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(prog='Advent of Code Utilities')
parser.add_argument('-t', '--testing', action='store_true')
args = parser.parse_args()

DATETIME_FORMAT = r'%y/%m/%d %H:%M:%S'
WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
PRODUCTION = args.testing
COOLDOWN_TIME = timedelta(minutes = (10 if PRODUCTION else 0))

# args 
# 1 - year
# 2 - date

user_agent = 'lewellync@github.com/1.0'
headers = {'User-Agent': user_agent}
# req = urllib.request.Request("https://adventofcode.com/2024/day/1/input", headers)

while True:
    print("""Advent of Code Utilities
        1 - Retrieval
        2 - Submission
        3 - Exit
        """)
    choice = input('--> ')

    match choice:
        case '1':
            # check last run against current time, and break if less than 10 minutes
            curr_time = datetime.now()
            time_file_name = r'last_run.txt'
            with open(os.path.join(WORKING_DIR, time_file_name), 'r+') as timefile:
                last_run = timefile.read()
                timefile.seek(0)
                timefile.truncate()
                timefile.write(curr_time.strftime(DATETIME_FORMAT))
                if last_run and datetime.strptime(last_run, DATETIME_FORMAT) + timedelta(minutes=10) > curr_time:
                    print(r'!--! RUNNING WITHIN TEN MINUTES !--! DO NOT SPAM !--!')
                    break

            session_file = r'secrets\session.txt'
            session_path = os.path.join(WORKING_DIR, session_file)
            with open(session_path, 'r', encoding='utf-8') as file:
                session = file.read()
                x=2 
        case '2':
            continue
        case '3': 
            break