import logging.config
from pathlib import Path
from datetime import datetime, timedelta
import argparse
import logging
import json
from file import FileHelper

WORKING_DIR = Path(__file__).parent
UTILS_DIR = Path.joinpath(WORKING_DIR, 'aoc_utils')

# configuration stored in file that is loaded
logging_conf_path = Path.joinpath(WORKING_DIR / 'logging.json')
with open(logging_conf_path, 'r') as logging_conf:
    logging_json = json.load(logging_conf)

logging.config.dictConfig(logging_json)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(prog='Advent of Code Utilities')
parser.add_argument('-t', '--testing', action='store_true')
args = parser.parse_args()

DATETIME_FORMAT = r'%y/%m/%d %H:%M:%S'
PRODUCTION = args.testing
COOLDOWN_TIME = timedelta(minutes = (10 if PRODUCTION else 0))

# TODO - look up proper command line argument design, is this fine? too basic?
while True:
    print("""Advent of Code Utilities
        1 - Retrieval
        2 - Submission
        3 - Exit
        """)
    choice = input('--> ')

    match choice:
        case '1':
            year = input('Year: ')
            day = input('Day: ')

            # check last run against current time, and break if less than 10 minutes
            curr_time = datetime.now()
            time_file_name = r'last_run.txt'
            with open(Path.joinpath(UTILS_DIR, time_file_name), 'r+') as timefile:
                last_run = timefile.read()
                if last_run and datetime.strptime(last_run, DATETIME_FORMAT) + timedelta(minutes=10) > curr_time:
                    logger.warning(f'!--! RUNNING TOO OFTEN !--!  !--! DO NOT SPAM !--!')
                    break
                    
                # it's been 10 minutes, so overwrite the last run time
                # NOTE - is there a better way to overwrite a file in python? is storing a value in a file okay?
                timefile.seek(0)
                timefile.truncate()
                timefile.write(curr_time.strftime(DATETIME_FORMAT))

            session_file = r'secrets\session.txt'
            session_path = Path.joinpath(UTILS_DIR, session_file)
            with open(session_path, 'r', encoding='utf-8') as file:
                session = file.read()
            
            if not session:
                logger.warning(r'!--! NO SESSION KEY LOADED !--!')
                break
            
            user_agent = 'lewellync@github.com/1.0'
            headers = {'User-Agent': user_agent, 'session': session}

            # req = urllib.request.Request("https://adventofcode.com/{year}/day/{day}/input", headers)

            # create answer directory and files
            FileHelper.create_answer_structure(WORKING_DIR, year, day)

            break
        case '2':
            continue
        case '3': 
            break