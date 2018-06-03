def read_from_file(file):
    """
    read data from file
    :param file: str
    :return: list
    """
    with open(file, "r") as open_file:
        lst = []
        for line in open_file.readlines():
            lst.append(line.strip())
    return lst


def special_read_language_list():
    """
    read data from file with name language_list.txt
    :return: dict
    """

    path = 'language_list.txt'

    with open(path, 'r') as f:
        data = dict()
        for line in f.readlines():
            words = line.strip().split()
            data[words[1]] = words[0]
    return data
