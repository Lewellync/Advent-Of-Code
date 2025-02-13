from pathlib import Path
from datetime import datetime, timedelta
import argparse
import urllib

# TODO - refactor into util folder
class FileHelper:
    @staticmethod
    def create_dir(self, path: Path):
        if not path.is_dir():
            Path.mkdir(path, parents=True)

    @staticmethod
    def create_file(self, path: Path, delete_empty_directory=False):
        if not path.is_file():
            if path.exists() and not path.iterdir() and delete_empty_directory:
                Path.rmdir(path)
            else:
                if delete_empty_directory:
                    raise FileExistsError('A directory with that name exists and it is not empty')
        Path.touch(path)

    # build file structure
    # year
    #   day(day_number)
    #       input.txt answer.py
    @staticmethod
    def create_answer_structure(self, path: Path, year, day, input):
        answer_path = Path.joinpath(WORKING_DIR / year / day)
        self.create_dir(answer_path)
        # TODO - create template file for this
        self.create_file(Path.joinpath(answer_path / 'answer.py'))
        # TODO - incorporate this into the GET call
        self.create_file(Path.joinpath(answer_path / 'input.txt'))

parser = argparse.ArgumentParser(prog='Advent of Code Utilities')
parser.add_argument('-t', '--testing', action='store_true')
args = parser.parse_args()

WORKING_DIR = Path(__file__).parent
UTILS_DIR = Path.joinpath(WORKING_DIR, 'aoc_utils')

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
                    print(r'!--! RUNNING WITHIN TEN MINUTES !--! DO NOT SPAM !--!')
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
            
            user_agent = 'lewellync@github.com/1.0'
            headers = {'User-Agent': user_agent}

            req = urllib.request.Request("https://adventofcode.com/{year}/day/{day}/input", headers)

            # create answer directory and files
            FileHelper.create_answer_structure(WORKING_DIR, year, day, input)

            break
        case '2':
            continue
        case '3': 
            break