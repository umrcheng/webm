from utli.load import CONFIG
from utli import file_processing


def get_path_name(p: str) -> str:
    """
    从一个文件路径中提取文件名。

    该函数接受一个字符串参数p，该参数可以是包含文件名的目录路径。
    函数首先检查路径中是否包含"/"，如果包含，则说明是Unix风格的路径，
    否则认为是Windows风格的路径。之后返回路径中的文件名部分。

    参数:
    p (str): 文件的路径，可以是Unix风格或Windows风格的路径。

    返回:
    str: 路径中的文件名部分。
    """
    # 检查路径中是否包含"/"，以确定路径的风格
    if p.find("/") != -1:
        # 如果是Unix风格的路径，分割路径并返回最后一部分
        return p.split("/")[-1]

    # 如果是Windows风格的路径，分割路径并返回最后一部分
    return p.split("\\")[-1]


def in_path(name: str) -> str:
    """
    检查配置中的路径，看给定的名称是否存在于某个路径中。

    遍历CONFIG字典中的路径列表，对于每个路径，检查给定的名称是否包含在路径中。
    如果找到包含该名称的路径，则返回该路径；如果未找到，则返回None。

    参数:
    - name: str，要检查的名称。

    返回:
    - 包含给定名称的路径字符串，如果未找到则返回None。
    """
    # 遍历配置中的路径列表
    for item in CONFIG["path"]:
        # 检查名称是否在路径中
        if name in item:
            # 如果名称在路径中，返回该路径
            return item
    # 如果没有找到包含名称的路径，返回None
    return ""


def get_path_list(p1: str, p2: str) -> list:
    path = os.path.join(p1, p2)

    # 如果路径参数为空，则直接返回空列表
    if not path:
        return []

    info = []
    for item in os.listdir(path):
        info.append({
            "name": item,
            "path": os.path.join(path, item),
            "type": "file" if os.path.isfile(os.path.join(path, item)) else "dir",
            "time": file_processing.get_file_time(os.path.join(path, item))
        })
    return info


def get_path_dir_and_file_name(path: str) -> dict[str, str]:
    """
    从给定的路径中提取目录名和文件名。

    参数:
    path (str): 一个字符串格式的路径，应包含目录名和文件名。

    返回:
    dict[str, str]: 字典，包含两个键值对，'dir_name' 对应目录名，'file_name' 对应文件名。
    """
    # 分割路径
    parts = path.split('/')

    # 提取前缀
    dir_name = parts[1]
    # 提取文件名
    file_name = parts[-1]

    return {"dir_name": dir_name, "file_name": file_name}


def get_path_dir_name(path: str, name: str) -> str:
    return os.path.join(path, name)


def path_cl(path: str):
    if not path:
        return {}
    dir_name = get_path_dir_and_file_name(path)["dir_name"]
    abs_path = in_path(dir_name)
    if not abs_path:
        return {}

    abs_path.replace(f"{dir_name}", "")

    path = get_path_dir_name(abs_path, path)
    if not file_processing.get_file_exists(path):
        return {}

    return path


import os


def print_directory_tree(path, prefix=''):
    entries = os.listdir(path)
    entries.sort()  # 可选：按字母顺序排序

    for entry in entries:
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            print(f'{prefix}{entry}/')
            print_directory_tree(full_path, prefix + '  ')
        else:
            print(f'{prefix}{entry}')
