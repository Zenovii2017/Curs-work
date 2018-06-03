from file.read import read_from_file, special_read_language_list
from Data.get_data import get_curriculum_items


def easy_checker(category, open_file):
    """
    check if in list categories is input category or not. if not it check if
    input category is similar to at least one of the list. And returned similar
    to input.
    :param category: str
    :param open_file: str
    :return: str
    """
    open_file = read_from_file(open_file)
    if category in open_file:
        return category

    lst = []
    for word in open_file:
        coefficient = short_Jacquard_algorithm(word, category)
        if lst == []:
            lst = [coefficient, word]
        else:
            if lst[0] < coefficient:
                lst = [coefficient, word]
    if lst[0] >= 0.5:
        return lst[1]
    else:
        return None


def check(data):
    """
    start checking list with courses on input parametrs
    :param data: list
    :return: str
    """
    print("Please write or copy themes subject in file theme.txt")
    answer = input(
        "If you write it, please input something. Your answer: ")
    new_data = []
    for course in data:
        get_data = get_curriculum_items(course["id"])
        get_data.append({"title": course["title"], "url": course["url"]})
        new_data.append(get_data)
    opened_file = read_from_file("theme.txt")
    returned_data = []
    for theme in opened_file:
        for course in new_data:
            for course_data in course:
                try:
                    if short_Jacquard_algorithm(course_data["title"],
                                                theme) >= 0.7 and \
                            course not in returned_data:
                        returned_data.append(course)
                        break
                except:
                    pass
    return returned_data


def short_Jacquard_algorithm(text1, text2):
    """
    analyze two texts
    It use a Jacquard algorithm? it means it delete all digits and punctuation
    delete repeated letters
    :param text1: str
    :param text2: str
    :return: float
    """

    def make_new_text(text):
        new_text = set()
        for letter in text:
            if letter.isalpha():
                new_text.add(letter.lower())
        return new_text

    new_text1 = make_new_text(text1)
    new_text2 = make_new_text(text2)
    a = len(new_text1)
    b = len(new_text2)
    c = 0
    for letter in new_text1:
        if letter in new_text2:
            c += 1
    coefficient = c / (a + b - c)
    return coefficient


def search_language(language):
    """
    search language in dict and then return language in iso 639.2
    :param language: str
    :return: str
    """
    open_file = special_read_language_list()
    if language in open_file:
        return open_file[language]
    lst = []
    for i in open_file:
        coefficient = short_Jacquard_algorithm(language, i)
        if lst == []:
            lst = [coefficient, i]
        else:
            if lst[0] < coefficient:
                lst = [coefficient, open_file[i]]
    if lst[0] >= 0.5:
        return lst[1]
    return None
