from pathlib import Path


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
    def create_answer_structure(self, path: Path, year, day):
        logger.info(f'Creating {year}-12-{day}')
        answer_path = Path.joinpath(path / year / day)
        self.create_dir(answer_path)
        # TODO - create template file for this
        self.create_file(Path.joinpath(answer_path / 'answer.py'))