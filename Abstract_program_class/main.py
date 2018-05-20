from Data.get_data import get_courses_list
from URL.make_url import make_url
from URL.url import URL
from checker.checker import check_catogory, check
from file.write import write_list_with_courses
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

        url = make_url()
        data = get_courses_list(url)
        write_list_with_courses(data)

    else:

        category = input("Please input category of course: ").lower()
        category = check_catogory(category)
        url = URL().add_category(category).url()
        data = get_courses_list(url)
        write_list_with_courses(check(data))


if __name__ == '__main__':
    main()
