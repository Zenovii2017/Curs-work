from Data.get_data import get_courses_list, cut_data
from URL.make_url import *
from checker.checker import check
from file.write import write_list_with_courses, special_write
from greetings.greetings_with_user import greetings_with_user, choice


def main():
    """
    main fuction that do all work.
    At start say main information to user, then ask user what methods he want
    use.Then ask all need information, and then make url and download data.
    And then check data and write result in file.
    :return: None
    """
    greetings_with_user()
    user_choice = choice()
    if user_choice == "udemy":
        url = short_make_url(True)
        url = url.url()
        data = get_courses_list(url)
        write_list_with_courses(data)

    else:
        print("It will be more better, if you input category and subcategory "
              "of courses.")
        url = short_make_url()
        url = url.url()
        data = get_courses_list(url)
        data = cut_data(data)
        checked_data = check(data)
        special_write(checked_data)


if __name__ == '__main__':
    main()
