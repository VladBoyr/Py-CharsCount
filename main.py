import fnmatch
import os
import pandas as pd


def get_files(path, pattern):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if fnmatch.fnmatch(item, pattern) and os.path.isfile(full_path):
            yield full_path


if __name__ == '__main__':
    text = []
    for file_path in get_files(path='.', pattern='*.txt'):
        with open(file_path, "r") as text_file:
            text.append(list(text_file.read()))
    print(pd.Series(text).value_counts())
