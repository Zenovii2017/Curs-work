from checker.checker import *
from URL.url import URL
from file.read import read_from_file


def short_make_url(ident=False):
    """
    make url with input data user
    :return: str
    """
    url = URL()
    answer = input("Do you need to see list with category?\n").lower()
    if answer == "yes":
        print("List with all categories: \n",
              read_from_file("CourseCategory.txt"), "\n")
    print("if you dont want input category dont input anything.")
    category = input("Please input category of course: \n")
    if category or not ident:
        new_category = easy_checker(category, "CourseCategory.txt")
        if not ident:
            while not new_category:
                print("Entered category not found.\n")
                print("You must input category")
                category = input("Please input category of course: ")
                new_category = easy_checker(category, "CourseCategory.txt")
            else:
                if new_category is not None:
                    url.add_category(new_category)
        else:
            while not new_category:
                print("Entered category not found.\n")
                category = input("Please input category of course: ")
                if category == "":
                    break
                new_category = easy_checker(category, "CourseCategory.txt")
            else:
                if category != "":
                    url.add_category(new_category)

    answer = input("Do you need to see list with subcategory?\n").lower()
    if answer == "yes":
        print("List with all subcategories: \n",
              read_from_file("CourseSubcategory.txt"), "\n")
    print("if you dont want input subcategory dont input anything.")
    subcategory = input("Please input subcategory of course: \n")
    if subcategory:
        new_subcategory = easy_checker(subcategory, "CourseSubcategory.txt")
        while not new_subcategory:
            print("Entered subcategory not found.\n")
            subcategory = input("Please input subcategory of course: ")
            if subcategory == "":
                break
            new_subcategory = easy_checker(subcategory,
                                           "CourseSubcategory.txt")
        else:
            if subcategory != "":
                url.add_subcategory(new_subcategory)
    if ident:
        url = long_make_url(url)
    return url


def long_make_url(url):
    """
    its function is for make url if you choose udemy way
    :param url: str
    :return: str
    """
    print("If you dont want input answer to some question then press Enter!\n")
    answer = input(
        "If you want get courses with affiliate agreed, input yes: ").lower()
    if answer != "":
        if answer == "yes":
            url.is_affiliate_agreed(True)
        else:
            url.is_affiliate_agreed(False)
    print("\n")

    answer = input(
        "If you want get courses with fixed price, input yes: ").lower()
    if answer != "":
        if answer == "yes":
            url.is_fixed_priced_deals_agreed(True)
        else:
            url.is_fixed_priced_deals_agreed(False)
    print("\n")

    answer = input(
        "If you want get courses with percentage deals agreed, input yes: ").lower()
    if answer != "":
        if answer == "yes":
            url.is_fixed_priced_deals_agreed(True)
        else:
            url.is_fixed_priced_deals_agreed(False)
    print("\n")

    print(
        "Next if you want you can input language, but this works very bad beca"
        "use program read your input language and then search it in dict and "
        "then return language in iso 639.2\nand program can make mistake. "
        "Because of that it much better if you dont input language.\n")
    answer = input("Input language that you need: ")
    if answer != "":
        input_language = search_language(answer)
        if input_language:
            url.language(input_language)
        else:
            while not input_language:
                answer = input("Input language that you need: ")
                if input_language == "":
                    break
                input_language = search_language(answer)
            else:
                if input_language != "":
                    url.language(input_language)

    answer = input(
        "If you want get courses with small simple quiz, input yes: ").lower()
    if answer != "":
        if answer == "yes":
            url.has_simple_quiz(True)
        else:
            url.has_simple_quiz(False)
    print("\n")

    answer = input(
        "If you want get courses with closed caption, input yes: ").lower()
    if answer != "":
        if answer == "yes":
            url.has_closed_caption(True)
        else:
            url.has_closed_caption(False)
    print("\n")

    answer = input(
        "If you want get courses with coding exercises, input yes: ").lower()
    if answer != "":
        if answer == "yes":
            url.has_coding_exercises(True)
        else:
            url.has_coding_exercises(False)
    print("\n")

    answer = input(
        "If you want see all instructional levels, input yes: ").lower()
    if answer == "yes":
        print(read_from_file("instructional_level.txt"))
    answer = input(
        "Input your instructial level: ").lower()
    if answer != "":
        answer = easy_checker(answer, "instructional_level.txt")
        if answer:
            url.instructional_level(answer)
        else:
            while not answer:
                answer = input(
                    "Input your instructial level: ").lower()
                if answer == "":
                    break
                answer = easy_checker(answer, "instructional_level.txt")
            else:
                if answer != "":
                    url.instructional_level(answer)
    print("\n")

    answer = input(
        "If you want see all ordering types, input yes: ").lower()
    if answer == "yes":
        print(read_from_file("orderinglist.txt"))
    answer = input(
        "Input your ordering type: ").lower()
    if answer != "":
        answer = easy_checker(answer, "orderinglist.txt")
        if answer:
            url.ordering(answer)
        else:
            while not answer:
                answer = input(
                    "Input your ordering type: ").lower()
                if answer == "":
                    break
                answer = easy_checker(answer, "orderinglist.txt")
            else:
                if answer != "":
                    url.ordering(answer)
    print("\n")

    return url
