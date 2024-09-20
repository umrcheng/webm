import os


def get_file_time(path):
    return os.path.getmtime(path)


def get_file_size(path):
    return os.path.getsize(path)


def get_file_exists(path):
    return os.path.exists(path)
